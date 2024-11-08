from flask import Flask
from flask_smorest import Api
from db import db
import models
from resources import blp as BookBlueprint

app = Flask(__name__)
app.config["API_TITLE"] = "Library API"
app.config["API_VERSION"] = "v0.0.1"
app.config["OPENAPI_VERSION"] = "3.1.0"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database-file.db"

db.init_app(app)
api = Api(app)
api.register_blueprint(BookBlueprint)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
