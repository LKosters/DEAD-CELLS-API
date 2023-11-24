from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

@app.route('/')
def scrape_and_return_json():
    
    url = 'https://deadcells.wiki.gg/wiki/Melee_weapons'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', attrs={'class': 'wikitable'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    data = []
    for row in rows[1:]:  

        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        img = row.find('img')['src']  

        weapon_data = {
            'weapon': cols[1],
            'description': cols[2],
            'blueprint_location': cols[3],
            'base_dps': cols[4],
            'scaling': scaling,  # Add the scaling value to the weapon_data dictionary
            'image': img
        }
        data.append(weapon_data)

    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
