import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' +  os.path.join(basedir, 'WebAppsDatbase.db')

db = SQLAlchemy(app)
db.Model.metadeta.reflect(db.engine)

class UserSurvey(db.Model):
    __tablename__ = "covid_data"
    id = db.Column(db.Integer, primary_key=True)
