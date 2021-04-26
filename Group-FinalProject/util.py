import json
import numpy as np
import sqlite3


def get_an_item(db, username, item_name):
    owner_id_query = "SELECT ID FROM Users WHERE username= '%s'" % username

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(owner_id_query)
    owner_id = cursor.fetchall()
    owner_id = owner_id[0][0]

    query = "SELECT * FROM Available_Items WHERE item_name = '%s' AND owner_id=%d" % (item_name, owner_id)

    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_results


def get_all_items(db):
    query = "SELECT * FROM Available_Items"

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_results


def get_a_user(db, username, password):
    query = "SELECT * FROM Users WHERE username = '%s' AND password = '%s'" % (username, password) 

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_results


def insert_a_user(db, email, password, first_name="", last_name="", username="", card=0000000000000000, exp="",
                  cvc=000):
    query = "INSERT INTO Users (first_name, last_name, email, username, password, card_number, expiration_date, cvc)\
			VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    data_tuple = (first_name, last_name, email, username, password, card, exp, cvc)

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query, data_tuple)
    connection.commit()
    cursor.close()
    connection.close()


def insert_an_item(db, is_rented, item_name, category, price, owner_id=0, description="", photo_url="/static/images/item.png", date_added="",
                   date_removed=""):
    if is_rented:
        itemid = "SELECT item_id FROM Available_Items WHERE item_name ='%s' AND owner_id = %d" % (item_name, owner_id)
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(item_id)
        itemid = cursor.fetchall()

        query = "INSERT INTO rented_items (item_id, owner_id, date_rented, due_date) VALUES (?, ?, ?, ?)"
        data_tuple = (itemid, owner_id, date_added, date_removed)
    else:
        query = "INSERT INTO Available_Items (owner_id, item_name, category, price, description, photo_uri, date_added, date_removed) " \
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        data_tuple = (owner_id, item_name, category, price, description, photo_url, date_added, date_removed)

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query, data_tuple)
    connection.commit()
    cursor.close()
    connection.close()


def get_user_items(db, owner_id):
    query = "SELECT * FROM Available_Items WHERE owner_id = '%s'" % owner_id

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_results

def get_owner_id(db, username, password):
    query = "SELECT ID FROM Users WHERE username='%s' AND password='%s'" % (username, password)

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close

    return query_results

def get_username(db, owner_id):
    query = "SELECT username FROM Users WHERE ID=%d" % owner_id

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close

    return query_results

def add_to_cart(item_name, price, cart_list):
    cart_list.append((item_name, price))
    print(cart_list)

    return cart_list

def search_for_items(db, item_name):
    query = "SELECT * FROM Available_Items WHERE item_name= '%s'" % item_name

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_results

def search_for_items_cat(db, category):
    cat = {
        'Tools': 6,
        'Games': 10,
        'Appliances': 3,
        'Movies': 11,
        'Yard': 1,
        'Household': 2,
        'Recreational': 4,
        'Party': 5,
        'Electronics': 7,
        'Automotive': 8,
        'Beach': 9,
        'Miscellanious': 12
    }

    category = cat.get(category, -1)

    query = "SELECT * FROM Available_Items WHERE category= %d" % category

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_results

def convert_to_binary(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
