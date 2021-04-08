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
    age = db.Column(db.String(50))  
    gender = db.Column(db.String(200))
    fearFactor = db.Column(db.String(10))
    anxiousFactor = db.Column(db.String(10))
    angerFactor = db.Column(db.String(10))
    happyFactor = db.Column(db.String(10))
    sadFactor = db.Column(db.String(10))
    emotionFactor = db.Column(db.String(10))
    whyFactor = db.Column(db.String(10))
    meaningFactor = db.Column(db.String(10))
    job = db.Column(db.String(50))
    
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
        
    def repr(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id_num,self.country, self.age,self.gender,self.fearFactor,self.anxiousFactor,self.angerFactor,self.happyFactor,self.sadFactor,self.emotionFactor,self.whyFactor,self.meaningFactor, self.job)

    def iter(self):
        return iter([self.id_num,self.country, self.age,self.gender,self.fearFactor,self.anxiousFactor,self.angerFactor,self.happyFactor,self.sadFactor,self.emotionFactor,self.whyFactor,self.meaningFactor, self.job])



    
db.create_all()
with open('t.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    #print(df)
    for line in reader:
        #print(line[0])
        response = Survey(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12])
        db.session.add(response)
        db.session.commit()

try:
    for i in df:
        '''
        s = Survey(country = "usa",age='t',gender='t',fearFactor='t',anxiousFactor='t',angerFactor='t',happyFactor='t',sadFactor='t',emotionFactor='t',whyFactor='t',meaningFactor = 't',job = 't')
        db.session.add(s)
        db.session.commit()
        '''
        #print(i[1])
except:
    print("error")

s1 = Survey.query.filter(Survey.country == 'usa').first()
print(s1.country)
    





    

# evil gloabl variable...
# the data should be obtained from your db


sample_data = {
	'user_data':[
		[1,"USA",70.0,"Male",2,2,1,2,2,"anticipation of whats going to happen next","Lot's of predictions from differnet resources","Family,Psychologist"],
		[2,"Switzerland",25.0,"Female",3,4,3,4,4,"A mix of awe and anxiety. Awe at how wonderful of a challenge this is for our world to tackle together (especially on issues that have plagued us for decades) and anxiety on how much we may not be thinking about those who are most vulnerable","Reading thought leadership articles and social media","Reading,Global Public Servant (WEF)"],
		[3,"USA",26.0,"Female",3,3,1,4,4,"A mix of happy to be safe and home and sad for people who aren't","Seeing what's happening in the news","Family,Student"],
		[4,"USA",11.0,"Male",2,1,5,1,3,"Anger,No sports" ,"Family,Student"],
		[5,"USA",28.0,"Male",4,3,4,1,4,"Anger","a system that cares about profit more than general wellbeing","trying to help","reporter"],
		[6,"USA",24.0,"Female",4,4,5,1,4,"Anger","The US federal government" ,"Friends","Graduate student"],
		[7,"USA",21.0,"Female",4,3,5,3,2,"Anger","People are not being responsible in doing their part in staying in doors. It is causing a major spread in our environment. Due to this spread, I am not allowed to be outdoors or stay in my apartment in Austin. I am very active outside, so this is a challenge for me to stay inside. ","Being alone,Student"],
		[8,"USA",22.0,"Male",3,4,5,2,1,"Anger","Inaction of the people and government","Friends","Janitor"],
		[9,"USA",39.0,"Male",2,2,4,1,2,"Anger","Impacts on day-to-day life","Exercising","Software Engineer"],
		[10,"USA",78.0,"Male",5,5,5,1,1,"Anger","National leadership incompetence","Family","Executive retired"]		
	]
}



@app.route('/')
def index():
    labels = util.cluster_user_data(sample_data['user_data'])
    return render_template('index.html', labels_html=labels, column_html=column_names, data_html=sample_data['user_data'])


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

