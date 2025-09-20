from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from app import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    image_url = db.Column(db.String)

    # Relationship
    recipes = db.relationship('Recipe', back_populates='user')

    # Prevent recursion in serialization
    serialize_rules = ('-recipes.user',)


class Recipe(db.Model, SerializerMixin):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    minutes_to_complete = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='recipes')

    serialize_rules = ('-user.recipes',)
