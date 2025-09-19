from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Recipe   # now safe, since db is defined in models

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/")
    def index():
        return "Flask app is running!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5555, debug=True)
