# -- Flask Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

import requests
import smtplib
import os
import random

# Additional Imports
import datetime as dt
import model as model

# -- Initialization section --
app = Flask(__name__)
app.jinja_env.globals['current_time'] = dt.datetime.now()

# -- Routes --


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/results', methods=["POST"])
def results():
    form = request.form
    distance = form['distance']
    cost = form['cost']
    level = form['type']
    preference = form['preference']
    latitude = form['latitude']
    longitude = form['longitude']
    #api key
    api_key = str(os.getenv("api_key"))
    if level == "active":
        activities = ['amusement_park', 'aquarium', 'art_gallery', 'bowling_alley', 'cafe', 'campground', 'gym', 'library', 'movie_theater', 'museum', 'park', 'restaurant']
        activity = random.choice(activities)
    else:
        activities = ['aquarium', 'art_gallery', 'cafe', 'library', 'movie_theater', 'museum', 'park', 'restaurant']
        activity = random.choice(activities)
    # place search - for later
    #https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=43.6514467,%20-79.37950889999999&type=restaurant&radius=5000&key=AIzaSyCnN73kgwTBjjYGNg3HIfB5e9_KrtwqkfQ
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    # get response
    #r = requests.get(url + "location=" + lat + "%" + long + "&type=" + activity + "&radius=" + distance + "&key=" + api_key)
    #return render_template('results.html')
    
    response = requests.get(url + "location=" + latitude + ",%20" + longitude + "&type=" + activity + "&radius=" + "5000" + "&key=" + api_key).json()
    return response
