Tennis Match Predictor
======================


Try it here: https://tennis-match-predictor.herokuapp.com/

Training data created by JeffSackmann and can be found here: https://github.com/JeffSackmann/tennis_atp

Up-to-date player data for predictions pulled from https://www.ultimatetennisstatistics.com/ with Selenium

# Running the code locally
1. Clone this repo
  ```
  git clone 
  ```
2. Install the dependencies:
  ```
  pip install -r requirements.txt 
  ```
3. Install chromedriver for selenium and configure environment variables
- see instructions here:https://chromedriver.chromium.org/getting-started

4. Run the app
```
python app.py
```

Now, the app can be accessed at http://127.0.0.1:5000/
Simply provide player names and select match specifics on the form and click predict to get win probabilities
- Player names must match exactly how they are stored on https://www.ultimatetennisstatistics.com/. 
  i.e. Juan Martin Del Potro and not Juan Del Potro
- Predictions take around 10 seconds to generate as it takes time to pull the data from the website.  I plan to 
  improve this in the future
  
