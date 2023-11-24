from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json

def scrape_deployable_traps():
    
    url = 'https://deadcells.wiki.gg/wiki/Deployable_traps'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', attrs={'class': 'wikitable'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    data = []
    for row in rows[1:]:  

        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        images = row.find_all('img')
        
        weapon_img = 'https://deadcells.wiki.gg' + images[0]['src']
        
        if len(images) > 1:
            scaling_img = 'https://deadcells.wiki.gg' + images[1]['src']
        else:
            scaling_img = None
        
        weapon_data = {
            'weapon': cols[1],
            'description': cols[2],
            'blueprint_location': cols[3],
            'base_dps': cols[4],
            'base_cooldown': cols[5],
            'scaling': scaling_img, 
            'weapon_img': weapon_img
        }
        data.append(weapon_data)

    return jsonify(data)
