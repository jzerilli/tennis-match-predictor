import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sys
from scraper import getPlayerStats, getHeadToHead 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask_bootstrap import Bootstrap

app = Flask(__name__) #Initialize the flask App
Bootstrap(app)
# model = pickle.load(open('model.pkl', 'rb'))

pred_cols = ['is_clay', 'is_hard' ,'is_grass', 'is_carpet', 'tourney_level', 'best_of', 'rank_diff','age_diff', 'ht_diff', 'hand_diff', 
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

    features = request.form.values()

    p1 = request.form.get('p1_name')
    p2 = request.form.get('p2_name')

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920x1080")
    # driver=webdriver.Chrome('./chromedriver', options = chrome_options)
    # surface = request.form.get('Surface')
    # print(p1, "stats ", getPlayerStats(driver, p1, surface))

    
    tourney_round = request.form.get('Round')
    level = request.form.get('Level')

    # driver.close()
    # print(str(select))

    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    # output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Expected winner $ {}'.format(str(p1)))

if __name__ == "__main__":
    app.run(debug=True)