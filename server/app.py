from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # Import models so Alembic sees them
    from models import User, Recipe

    @app.route('/')
    def index():
        return "Flask app is running!"

    return app


# Entry point
if __name__ == "__main__":
    app = create_app()
    app.run(port=5555, debug=True)
