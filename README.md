Library Management System API
Overview

The Library Management System API is a Django-based backend application for managing library resources. It allows users to perform CRUD operations on books and library users, as well as checkout and return books. The project uses Django REST Framework (DRF) for API creation, and user authentication is managed with Django's built-in authentication system.
Features

    CRUD Operations: Create, read, update, and delete books and library users.
    User Authentication: Login functionality using Django’s authentication system.
    Book Checkout and Return: Allows authenticated users to check out and return books.
    Transaction History: Provides checkout history for users.
    Public Book List: Displays available books to non-authenticated users.

Technologies Used

    Django: Backend framework for building the API.
    Django REST Framework: For creating and managing the API endpoints.
    PythonAnywhere: Hosting for deployment.

Project Setup
Prerequisites

    Python 3.x
    Django 4.x
    Django REST Framework

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/library-management-api.git
cd library-management-api

Create a virtual environment and activate it:

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

bash

pip install -r requirements.txt

Apply migrations:

bash

python manage.py migrate

Create a superuser:

bash

python manage.py createsuperuser

Run the server:

bash

    python manage.py runserver

API Endpoints
User Authentication

    Login: /login/

Book Management

    List all books: GET /books/
    Create a book: POST /books/
    Retrieve a book: GET /books/{id}/
    Update a book: PUT /books/{id}/
    Delete a book: DELETE /books/{id}/

User Management

    List all users: GET /users/
    Create a user: POST /users/
    Retrieve a user: GET /users/{id}/
    Update a user: PUT /users/{id}/
    Delete a user: DELETE /users/{id}/

Transactions

    Checkout a book: POST /transactions/checkout/{book_id}/
    Return a book: POST /transactions/return/{transaction_id}/
    View checkout history: GET /transactions/history/

Future Enhancements

    Search functionality: Add the ability to search for books by title, author, or ISBN.
    Reservation system: Allow users to reserve books that are currently unavailable.
    Book categories and tags: Introduce categories and tags to better organize and filter books.
    Enhanced user roles: Implement roles such as librarian, member, and guest with different access levels.