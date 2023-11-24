from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
from flask import render_template

from scrapers.melee_weapons import scrape_melee_weapons


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/api/v1/weapons', methods=['GET'])
def get_weapons():
    return scrape_melee_weapons()

if __name__ == '__main__':
    app.run(port=5000)
