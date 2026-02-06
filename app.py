from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("API_FOOTBALL_KEY")

HEADERS = {
    "x-apisports-key": API_KEY
}

BARCA_ID = 529  # FC Barcelona

@app.route("/")
def home():
    return {"message": "Barca Live API is running"}

@app.route("/matches")
def matches():
    url = "https://v3.football.api-sports.io/fixtures"
    params = {
        "team": BARCA_ID,
        "season": 2025
    }

    r = requests.get(url, headers=HEADERS, params=params)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run()
