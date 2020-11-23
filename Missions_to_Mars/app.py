from mission_to_mars_v2 import scrape
from flask import Flask, jsonify, render_template
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pymongo


CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.mars

app = Flask(__name__)


@app.route("/")
def main():
    mars_data = scrape()
    return render_template("index.html", mars_data = mars_data)

@app.route("/overlords")
def overlords():
    mars_data = scrape()
    return render_template("index.html", mars_data = mars_data)

@app.route("/scrape_data")
def scrape_data():
    db.mars.insert_many(mars_data())
    return "Successfully scraped Mars data"

@app.route("/all")
def all_data():
    results = []
    for result in db.mars.find():
        results.append({key: value for key, value in result.items() if not key == "_id"})
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug = True)
