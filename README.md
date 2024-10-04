# Django REST Framework API

## Overview

This API is built with Django and Django REST Framework (DRF) to provide a robust backend for an e-commerce application. It includes features for user profile management, product management, category management, cart and wishlist functionality, and order management.

## Features

- **User Profile Management**:
  - Create, update, and delete user profiles.
  - Authentication with JWT tokens.
  
- **Product Management**:
  - CRUD operations for products.
  
- **Category Management**:
  - Create, update, and delete categories.
  - Assign products to categories.
  
- **Cart Management**:
  - Add, remove, and view items in the cart.
  
- **Wishlist Management**:
  - Add, remove, and view items in the wishlist.
  
- **Order Management**:
  - Place orders and view order history.

## Installation

### Prerequisites

- Python 3.6+
- Django 3.2+
- Django REST Framework

### Clone the Repository

```bash
git clone https://github.com/mohit-trootech/Ecommerce-API
cd Ecommerce-API
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Django Secret Key

You can generate a Django secret key using the following command in a Python shell:

```python
import secrets
print(secrets.token_urlsafe(50))
```

### Configure Settings

1. Add your generated secret key to the `.env` file:

```text
SECRET_KEY='your_generated_secret_key'
```

### Run Migrations

```bash
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

## Endpoints

- **User Management**
  - `POST /api/register/` - Register a new user
  - `POST /api/login/` - User login
  - `GET /api/profile/{id}` - Retrieve user profile
  - `PUT /api/profile/{id}` - Update user profile

- **Product Management**
  - `GET /api/products/` - List all products
  - `POST /api/products/` - Create a new product
  - `GET /api/products/{id}/` - Retrieve a specific product
  - `PUT /api/products/{id}/` - Update a specific product
  - `DELETE /api/products/{id}/` - Delete a specific product

- **Category Management**
  - `GET /api/categories/` - List all categories
  - `POST /api/categories/` - Create a new category
  - `GET /api/categories/{id}/` - Retrieve a specific category
  - `PUT /api/categories/{id}/` - Update a specific category
  - `DELETE /api/categories/{id}/` - Delete a specific category

- **Cart Management**
  - `GET /api/cart/` - View cart
  - `POST /api/cart/` - Add item to cart
  - `POST /api/cart/{id}/` - Remove item from cart

- **Wishlist Management**
  - `GET /api/wishlist/` - View wishlist
  - `POST /api/wishlist/` - Add item to wishlist
  - `POST /api/wishlist/{id}/` - Remove item from wishlist

- **Order Management**
  - `GET /api/orders/` - View all orders
  - `POST /api/orders/` - Place a new order
  - `GET /api/orders/{id}/` - Retrieve a specific order

## Contributions

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Reach Me

For any questions or suggestions, feel free to reach out:

- **Email**: <mohit.prajapat@trootech.com>
- **GitHub**: [mohit-trootech](https://github.com/mohit-trootech)
