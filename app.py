<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"
=======
from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config["DEBUG"] = True # for testing

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/name")
def name():
    return "Potato."

@app.route("/website")
def website():
    return "https://github.com/dragonkittymeowr"

#@app.route("/search")
#def search():
#    return "Search"

@app.route("/search/<search_query>")
def search(search_query):
    return search_query
>>>>>>> 901c4212c26e62a45b1d28fe16fffa6131d4a9ff

if __name__ == "__main__":
    app.run(host="0.0.0.0")

<<<<<<< HEAD

=======
>>>>>>> 901c4212c26e62a45b1d28fe16fffa6131d4a9ff
