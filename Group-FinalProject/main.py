import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import util

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RentAnItemDb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    cardNo = db.Column(db.Integer)
    expDate = db.Column(db.String(30))
    cvc = db.Column(db.Integer)
    items = db.relationship('AvailableItems', backref='users', lazy=True)


class AvailableItems(db.Model):
    __tablename__ = 'available_items'
    itemId = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500))
    photoUri = db.Column(db.String(240))
    dateAdded = db.Column(db.String(50), nullable=False)
    dueDate = db.Column(db.String(50))
    rented = db.relationship('RentedItems', backref='available_items', lazy=True)


class RentedItems(db.Model):
    __tablename_ = "rented_items"
    itemId = db.Column(db.Integer, db.ForeignKey('available_items.itemId'), primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('available_items.ownerId'), nullable=False)
    dateRented = db.Column(db.String(50), nullable=False)
    dueDate = db.Column(db.String(50))