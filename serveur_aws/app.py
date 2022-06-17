from chalice import Chalice

import logging
import json
import sys
import numpy as np
import bdd
import reqs
import re 
import random as rd


app = Chalice(app_name='Yummy\'Dmvice')

conn = bdd.connect()

print(conn)

@app.route('/', methods=["GET"])
def default():
    return "Yuumy D'vice test"

@app.route('/save_data', methods=["GET"])
def save_data():
    return 1

@app.route('/getDataBusiness/{param}')
def getDataBusiness(param):
	req = reqs.databusiness.replace("?n", param)
	res = bdd.request(req, conn)
	
	return res

@app.route('/addReviews/{param}')
def addReviews(param):
	
	tab = param.split(',')
	
	user_id = tab[1]
	
	res = [1]
	while(len(res) != 0):
		nb = rd.randint(20, 1000000000)
		res = bdd.request("select review_id from Reviews where review_id ='"+str(nb)+"';", conn)
		print(res)
	
	#print(id)
	
	param = str(nb) + ',' + param
	
	req = reqs.addReview.replace("?r", param)
	
	req = re.sub("%20", " ", req)
	
	#print(req)
	
	bdd.insert(req, conn)
	
	req2 = "UPDATE Users SET review_count = review_count + 1 WHERE user_id = "+user_id+";"
	
	print(req2)
	
	bdd.insert(req2, conn)
	
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
		reqfinal = req + add #+ " limit 30"
		res = bdd.request(reqfinal, conn)
		
		ids = {}

		count = 0
		
		
		
		for row in res:
		  	
		    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10], "categories":row[11], "price":row[12]}
		    ids[count] = str(row[10])
		    count += 1
		
		#print(ids.values())
		
		#print(len(list(ids.values())))
		
		ids_list = ','.join(list(ids.values())) + '_'
		
		for i in list(ids.values()):
			
			ids_list += str(id_new) + ','
		
		#print(ids_list[:-1])
		
		print(model)
		
		res = bdd.reco(ids_list[:-1], model)
		
		#print("result here : ")
		print(res)
		
		res = res.split(',')
		
		final = {}
		
		size = min(50, len(res))
		
		for i in range(size):#len(res)):
			
			bid = res[i].replace("\n", "")
			print(bid)
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
		size = min(50, len(res))
		for row in res:
		    if count < size :
		        print(row)
		        d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10], "categories":row[11], "price":row[12]}
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
	    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10], "categories":row[11], "price":row[12]}
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
		    d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10], "categories":row[11], "price":row[12]}
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
		
		size = min(50, len(res))
		
		for i in range(size):
			
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
		
		size = min(50, len(res))
		
		
		for row in res:
		    if count < size :	
		        d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8] ,"image_id":row[9], "id_new":row[10], "categories":row[11], "price":row[12]}
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
			d[count] = {"business_id":row[0],"name":row[1],"address":row[2],"city":row[3], "state":row[4],"postal_code":row[5],"latitude":row[6],"longitude":row[7],"stars":row[8],"image_id":row[9], "categories":row[11], "price":row[12]}
			count += 1

	return json.dumps(d)

@app.route('/verifyUsernamePassword/{id}')
def verifiyUsernamePassword(id) :
	
	ids = id.split(",")
	
	user = ids[0]

	res = bdd.request(reqs.verifyLoginPw.replace("?e", user), conn)

	d = {}
	count = 0
	for row in res:
		#user_id, password, name, review_count, id_new from
		d[count] = {"user_id":row[0],"password":row[1],"name":row[2],"review_count":row[3],"id_new":row[4], "favorite_categories":row[5]}
		count += 1

	return  json.dumps(d)

@app.route('/addUser/{user}')
def get_user(user):
	
	res = bdd.request('select max(id_new)+1 from Users;', conn)
	id = res[0][0]
	
	# (user_id, name, password, identifiant, id_new, review_count, average_stars)
	
	user = "'"+str(id)+"'," + user + ',' + str(id) + ',0, 0'
	req = reqs.addUser.replace("?v", user)
	
	print(req)
	
	bdd.insert(req, conn)
	
	res = bdd.request(reqs.userID.replace("?n", str(id)), conn)
	
	return res[0][0]

	

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


