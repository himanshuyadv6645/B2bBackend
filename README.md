# B2B Wholesale Electronics Marketplace

> A production-ready B2B Wholesale Electronics Marketplace built with Django REST Framework.
> Similar to Moglix, IndiaMart, Udaan, and Romegramart.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, Django 6, DRF |
| Database | Supabase PostgreSQL |
| Auth | JWT (SimpleJWT) |
| Images | Cloudinary |
| API Docs | drf-spectacular (Swagger) |
| Filters | django-filter |

---

## Project Structure

```
B2b/
├── config/                     # Django settings (dev/prod/test)
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py      # Supabase PostgreSQL
│   │   ├── production.py
│   │   └── testing.py          # SQLite for tests
│   └── urls.py                 # Root URL router
│
├── apps/                       # All Django apps (17 modules)
│   ├── authentication/         # Custom User model, JWT
│   ├── users/                  # Profile management
│   ├── buyers/                 # Buyer profile, addresses
│   ├── sellers/                # Seller profile, warehouses
│   ├── categories/             # Hierarchical categories
│   ├── brands/                 # Brand management
│   ├── products/               # Products, images, documents
│   ├── product_variants/       # Variants (color, size, etc.)
│   ├── pricing/                # Seller pricing + wholesale tiers
│   ├── inventory/              # Stock management
│   ├── wishlist/               # Buyer wishlist
│   ├── cart/                   # Shopping cart
│   ├── orders/                 # Orders, invoices
│   ├── reviews/                # Product & seller reviews
│   ├── notifications/          # In-app notifications
│   ├── dashboard/              # Dashboard stats
│   ├── analytics/              # Event tracking
│   └── payments/               # Payment & refund models
│
├── common/                     # Shared utilities
│   ├── models.py               # BaseModel, SoftDeleteModel
│   ├── permissions.py          # Role-based permissions
│   ├── pagination.py           # Standard pagination
│   ├── exceptions.py           # Custom error handler
│   ├── response.py             # Standard API responses
│   ├── validators.py           # GSTIN, PAN, phone, pincode
│   └── throttling.py           # Rate limiting
│
└── utils/                      # Helper functions
    ├── file_upload.py          # Cloudinary upload/delete
    ├── email.py                # Email utilities
    └── helpers.py              # UUID, slug, masking
```

---

## All Models — What They Do & How They're Related

### 1. `User` (authentication app)

**What it does:**
The central authentication model. Stores email, password, phone, and role (admin/buyer/seller). Custom user model — no username, only email-based login. Handles JWT authentication.

**Relationships:**
- `1:1 → BuyerProfile` (when role=buyer, auto-created via signal)
- `1:1 → SellerProfile` (when role=seller, auto-created via signal)
- `1:N → Notification` (user receives notifications)
- `1:N → AnalyticsEvent` (tracks user actions)

```
User ──1:1──> BuyerProfile
User ──1:1──> SellerProfile
User ──1:N──> Notification
User ──1:N──> AnalyticsEvent
```

---

### 2. `BuyerProfile` (buyers app)

**What it does:**
Stores buyer-specific information: name, company, GSTIN, PAN, business type. Created automatically when a user registers as buyer.

**Relationships:**
- `N:1 → User` (linked user account)
- `1:N → BuyerAddress` (multiple billing/shipping addresses)
- `1:N → Wishlist` (saved products)
- `1:1 → Cart` (one cart per buyer)
- `1:N → Order` (purchase orders)
- `1:N → ProductReview` (reviews written)
- `1:N → SellerReview` (seller reviews written)

```
BuyerProfile ──N:1──> User
BuyerProfile ──1:N──> BuyerAddress
BuyerProfile ──1:1──> Cart
BuyerProfile ──1:N──> Wishlist
BuyerProfile ──1:N──> Order
BuyerProfile ──1:N──> ProductReview
BuyerProfile ──1:N──> SellerReview
BuyerProfile ──1:N──> Invoice (as buyer)
```

---

### 3. `BuyerAddress` (buyers app)

**What it does:**
Stores billing and shipping addresses for a buyer. Supports multiple addresses with a default flag. When an address is set as default, other defaults of same type are auto-unset.

**Relationships:**
- `N:1 → BuyerProfile`
- `1:N → Order` (used as billing_address or shipping_address)

```
BuyerAddress ──N:1──> BuyerProfile
Order ──billing_address──> BuyerAddress
Order ──shipping_address──> BuyerAddress
```

