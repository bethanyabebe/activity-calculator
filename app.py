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
    #"name", "photo_reference", "formatted_address", "pricing_level" + "rating" (optional)
    #https://maps.googleapis.com/maps/api/place/photo?photoreference=PHOTO_REFERENCE&sensor=false&maxheight=MAX_HEIGHT&maxwidth=MAX_WIDTH&key=YOUR_API_KEY 
    #return response

    #for location in response:
    # location=response["rows"][0]["elements"][0]
    # location_name = location["name"]
    # data = {
    #     'name':location_name,
    #     }
    # return render_template('results.html',data=data)

    url_place="https://maps.googleapis.com/maps/api/place/details/json?place_id="

    #for place in response["results"]:
    my_place_id = "ChIJfx3HmItZwokR7ssq4aeNH6Y"
    my_field = "name,formatted_address" 
    place_details = requests.get(url_place+my_place_id+"&fields="+my_field+"&key="+api_key).json()
    #print(place_details)
    return place_details
    #ChIJN1t_tDeuEmsRUsoyG[…]&fields=name,rating,formatted_phone_number&key=YOUR_API_KEY
    
    #clue = model.random_clue()
    # data = {
    #     'clue':clue,
    # }
    # return render_template('clue.html',data=data)