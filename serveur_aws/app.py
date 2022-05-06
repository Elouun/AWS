from chalice import Chalice

import logging
import json
import sys
import numpy as np
import bdd


app = Chalice(app_name='Yummy\'Dmvice')

#conn = bdd.connect()

@app.route('/', methods=["GET"])
def default():
    return "hello"

@app.route('/save_data', methods=["GET"])
def save_data():
    return 1

@app.route('/get_restaurant/{name}')
def get_restaurant(name):

    #res = bdd.request("select * from test", conn)
    #print(len(res))

    return name