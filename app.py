import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sys

app = Flask(__name__) #Initialize the flask App
# model = pickle.load(open('model.pkl', 'rb'))

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
    surface = request.form.get('Surface')
    tourney_round = request.form.get('Round')

    # print(str(select))

    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    # output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Expected winner $ {}'.format(str(p1)))

if __name__ == "__main__":
    app.run(debug=True)