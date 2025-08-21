# mg_one E-Commerce Application

This repository contains the source code for **mg_one**, an e-commerce web application. The project is structured as a Django-based backend with several service-specific modules for SMS, payments, stock management, and more.

## Features

- Product catalog and item attribution
- Location-based inventory and warehouse management
- SMS notification services (Twilio and Fast2SMS integration)
- Payment gateway integration (RazorPay)
- Admin and RESTful API support
- Modular, extensible architecture

## Project Structure

- `baseServer/`  
  Core server logic and setup (directory content undiscovered).

- `fast2sms/`  
  Integration and utilities for Fast2SMS (directory content undiscovered).

- `itemAttribution/`  
  Product and item attribute management (directory content undiscovered).

- `locationHierarchy/`  
  Handles location models, admin, migrations, and views for organizing inventory by location.
  - `admin.py` - Django admin configuration
  - `apps.py` - App configuration
  - `models.py` - Location models
  - `tests.py` - Tests
  - `views.py` - Views/endpoints
  - `migrations/` - DB migrations

- `locationItem/`  
  Inventory items per location (directory content undiscovered).

- `mgOne/`  
  Project settings and core Django configuration (directory content undiscovered).

- `razorPayService/`  
  RazorPay payment gateway integration.
  - `admin.py`, `apps.py`, `models.py`, `tests.py`, `views.py`
  - `migrations/` - DB migrations

- `static/`  
  Static files for admin and API docs.
  - `admin/` - Django admin static files
  - `rest_framework/` - DRF static files

- `stockWarehouse/`  
  Warehouse stock management (directory content undiscovered).

- `twilioService/`  
  Twilio SMS integration.
  - `admin.py`, `apps.py`, `models.py`, `service.py`, `tests.py`, `views.py`
  - `migrations/` - DB migrations

- `manage.py`  
  Django project management script

- `db.sqlite3`  
  SQLite database (for development)

- `requirements.txt`  
  Python/Django dependencies

- `Procfile` and `Runtime.txt`  
  Deployment configuration (e.g., Heroku)

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/vishnu96ray/mg_one.git
   cd mg_one
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE) (if applicable)

---

**Note:** Some directories lack discovered files in this summary. For details, explore each folder in the repository.
