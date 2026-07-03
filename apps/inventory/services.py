from django.db import transaction, models
from apps.inventory.models import Inventory, StockHistory, InventoryLog


class InventoryService:
    @staticmethod
    def get_inventory(seller, variant=None):
        queryset = Inventory.objects.filter(seller=seller).select_related(
            'variant__product', 'warehouse', 'seller'
        ).prefetch_related('variant__images', 'variant__product__images')
        if variant:
            queryset = queryset.filter(variant=variant)
        return queryset

    @staticmethod
    def create_inventory(seller, data):
        inventory, created = Inventory.objects.get_or_create(
            seller=seller,
            variant=data['variant'],
            warehouse=data['warehouse'],
            defaults={
                'total_stock': data.get('total_stock', 0),
                'low_stock_threshold': data.get('low_stock_threshold', 10),
            },
        )
        if not created:
            inventory.total_stock = data.get('total_stock', inventory.total_stock)
            inventory.low_stock_threshold = data.get('low_stock_threshold', inventory.low_stock_threshold)
            inventory.save()
        return inventory

    @staticmethod
    @transaction.atomic
    def adjust_stock(inventory, quantity, change_type, notes='', performed_by=None):
        # Lock the row so concurrent stock changes can't race on the check below.
        inventory = Inventory.objects.select_for_update().get(pk=inventory.pk)
        old_stock = inventory.total_stock

        if change_type == 'add':
            inventory.total_stock += quantity
        elif change_type == 'remove':
            if inventory.available_stock < quantity:
                raise ValueError('Insufficient stock')
            inventory.total_stock -= quantity
        elif change_type == 'adjustment':
            inventory.total_stock = quantity

        inventory.save()

        StockHistory.objects.create(
            inventory=inventory,
            change_type=change_type,
            quantity_change=quantity,
            previous_stock=old_stock,
            new_stock=inventory.total_stock,
            notes=notes,
        )

        InventoryLog.objects.create(
            inventory=inventory,
            action=f'stock_{change_type}',
            old_values={'total_stock': old_stock, 'available_stock': old_stock - inventory.reserved_stock},
            new_values={'total_stock': inventory.total_stock, 'available_stock': inventory.available_stock},
            performed_by=performed_by,
        )

        return inventory

    @staticmethod
    @transaction.atomic
    def reserve_stock(inventory, quantity, seller=None):
        if seller and inventory.seller != seller:
            raise ValueError('Cannot reserve stock from another seller')
        # Lock the row so two concurrent orders can't both pass the availability
        # check and oversell the same units.
        inventory = Inventory.objects.select_for_update().get(pk=inventory.pk)
        if inventory.available_stock < quantity:
            raise ValueError('Insufficient stock to reserve')
        inventory.reserved_stock += quantity
        inventory.save()
        return inventory

    @staticmethod
    @transaction.atomic
    def release_stock(inventory, quantity):
        inventory = Inventory.objects.select_for_update().get(pk=inventory.pk)
        inventory.reserved_stock = max(0, inventory.reserved_stock - quantity)
        inventory.save()
        return inventory

    @staticmethod
    def get_low_stock_items(seller=None):
        queryset = Inventory.objects.filter(
            available_stock__lte=models.F('low_stock_threshold')
        )
        if seller:
            queryset = queryset.filter(seller=seller)
        return queryset
