import os

from flask import Flask, render_template, jsonify, json, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus

import util

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RentAnItemDb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'for cookies'

db = SQLAlchemy(app)
ownerId = 0
username=''
password=''
shopping_cart=[0]

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


@app.route('/')
def index():
    items = util.get_all_items('RentAnItemDb.db')
    items_with_owners = []
    print(items)
    print('\n\n')
    
    for item in items:
        addname = list(item)
        name= util.get_username('RentAnItemDb.db', item[1])
        name= name[0]
        addname.append(name)
        items_with_owners.append(addname)


    print(items_with_owners)
    return render_template('index.html', items_list= items_with_owners)


@app.route('/login')
def login():
  return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/readmore/<ownername>/<item_name>')
def readmore(ownername, item_name):
    item = util.get_an_item('RentAnItemDb.db', ownername, item_name)
    return render_template('read_more.html', item_name=item[0][2], price=item[0][4], description=item[0][5], date_added=item[0][6], 
                            end_date=item[0][7], owner= ownername)


@app.route('/checkout')
def checkout():
    return render_template('checkout.html', items_list=shopping_cart)


@app.route('/addItem')
def add_item():
    return render_template('AddItem.html')

@app.route('/account')
def account():
    if ownerId == 0:
        flash('You are not signed in')
    else:
        userinfo = util.get_a_user('RentAnItemDb.db', username, password)
        print(userinfo[0][1])
        return render_template('account.html', firstname= userinfo[0][1], lastname= userinfo[0][2], email= userinfo[0][3], username= username)

    return render_template('account.html')

@app.route('/cart/<item_name>/<price>/<time>')
def add_to_cart(item_name, price, time):
    global shopping_cart
    shopping_cart = util.add_to_cart(item_name, price + "/" + time, shopping_cart)
    shopping_cart[0] = shopping_cart[0] + float(price)

    flash('Item added to your cart!')

    
    return render_template('index.html')

@app.route('/api/saveItem', methods=['POST'])
def save_new_item():
    item_name = request.form['item_name']
    category = request.form['category']
    price = request.form['price'] + '/' + request.form['per']
    description = request.form['description']
    date_added = request.form['date_added']
    due_date = request.form['due_date']

    util.insert_an_item('RentAnItemDb.db', False, item_name, category, price, ownerId, description, "", date_added, due_date)

    return render_template('read_more.html')
                              
@app.route('/api/signup', methods=['POST'])
def add_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    global username 
    username = request.form['username']
    global password
    password = request.form['password']
    global ownerId

    util.insert_a_user('RentAnItemDb.db', email, password, first_name, last_name, username)
    ownerId = util.get_owner_id('RentAnItemDb.db', username, password)
    ownerId = ownerId[0][0]
    print(ownerId)
    return render_template('account.html', firstname= first_name, lastname= last_name, email= email, username=username)

@app.route('/api/login', methods=['POST'])
def login_a_user():
    global username
    username = request.form['Uname']
    global password
    password = request.form['Pass']
    global ownerId
    ownerId = util.get_owner_id('RentAnItemDb.db', username, password)
    ownerId = ownerId[0]
    print(ownerId)

    userinfo = util.get_a_user('RentAnItemDb.db', username, password)
    print(userinfo[0][1])
    return render_template('account.html', firstname= userinfo[0][1], lastname= userinfo[0][2], email= userinfo[0][3], username= username)


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)
