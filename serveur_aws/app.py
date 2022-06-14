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

print(conn)

@app.route('/', methods=["GET"])
def default():
    return "Yuumy D'vice test"

@app.route('/save_data', methods=["GET"])
def save_data():
    return 1

@app.route('/addReviews/{param}')
def addReviews(param):
	
	tab = param.split(',')
	
	res = bdd.request('select max(review_id)+1 from Reviews where CHAR_LENGTH(review_id) < 15;', conn)
	id = res[0][0]
	
	param = str(id) + ',' + param
	
	req = reqs.addReview.replace("?r", param)
	
	req = re.sub("%20", " ", req)
	
	print(req)
	
	bdd.insert(req, conn)
	
	return 'ok'
	

@app.route('/getCategoriesOr/{param}')
def getCategoriesOr(param):
	
	tab = param.split(',')
	
	d = {}
	
	#print(tab)
	
	args = tab[-1].split('_')
	
	if args[0] == 'usr':
		
		model = args[2]
		
		id_new = args[1]
		
		param = ''
		
		add = ""
		cpt = 0 
		for i in tab[:-1] :
			if cpt==0 :
				add = " where " + i + " = 1"
			else :
				add = add + " or " + i + " = 1" 
			cpt = cpt+1

		req = reqs.reduceRestaurantBis
		reqfinal = req + add 
		res = bdd.request(reqfinal, conn)
		
		ids = {}

		count = 0
		for row in res:
		    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10]}
		    ids[count] = str(row[10])
		    count += 1
		
		#print(ids.values())
		
		#print(len(list(ids.values())))
		
		ids_list = ','.join(list(ids.values())) + '_'
		
		for i in list(ids.values()):
			
			ids_list += str(id_new) + ','
		
		#print(ids_list[:-1])
		
		res = bdd.reco(ids_list[:-1], model)
		
		#print("result here : ")
		#print(res)
		
		res = res.split(',')
		
		final = {}
		
		for i in range(len(res)):
			
			bid = res[i].replace("\n", "")
			count = list(ids.keys())[list(ids.values()).index(bid)]
			final[i] = d[count]
			
			#print(final[i])
			#print(d[count])
		
		return json.dumps(final)
		
	else :
		
		add = ""
		cpt = 0 
		for i in tab :
			if cpt==0 :
				add = " where " + i + " = 1"
			else :
				add = add + " or " + i + " = 1" 
			cpt = cpt+1

		req = reqs.reduceRestaurantBis
		reqfinal = req + add 
		res = bdd.request(reqfinal, conn)

		count = 0
		for row in res:
			
		    print(row)
		    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10]}
		    count += 1
	
		return  json.dumps(d)


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
	    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10]}
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

@app.route('/getCategories/{param}')
def get_categories(param):

	tab = param.split(',')
	
	args = tab[-1].split('_')
	
	d = {}
	
	if args[0] == 'usr':
		
		model = args[2]
		
		id_new = args[1]
		
		param = ''
		
		add = ""
		cpt = 0 
		for i in tab[:-1] :
			if cpt==0 :
				add = " where " + i + " = 1"
			else :
				add = add + " and " + i + " = 1" 
			cpt = cpt+1

		req = reqs.reduceRestaurantBis
		reqfinal = req + add 
		res = bdd.request(reqfinal, conn)
		
		ids = {}

		count = 0
		for row in res:
		    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10]}
		    ids[count] = str(row[10])
		    count += 1
		
		#print(ids.values())
		
		print(len(list(ids.values())))
		
		ids_list = ','.join(list(ids.values())) + '_'
		
		for i in list(ids.values()):
			
			ids_list += str(id_new) + ','
		
		#print(ids_list[:-1])
		
		res = bdd.reco(ids_list[:-1], model)
		
		print("result here : ")
		print(res)
		
		res = res.split(',')
		
		final = {}
		
		for i in range(len(res)):
			
			bid = res[i].replace("\n", "")
			count = list(ids.keys())[list(ids.values()).index(bid)]
			final[i] = d[count]
			
			print(final[i])
			print(d[count])
		
		return json.dumps(final)
	
	
	
	else :
	
		add = ""
		cpt = 0 
		for i in tab :
			if cpt==0 :
				add = " where " + i + " = 1"
			else :
				add = add + " and " + i + " = 1" 
			cpt = cpt+1

		req = reqs.reduceRestaurantBis
		reqfinal = req + add 
		res = bdd.request(reqfinal, conn)

		d = {}
		count = 0
		for row in res:
		    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10]}
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

@app.route('/getStatistiques')
def get_stats():

    req = reqs.statistiques
    res = bdd.request(req, conn)

    return res

@app.route('/getCloserRestaurant')
def getCloserRestaurant() :

	request = app.current_request
	params = request.query_params

	d = {}	
	if  params :

		long = params.get('long')
		lat = params.get('lat')

		res = bdd.request(reqs.getCloserRestaurants.replace("?long", long).replace("?lat", lat).replace("?nb", "20"), conn)

		count = 0
		for row in res:
			d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8],"image_id":row[9]}
			count += 1

	return json.dumps(d)

@app.route('/TendMonth/{name}')
def TendMonth(name):

    if name=='janvier' :
        result=reqs.Janvier
    elif name=='fevrier' :
        result=reqs.Fevrier
    elif name=='mars' : 
        result=reqs.Mars 
    elif name=='avril' : 
        result=reqs.Avril
    elif name=='mai' : 
        result=reqs.Mai
    elif name=='juin' : 
        result=reqs.Juin
    elif name=='juillet' : 
        result=reqs.Juillet
    elif name=='aout' : 
        result=reqs.Aout
    elif name=='septembre' : 
        result=reqs.Septembre
    elif name=='octobre' : 
        result=reqs.Octobre
    elif name=='novembre' : 
        result=reqs.Novembre
    else : 
        result=reqs.Decembre
        
    return result

@app.route('/TendDay/{name}')
def TendDay(name):

    if name=='lundi' :
        result=reqs.Lundi
    elif name=='mardi' :
        result=reqs.Mardi
    elif name=='mercredi' : 
        result=reqs.Mercredi 
    elif name=='jeudi' : 
        result=reqs.Jeudi
    elif name=='vendredi' : 
        result=reqs.Vendredi
    elif name=='samedi' : 
        result=reqs.Samedi
    elif name=='dimanche' : 
        result=reqs.Dimanche

    return result

@app.route('/verifyUsernamePassword/{id}')
def verifiyUsernamePassword(id) :
	
	ids = id.split(",")
	
	user = ids[0]
	mdp = ids[1]

	res = bdd.request(reqs.verifyLoginPw.replace("?e", user).replace("?p", mdp), conn)

	d = {}
	count = 0
	for row in res:
		d[count] = {"user_id":row[0],"name":row[1],"review_count":row[2],"id_new":row[3]}
		count += 1

	return  json.dumps(d)

@app.route('/addUser/{user}')
def get_user(user):
	
	res = bdd.request('select max(id_new)+1 from Users;', conn)
	id = res[0][0]
	
	# (user_id, name, password, identifiant, id_new, review_count, average_stars)
	
	user = "'"+str(id)+"'," + user + ',' + str(id) + ',0, 0'
	req = reqs.addUser.replace("?v", user)
	
	bdd.insert(req, conn)
	
	return 'ok'

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
