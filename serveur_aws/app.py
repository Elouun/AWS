from chalice import Chalice

import logging
import json
import sys
import numpy as np
import bdd
import reqs


app = Chalice(app_name='Yummy\'Dmvice')

#conn = bdd.connect()

@app.route('/', methods=["GET"])
def default():
    return "hello"

@app.route('/save_data', methods=["GET"])
def save_data():
    return 1

@app.route('/getRestaurant/{name}')
def get_restaurant(name):

    req = reqs.restaurant.replace("?n", name)
    #res = bdd.request("select * from test", conn)
    #print(len(res))

    return req

@app.route('/getRestaurant/{id}')
def get_restaurant(id):

    #req = reqs.restaurant.replace("?n", name)
    #res = bdd.request("select * from test", conn)
    #print(len(res))

    return 1


@app.route('/getUser/{name}')
def get_user(name):

    #res = bdd.request("select * from test", conn)
    #print(len(res))

    return name

@app.route('/getReco')
def get_user():

    request = app.current_request

    params = request.query_params

    #http://127.0.0.1:8000/getReco?ouille=ouille&argh=argh

    if  params :

        search = params.get('search')
        search = search.split(',')

        print(search)
    

        return 1

    return "no param"