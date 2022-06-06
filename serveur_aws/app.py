from chalice import Chalice

import logging
import json
import sys
import numpy as np
import bdd
import reqs
import re 


app = Chalice(app_name='Yummy\'Dmvice')

conn = bdd.connect()

@app.route('/', methods=["GET"])
def default():
    return "Yuumy D'vice"

@app.route('/save_data', methods=["GET"])
def save_data():
    return 1


@app.route('/getCountRestaurantNameAlmost/{name}')
def get_restaurant(name):

	req = reqs.countRestaurantNameAlmost.replace("?key", name)
	res = bdd.request(req, conn)
	
	return  res[0][0]

@app.route('/getRestaurantNameAlmost/{name}')
def get_restaurant(name):

	req = reqs.restaurantNameAlmost.replace("?key", name)
	res = bdd.request(req, conn)
	d = {}
	count = 0
	for row in res:
	    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8]}
	    count += 1
	return  json.dumps(d)

@app.route('/getRestaurant/{name}')
def get_restaurant(name):

	names = re.sub("%20", " ", name)
	req = reqs.restaurant.replace("?n", names)
	res = bdd.request(req, conn)
	
	d = {}
	count = 0
	for row in res:
	    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8]}
	    count += 1
	return  json.dumps(d)

@app.route('/getCategories/{list}')
def get_categories(list):

	tab = list.split(',')
	add = ""
	cpt = 0 
	for i in tab :
		if cpt==0 :
			add = " where " + i + " = 1"
		else :
			add = add + " and " + i + " = 1" 
		cpt = cpt+1
		
	req = reqs.reduceRestaurant
	reqfinal = req + add 
	res = bdd.request(reqfinal, conn)
	
	d = {}
	count = 0
	for row in res:
	    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8]}
	    count += 1
	return  json.dumps(d)

@app.route('/getReviewsFromId/{bId}')
def getReviewsFromId(bId):
	
	req = reqs.reviews_by_restaurant_id.replace("?id", bId)
	
	res = bdd.request(req, conn)
	
	d = {}
	count = 0
	for row in res:
	    d[count] = {"name":row[0],"text":row[1],"stars":row[2]}
	    count += 1
	return  json.dumps(d)


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
	
	d = {}
	count = 0
	for row in res:
	    d[count] = {"user_id":row[0],"name":row[1],"review_count":row[2],"id_new":row[3]}
	    count += 1
	return  json.dumps(d)
        
        if res[0]["count"] == 1 :
            return "ok"

       return  json.dumps(d)

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
