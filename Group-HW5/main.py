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
    
    grp1usa = util.query('WebAppsDatabase.db', 1, 'USA')
    grp1canada = util.query('WebAppsDatabase.db', 1, 'Canada')
    grp1uk = util.query('WebAppsDatabase.db', 1, 'UK')
    grp1romania = util.query('WebAppsDatabase.db', 1, 'Romania')
    grp1switz = util.query('WebAppsDatabase.db', 1, 'Switzerland')
    grp1rwanda = util.query('WebAppsDatabase.db', 1, 'Rwanda')
    grp1cyprus = util.query('WebAppsDatabase.db', 1, 'Cyprus')
    grp1isreal = util.query('WebAppsDatabase.db', 1, 'Isreal')
    grp1portugal = util.query('WebAppsDatabase.db', 1, 'Portugal')
    grp1ireland = util.query('WebAppsDatabase.db', 1, 'Ireland I')
    grp1germany = util.query('WebAppsDatabase.db', 1, 'Germany')
    grp1australia = util.query('WebAppsDatabase.db', 1, 'Australia')
    grp1china = util.query('WebAppsDatabase.db', 1, 'China')
    grp1nz = util.query('WebAppsDatabase.db', 1, 'New Zealand')
    grp1pal = util.query('WebAppsDatabase.db', 1, 'Palestine')

    grp2usa = util.query('WebAppsDatabase.db', 2, 'USA')
    grp2canada = util.query('WebAppsDatabase.db', 2, 'Canada')
    grp2uk = util.query('WebAppsDatabase.db', 2, 'UK')
    grp2romania = util.query('WebAppsDatabase.db', 2, 'Romania')
    grp2switz = util.query('WebAppsDatabase.db', 2, 'Switzerland')
    grp2rwanda = util.query('WebAppsDatabase.db', 2, 'Rwanda')
    grp2cyprus = util.query('WebAppsDatabase.db', 2, 'Cyprus')
    grp2isreal = util.query('WebAppsDatabase.db', 2, 'Isreal')
    grp2portugal = util.query('WebAppsDatabase.db', 2, 'Portugal')
    grp2ireland = util.query('WebAppsDatabase.db', 2, 'Ireland I')
    grp2germany = util.query('WebAppsDatabase.db', 2, 'Germany')
    grp2australia = util.query('WebAppsDatabase.db', 2, 'Australia')
    grp2china = util.query('WebAppsDatabase.db', 2, 'China')
    grp2nz = util.query('WebAppsDatabase.db', 2, 'New Zealand')
    grp2pal = util.query('WebAppsDatabase.db', 2, 'Palestine')


    grp3usa = util.query('WebAppsDatabase.db', 3, 'USA')
    grp3canada = util.query('WebAppsDatabase.db', 3, 'Canada')
    grp3uk = util.query('WebAppsDatabase.db', 3, 'UK')
    grp3romania = util.query('WebAppsDatabase.db', 3, 'Romania')
    grp3switz = util.query('WebAppsDatabase.db', 3, 'Switzerland')
    grp3rwanda = util.query('WebAppsDatabase.db', 3, 'Rwanda')
    grp3cyprus = util.query('WebAppsDatabase.db', 3, 'Cyprus')
    grp3isreal = util.query('WebAppsDatabase.db', 3, 'Isreal')
    grp3portugal = util.query('WebAppsDatabase.db', 3, 'Portugal')
    grp3ireland = util.query('WebAppsDatabase.db', 3, 'Ireland I')
    grp3germany = util.query('WebAppsDatabase.db', 3, 'Germany')
    grp3australia = util.query('WebAppsDatabase.db', 3, 'Australia')
    grp3china = util.query('WebAppsDatabase.db', 3, 'China')
    grp3nz = util.query('WebAppsDatabase.db', 3, 'New Zealand')
    grp3pal = util.query('WebAppsDatabase.db', 3, 'Palestine')

    grp4usa = util.query('WebAppsDatabase.db', 4, 'USA')
    grp4canada = util.query('WebAppsDatabase.db', 4, 'Canada')
    grp4uk = util.query('WebAppsDatabase.db', 4, 'UK')
    grp4romania = util.query('WebAppsDatabase.db', 4, 'Romania')
    grp4switz = util.query('WebAppsDatabase.db', 4, 'Switzerland')
    grp4rwanda = util.query('WebAppsDatabase.db', 4, 'Rwanda')
    grp4cyprus = util.query('WebAppsDatabase.db', 4, 'Cyprus')
    grp4isreal = util.query('WebAppsDatabase.db', 4, 'Isreal')
    grp4portugal = util.query('WebAppsDatabase.db', 4, 'Portugal')
    grp4ireland = util.query('WebAppsDatabase.db', 4, 'Ireland I')
    grp4germany = util.query('WebAppsDatabase.db', 4, 'Germany')
    grp4australia = util.query('WebAppsDatabase.db', 4, 'Australia')
    grp4china = util.query('WebAppsDatabase.db', 4, 'China')
    grp4nz = util.query('WebAppsDatabase.db', 4, 'New Zealand')
    grp4pal = util.query('WebAppsDatabase.db', 4, 'Palestine')
    

    labels = util.cluster_user_data(user_data)
    return render_template('index.html', labels_html=labels, column_html=column_names, 
        data1usa_html= grp1usa, data1canada_html=grp1canada, data1uk_html=grp1uk, data1romania_html=grp1romania, data1switz_html=grp1switz,
        data1rwanda_html= grp1rwanda, data1cyprus_html=grp1cyprus, data1isreal_html=grp1isreal, data1portugal_html=grp1portugal, data1ireland_html=grp1ireland,
        data1germany_html= grp1germany, data1australia_html=grp1australia, data1china_html=grp1china, data1nz_html=grp1nz, data1pal_html=grp1pal,
        data2usa_html= grp2usa, data2canada_html=grp2canada, data2uk_html=grp2uk, data2romania_html=grp2romania, data2switz_html=grp2switz,
        data2rwanda_html= grp2rwanda, data2cyprus_html=grp2cyprus, data2isreal_html=grp2isreal, data1por2ugal_html=grp2portugal, data2ireland_html=grp2ireland,
        data2germany_html= grp2germany, data2australia_html=grp2australia, data2china_html=grp2china, data2nz_html=grp2nz, data2pal_html=grp2pal,
        data3usa_html= grp3usa, data3canada_html=grp3canada, data3uk_html=grp3uk, data3romania_html=grp3romania, data3switz_html=grp3switz,
        data3rwanda_html= grp3rwanda, data3cyprus_html=grp3cyprus, data3isreal_html=grp3isreal, data3portugal_html=grp3portugal, data3ireland_html=grp3ireland,
        data3germany_html= grp3germany, data3australia_html=grp3australia, data3china_html=grp3china, data3nz_html=grp3nz, data3pal_html=grp1pal,
        data4usa_html= grp4usa, data4canada_html=grp4canada, data4uk_html=grp4uk, data4romania_html=grp4romania, data4switz_html=grp4switz,
        data4rwanda_html= grp4rwanda, data4cyprus_html=grp4cyprus, data4isreal_html=grp4isreal, data4portugal_html=grp4portugal, data4ireland_html=grp4ireland,
        data4germany_html= grp4germany, data4australia_html=grp4australia, data4china_html=grp4china, data4nz_html=grp4nz, data4pal_html=grp4pal)
    

if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
