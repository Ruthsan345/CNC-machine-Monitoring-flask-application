from flask import Flask,redirect,url_for,request,render_template,jsonify
import requests 
import json
import pprint 
import os
from jinja2 import Template

app=Flask(__name__)

@app.route("/suggestion/")
def videopage():
    return render_template('video.html')

@app.route("/contacts")
def contact():
    return render_template('contact.html')

@app.route("/character/<int:charId>/<name>")
def pro(charId,name):
    response=apireq()
    for item in response['results']:
        if(item['id'] == charId):
            response=item
            comic = requests.get(response['comics']['collectionURI']+'?ts=1&apikey=dc007599f10a375a5e4eb42d0416e503&hash=3e59e1c6112551c5a0f70dc69c30911a')
            comic = comic.json()
    if comic["data"]["count"] <= 4:
        return render_template('404.html',response=response)
    else:    
        return render_template('pro.html',response=response,apicomic=comic['data']['results'])

@app.route("/error/")
def errorpage():
    return render_template('login.html',error='Invalid Username and Password !!Please try again')

@app.route("/",methods=['POST','GET'])
def index():
    response = requests.get('https://gateway.marvel.com/v1/public/characters?limit=100&ts=1&apikey=dc007599f10a375a5e4eb42d0416e503&hash=3e59e1c6112551c5a0f70dc69c30911a')
    response = response.json()
    f = open("json/data.json", "w")
    f.write(json.dumps(response['data'], indent=4, sort_keys=True))
    f.close()
    comic = requests.get('https://gateway.marvel.com:443/v1/public/comics?ts=1&apikey=dc007599f10a375a5e4eb42d0416e503&hash=3e59e1c6112551c5a0f70dc69c30911a')
    comic = comic.json()
    return render_template('index.html',response=response,apicomic=comic['data']['results'])

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =='POST':
        user=request.form['name']
        pass1=request.form['pass']
        if user == pass1:
            return redirect(url_for('successpage',name=user))
        else:
            return redirect(url_for('errorpage'))

    else:
        user=request.args.get('name')
        return redirect(url_for('successpage',name=user))

def apireq():
    with open("json/data.json") as blog_file:
        data = json.load(blog_file)
    return data

if __name__=="__main__":
    app.run(debug=True)