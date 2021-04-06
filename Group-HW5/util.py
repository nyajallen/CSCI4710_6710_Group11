from sklearn.cluster import KMeans
import numpy as np
import sqlite3


def query(db, query_group):
    group = {
        1: "SELECT * FROM CovidData WHERE age <=35 AND gender = 'Male'",
        2: "SELECT * FROM CovidData WHERE age >=36 AND gender = 'Male'",
        3: "SELECT * FROM CovidData WHERE age <=35 AND gender = 'Female'",
        4: "SELECT * FROM CovidData WHERE age >=36 AND gender = 'Female'"
    }

    query = group.get(query_group, "Null")

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_results


def get_country(db, country_group):
    group = {
        1: "SELECT * FROM CovidData WHERE Country = 'USA'",
        2: "SELECT * FROM CovidData WHERE Country = 'Canada'",
        3: "SELECT * FROM CovidData WHERE Country = 'UK'",
        4: "SELECT * FROM CovidData WHERE Country = 'Romania'",
        5: "SELECT * FROM CovidData WHERE Country = 'Switzerland'",
        6: "SELECT * FROM CovidData WHERE Country = 'Rwanda'",
        7: "SELECT * FROM CovidData WHERE Country = 'Cyprus'",
        8: "SELECT * FROM CovidData WHERE Country = 'Israel'",
        9: "SELECT * FROM CovidData WHERE Country = 'Portugal'",
        10: "SELECT * FROM CovidData WHERE Country = 'Ireland I'",
        11: "SELECT * FROM CovidData WHERE Country = 'Germany'",
        12: "SELECT * FROM CovidData WHERE Country = 'Australia'",
        13: "SELECT * FROM CovidData WHERE Country = 'China'",
        14: "SELECT * FROM CovidData WHERE Country = 'New Zealand'",
        15: "SELECT * FROM CovidData WHERE Country = 'Palestine'"
    }
    
    query = group.get(country_group, "Null")
                     
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def cluster_user_data(input_data, emotional_col_start=4, emotional_col_end=9, n_clusters=3):
    """
    This function cluster user data based on KMeans algorithm
    By default, it will split your data into three groups
    """
    # collect answers for five emotional questions
    # which are located from 4th col to 9th col
    emotional_data = [i[emotional_col_start:emotional_col_end] for i in input_data]
    # use kmeans to cluster data
    kmeans = KMeans(n_clusters).fit(emotional_data)
    # return cluster labels
    return kmeans.labels_


def split_user_data(input_data, labels, n_clusters=3):
    """
    this function will split input data into groups
    based on labels
    """
    result_list = []
    for i in range(n_clusters):
        # find indices of each group elements, without [0] the result is tuple
        tmp_indices = np.where(labels == i)[0]
        result_list.append([input_data[i] for i in tmp_indices])

    return result_list
