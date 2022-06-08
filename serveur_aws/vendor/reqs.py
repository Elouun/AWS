restaurant = 'Select * from Business where name = "?n"'
restaurantNameAlmost = 'select business_id, name, address, city, state, postal_code, latitude, longitude, stars from Business where name like "%?key%"'

countRestaurantNameAlmost = 'select count(*) from Business where name like "%?key%"'

restaurantID = 'Select * from Business where business_id = "?n"'

user = 'select * from Users where name = "?n"'
userID = 'Selct * from Users where user_id = "?n"'

review_by_user = 'SELECT text,stars FROM Users u,Reviews r where u.user_id = r.user_id and name="?n" limit 5'
review_by_user_id = 'SELECT text,stars FROM Users u,Reviews r where u.user_id = r.user_id and user_id="?n" limit 5'

reviews_by_restaurant_id = 'SELECT u.name, text, stars FROM Users u,Reviews r where u.user_id = r.user_id and business_id="?id" order by date desc limit 5'

addUser = 'INSERT INTO Users(identifiant, name, password) VALUES (?v)'

restauetoiles = 'select * from Business where stars = "?n"'

restauVille = 'select * from Business where city = "?n"'

restaualcoholterrasse = 'select * from Business where Alcohol = 1 and OutdoorSeating = 1 and city = "?n"'

verifyLoginPw = 'select user_id, name, review_count, id_new from Users u where u.identifiant = "?e" and u.password = "?p"'

getCloserRestaurants = 'select b.business_id, b.name, b.address, b.city, b.state, b.postal_code, b.latitude, b.longitude, b.stars, ST_Distance_Sphere(point(?long, ?lat),point(b.longitude,b.latitude)) as distance from Business  b order by distance limit ?nb'

categories = ' select * from Business where Alcohol = 1 and NoiseLevel = 2 and RestaurantsTakeOut = 1 and OutdoorSeating = 1 and Romantic = 1 and Intimate = 1 and Classy = 1 and Hipster = 1 and Divey = 1 and Touristy = 1 and Trendy = 1 and Upscale = 1 and Casual = 1 and Caters = 1 and BikeParking = 1 and BusinessParking = 1 and GoodForKids = 1 and HasTV = 1 and OutdoorSeating1 = 1 and RestaurantsAttire = 1 and RestaurantsPriceRange2 = 2 and RestaurantsReservations = 1 and Wifi = 1 and Tea_Rooms = 1 and Pasta_Shops = 1 and Seafood_Markets = 1 and Acai_Bowls = 1 and Party__Event_Planning = 1 and Creperies = 1 and Lebanese = 1 and Coffe_Roasteries = 1 and Imported_Food = 1 and Gas_Stations = 1 and Karaoke = 1 and Brazilian = 1 and Cuban = 1 and Health_Markets = 1 and Hot_Pot = 1 and African = 1 and Irish = 1 and Automotive = 1 and Meat_shops = 1 and Fish__Chips = 1 and Poke = 1 and Waffles = 1 and Cheesesteaks = 1 and Food_Court = 1 and Hawaiian = 1 and Pakistani = 1 and Dive_Bars = 1 and Taiwanese = 1 and Soul_Food = 1 and Spanish = 1 and Dim_Sum = 1 and Wraps = 1 and CajunCreole = 1 and French = 1 and Ramen = 1 and Bubble_Tea = 1 and Canadian_New = 1 and Halal = 1 and Donuts = 1 and TapasSmall_Plates = 1 and Ethnic_Food = 1 and Bagels = 1 and Chicken_Shop = 1 and Hot_Dogs = 1 and Greek = 1 and Caribbean = 1 and Comfort_Food = 1 and Korean = 1 and Lounges = 1 and Noodles = 1 and Indian = 1 and Latin_American = 1 and Tacos = 1 and Ice_Cream__Frozen_Yogurt = 1 and Juice_Bars__Smoothies = 1 and Vietnamese = 1 and GlutenFree = 1 and Steakhouses = 1 and Soup = 1 and TexMex = 1 and Vegan = 1 and Beer = 1 and Wine__Spirits = 1 and Thai = 1 and Barbeque = 1 and Mediterranean = 1 and Vegetarian = 1 and Asian_Fusion = 1 and Delis = 1 and Desserts = 1 and Specialty_Food = 1 and Bakeries = 1 and Sushi_Bars = 1 and Chicken_Wings = 1 and Japanese = 1 and Cafes = 1 and Salad = 1 and Seafood = 1 and Italian = 1 and Chinese = 1 and Mexican = 1 and Coffe__Tea = 1 and Burgers = 1 and American_New = 1 and Breakfast_Brunch = 1 and Pizza = 1 and Fast_Food = 1 and American_Traditional = 1 and Sandwiches = 1 '

perso = 'select * from Business'

reduceRestaurant = 'select business_id, name, address, city, state, postal_code, latitude, longitude, stars from Business'

statistiques = 'SELECT count(u.user_id) as nb_user , count(b.business_id) as nb_restau FROM Users u ,Business b WHERE 1'
