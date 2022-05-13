from chalice import Chalice

import logging
import json
import sys
import numpy as np
import bdd
import reqs


app = Chalice(app_name='Yummy\'Dmvice')

conn = bdd.connect()

@app.route('/', methods=["GET"])
def default():
    return "hello"

@app.route('/save_data', methods=["GET"])
def save_data():
    return 1

@app.route('/getRestaurant/{name}')
def get_restaurant(name):

    req = reqs.restaurant.replace("?n", name)
    res = bdd.request(req, conn)

    return res

@app.route('/getRestaurantid/{id}')
def get_restaurant_id(id):

    req = reqs.restaurantID.replace("?n", id)
    res = bdd.request(req, conn)

    return res


@app.route('/getUserid/{id}')
def get_user_id(id):

    req = reqs.userID.replace("?n", id)
    res = bdd.request(req, conn)

    return res

@app.route('/getUser/{name}')
def get_user(name):

    req = reqs.user.replace("?n", name)
    res = bdd.request(req, conn)

    return res

@app.route('/getReviewByUser/{name}')
def get_Ruser(name):

    req = reqs.review_by_user.replace("?n", name)
    res = bdd.request(req, conn)

    return res

@app.route('/getReviewByUserid/{id}')
def get_Ruser_id(id):

    req = reqs.review_by_user_id.replace("?n", id)
    res = bdd.request(req, conn)

    return res

@app.route('/getRestaurantEtoile/{nb}')
def get_restaurantEtoile(nb):

    req = reqs.restauetoiles.replace("?n", nb)
    res = bdd.request(req, conn)

    return res

@app.route('/getRestaurantVille/{name}')
def get_restaurantVille(name):

    req = reqs.restauVille.replace("?n", name)
    res = bdd.request(req, conn)

    return res

@app.route('/getRestaurantAlcohol/{name}')
def get_restaurantAlco(name):

    req = reqs.restaualcoholterrasse.replace("?n",name)
    res = bdd.request(req, conn)

    return res

@app.route('/getCloserRestaurant')
def getCloserRestaurant() :

    request = app.current_request
    params = request.query_params

    if  params :

        long = params.get('long')
        lat = params.get('lat')
      
        res = bdd.request(reqs.getCloserRestaurants.replace("?long", long).replace("?lat", lat).replace("?nb", "3"), conn)
        
        return res[0]



    return "no param"


@app.route('/verifyUsernamePassword')
def verifiyUsernamePassword() :

    request = app.current_request

    params = request.query_params

    #http://127.0.0.1:8000/getReco?ouille=ouille&argh=argh

    if  params :

        mdp = params.get('mdp')
        user = params.get('user')
      
        res = bdd.request(reqs.verifyLoginPw.replace("?e", user).replace("?p", mdp), conn)
        
        if res[0]["count"] == 1 :
            return "ok"

        return "not exist"

    return "no param"

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