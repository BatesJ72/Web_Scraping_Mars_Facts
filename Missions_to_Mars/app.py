from mission_to_mars_v2 import scrape
from flask import Flask, jsonify, render_template
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pymongo


CONN = os.getenv("MONGO_URI")
client = pymongo.MongoClient(CONN)
db = client.mars

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")
    

@app.route("/scrape_data")
def scrape_data():
    db.mars.insert_many(scrape())
    return "Successfully scraped Mars data"

@app.route("/all")
def all_data():
    results = []
    for result in db.mars.find():
        results.append({key: value for key, value in result.items() if not key == "_id"})
    return jsonify(results)


# @app.route("/fact_table")
# def fact_table():
#     return mars_fact_table.html

if __name__ == "__main__":
    app.run(debug = True)