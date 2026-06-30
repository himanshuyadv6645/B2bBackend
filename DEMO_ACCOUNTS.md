# B2B Market - Demo Accounts

## Admin

| Email | Password | Role |
|-------|----------|------|
| himanshu@admin.com | himanshu | Admin |

---

## Buyers (6 Accounts)

| Email | Password | Name | Company | City |
|-------|----------|------|---------|------|
| ravi@buyer.com | buyer123 | Ravi Kumar | Ravi Enterprises | Mumbai |
| priya@buyer.com | buyer123 | Priya Sharma | Sharma Traders | Delhi |
| amit@buyer.com | buyer123 | Amit Patel | Patel Electronics | Ahmedabad |
| neha@buyer.com | buyer123 | Neha Gupta | Gupta Solutions | Bangalore |
| vikram@buyer.com | buyer123 | Vikram Singh | Singh Mart | Jaipur |
| anjali@buyer.com | buyer123 | Anjali Reddy | Reddy Computers | Hyderabad |

---

## Sellers (3 Accounts)

| Email | Password | Company | City | Status |
|-------|----------|---------|------|--------|
| techhub@seller.com | seller123 | TechHub Electronics | Mumbai | Approved |
| digital@seller.com | seller123 | Digital World | Delhi | Approved |
| circuit@seller.com | seller123 | Circuit Masters | Pune | Approved |

---

## Demo Data Summary

| Entity | Count |
|--------|-------|
| Users | 10 (1 admin + 6 buyers + 3 sellers) |
| Categories | 10 (1 parent + 9 children) |
| Brands | 12 |
| Products | 15 |
| Product Variants | 29 |
| Seller Pricing | 46 |
| Wholesale Tiers | 184 |
| Inventory | 46 |
| Cart Items | 8 |
| Orders | 14 |
| Order Items | 29 |
| Reviews | 3 |
| Notifications | 41 |

---

## Products Available

| Product | Category | Brand | Base Price |
|---------|----------|-------|------------|
| Dell Latitude 5540 | Laptops | Dell | ₹72,999 |
| HP ProBook 450 G10 | Laptops | HP | ₹54,999 |
| Lenovo ThinkPad X1 Carbon | Laptops | Lenovo | ₹1,24,999 |
| MacBook Air M3 15" | Laptops | Apple | ₹1,44,900 |
| Samsung Galaxy S24 Ultra | Mobile | Samsung | ₹1,29,999 |
| iPhone 15 Pro Max | Mobile | Apple | ₹1,59,900 |
| Cisco Catalyst 9300 | Networking | Cisco | ₹4,85,000 |
| TP-Link SG1024DE | Networking | TP-Link | ₹8,499 |
| Sony WH-1000XM5 | Audio | Sony | ₹29,990 |
| JBL Charge 5 | Audio | JBL | ₹17,999 |
| Hikvision CCTV | Security | Hikvision | ₹5,999 |
| Samsung 990 Pro SSD | Storage | Samsung | ₹10,999 |
| HP LaserJet M404dn | Printer | HP | ₹32,999 |
| APC Smart-UPS 1500VA | Power | APC | ₹54,999 |
| Logitech MX Master 3S | Accessories | Logitech | ₹9,995 |

---

## Wholesale Pricing Example (Dell Latitude 5540)

| Quantity | Price/Unit | Discount |
|----------|------------|----------|
| 1 - 10 | ₹72,999 | Base |
| 11 - 50 | ₹69,349 | 5% off |
| 51 - 200 | ₹64,239 | 12% off |
| 201+ | ₹59,859 | 18% off |

---

## How to Run

```bash
# Backend
cd D:\B2b
python manage.py migrate
python manage.py seed_data --clear
python manage.py runserver

# Frontend
cd D:\B2b\frontend
npm run dev
```

Backend: http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/api/docs/
Frontend: http://localhost:5173