---

### 4. `SellerProfile` (sellers app)

**What it does:**
Stores seller company info: company name, GSTIN, PAN, logo, description. Has approval status (pending → approved/rejected/suspended). Admin must approve before seller can list products.

**Relationships:**
- `N:1 → User` (linked user account)
- `1:N → SellerWarehouse` (storage locations)
- `1:N → SellerPricing` (price per variant)
- `1:N → Inventory` (stock per warehouse)
- `1:N → SellerOrder` (order fulfillment)
- `1:N → Invoice` (as seller)
- `1:N → ProductReview` (reviews received)
- `1:N → SellerReview` (seller reviews)

```
SellerProfile ──N:1──> User
SellerProfile ──1:N──> SellerWarehouse
SellerProfile ──1:N──> SellerPricing
SellerProfile ──1:N──> Inventory
SellerProfile ──1:N──> SellerOrder
SellerProfile ──1:N──> Invoice
SellerProfile ──1:N──> ProductReview
SellerProfile ──1:N──> SellerReview
```

---

### 5. `SellerWarehouse` (sellers app)

**What it does:**
Each seller can have multiple warehouses (storage/delivery locations). Each warehouse has its own address. One warehouse can be marked as primary.

**Relationships:**
- `N:1 → SellerProfile`
- `1:N → Inventory` (stock stored here)
- `1:N → SellerPricing` (optional: price varies by warehouse)
- `1:N → SellerOrder` (fulfilled from here)

```
SellerWarehouse ──N:1──> SellerProfile
SellerWarehouse ──1:N──> Inventory
SellerWarehouse ──1:N──> SellerPricing
SellerWarehouse ──1:N──> SellerOrder
```

---

### 6. `Category` (categories app)

**What it does:**
Hierarchical product categories (self-referencing tree). Example: Electronics → Cameras → CCTV Cameras. Supports unlimited depth. Each category has a `level` and `path` for tree traversal.

**Relationships:**
- `N:1 → Category` (parent, self-referencing)
- `1:N → Category` (children)
- `1:N → Product` (products belong to leaf categories)

```
Category ──N:1──> Category (parent)
Category ──1:N──> Category (children)
Category ──1:N──> Product
```

---

### 7. `Brand` (brands app)

**What it does:**
Product brands like "Hikvision", "D-Link", "Logitech". Used for filtering and grouping products.

**Relationships:**
- `1:N → Product` (brand has many products)

```
Brand ──1:N──> Product
```

---

### 8. `Product` (products app)

**What it does:**
The core product entity. Represents a base product (e.g., "Hikvision DS-2CD2143G2-I Camera"). Contains name, description, SKU, HSN code, SEO fields. Has denormalized price range, seller count, stock count for fast listing. Supports soft delete.

**Relationships:**
- `N:1 → Category` (which category)
- `N:1 → Brand` (which brand, optional)
- `1:N → ProductVariant` (variants like color/storage)
- `1:N → ProductAttribute` (specs: weight, material, etc.)
- `1:N → ProductImage` (product photos)
- `1:N → ProductDocument` (manuals, datasheets)
- `1:N → ProductReview` (reviews)

```
Product ──N:1──> Category
Product ──N:1──> Brand
Product ──1:N──> ProductVariant
Product ──1:N──> ProductAttribute
Product ──1:N──> ProductImage
Product ──1:N──> ProductDocument
Product ──1:N──> ProductReview
```

---

### 9. `ProductVariant` (product_variants app)

**What it does:**
Represents a specific variant of a product. Example: "Hikvision Camera - Black 64GB", "Hikvision Camera - White 128GB". Each variant has its own SKU, images, and attributes. Multiple sellers can sell the same variant at different prices. Supports soft delete.

**Relationships:**
- `N:1 → Product` (belongs to product)
- `1:N → VariantAttribute` (color: Black, storage: 64GB)
- `1:N → VariantImage` (variant-specific photos)
- `1:N → SellerPricing` (multiple sellers, each with own price)
- `1:N → Inventory` (stock per seller per warehouse)
- `1:N → CartItem` (added to cart)
- `1:N → OrderItem` (sold in orders)
- `1:N → Wishlist` (wishlisted by buyers)
- `1:N → ProductReview` (variant reviews)

