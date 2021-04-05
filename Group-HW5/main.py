import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import util

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' +  os.path.join(basedir, 'WebAppsDatbase.db')

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect = True)
covidData = Base.classes.covid_data

column_names = ["index","What country do you live in?","How old are you?","What is your gender?","To what extent do you feel FEAR due to the coronavirus?","To what extent do you feel ANXIOUS due to the coronavirus?","To what extent do you feel ANGRY due to the coronavirus?","To what extent do you feel HAPPY due to the coronavirus?","To what extent do you feel SAD due to the coronavirus?","Which emotion is having the biggest impact on you?","What makes you feel that way?","What brings you the most meaning during the coronavirus outbreak?","What is your occupation?"]

@app.route('/')
def index():
    user_data = db.session.query(covidData).all()
    labels = util.cluster_user_data(user_data)
    return render_template('index.html', labels_html=labels, column_html=column_names, data_html=user_data)

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
