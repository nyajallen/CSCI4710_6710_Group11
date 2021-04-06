import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

import util

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///WebAppsDatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

covidData = db.Table('CovidData', db.metadata, autoload=True, autoload_with=db.engine)


column_names = ["index", "What country do you live in?", "How old are you?", "What is your gender?",
                "To what extent do you feel FEAR due to the coronavirus?",
                "To what extent do you feel ANXIOUS due to the coronavirus?",
                "To what extent do you feel ANGRY due to the coronavirus?",
                "To what extent do you feel HAPPY due to the coronavirus?",
                "To what extent do you feel SAD due to the coronavirus?",
                "Which emotion is having the biggest impact on you?", "What makes you feel that way?",
                "What brings you the most meaning during the coronavirus outbreak?", "What is your occupation?"]


@app.route('/')
def index():
    user_data = db.session.query(covidData).all()
    group1 = util.query('WebAppsDatabase.db', 1)
    group2 = util.query('WebAppsDatabase.db', 2)
    group3 = util.query('WebAppsDatabase.db', 3)
    group4 = util.query('WebAppsDatabase.db', 4)
    labels = util.cluster_user_data(user_data)
    return render_template('index.html', labels_html=labels, column_html=column_names, data1_html=group1, data2_html=group2, data3_html=group3, data4_html=group4)
    

if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
