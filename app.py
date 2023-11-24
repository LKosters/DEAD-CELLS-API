from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
from flask import render_template

from scrapers.weapons.melee_weapons import scrape_melee_weapons
from scrapers.weapons.ranged_weapons import scrape_ranged_weapons
from scrapers.weapons.shields import scrape_shields
from scrapers.weapons.deployable_traps import scrape_deployable_traps

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/api/v1/melee-weapons', methods=['GET'])
def get_melee_weapons():
    return scrape_melee_weapons()

@app.route('/api/v1/ranged-weapons', methods=['GET'])
def get_ranged_weapons():
    return scrape_ranged_weapons()

@app.route('/api/v1/shields', methods=['GET'])
def get_shields():
    return scrape_shields()

@app.route('/api/v1/deployable-traps', methods=['GET'])
def get_deployable_traps():
    return scrape_deployable_traps()

if __name__ == '__main__':
    app.run(port=5000)
