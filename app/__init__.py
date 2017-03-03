from flask import Flask
import pyrebase
import os
import json

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)

config = {
  "apiKey": "AIzaSyB07PemCqeZDjBjgJu7dAOp6gUJI7KkirE",
  "authDomain": "coffeecu-6f84a.firebaseapp.com",
  "databaseURL": "https://coffeecu-6f84a.firebaseio.com",
  "storageBucket": "coffeecu-6f84a.appspot.com",
  "messagingSenderId": "896491819806",
  "serviceAccount": "serviceAccount.json"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

with open('majors.json', 'r') as datafile:
    majors = json.load(datafile)

from app import views
