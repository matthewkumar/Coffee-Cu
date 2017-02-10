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

if __name__ == "__main__":
    app.run(host="0.0.0.0")

