from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/api/v1/weapons', methods=['GET'])
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

        images = row.find_all('img')  # Get all images in the row
        
        weapon_img = 'https://deadcells.wiki.gg' + images[0]['src']  # Get the source of the first image 

        scaling_img = 'https://deadcells.wiki.gg' + images[1]['src']  # Get the source of the second image
        

        weapon_data = {
            'weapon': cols[1],
            'description': cols[2],
            'blueprint_location': cols[3],
            'base_dps': cols[4],
            'scaling': scaling_img, 
            'weapon_img': weapon_img
        }
        data.append(weapon_data)

    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
