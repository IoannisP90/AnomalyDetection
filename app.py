import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('finalized_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [request.form.values()]
    prediction = model.predict(pd.DataFrame(features))

    output = prediction
    if output == -1:
        template = render_template('index.html', prediction_text='Anomaly')
    else:
        template = render_template('index.html', prediction_text='Not an Anomaly')
    return template


if __name__ == "__main__":
    app.run(debug=True)