```
ProductVariant ──N:1──> Product
ProductVariant ──1:N──> VariantAttribute
ProductVariant ──1:N──> VariantImage
ProductVariant ──1:N──> SellerPricing
ProductVariant ──1:N──> Inventory
ProductVariant ──1:N──> CartItem
ProductVariant ──1:N──> OrderItem
ProductVariant ──1:N──> Wishlist
```

---

### 10. `SellerPricing` (pricing app)

**What it does:**
**The core B2B pricing model.** Each seller sets their own price for each variant. One variant can have MANY sellers, each with different:
- Selling price
- Offer price
- Tax rate (GST)
- Shipping charge
- MOQ (minimum order quantity)
- Warranty
- Delivery time

This is what enables **price comparison** between sellers.

**Relationships:**
- `N:1 → SellerProfile` (which seller)
- `N:1 → ProductVariant` (which variant)
- `N:1 → SellerWarehouse` (optional: from which warehouse)
- `1:N → WholesaleTier` (tiered bulk pricing)

```
SellerPricing ──N:1──> SellerProfile
SellerPricing ──N:1──> ProductVariant
SellerPricing ──N:1──> SellerWarehouse
SellerPricing ──1:N──> WholesaleTier
```

**Example flow:**
```
Variant: "CCTV Camera 4MP"
├── Seller A: Rs. 2,500/unit, MOQ 5, GST 18%
├── Seller B: Rs. 2,350/unit, MOQ 10, GST 18%
└── Seller C: Rs. 2,200/unit, MOQ 20, GST 12%

Buyer sees all 3 sellers → compares → picks cheapest
```

---

### 11. `WholesaleTier` (pricing app)

**What it does:**
**Tiered/bulk pricing for wholesale.** Each SellerPricing can have multiple price tiers based on quantity. The more you buy, the cheaper per unit.

**Example:**
```
Seller A sells CCTV Camera:
├── 1 - 20 units    → Rs. 2,500 per unit
├── 21 - 50 units   → Rs. 2,200 per unit
├── 51 - 100 units  → Rs. 1,900 per unit
└── 100+ units      → Rs. 1,600 per unit
```

When a buyer adds quantity to cart, the system automatically picks the right tier price.

**Relationships:**
- `N:1 → SellerPricing` (belongs to a pricing entry)

```
WholesaleTier ──N:1──> SellerPricing
```

---

### 12. `Inventory` (inventory app)

**What it does:**
Tracks stock levels for each seller + variant + warehouse combination. Has `total_stock`, `reserved_stock` (locked during checkout), and `available_stock` (auto-calculated). Low stock alerts via `low_stock_threshold`.

**Relationships:**
- `N:1 → SellerProfile`
- `N:1 → ProductVariant`
- `N:1 → SellerWarehouse`
- `1:N → StockHistory` (stock change log)
- `1:N → InventoryLog` (audit trail)

```
Inventory ──N:1──> SellerProfile
Inventory ──N:1──> ProductVariant
Inventory ──N:1──> SellerWarehouse
Inventory ──1:N──> StockHistory
Inventory ──1:N──> InventoryLog
```

---

### 13. `StockHistory` (inventory app)

**What it does:**
Immutable log of every stock change. Records what changed, old vs new stock, why (order, restock, adjustment), and who did it.

```
StockHistory ──N:1──> Inventory
```

---

### 14. `InventoryLog` (inventory app)

**What it does:**
Detailed audit log with JSON snapshots of old/new values. Used for debugging and compliance.

```
InventoryLog ──N:1──> Inventory
InventoryLog ──N:1──> User (performed_by)
```

---

### 15. `Wishlist` (wishlist app)

**What it does:**
Buyers can save variants to their wishlist for later. One entry per buyer-variant pair.

**Relationships:**
- `N:1 → BuyerProfile`
- `N:1 → ProductVariant`

```
Wishlist ──N:1──> BuyerProfile
Wishlist ──N:1──> ProductVariant
```

---

### 16. `Cart` & `CartItem` (cart app)

**What it does:**
Each buyer has one cart. Cart contains multiple items. Each item is tied to a specific **seller + variant** combination (because different sellers have different prices). Validates MOQ, stock, and applies tier pricing.

**CartItem fields:**
- `seller` → which seller
- `variant` → which variant
- `quantity` → how many
- `unit_price` → auto-calculated from wholesale tiers
- `tax_rate` → GST from pricing
- `total_price` → quantity × unit_price

