import json

from sklearn.cluster import KMeans
import numpy as np
import sqlite3


def query(db, query_group, country):
    group = {
        1: "SELECT * FROM CovidData WHERE age <=35 AND gender = 'Male'",
        2: "SELECT * FROM CovidData WHERE age >=36 AND gender = 'Male'",
        3: "SELECT * FROM CovidData WHERE age <=35 AND gender = 'Female'",
        4: "SELECT * FROM CovidData WHERE age >=36 AND gender = 'Female'"
    }

    query = group.get(query_group, "Null") + " AND country = '%s' COLLATE NOCASE" % (country)

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(query)
    query_results = cursor.fetchall()
    cursor.close()
    connection.close()

    if len(query_results) >= 10:
        labels = cluster_user_data(query_results)
        query_results = split_user_data(query_results, labels)

    description = {
        1: "This group contains users from %s and are young males" % country,
        2: "This group contains users from %s and are middle-aged to old males" % country,
        3: "This group contains users from %s and are young females" % country,
        4: "This group contains users from %s and are middle-aged to old females" % country
    }

    group_desc = description.get(query_group, "Null")

    survey_query_results = {
        'group %s' % query_group: {'group_desc': group_desc,
                                   'query_results': query_results}
    }

    return survey_query_results


def get_country(data):
    return data[1]


def parse_team(query_result):
    """
    this function jsonifies team query results
    """
    result_list = []
    for element in query_result:
        result_list.append({'team_name': element.name, 'id': element.id})
    # print({'all_teams':result_list})
    return json.dumps({'all_teams': result_list})


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
