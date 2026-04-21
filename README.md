# Flask App

A REST API built with Flask that allows users to manage products, track inventory, and handle user authentication with role-based access control.

## Features

- User registration and login
- JWT authentication
- Role-based access control (admin and user)
- Product management (create, read, delete)
- Inventory tracking (stock in and stock out)
- Simple frontend dashboard

## Technologies Used

- Python / Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-Bcrypt
- Flask-Migrate
- SQLite
- HTML / CSS / JavaScript

## How to Run the Project

**1. Clone the repository**
```bash
git clone https://github.com/aminSHARIFF/flask-app.git
cd flask-app
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up the database**
```bash
export FLASK_APP=run.py
flask db init
flask db migrate -m "initial"
flask db upgrade
```

**4. Run the app**
```bash
flask run
```

**5. Open in browser**
http://127.0.0.1:5000

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register a new user |
| POST | /auth/login | Login and get a token |
| GET | /auth/me | Get current logged in user |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /products | Get all products |
| POST | /products | Create a product (admin only) |
| PATCH | /products/:id | Update a product (admin only) |
| DELETE | /products/:id | Delete a product (admin only) |

### Inventory
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /inventory/in/:id | Add stock to a product |
| POST | /inventory/out/:id | Remove stock from a product |

## Default Roles

- **user** — can view products and manage stock
- **admin** — can create, update and delete products

