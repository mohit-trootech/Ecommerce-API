# Todos API

## Overview

A simple RESTful API built with Django Rest Framework for managing todos with basic CRUD operations.

## Features

- Supports over 100,000 records with pagination.
- GET requests require no authentication.
- POST, PATCH, PUT, DELETE requests require an API key.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework

## API Endpoints

- `GET /api/todos/?page={page}`: Retrieve todos with pagination.
- `POST /api/todos/`: Create a new todo (API Key required).
- `PATCH /api/todos/{id}/`: Update a todo (API Key required).
- `PUT /api/todos/{id}/`: Replace a todo (API Key required).
- `DELETE /api/todos/{id}/`: Delete a todo (API Key required).

## Installation & Configuration

- Clone the repository:

```bash
git clone https://github.com/mohit-trootech/api-todos
cd api-todos
```

- Install dependencies:

```bash
# Install Virtual Envirnment - *recomended*
pip install -r requirements.txt
```

- Install Dependencies:

- Configure Settings:

Update `settings.py` with API keys and database configuration.
Generate a secret key:

```bash
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

- Run Migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

- Create Admin User

```bash
python manage.py createsuperuser
```

- Start Server:

```bash
python manage.py runserver
```

## Contributing

Feel free to submit issues, propose changes, or contribute directly through pull requests.

## License

This project is licensed under the MIT License.
