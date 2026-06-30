from django.contrib.auth import get_user_model

User = get_user_model()


class UserService:
    @staticmethod
    def change_password(user, old_password, new_password):
        if not user.check_password(old_password):
            raise ValueError('Current password is incorrect.')
        user.set_password(new_password)
        user.save(update_fields=['password', 'updated_at'])
        return True

    @staticmethod
    def update_profile(user, data):
        for field, value in data.items():
            if value is not None:
                setattr(user, field, value)
        user.save()
        return user

    @staticmethod
    def get_all_users(role=None, is_active=None):
        queryset = User.objects.all()
        if role:
            queryset = queryset.filter(role=role)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)
        return queryset

    @staticmethod
    def toggle_user_status(user_id):
        user = User.objects.get(id=user_id)
        user.is_active = not user.is_active
        user.save(update_fields=['is_active', 'updated_at'])
        return user
