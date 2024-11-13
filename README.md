<div align="center">
    <a href="[Speakeasy](https://speakeasyapi.dev/)">
        <img src="https://github.com/speakeasy-api/speakeasy/assets/68016351/e959f81a-b250-4003-8c5c-a45b9463fc95" alt="Speakeasy Logo" width="400">
        <h2>Speakeasy Flask OpenAPI Example</h2>
    </a>
</div>

This is a simple Library API built with Flask, Flask-Smorest, and SQLAlchemy. It provides endpoints to manage books in a library, including creating, reading, updating, and deleting books. The API documentation is available via Swagger UI.

## Features

* Create, read, update, and delete books
* OpenAPI documentation served via Swagger UI
* SQLite database for data storage

* **Requirements**
* Python 3.7+
* Flask
* Flask-Smorest
* Flask-SQLAlchemy
* Flask-Marshmallow
* PyYAML

## Installation
  
Clone the repository:

```bash
git clone https://github.com/speakeasy-api/openapi-flask-example.git
cd openapi-flask-example
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the Flask application:

```bash
python app.py
```

The application will start on http://127.0.0.1:5000.

## API Endpoints

* GET /books/ - List all books
* POST /books/ - Create a new book
* GET /books/<int:book_id> - Get a book by ID
* PUT /books/<int:book_id> - Update a book by ID
* DELETE /books/<int:book_id> - Delete a book by ID
* OpenAPI document is available to download at http://127.0.0.1:5000/openapi.yaml.

## Project Structure

* app.py - The main application file
* db.py - Database initialization
* models.py - Database models
* resources.py - API resources and blueprints
* schemas.py - Marshmallow schemas
