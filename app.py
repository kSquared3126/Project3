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
        if (dealer_list[0] == 'KING' or 'QUEEN' or 'JACK') and (dealer_list[1] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            dealer_sum = 10 + (int)(dealer_list[1])
        elif (dealer_list[1] == 'KING' or 'QUEEN' or 'JACK') and (dealer_list[0] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            dealer_sum = 10 + (int)(dealer_list[0]) 
        elif (dealer_list[0] == 'ACE') and (dealer_list[1] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            dealer_sum = 11 + (int)(dealer_list[1])
        elif (dealer_list[1] == 'ACE') and (dealer_list[0] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            dealer_sum = 11 + (int)(dealer_list[0])    
        elif (dealer_list[0] == 'ACE') and (dealer_list[1] == 'KING' or 'QUEEN' or 'JACK' or 'ACE'):
            dealer_sum = 21
        elif (dealer_list[1] == 'ACE') and (dealer_list[0] == 'KING' or 'QUEEN' or 'JACK' or 'ACE'):
            dealer_sum = 21
        elif (dealer_list[0] == 'ACE') and (dealer_list[1] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            dealer_sum = 11 + (int)(dealer_list[1])
        elif (dealer_list[1] == 'ACE') and (dealer_list[0] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            dealer_sum = 11 + (int)(dealer_list[0])
        elif (dealer_list[0] == 'ACE') and (dealer_list[1] == 'ACE'):
            dealer_sum = 22
        else: 
            dealer_sum = (int)(dealer_list[0]) + (int)(dealer_list[1])
        print(dealer_sum)
                
#player start
        response = requests.get(begin).text 
        response_info = json.loads(response)
        player_list = []
        player_list = response_info['cards'][0]['value'], response_info['cards'][1]['value']
        player_list = list(player_list)
        if (player_list[0] == 'KING' or 'QUEEN' or 'JACK') and (player_list[1] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            player_sum = 10 + (int)(player_list[1])
        elif (player_list[1] == 'KING' or 'QUEEN' or 'JACK') and (player_list[0] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            player_sum = 10 + (int)(player_list[0]) 
        elif (player_list[0] == 'ACE') and (player_list[1] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            player_sum = 11 + (int)(player_list[1])
        elif (player_list[1] == 'ACE') and (player_list[0] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            player_sum = 11 + (int)(player_list[0])    
        elif (player_list[0] == 'ACE') and (player_list[1] == 'KING' or 'QUEEN' or 'JACK' or 'ACE'):
            player_sum = 21
        elif (player_list[1] == 'ACE') and (player_list[0] == 'KING' or 'QUEEN' or 'JACK' or 'ACE'):
            player_sum = 21
        elif (player_list[0] == 'ACE') and (player_list[1] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            player_sum = 11 + (int)(player_list[1])
        elif (player_list[1] == 'ACE') and (player_list[0] != 'KING' and 'QUEEN' and 'JACK' and 'ACE'):
            player_sum = 11 + (int)(player_list[0])
        elif (player_list[0] == 'ACE') and (player_list[1] == 'ACE'):
            player_sum = 22
        else: 
            player_sum = (int)(player_list[0]) + (int)(player_list[1])
        print(player_sum)


        name= request.form["fname"]
        
        #write user submission to csv
        with open('names.csv', 'a', newline='') as csvfile:
            fieldnames = ['first_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': name})


    #redirect user to game

        return render_template('game.html', name=name, dealer_list=dealer_list, player_list = player_list, dealer_sum = dealer_sum, player_sum = player_sum)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)