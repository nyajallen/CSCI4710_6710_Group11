import json

from numpy as np
import sqlite

def get_an_item(db, itemId):
	query = "SELECT * FROM Available_Items WHERE item_id = %d" % itemId

	connection = sqlite3.connect(db)
    cursor = connection.cursor()
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

def get_a_user(db, username):
	query = "SELECT * FROM Users WHERE username = '%s'" % username

	connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_results

def insert_a_user(db, first_name="", last_name="", email, username="", password, card=0000000000000000, exp="", cvc=000):
	query = "INSERT INTO Users (first_name, last_name, email, username, password, card_number, exp_date, cvc)\
			VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

	data_tuple = (first_name, last_name, email, username, password, card, exp, cvc)

	connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query, data_tuple)
    connection.commit()
    cursor.close()
    connection.close()


def insert_an_item(db, isRented, owner_id=0, category, price, description="", photo_url="", date_added="", date_removed=""):

	if isRented:
		query = "INSERT INTO rented_items (owner_id, date_rented, due_date) VALUES (?, ?, ?)"
		data_tuple = (owner_id, date_added, date_removed)
	else:
		query = "INSERT INTO Available_Items (owner_id, category, price, description, photo_url, date_added, date_removed)\
				VALUES (?, ?, ?, ?, ?, ?, ?)"
		photo_url = convertToBinaryData(photo_url)
		data_tuple = (owner_id, category, price, description, photo_url, date_added, date_removed)

	connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query, data_tuple)
    connection.commit()
    cursor.close()
    connection.close()

def get_user_items(db, username):

	ownerID_query = "SELECT owner_id FROM Users WHERE username= '%s'" % username

	connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(ownerID_query)
    owner_id = cursor.fetchall()

    query = "SELECT * FROM Available_Items WHERE username = '%s'" % owner_id
    cursor.execute(query)
    query_results = cursor.fetchall()

    cursor.close()
    connection.close()

    return query_results

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
