from flask import Flask, render_template
import util
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect


#-*- mode: python -*-
#-*- coding: utf-8 -*-

# get current app directory
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

# define SQLAlchemy URL, a configuration parameter
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# The db object instantiated from the class SQLAlchemy represents the database and
# provides access to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy(app)


class Survey(db.Model):
    __tablename__ = 'data-survey'
    index = db.Column( 'id_num',db.Integer,  primary_key=True)
    country = db.Column(db.String(100))
    age = db.Column(db.Integer)  
    gender = db.Column(db.String(10))
    fearFactor = db.Column(db.Integer)
    anxiousFactor = db.Column(db.Integer)
    angerFactor = db.Column(db.Integer)
    happyFactor = db.Column(db.Integer)
    sadFactor = db.Column(db.Integer)
    emotionFactor = db.Column(db.Text())
    whyFactor = db.Column(db.Text())
    meaningFactor = db.Column(db.Text())
    job = db.Column(db.Text())
    
    def __init__(self, index, country, age, gender, fearFactor, anxiousFactor, angerFactor, happyFactor, sadFactor, emotionFactor, whyFactor, meaningFactor, job):
        self.id_num = index
        self.country = country
        self.age = age
        self.gender = gender
        self.fearFactor = fearFactor
        self.anxiousFactor = anxiousFactor
        self.angerFactor = angerFactor
        self.happyFactor = happyFactor
        self.sadFactor = sadFactor
        self.emotionFactor = emotionFactor
        self.whyFactor = whyFactor
        self.meaningFactor = meaningFactor
        self.job = job
        
    #def __getitem__(self):
        #return self.id_num,self.country, self.age,self.gender,self.fearFactor,self.anxiousFactor,self.angerFactor,self.happyFactor,self.sadFactor,self.emotionFactor,self.whyFactor,self.meaningFactor, self.job
        
    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id_num,self.country, self.age,self.gender,self.fearFactor,self.anxiousFactor,self.angerFactor,self.happyFactor,self.sadFactor,self.emotionFactor,self.whyFactor,self.meaningFactor, self.job)

    def __iter__(self):
        return iter([self.index,self.country, self.age,self.gender,self.fearFactor,self.anxiousFactor,self.angerFactor,self.happyFactor,self.sadFactor,self.emotionFactor,self.whyFactor,self.meaningFactor, self.job])



db.drop_all()    
db.create_all()
with open('t.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    #print(df)
    for line in reader:
        #print(line[0])
        response = Survey(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9].decode('utf-8'), line[10].decode('utf-8'), line[11].decode('utf-8'), line[12].decode('utf-8'))
        db.session.add(response)
        db.session.commit()



#table = Survey.query.all()
#def object_as_dict(obj):
    #return {c.key: getattr(obj, c.key)
            #for c in inspect(obj).mapper.column_attrs}


#try:
    #user_dict = object_as_dict(table)
    #for row in table:
        #print(object_as_dict(row))
    #for row in user_data:
        #print(row._asdict())
        #user_data.append(row.index,row.country,row.age,row.gender,row.fearFactor,row.anxiousFactor,row.angerFactor,row.happyFactor,row.sadFactor,row.emotionFactor,row.whyFactor,row.meaningFactor,row.job)
#except:
    #print("error")

column_names = ["index","What country do you live in?","How old are you?","What is your gender?","To what extent do you feel FEAR due to the coronavirus?","To what extent do you feel ANXIOUS due to the coronavirus?","To what extent do you feel ANGRY due to the coronavirus?","To what extent do you feel HAPPY due to the coronavirus?","To what extent do you feel SAD due to the coronavirus?","Which emotion is having the biggest impact on you?","What makes you feel that way?","What brings you the most meaning during the coronavirus outbreak?","What is your occupation?"]



@app.route('/')
def index():
    #labels = util.cluster_user_data(Survey.query.all())
    return render_template('index.html', column_html=column_names, data_html=Survey.query.all())


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

