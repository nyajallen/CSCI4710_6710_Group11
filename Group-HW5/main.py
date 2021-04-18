import json
import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import util

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///WebAppsDatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

covidData = db.Table('CovidData', db.metadata, autoload=True, autoload_with=db.engine)

SURVEY_DATA_COUNTRY = ['China', 'United States of America', 'United Kingdom', 'Canada', 'Romania', 'Switzerland',
                       'Rwanda', 'Hong Kong', 'France', 'Cyprus', 'Spain', 'Columbia',
                       'Israel', 'Portugal', 'Ireland I', 'Germany', 'Australia', 'New Zealand', 'Palestine']

column_names = ["index", "What country do you live in?", "How old are you?", "What is your gender?",
                "To what extent do you feel FEAR due to the coronavirus?",
                "To what extent do you feel ANXIOUS due to the coronavirus?",
                "To what extent do you feel ANGRY due to the coronavirus?",
                "To what extent do you feel HAPPY due to the coronavirus?",
                "To what extent do you feel SAD due to the coronavirus?",
                "Which emotion is having the biggest impact on you?", "What makes you feel that way?",
                "What brings you the most meaning during the coronavirus outbreak?", "What is your occupation?"]


@app.route('/api/query_survey_results/<country_name>', methods=['GET'])
def query_survey_results(country_name=''):

    if country_name in SURVEY_DATA_COUNTRY:
        if country_name == 'United States of America':
            country_name = 'USA'
        elif country_name == 'United Kingdom':
            country_name = 'UK'
        elif country_name == 'Cyprus':
            country_name = 'C yprus'

        group = [1, 2, 3, 4]
        survey_query_data = {}
        for x in group:
            query_result = util.query('WebAppsDatabase.db', x, country_name)
            split_result = util.split_and_desc(query_result, x, country_name)
            survey_query_data.update(split_result)
    else:
        survey_query_data = {'user_data': [country_name + " does not have any survey data"]}

    return json.dumps(survey_query_data)


@app.route('/query_tables')
def query_tables():
    # list of group numbers
    groups = [1, 2, 3, 4]
    # list to hold group data
    user_data = []
    # list of all countries
    countries = ['USA', 'Canada', 'UK', 'Romania', 'Switzerland', 'Rwanda', 'Hong Kong', 'France', 'C yprus', \
                 'Israel', 'Portugal', 'Ireland I', 'Germany', 'Australia', 'China', 'New Zealand', 'Palestine']
    # loop to query data for each group
    for x in groups:
        # loop split data by country
        for country in countries:
            data = util.query('WebAppsDatabase.db', x, country)

            # loop to split data if there are more than 10 elements
            if len(data) >= 10:
                labels = util.cluster_user_data(data)
                data = util.split_user_data(data, labels)

            # adds data to user_data list
            user_data.append(data)
    # loop to see if an element is a list of split data 
    # Only used to see which countries are at which index and have split data
    for data in user_data:
        if len(data) != 0:
            print(data[0][1])
            print(user_data.index(data))
            print("\n")
            if isinstance(data[0], list):
                country = util.get_country(data[0][0])
                print("***SPLIT***")
                print(country)
                print(user_data.index(data))
                print("\n")
    
    return render_template('index.html', column_html=column_names, 
        data1usa1_html= user_data[0][0], data1usa2_html= user_data[0][1], data1usa3_html= user_data[0][2],
        data1canada_html=user_data[1], data1uk_html=user_data[2],
        data1romania1_html=user_data[3][0], data1romania2_html=user_data[3][1], data1romania3_html=user_data[3][2],
        data1switz_html=user_data[4], data1rwanda_html= user_data[5], data1isreal_html=user_data[9], data1germany_html= user_data[12], 
        data2usa1_html= user_data[17][0], data2usa2_html= user_data[17][1], data2usa3_html= user_data[17][2],
        data2canada_html=user_data[18], data2uk_html=user_data[19], data2romania_html=user_data[20], data2switz_html=user_data[21],
        data2rwanda_html= user_data[22], data2hongkong_html=user_data[23], data2france_html=user_data[24],
        data2germany_html= user_data[29], data2nz_html=user_data[32], data2pal_html=user_data[33],
        data3usa1_html= user_data[34][0], data3usa2_html= user_data[34][1], data3usa3_html= user_data[34][2],
        data3canada_html=user_data[35], data3uk_html=user_data[36],
        data3romania1_html=user_data[37][0], data3romania2_html=user_data[37][1], data3romania3_html=user_data[37][2],
        data3switz1_html=user_data[38][0], data3switz2_html=user_data[38][1], data3switz3_html=user_data[38][2],
        data3rwanda_html= user_data[39], data3portugal_html=user_data[44],
        data3ireland_html=user_data[45], data3germany_html= user_data[46], data3australia_html=user_data[47], data3china_html=user_data[48],
        data4usa1_html= user_data[51][0], data4usa2_html= user_data[51][1], data4usa3_html= user_data[51][2],
        data4canada1_html=user_data[52][0], data4canada2_html=user_data[52][1], data4canada3_html=user_data[52][2],
        data4uk_html=user_data[53], data4romania1_html=user_data[54][0], data4romania2_html=user_data[54][1], data4romania3_html=user_data[54][2],
        data4switz_html=user_data[55], data4portugal_html=user_data[61], data4germany_html= user_data[63], data4australia_html=user_data[64])
    

@app.route('/')
def index():
    return render_template('intro.html')

@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
