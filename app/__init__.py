from flask import Flask
import pyrebase

app = Flask(__name__)
app.config.from_object('config')

config = {
  "apiKey": "AIzaSyB07PemCqeZDjBjgJu7dAOp6gUJI7KkirE",
  "authDomain": "coffeecu-6f84a.firebaseapp.com",
  "databaseURL": "https://coffeecu-6f84a.firebaseio.com",
  "storageBucket": "coffeecu-6f84a.appspot.com",
  "messagingSenderId": "896491819806"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

from app import views