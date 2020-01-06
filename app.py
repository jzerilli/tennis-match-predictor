import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sys
from scraper import getPlayerStats, getHeadToHead 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
    


app = Flask(__name__) #Initialize the flask App

with open(f'model.pkl', 'rb') as f:
    model = pickle.load(f)

headers = ['is_clay', 'is_hard' ,'is_grass', 'is_carpet', 'tourney_level', 'best_of', 'rank_diff','age_diff', 'ht_diff', 'hand_diff', 
'1yr_serve_pct_diff', '1yr_ace_pct_diff', '1yr_bp_save_pct_diff','1yr_serve_pts_won_pct_diff', '1yr_break_pct_diff', '1yr_ret_pts_won_pct_diff',
'year_win_pct_diff', 'year_surface_win_pct_diff', 'wins_vs_opp_diff', 'wildcard_diff', 'qualifier_diff']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''



    p1 = request.form.get('p1_name')
    p2 = request.form.get('p2_name')

    # tourney_round = request.form.get('Round')
    level = int(request.form.get('Level'))
    bestof = int(request.form.get('bestof'))

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver=webdriver.Chrome('./chromedriver', options = chrome_options)
    driver.get("https://www.ultimatetennisstatistics.com/")

    surface = request.form.get('Surface')

    p1_stats = getPlayerStats(driver, p1, surface)
    p2_stats = getPlayerStats(driver, p2, surface)
    h2h = getHeadToHead(driver, p1, p2)

    driver.quit()


    data = []
    if surface == "C":
        data = [1, 0, 0, 0]
    elif surface == "H":
        data = [0, 1, 0, 0]
    else:
        data = [0, 0, 1, 0]

    data += [level, bestof]
    data += list(map(lambda x, y: x - y, p1_stats, p2_stats))
    data += [(h2h[0] - h2h[1])]
    data += [0, 0]


    input_variables = pd.DataFrame([data],
                                columns=headers, 
                                dtype=float)
    
    print(model.predict(input_variables))
    probs = model.predict_proba(input_variables)
    p1_prob = round(probs[0,1] * 100, 2)
    p2_prob = round(probs[0,0] * 100, 2)

    return render_template('index.html', prediction_text=f'Winner Probabilities {p1} : {p1_prob}% {p2} {p2_prob}%')

if __name__ == "__main__":
    app.run(debug=True)