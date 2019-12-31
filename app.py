# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 00:20:51 2019

@author: PSK
"""
from flask import Flask ,render_template,url_for,request
import pandas as pd
import pickle 

loaded_model = pickle.load(open('XG_Boost_model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv('real_2018.csv')
    my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)