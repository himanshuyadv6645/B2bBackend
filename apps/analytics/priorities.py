"""Priority weights for behavioural events.

Every tracked event carries a weight that reflects how strong a buying signal it
is. These weights drive recommendation scoring: we group a user's events by
product, multiply by weight, sum them, and recommend the highest-scoring product.

Ordering (high -> low), as agreed:
  payment / checkout  > buy-now > add-to-cart > wishlist > product view
  > search > category / subcategory click

Cart and checkout actions outrank a category or subcategory click by design: a
click is mild curiosity, adding to cart or starting checkout is real intent.
Wishlisting sits high too — it is an explicit "I want this".
"""

EVENT_WEIGHTS = {
    'payment_initiated': 10,   # reached payment - strongest intent
    'checkout_started': 9,     # entered checkout
    'buy_now': 8,              # jumped straight to buying
    'add_to_cart': 7,          # cart - high intent
    'wishlist_add': 6,         # explicit "I want this"
    'product_view': 3,         # looked at a product
    'search': 2,               # searched for something
    'category_view': 1,        # category click - mild curiosity
    'subcategory_view': 1,     # subcategory click - mild curiosity
}

# Events that don't count toward interest scoring (already-converted / noise).
EXCLUDED_EVENTS = {'order_placed', 'remove_from_cart'}

# Weight used for any event_type not listed above.
DEFAULT_WEIGHT = 0

# A user's top product must score at least this much before we send a
# recommendation, so a single stray click never triggers a notification.
RECOMMENDATION_MIN_SCORE = 7

# Don't recommend the same product to the same user again within this window.
RECOMMENDATION_COOLDOWN_DAYS = 7
