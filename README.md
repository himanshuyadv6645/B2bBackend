# B2B Wholesale Electronics Marketplace - Backend

> Django REST Framework API for B2B wholesale electronics marketplace. Similar to Moglix, IndiaMart, Udaan.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, Django 6, DRF 3.17 |
| Database | PostgreSQL (Supabase) |
| Auth | JWT (SimpleJWT) |
| Images | Cloudinary |
| API Docs | drf-spectacular (Swagger) |
| Filters | django-filter |

---

## Project Structure

```
backend/
├── config/                  # Django settings
│   ├── settings/
│   │   ├── base.py          # Base settings
│   │   ├── development.py   # Local dev (Supabase PostgreSQL)
│   │   ├── production.py    # Production (DATABASE_URL)
│   │   └── testing.py       # SQLite for tests
│   ├── urls.py              # Root URL router
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/                    # 17 Django apps
│   ├── authentication/      # Custom User model, JWT auth
│   ├── users/               # User profile
│   ├── buyers/              # Buyer profile, addresses
│   ├── sellers/             # Seller profile, warehouses
│   ├── categories/          # Hierarchical categories
│   ├── brands/              # Brand management
│   ├── products/            # Products, images
│   ├── product_variants/    # Product variants
│   ├── pricing/             # Wholesale tier pricing
│   ├── inventory/           # Stock management
│   ├── wishlist/            # Buyer wishlist
│   ├── cart/                # Shopping cart
│   ├── orders/              # Orders, invoices
│   ├── reviews/             # Product & seller reviews
│   ├── notifications/       # In-app notifications
│   ├── dashboard/           # Dashboard stats
│   ├── analytics/           # Event tracking
│   ├── payments/            # Payment models
│   ├── banners/             # Homepage banners
│   └── seo/                 # SEO landing pages
│
├── common/                  # Shared utilities
├── utils/                   # Helper functions
├── api/                     # Vercel serverless handler
│   └── index.py
├── manage.py
├── requirements.txt
├── vercel.json
└── .env
```

---

## Local Development

### Prerequisites
- Python 3.12+
- PostgreSQL (or use Supabase)

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/gitmanhimanshu/b2b-backend.git
cd b2b-backend

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure .env
# Edit .env with your Supabase/PostgreSQL credentials

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py create_superadmin --email admin@b2b.com --password admin123

# 7. Seed categories (optional)
python manage.py seed_categories

# 8. Run server
python manage.py runserver

# 9. Access API docs
# http://localhost:8000/api/docs/
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in:

```env
# Django
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
SITE_URL=http://localhost:5173

# Database (Supabase)
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=db.xxxxx.supabase.co
DATABASE_PORT=5432

# Cloudinary (for image uploads)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# JWT
JWT_ACCESS_TOKEN_LIFETIME_MINUTES=30
JWT_REFRESH_TOKEN_LIFETIME_DAYS=7
```

---

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register/` | Register |
| POST | `/api/v1/auth/login/` | Login (JWT) |
| POST | `/api/v1/auth/token/refresh/` | Refresh token |
| POST | `/api/v1/auth/logout/` | Logout |
| GET | `/api/v1/auth/profile/` | Current user |

### Health Check
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/health/` | Server health (public) |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/products/` | List products |
| GET | `/api/v1/products/{slug}/` | Product detail |
| POST | `/api/v1/products/create/` | Create product (seller) |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/categories/` | List categories |
| GET | `/api/v1/categories/tree/` | Full category tree |

### Brands
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/brands/` | List brands |
| GET | `/api/v1/brands/{slug}/` | Brand detail |

### Pricing
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/pricing/` | List pricing (seller) |
| POST | `/api/v1/pricing/create/` | Create pricing |
| GET | `/api/v1/pricing/compare/{variant_id}/` | Compare sellers |

### Cart
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/cart/` | Get cart |
| POST | `/api/v1/cart/add/` | Add to cart |
| PATCH | `/api/v1/cart/item/{id}/` | Update quantity |
| DELETE | `/api/v1/cart/item/{id}/remove/` | Remove item |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/v1/orders/` | List/Create orders |
| GET | `/api/v1/orders/{order_number}/` | Order detail |

### SEO
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/seo/resolve/{path}/` | Resolve SEO page |
| POST | `/api/v1/seo/generate/` | Generate SEO pages |
| GET | `/api/v1/seo/sitemap.xml` | XML Sitemap |
| GET | `/api/v1/seo/robots.txt` | Robots.txt |

Full Swagger docs: `/api/docs/`

---

## Deploy to Vercel

### Step 1: Push to GitHub
```bash
git add -A
git commit -m "Initial commit"
git push origin master
```

### Step 2: Import to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click **"Add New Project"**
3. Import `gitmanhimanshu/b2b-backend`
4. Framework Preset: **Other**
5. Click **"Deploy"** (will fail first time - that's OK)

### Step 3: Set Environment Variables
In Vercel Dashboard → Settings → Environment Variables, add:

| Variable | Value |
|----------|-------|
| `DJANGO_SETTINGS_MODULE` | `config.settings.production` |
| `DJANGO_SECRET_KEY` | Generate a new secret key |
| `DATABASE_URL` | `postgres://user:pass@host:port/dbname` |
| `SITE_URL` | `https://your-backend.vercel.app` |
| `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | Your Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Your Cloudinary API secret |

### Step 4: Redeploy
1. Go to **Deployments** tab
2. Click **"Redeploy"** on latest deployment
3. Wait for build to complete

### Step 5: Run Migrations
After first deploy, run migrations via Vercel CLI:
```bash
# Install Vercel CLI
npm i -g vercel

# Link to your project
vercel link

# Run migrations
vercel env pull .env.local
python manage.py migrate
```

Or use Supabase SQL Editor to run migrations directly.

### Step 6: Create Superuser
```bash
python manage.py create_superadmin --email admin@b2b.com --password yourpass
```

### Your backend is live at:
```
https://your-project-name.vercel.app/api/docs/
https://your-project-name.vercel.app/api/v1/health/
```

---

## Post-Deployment Checklist

- [ ] Health check returns `{"status": "healthy", "database": "connected"}`
- [ ] Swagger docs load at `/api/docs/`
- [ ] Can register a new user
- [ ] Can login and get JWT token
- [ ] Can fetch products list
- [ ] Cloudinary image upload works
- [ ] Update `SITE_URL` in frontend to point to this backend URL
