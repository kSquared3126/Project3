from flask import Flask, render_template, jsonify, request
from requests.models import Response
import numpy as np
import requests
import csv
from csv import DictWriter
import json

deck = "86e0mbm72b4b"
begin = f"https://deckofcardsapi.com/api/deck/{deck}/draw/?count=2"
draw1 = f"https://deckofcardsapi.com/api/deck/{deck}/draw/?count=1"

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET": 

        return render_template('index.html')

#take username submission
    if request.method == 'POST': 

#dealer start
        response = requests.get(begin).text 
        response_info = json.loads(response)
        dealer_list = []
        dealer_list = response_info['cards'][0]['value'], response_info['cards'][1]['value']
        dealer_list = list(dealer_list)
        dcard1 = response_info['cards'][0]['image']
        dcard2 = response_info['cards'][1]['image']
       
                
#player start
        response = requests.get(begin).text 
        response_info = json.loads(response)
        player_list = []
        player_list = response_info['cards'][0]['value'], response_info['cards'][1]['value']
        player_list = list(player_list)
        pcard1 = response_info['cards'][0]['image']
        pcard2 = response_info['cards'][1]['image']


        name= request.form["fname"]
        
        #write user submission to csv
        with open('names.csv', 'a', newline='') as csvfile:
            fieldnames = ['first_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': name})

    #redirect user to game

        return render_template('game.html', name=name, dealer_list=dealer_list, player_list = player_list, dcard1 = dcard1, dcard2 = dcard2, pcard1=pcard1, pcard2=pcard2)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)