@app.route('/TendMonth/{name}')
def TendMonth(name):
	
	from datetime import datetime
	
	# month / day / year
	
	d1 = datetime.strptime(name, '%m_%d_%Y')
	
	day = d1.weekday()
	month = d1.month
	
	print(day)
	print(month)
	
	# lundi = 0
	# mardi = 1
	# mercredi = 2
	
	# janvier = 1
	# frevier = 2
	
	if month== 1 :
		if day==0:
			result = reqs.janLundi
		elif day==1:
			result = reqs.janMardi
		elif day==2:
			result = reqs.janMercredi
		elif day==3:
			result = reqs.janJeudi
		elif day==4:
			result = reqs.janVendredi
		elif day==5:
			result = reqs.janSamedi
		else :
			result = reqs.janDimanche
	elif month== 2 :
		if day==0:
			result = reqs.fevLundi
		elif day==1:
			result = reqs.fevMardi
		elif day==2:
			result = reqs.fevMercredi
		elif day==3:
			result = reqs.fevJeudi
		elif day==4:
			result = reqs.fevVendredi
		elif day==5:
			result = reqs.fevSamedi
		else :
			result = reqs.fevDimanche
	elif month== 3 :
		if day==0:
			result = reqs.marLundi
		elif day==1:
			result = reqs.marMardi
		elif day==2:
			result = reqs.marMercredi
		elif day==3:
			result = reqs.marJeudi
		elif day==4:
			result = reqs.marVendredi
		elif day==5:
			result = reqs.marSamedi
		else :
			result = reqs.marDimanche
	elif month==4 :
		if day==0:
			result = reqs.avrLundi
		elif day==1:
			result = reqs.avrMardi
		elif day==2:
			result = reqs.avrMercredi
		elif day==3:
			result = reqs.avrJeudi
		elif day==4:
			result = reqs.avrVendredi
		elif day==5:
			result = reqs.avrSamedi
		else :
			result = reqs.avrDimanche
	elif month==5:
		if day==0:
			result = reqs.maiLundi
		elif day==1:
			result = reqs.maiMardi
		elif day==2:
			result = reqs.maiMercredi
		elif day==3:
			result = reqs.maiJeudi
		elif day==4:
			result = reqs.maiVendredi
		elif day==5:
			result = reqs.maiSamedi
		else :
			result = reqs.maiDimanche
	elif month==6 :
		if day==0:
			result = reqs.juinLundi
		elif day==1:
			result = reqs.juinMardi
		elif day==2:
			result = reqs.juinMercredi
		elif day==3:
			result = reqs.juinJeudi
		elif day==4:
			result = reqs.juinVendredi
		elif day==5:
			result = reqs.juinSamedi
		else :
			result = reqs.juinDimanche
	elif month==7 :
		if day==1:
			result = reqs.juilletLundi
		elif day==2:
			result = reqs.juilletMardi
		elif day==3:
			result = reqs.juilletMercredi
		elif day==4:
			result = reqs.juilletJeudi
		elif day==5:
			result = reqs.juilletVendredi
		elif day==6:
			result = reqs.juilletSamedi
		else :
			result = reqs.juilletDimanche
	elif month== 8 :
		if day==1:
			result = reqs.aoutLundi
		elif day==2:
			result = reqs.aoutMardi
		elif day==3:
			result = reqs.aoutMercredi
		elif day==4:
			result = reqs.aoutJeudi
		elif day==5:
			result = reqs.aoutVendredi
		elif day==6:
			result = reqs.aoutSamedi
		else :
			result = reqs.aoutDimanche
	elif month==9 :
		if day==1:
			result = reqs.sepLundi
		elif day==2:
			result = reqs.sepMardi
		elif day==3:
			result = reqs.sepMercredi
		elif day==4:
			result = reqs.sepJeudi
		elif day==5:
			result = reqs.sepVendredi
		elif day==6:
			result = reqs.sepSamedi
		else :
			result = reqs.sepDimanche
	elif month==10 :
		if day==1:
			result = reqs.octLundi
		elif day==2:
			result = reqs.octMardi
		elif day==3:
			result = reqs.octMercredi
		elif day==4:
			result = reqs.octJeudi
		elif day==5:
			result = reqs.octVendredi
		elif day==6:
			result = reqs.octSamedi
		else :
			result = reqs.octDimanche
	elif month==11 :
		if day==1:
			result = reqs.novLundi
		elif day==2:
			result = reqs.novMardi
		elif day==3:
			result = reqs.novMercredi
		elif day==4:
			result = reqs.novJeudi
		elif day==5:
			result = reqs.novVendredi
		elif day==6:
			result = reqs.novSamedi
		else :
			result = reqs.novDimanche
	else :
		if day==1:
			result = reqs.decLundi
		elif day==2:
			result = reqs.decMardi
		elif day==3:
			result = reqs.decMercredi
		elif day==4:
			result = reqs.decJeudi
		elif day==5:
			result = reqs.decvendredi
		elif day==6:
			result = reqs.decSamedi
		else :
			result = reqs.decDimanche


	return result