**Relationships:**
- `Cart 1:1 → BuyerProfile`
- `CartItem N:1 → Cart`
- `CartItem N:1 → SellerProfile`
- `CartItem N:1 → ProductVariant`

```
Cart ──1:1──> BuyerProfile
CartItem ──N:1──> Cart
CartItem ──N:1──> SellerProfile
CartItem ──N:1──> ProductVariant
```

---

### 17. `Order`, `OrderItem`, `SellerOrder` (orders app)

**What it does:**

**Order:** The buyer's complete order. Contains billing/shipping address, totals, status tracking. Auto-generated order number (ORD-2026-XXXXX).

**OrderItem:** Individual line items within an order. Stores product name/image as snapshot at time of order (denormalized for history).

**SellerOrder:** When an order has items from multiple sellers, each seller gets their own SellerOrder. The seller manages shipping/tracking on their SellerOrder. When ALL seller orders are delivered, the main Order is marked delivered.

**Status flow:**
```
pending → confirmed → processing → shipped → delivered
                                          ↘ cancelled → refunded
```

**Relationships:**
```
Order ──N:1──> BuyerProfile
Order ──N:1──> BuyerAddress (billing)
Order ──N:1──> BuyerAddress (shipping)
Order ──1:N──> OrderItem
Order ──1:N──> SellerOrder
Order ──1:N──> Invoice
Order ──1:N──> Payment
Order ──1:N──> Refund

OrderItem ──N:1──> Order
OrderItem ──N:1──> SellerProfile
OrderItem ──N:1──> ProductVariant

SellerOrder ──N:1──> Order
SellerOrder ──N:1──> SellerProfile
SellerOrder ──N:1──> SellerWarehouse
```

---

### 18. `Invoice` (orders app)

**What it does:**
Auto-generated when an order is delivered. Contains GST breakdown (CGST/SGST/IGST), seller snapshot, buyer billing snapshot. Can be downloaded as PDF.

**Relationships:**
```
Invoice ──N:1──> Order
Invoice ──N:1──> SellerOrder
Invoice ──N:1──> SellerProfile
Invoice ──N:1──> BuyerProfile
```

---

### 19. `ProductReview` (reviews app)

**What it does:**
Buyers can review products they've purchased (1 review per order item). Updates product's average_rating and total_reviews automatically.

**Relationships:**
```
ProductReview ──N:1──> Product
ProductReview ──N:1──> ProductVariant
ProductReview ──N:1──> BuyerProfile
ProductReview ──N:1──> SellerProfile
ProductReview ──N:1──> OrderItem
```

---

### 20. `SellerReview` (reviews app)

**What it does:**
Buyers can review sellers after a delivered order. Updates seller's average rating automatically.

**Relationships:**
```
SellerReview ──N:1──> SellerProfile
SellerReview ──N:1──> BuyerProfile
SellerReview ──N:1──> Order
```

---

### 21. `Notification` (notifications app)

**What it does:**
In-app notifications for order updates, promotions, system alerts. Supports email/SMS ready flags.

**Relationships:**
```
Notification ──N:1──> User
```

---

### 22. `Payment` & `Refund` (payments app)

**What it does:**
Payment gateway integration layer. Stores gateway name, transaction ID, amount, status. Gateway-agnostic — ready for Razorpay, Cashfree, etc. Refund tracks money returned.

**Relationships:**
```
Payment ──N:1──> Order
Payment ──N:1──> Invoice
Refund ──N:1──> Payment
Refund ──N:1──> Order
```

---

### 23. `AnalyticsEvent` (analytics app)

**What it does:**
Tracks all user interactions: product views, searches, add-to-cart, purchases. Used for popular products, trending, and business intelligence.

**Relationships:**
```
AnalyticsEvent ──N:1──> User
```

---

## Complete Entity Relationship Diagram

