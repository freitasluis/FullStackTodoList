from flask import Flask
from dbModels import db

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, you're using Flask!"

    @app.route("/disclaimer")
    def disclaimer():
        return "Hey, I'm trying to learn here"

    # Configure database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database
    db.init_app(app)

    # Import routes
    from apiRoutes import api
    api.init_app(app) # Register API routes

    return app


