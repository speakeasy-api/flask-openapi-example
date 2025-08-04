<div align="center">
 <a href="https://www.speakeasy.com/" target="_blank">
  <img width="1500" height="500" alt="Speakeasy" src="https://github.com/user-attachments/assets/0e56055b-02a3-4476-9130-4be299e5a39c" />
 </a>
 <br />
 <br />
  <div>
   <a href="https://speakeasy.com/docs/create-client-sdks/" target="_blank"><b>Docs Quickstart</b></a>&nbsp;&nbsp;//&nbsp;&nbsp;<a href="https://go.speakeasy.com/slack" target="_blank"><b>Join us on Slack</b></a>
  </div>
 <br />

</div>

<hr />

This is a simple Library API built with Flask, `flask-smorest`, and SQLAlchemy. It provides the endpoints used to manage books in a library, including creating, reading, updating, and deleting books. The API documentation is available via Swagger UI.

## Features

* Create, read, update, and delete books
* OpenAPI documentation served via Swagger UI
* SQLite database for data storage

## Prerequisites:

* Python 3.7+
* Flask
* `flask-smorest`
* Flask-SQLAlchemy
* `flask-marshmallow`
* PyYAML


## Installation
  
Clone the repository:

```bash
git clone https://github.com/speakeasy-api/openapi-flask-example.git
cd openapi-flask-example
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

Run the Flask application:

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`.

## API endpoints

* GET /books/ - List all books
* POST /books/ - Create a new book
* GET /books/<int:book_id> - Get a book by ID
* PUT /books/<int:book_id> - Update a book by ID
* DELETE /books/<int:book_id> - Delete a book by ID
* OpenAPI document is available to download at `http://127.0.0.1:5000/openapi.yaml`.

## Project structure

* `app.py` - The main application file
* `db.py` - Database initialization
* `models.py` - Database models
* `resources.py` - API resources and blueprints
* `schemas.py` - Marshmallow schemas