```
                        ┌──────────┐
                        │   User   │
                        └────┬─────┘
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────▼─────┐  ┌────▼────┐   ┌────▼─────┐
        │BuyerProfile│  │ Seller  │   │Analytics │
        │           │  │ Profile │   │  Events  │
        └──┬──┬──┬──┘  └─┬─┬─┬──┘   └──────────┘
           │  │  │        │ │ │
     ┌─────┘  │  │   ┌────┘ │ └──────┐
     │        │  │   │      │        │
┌────▼───┐ ┌─▼┐ │ ┌──▼───┐ │  ┌────▼─────┐
│Address │ │Cart│ │ │Ware-│ │  │Wholesale │
│        │ └─┬─┘ │ │house│ │  │  Tiers   │
└────────┘   │   │ └──┬──┘ │  └──────────┘
        ┌────┘   │    │    │
        │   ┌────┘    │    └──────┐
        │   │         │           │
  ┌─────▼───▼─┐  ┌────▼────┐ ┌───▼──────┐
  │ CartItem  │  │Inventory│ │  Pricing │
  └─────┬─────┘  └────┬────┘ └───┬──────┘
        │              │          │
        │         ┌────▼────┐    │
        │         │ Stock   │    │
        │         │ History │    │
        │         └─────────┘    │
        │                        │
  ┌─────▼────────────────────────▼─────┐
  │          ProductVariant            │
  └──────┬──────────┬──────────┬───────┘
         │          │          │
   ┌─────▼───┐ ┌───▼────┐ ┌──▼────────┐
   │ Variant │ │ Variant│ │   Order   │
   │  Attrs  │ │ Images │ │   Item    │
   └─────────┘ └────────┘ └─────┬─────┘
                                │
              ┌─────────────────┘
              │
  ┌───────────▼──────────┐     ┌────────────┐
  │       Order          │────▶│  Invoice   │
  └───┬──────────┬───────┘     └────────────┘
      │          │
┌─────▼──┐  ┌───▼──────────┐
│Payment │  │ SellerOrder  │
└───┬────┘  └──────────────┘
    │
┌───▼────┐
│ Refund │
└────────┘

  ┌────────────┐     ┌────────────┐
  │  Product   │────▶│  Review    │
  └────────────┘     └────────────┘

  ┌────────────┐     ┌────────────┐
  │  Wishlist  │     │Notification│
  └────────────┘     └────────────┘
```

---

## API Endpoints Summary

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register/` | Register as buyer/seller |
| POST | `/api/v1/auth/login/` | Login (returns JWT) |
| POST | `/api/v1/auth/token/refresh/` | Refresh access token |
| POST | `/api/v1/auth/logout/` | Logout (blacklist token) |
| GET | `/api/v1/auth/profile/` | Get current user |

### Buyers
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/PATCH | `/api/v1/buyers/profile/` | Buyer profile |
| GET/POST | `/api/v1/buyers/addresses/` | List/Create addresses |
| GET/PUT/DELETE | `/api/v1/buyers/addresses/{id}/` | Address CRUD |

### Sellers
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/PATCH | `/api/v1/sellers/profile/` | Seller profile |
| GET/POST | `/api/v1/sellers/warehouses/` | List/Create warehouses |
| GET/PUT/DELETE | `/api/v1/sellers/warehouses/{id}/` | Warehouse CRUD |
| GET | `/api/v1/sellers/admin/sellers/` | Admin: list sellers |
| POST | `/api/v1/sellers/admin/sellers/{id}/approve/` | Admin: approve/reject |

### Categories & Brands
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/categories/` | List root categories |
| GET | `/api/v1/categories/tree/` | Full category tree |
| GET | `/api/v1/categories/{slug}/` | Category with children |
| GET | `/api/v1/brands/` | List brands |
| GET | `/api/v1/brands/{slug}/` | Brand details |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/products/` | List (filters: category, brand, price, search) |
| GET | `/api/v1/products/{slug}/` | Product detail |
| POST | `/api/v1/products/create/` | Seller: create product |
| PATCH | `/api/v1/products/{id}/update/` | Seller: update product |

### Product Variants
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/variants/?product={id}` | List variants |
| GET | `/api/v1/variants/{id}/` | Variant detail |
| POST | `/api/v1/variants/create/` | Seller: create variant |

### Pricing (with Wholesale Tiers)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/pricing/` | Seller: list your pricing |
| POST | `/api/v1/pricing/create/` | Seller: create pricing |
| PATCH | `/api/v1/pricing/{id}/` | Seller: update pricing |
| GET | `/api/v1/pricing/{id}/tiers/` | List wholesale tiers |
| POST | `/api/v1/pricing/{id}/tiers/` | Add tier (e.g., 1-20=Rs.1200) |
| DELETE | `/api/v1/pricing/{id}/tiers/{tier_id}/` | Delete tier |
| GET | `/api/v1/pricing/compare/{variant_id}/?quantity=50` | Compare sellers |

