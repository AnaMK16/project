from flask import Flask,  redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string
import requests

#create Flask object
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SECRET_KEY"] = "python"
#create database object
db = SQLAlchemy(app) 

# create class Urls which is a child class of db.Model
class Urls(db.Model): #create columns 
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    long = db.Column(db.String(250), nullable=False)
    short = db.Column(db.String(10), nullable=False)
#varible names have to match the column names in a database
    def __str__(self):
        return f'{self.short} {self.long}' 
# db.create_all()

          


@app.route('/<path:url>')
def shorten_url(url):
    #selects all columns where url(function parameter) is same as any rows of long(column)
    url1 = Urls.query.filter_by(long=url).first()
    
    
    if not url1: # if there is no record which follows the condition, the following code block will be executed
        letters = string.ascii_lowercase + string.ascii_uppercase
    
        rand_letters = random.choices(letters, k=3) #generates 3 random strings
        rand_letters = "".join(rand_letters) 
    
    
    
        #create Urls object 

        u1 = Urls(long=url, short=rand_letters) 
        db.session.add(u1)
        db.session.commit() #inserts the object in a database as a new recod 
        selectUrl =  Urls.query.filter_by(long=url).first() 
        return str(selectUrl)  # selects this record and returns it
    return str(url1)    
        
        
        

        
        

@app.route('/display/<name>')
def long_url(name):
    filtered_url = Urls.query.filter_by(short=name).first() #selects the row where name(function parameter) is same as any value of short(Column) 

    if filtered_url:  #if filtered_url returns some value longurl selects row where name is same as short
        longurl = Urls.query.filter_by(short=name).first()
        return redirect(longurl.long) #redirects to the url 
        

        
        


            

if __name__=='__main__':
    app.run(debug=True)        #runs server

            
