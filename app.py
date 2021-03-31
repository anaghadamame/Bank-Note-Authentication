# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:21:34 2021

@author: Anagha
"""


from flask import Flask,request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickel_in = open("Classify.pkl","rb")
Classify=pickle.load(pickel_in)

@app.route('/predict',methods=['Get'])
def predict_note():
    
    """Let's Authenticate the Bank Note
    Using docstrings for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
    """
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    pre=Classify.predict([[variance,skewness,curtosis,entropy]])
    print(pre)
    #return "Answer"+str(pre)
    if pre==0:
       return "The note is forged"
    else:
       return "The note is genuine"

if __name__=='__main__':
    app.run()

"""for watching Flasgger: API:http://127.0.0.1:5000/apidocs