**Wholesale Tier Example:**
```json
POST /api/v1/pricing/{pricing_id}/tiers/
{
    "min_quantity": 1,
    "max_quantity": 20,
    "price_per_unit": "1200.00",
    "discount_percent": "0.00",
    "notes": "Small quantity"
}

POST /api/v1/pricing/{pricing_id}/tiers/
{
    "min_quantity": 21,
    "max_quantity": 50,
    "price_per_unit": "1050.00",
    "discount_percent": "12.50"
}

POST /api/v1/pricing/{pricing_id}/tiers/
{
    "min_quantity": 51,
    "max_quantity": null,
    "price_per_unit": "900.00",
    "discount_percent": "25.00"
}
```

### Inventory
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/inventory/` | Seller: list stock |
| POST | `/api/v1/inventory/create/` | Seller: add inventory |
| POST | `/api/v1/inventory/{id}/adjust/` | Seller: adjust stock |
| GET | `/api/v1/inventory/history/` | Seller: stock history |

### Wishlist
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/wishlist/` | List wishlist |
| POST | `/api/v1/wishlist/` | Add to wishlist |
| DELETE | `/api/v1/wishlist/{id}/` | Remove from wishlist |

### Cart
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/cart/` | Get cart |
| POST | `/api/v1/cart/add/` | Add to cart |
| PATCH | `/api/v1/cart/item/{id}/` | Update quantity |
| DELETE | `/api/v1/cart/item/{id}/remove/` | Remove item |
| DELETE | `/api/v1/cart/clear/` | Clear cart |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/v1/orders/` | List/Create orders |
| GET | `/api/v1/orders/{order_number}/` | Order detail |
| POST | `/api/v1/orders/{order_number}/cancel/` | Cancel order |
| GET | `/api/v1/orders/seller/` | Seller: list orders |
| POST | `/api/v1/orders/seller/{id}/ship/` | Seller: ship order |
| POST | `/api/v1/orders/seller/{id}/deliver/` | Seller: deliver |
| GET | `/api/v1/orders/invoices/` | List invoices |
| GET | `/api/v1/orders/invoices/{id}/` | Invoice detail |

### Reviews
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/v1/reviews/products/` | Product reviews |
| GET/POST | `/api/v1/reviews/sellers/` | Seller reviews |

### Notifications
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/notifications/` | List notifications |
| GET | `/api/v1/notifications/unread-count/` | Unread count |
| POST | `/api/v1/notifications/{id}/read/` | Mark read |
| POST | `/api/v1/notifications/read-all/` | Mark all read |

### Dashboard
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/dashboard/buyer/` | Buyer stats |
| GET | `/api/v1/dashboard/seller/` | Seller stats |
| GET | `/api/v1/dashboard/admin/` | Admin stats |

### Analytics
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/analytics/track/` | Track event |
| GET | `/api/v1/analytics/stats/` | Event stats |
| GET | `/api/v1/analytics/popular/` | Popular entities |

---

## Setup & Run

```bash
# 1. Clone and install
pip install -r requirements.txt

# 2. Configure .env (Supabase credentials already set)

# 3. Run migrations
python manage.py migrate

# 4. Create superuser
python manage.py create_superadmin --email admin@b2b.com --password yourpass

# 5. Run server
python manage.py runserver

# 6. Access Swagger docs
http://localhost:8000/api/docs/
```

---

## Key Business Logic

### Price Comparison Flow
```
1. Buyer searches for "CCTV Camera 4MP"
2. System finds all ProductVariants matching
3. For each variant, loads all SellerPricing entries
4. Each pricing entry has wholesale tiers
5. Buyer selects quantity → system picks best tier price
6. Buyer sees sorted list: cheapest first
7. Buyer picks a seller → adds to cart
```

### Cart Price Calculation
```
When adding to cart:
1. Look up SellerPricing for (seller + variant)
2. Check wholesale tiers for quantity
3. Pick the matching tier's price_per_unit
4. Store as unit_price in CartItem
5. total_price = quantity × unit_price
```

### Order Creation Flow
```
1. Buyer clicks "Place Order"
2. System reads all CartItems
3. Groups items by seller
4. Creates Order (buyer-level)
5. Creates OrderItem for each item (with price snapshot)
6. Creates SellerOrder for each seller
7. Reserves stock in Inventory
8. Clears cart
9. Returns order with order_number
```
