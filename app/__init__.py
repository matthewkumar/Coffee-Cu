from flask import Flask
from flask_mail import Mail, Message
import pyrebase
import os

app = Flask(__name__)
mail = Mail(app)
app.config.from_object('config')
app.secret_key = os.urandom(24)

config = {
  "apiKey": "AIzaSyB07PemCqeZDjBjgJu7dAOp6gUJI7KkirE",
  "authDomain": "coffeecu-6f84a.firebaseapp.com",
  "databaseURL": "https://coffeecu-6f84a.firebaseio.com",
  "storageBucket": "coffeecu-6f84a.appspot.com",
  "messagingSenderId": "896491819806"
}
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'coffeeatcu@gmail.com',
	MAIL_PASSWORD = 'abcabc123'
	)

mail = Mail(app)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

from app import views