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
            survey_query_data.update(query_result)
    else:
        survey_query_data = {'user_data': [country_name + " does not have any survey data"]}

    return json.dumps(survey_query_data)


@app.route('/')
def index():
    return render_template('map.html')


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
