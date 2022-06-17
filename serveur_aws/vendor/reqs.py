restaurant = 'Select * from Business where name = "?n"'
restaurantNameAlmost = 'select business_id, name, address, city, state, postal_code, latitude, longitude, stars,  image_id, id_new, categories, RestaurantsPriceRange2 from Business NATURAL JOIN image where name like "%?key%"'

countRestaurantNameAlmost = 'select count(*) from Business where name like "%?key%"'

restaurantID = 'Select * from Business where business_id = "?n"'

addReview = 'insert into Reviews(review_id, business_id, user_id, date, text, stars)  values (?r)'

user = 'select * from Users where name = "?n"'
userID = 'Select * from Users where user_id = "?n"'

databusiness = ' SELECT * FROM Business WHERE id_new IN (?n)' 

review_by_user = 'SELECT text,stars FROM Users u,Reviews r where u.user_id = r.user_id and name="?n" limit 5'
review_by_user_id = 'SELECT text,stars FROM Users u,Reviews r where u.user_id = r.user_id and user_id="?n" limit 5'

reviews_by_restaurant_id = 'SELECT u.name, text, stars FROM Users u,Reviews r where u.user_id = r.user_id and business_id="?id" order by date desc limit 5'

addUser = 'insert into Users(user_id, name, password, identifiant, favorite_categories, id_new, review_count, average_stars) VALUES (?v);'

restauetoiles = 'select * from Business where stars = "?n"'

restauVille = 'select * from Business where city = "?n"'

restaualcoholterrasse = 'select * from Business where Alcohol = 1 and OutdoorSeating = 1 and city = "?n"'

verifyLoginPw = 'select user_id, password, name, review_count, id_new, favorite_categories from Users u where u.identifiant = "?e"'

getCloserRestaurants = 'select b.business_id, b.name, b.address, b.city, b.state, b.postal_code, b.latitude, b.longitude, b.stars, image_id, b.id_new, b.categories, b.RestaurantsPriceRange2, ST_Distance_Sphere(point(?long, ?lat),point(b.longitude,b.latitude)) as distance from Business b natural join image order by distance limit ?nb'

categories = ' select * from Business where Alcohol = 1 and NoiseLevel = 2 and RestaurantsTakeOut = 1 and OutdoorSeating = 1 and Romantic = 1 and Intimate = 1 and Classy = 1 and Hipster = 1 and Divey = 1 and Touristy = 1 and Trendy = 1 and Upscale = 1 and Casual = 1 and Caters = 1 and BikeParking = 1 and BusinessParking = 1 and GoodForKids = 1 and HasTV = 1 and OutdoorSeating1 = 1 and RestaurantsAttire = 1 and RestaurantsPriceRange2 = 2 and RestaurantsReservations = 1 and Wifi = 1 and Tea_Rooms = 1 and Pasta_Shops = 1 and Seafood_Markets = 1 and Acai_Bowls = 1 and Party__Event_Planning = 1 and Creperies = 1 and Lebanese = 1 and Coffe_Roasteries = 1 and Imported_Food = 1 and Gas_Stations = 1 and Karaoke = 1 and Brazilian = 1 and Cuban = 1 and Health_Markets = 1 and Hot_Pot = 1 and African = 1 and Irish = 1 and Automotive = 1 and Meat_shops = 1 and Fish__Chips = 1 and Poke = 1 and Waffles = 1 and Cheesesteaks = 1 and Food_Court = 1 and Hawaiian = 1 and Pakistani = 1 and Dive_Bars = 1 and Taiwanese = 1 and Soul_Food = 1 and Spanish = 1 and Dim_Sum = 1 and Wraps = 1 and CajunCreole = 1 and French = 1 and Ramen = 1 and Bubble_Tea = 1 and Canadian_New = 1 and Halal = 1 and Donuts = 1 and TapasSmall_Plates = 1 and Ethnic_Food = 1 and Bagels = 1 and Chicken_Shop = 1 and Hot_Dogs = 1 and Greek = 1 and Caribbean = 1 and Comfort_Food = 1 and Korean = 1 and Lounges = 1 and Noodles = 1 and Indian = 1 and Latin_American = 1 and Tacos = 1 and Ice_Cream__Frozen_Yogurt = 1 and Juice_Bars__Smoothies = 1 and Vietnamese = 1 and GlutenFree = 1 and Steakhouses = 1 and Soup = 1 and TexMex = 1 and Vegan = 1 and Beer = 1 and Wine__Spirits = 1 and Thai = 1 and Barbeque = 1 and Mediterranean = 1 and Vegetarian = 1 and Asian_Fusion = 1 and Delis = 1 and Desserts = 1 and Specialty_Food = 1 and Bakeries = 1 and Sushi_Bars = 1 and Chicken_Wings = 1 and Japanese = 1 and Cafes = 1 and Salad = 1 and Seafood = 1 and Italian = 1 and Chinese = 1 and Mexican = 1 and Coffe__Tea = 1 and Burgers = 1 and American_New = 1 and Breakfast_Brunch = 1 and Pizza = 1 and Fast_Food = 1 and American_Traditional = 1 and Sandwiches = 1 '

perso = 'select * from Business'

reduceRestaurantBis = 'select b.business_id, name, address, city, state, postal_code, latitude, longitude, stars, i.image_id, b.id_new, b.categories, b.RestaurantsPriceRange2 from Business b NATURAL JOIN image i'

reduceRestaurant = 'select business_id, name, address, city, state, postal_code, latitude, longitude, stars from Business'

statistiques = 'SELECT count(u.user_id) as nb_user FROM Users u UNION SELECT count(b.business_id) as nb_restau FROM Business b UNION SELECT count(c.business_id) as nb_reviews from Reviews c where date > SUBDATE(now(), INTERVAL 31 DAY)'

janLundi=' Alcohol ,  Sandwiches ;  Classy ,  Hipster ;  Alcohol ,  Cajun/Creole ;  American (Traditional) ,  Trendy ;  American (New) ,  Burgers ;  Classy ,  Romantic ;  American (New) ,  Seafood ;  Alcohol ,  Intimate ;  Alcohol ,  Burgers ;  Alcohol ,  Upscale ;  American (Traditional) ,  Seafood ;  Alcohol ,  Romantic ;  Classy ,  Upscale ;  Alcohol ,  American (New) ,  Breakfast & Brunch ,  Classy '
 
janMardi=' Japanese ,  Trendy ;  Alcohol ,  Cajun/Creole ;  American (Traditional) ,  Trendy ;  American (New) ,  Burgers ;  Classy ,  Romantic ;  American (New) ,  Seafood ;  Alcohol ,  Intimate ;  Alcohol ,  Burgers ;  Alcohol ,  Upscale ;  American (Traditional) ,  Seafood ;  Alcohol ,  Romantic ;  Classy ,  Upscale ;  Alcohol ,  American (New) ,  Breakfast & Brunch ,  Classy '
 
janMercredi=' Alcohol ,  Vegetarian ;  Alcohol ,  Cajun/Creole ;  American (Traditional) ,  Trendy ;  American (New) ,  Burgers ;  Classy ,  Romantic ;  American (New) ,  Seafood ;  Alcohol ,  Intimate ;  Alcohol ,  Burgers ;  Alcohol ,  Upscale ;  American (Traditional) ,  Seafood ;  Alcohol ,  Romantic ;  Classy ,  Upscale ;  Alcohol ,  American (New) ,  Breakfast & Brunch ,  Classy '
 
janJeudi=' Japanese ,  Ramen ;  Classy ,  Hipster ;  Alcohol ,  Cajun/Creole ;  American (Traditional) ,  Trendy ;  American (New) ,  Burgers ;  Classy ,  Romantic ;  American (New) ,  Seafood ;  Alcohol ,  Intimate ;  Alcohol ,  Burgers ;  Alcohol ,  Upscale ;  American (Traditional) ,  Seafood ;  Alcohol ,  Romantic ;  Classy ,  Upscale ;  Alcohol ,  American (New) ,  Breakfast & Brunch ,  Classy '
 
janVendredi=' Japanese ,  Trendy ;  Alcohol ,  Cajun/Creole ;  American (Traditional) ,  Trendy ;  American (New) ,  Burgers ;  Classy ,  Romantic ;  American (New) ,  Seafood ;  Alcohol ,  Intimate ;  Alcohol ,  Burgers ;  Alcohol ,  Upscale ;  American (Traditional) ,  Seafood ;  Alcohol ,  Romantic ;  Classy ,  Upscale ;  Alcohol ,  American (New) ,  Breakfast & Brunch ,  Classy '
 
janSamedi=' Japanese ,  Ramen ;  Alcohol ,  Cajun/Creole ;  American (Traditional) ,  Trendy ;  American (New) ,  Burgers ;  Classy ,  Romantic ;  American (New) ,  Seafood ;  Alcohol ,  Intimate ;  Alcohol ,  Burgers ;  Alcohol ,  Upscale ;  American (Traditional) ,  Seafood ;  Alcohol ,  Romantic ;  Classy ,  Upscale ;  Alcohol ,  American (New) ,  Breakfast & Brunch ,  Classy '
 
janDimanche=' Alcohol ,  Tapas/Small Plates ;  Alcohol ,  Cajun/Creole ;  American (Traditional) ,  Trendy ;  American (New) ,  Burgers ;  Classy ,  Romantic ;  American (New) ,  Seafood ;  Alcohol ,  Intimate ;  Alcohol ,  Burgers ;  Alcohol ,  Upscale ;  American (Traditional) ,  Seafood ;  Alcohol ,  Romantic ;  Classy ,  Upscale ;  Alcohol ,  American (New) ,  Breakfast & Brunch ,  Classy '

fevLundi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; Classy, Hipster; Classy, Romantic; Alcohol, Tapas/Small Plates; Alcohol, Intimate; Classy, Desserts; Alcohol, Upscale; Alcohol, Romantic; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
fevMardi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; Classy, Hipster; Classy, Romantic; Alcohol, Tapas/Small Plates; Alcohol, Intimate; Classy, Desserts; Alcohol, Upscale; Alcohol, Romantic; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
fevMercredi='Alcohol, Vegetarian; Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; Classy, Hipster; Classy, Romantic; Alcohol, Tapas/Small Plates; Alcohol, Intimate; Classy, Desserts; Alcohol, Upscale; Alcohol, Romantic; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
fevJeudi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; Classy, Hipster; Classy, Romantic; Alcohol, Tapas/Small Plates; Alcohol, Intimate; Classy, Desserts; Alcohol, Upscale; Alcohol, Romantic; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
fevVendredi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; Classy, Hipster; Classy, Romantic; Alcohol, Tapas/Small Plates; Alcohol, Intimate; Classy, Desserts; Alcohol, Upscale; Alcohol, Romantic; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
fevSamedi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; Classy, Hipster; Classy, Romantic; Alcohol, Tapas/Small Plates; Alcohol, Intimate; Classy, Desserts; Alcohol, Upscale; Alcohol, Romantic; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
fevDimanche='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; Classy, Hipster; Classy, Romantic; Alcohol, Tapas/Small Plates; Alcohol, Intimate; Classy, Desserts; Alcohol, Upscale; Alcohol, Romantic; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'

marLundi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; American (Traditional), Trendy; Classy, Hipster; Alcohol, Vegetarian; Alcohol, Burgers; American (Traditional), Seafood; Alcohol, American (New), Breakfast & Brunch, Classy'
 
marMardi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; American (Traditional), Trendy; Classy, Hipster; Alcohol, Vegetarian; Alcohol, Burgers; American (Traditional), Seafood; Alcohol, American (New), Breakfast & Brunch, Classy'
 
marMercredi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; American (Traditional), Trendy; Classy, Hipster; Alcohol, Vegetarian; Alcohol, Burgers; American (Traditional), Seafood; Alcohol, American (New), Breakfast & Brunch, Classy'
 
marJeudi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; American (Traditional), Trendy; Classy, Hipster; Alcohol, Vegetarian; Alcohol, Burgers; American (Traditional), Seafood; Alcohol, American (New), Breakfast & Brunch, Classy'
 
marVendredi='Alcohol, Upscale; Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; American (Traditional), Trendy; Classy, Hipster; Alcohol, Vegetarian; Alcohol, Burgers; American (Traditional), Seafood; Alcohol, American (New), Breakfast & Brunch, Classy'
 
marSamedi='Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; American (Traditional), Trendy; Classy, Hipster; Alcohol, Vegetarian; Alcohol, Burgers; American (Traditional), Seafood; Alcohol, American (New), Breakfast & Brunch, Classy'
 
marDimanche='Alcohol, Tapas/Small Plates; Alcohol, Upscale; Classy, Upscale; Japanese, Ramen; Japanese, Trendy; Alcohol, Sandwiches; American (Traditional), Trendy; Classy, Hipster; Alcohol, Vegetarian; Alcohol, Burgers; American (Traditional), Seafood; Alcohol, American (New), Breakfast & Brunch, Classy'

avrLundi='Alcohol, Sandwiches; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy; Pizza, Sandwiches; Alcohol, Chinese; Classy, Hipster; Alcohol, Vegetarian; Burgers, Fast Food'
 
avrMardi='Japanese, Trendy; Pizza, Sandwiches; Alcohol, Chinese; Classy, Hipster; Alcohol, Vegetarian; Burgers, Fast Food'
 
avrMercredi='Pizza, Sandwiches; Alcohol, Chinese; Classy, Hipster; Alcohol, Vegetarian; Burgers, Fast Food'

avrJeudi='Japanese, Ramen; Pizza, Sandwiches; Alcohol, Chinese; Classy, Hipster; Alcohol, Vegetarian; Burgers, Fast Food'
 
avrVendredi='Japanese, Trendy; Alcohol, Upscale; Pizza, Sandwiches; Alcohol, Chinese; Classy, Hipster; Alcohol, Vegetarian; Burgers, Fast Food'
 
avrSamedi='Japanese, Ramen; Pizza, Sandwiches; Alcohol, Chinese; Classy, Hipster; Alcohol, Vegetarian; Burgers, Fast Food'

avrDimanche='Alcohol, Tapas/Small Plates; Alcohol, Upscale; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy; Pizza, Sandwiches; Alcohol, Chinese; Classy, Hipster; Alcohol, Vegetarian; Burgers, Fast Food'
 
maiLundi='Alcohol, Sandwiches; Classy, Hipster; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy; Pizza, Sandwiches; Mexican, Tex-Mex; Alcohol, Vegetarian; Burgers, Fast Food'
 
maiMardi='Japanese, Trendy; Pizza, Sandwiches; Mexican, Tex-Mex; Alcohol, Vegetarian; Burgers, Fast Food'
 
maiMercredi='Pizza, Sandwiches; Mexican, Tex-Mex; Alcohol, Vegetarian; Burgers, Fast Food'
 
maiJeudi='Japanese, Ramen; Classy, Hipster; Pizza, Sandwiches; Mexican, Tex-Mex; Alcohol, Vegetarian; Burgers, Fast Food'
 
maiVendredi='Japanese, Trendy; Alcohol, Upscale; Pizza, Sandwiches; Mexican, Tex-Mex; Alcohol, Vegetarian; Burgers, Fast Food'
 
maiSamedi='Japanese, Ramen; Pizza, Sandwiches; Mexican, Tex-Mex; Alcohol, Vegetarian; Burgers, Fast Food'
 
maiDimanche='Alcohol, Tapas/Small Plates; Alcohol, Upscale; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy; Pizza, Sandwiches; Mexican, Tex-Mex; Alcohol, Vegetarian; Burgers, Fast Food'

juinLundi='Alcohol, Sandwiches; Classy, Hipster; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'
 
juinMardi='Japanese, Trendy'
 
juinMercredi='Alcohol, Vegetarian'
 
juinJeudi='Japanese, Ramen; Classy, Hipster'
 
juinVendredi='Japanese, Trendy; Alcohol, Upscale'
 
juinSamedi='Japanese, Ramen'
 
juinDimanche='Alcohol, Tapas/Small Plates; Alcohol, Upscale; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
juilletLundi='Alcohol, Sandwiches; Classy, Hipster; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy; Alcohol, Vegetarian'
 
juilletMardi='Japanese, Trendy; Alcohol, Vegetarian'
 
juilletMercredi='Alcohol, Vegetarian'
 
juilletJeudi='Japanese, Ramen; Classy, Hipster; Alcohol, Vegetarian'
 
juilletVendredi='Japanese, Trendy; Alcohol, Upscale; Alcohol, Vegetarian'
 
juilletSamedi='Japanese, Ramen; Alcohol, Vegetarian'
 
juilletDimanche='Alcohol, Tapas/Small Plates; Alcohol, Upscale; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy; Alcohol, Vegetarian'
 
aoutLundi='Alcohol, Sandwiches; Classy, Hipster; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'
 
aoutMardi='Japanese, Trendy'
 
aoutMercredi='Alcohol, Vegetarian'
 
aoutJeudi='Japanese, Ramen; Classy, Hipster'
 
aoutVendredi='Japanese, Trendy; Alcohol, Upscale'
 
aoutSamedi='Japanese, Ramen'
 
aoutDimanche='Alcohol, Tapas/Small Plates; Alcohol, Upscale; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
sepLundi='Alcohol, Sandwiches; Classy, Hipster; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy; Alcohol, Upscale; American (Traditional), Seafood; Alcohol, Romantic; Classy, Upscale'
 
sepMardi='Japanese, Trendy; Alcohol, Upscale; American (Traditional), Seafood; Alcohol, Romantic; Classy, Upscale'
 
sepMercredi='Alcohol, Vegetarian; Alcohol, Upscale; American (Traditional), Seafood; Alcohol, Romantic; Classy, Upscale'
 
sepJeudi='Japanese, Ramen; Classy, Hipster; Alcohol, Upscale; American (Traditional), Seafood; Alcohol, Romantic; Classy, Upscale'
 
sepVendredi='Japanese, Trendy; Alcohol, Upscale; American (Traditional), Seafood; Alcohol, Romantic; Classy, Upscale'
 
sepSamedi='Japanese, Ramen; Alcohol, Upscale; American (Traditional), Seafood; Alcohol, Romantic; Classy, Upscale'
 
sepDimanche='Alcohol, Tapas/Small Plates; Alcohol, American (New), Breakfast & Brunch, Classy; Alcohol, Upscale; American (Traditional), Seafood; Alcohol, Romantic; Classy, Upscale'
 
octLundi='Alcohol, Sandwiches; Classy, Hipster; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'
 
octMardi='Japanese, Trendy'
 
octMercredi='Alcohol, Vegetarian'
 
octJeudi='Japanese, Ramen; Classy, Hipster'
 
octVendredi='Japanese, Trendy; Alcohol, Upscale'
 
octSamedi='Japanese, Ramen'
 
octDimanche='Alcohol, Tapas/Small Plates; Alcohol, Upscale; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'

novLundi='Alcohol, Sandwiches; Classy, Hipster; Japanese, Ramen; Alcohol, Tapas/Small Plates; Classy, Desserts; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'
 
novMardi='Japanese, Trendy; Japanese, Ramen; Alcohol, Tapas/Small Plates; Classy, Desserts; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'
 
novMercredi='Alcohol, Vegetarian; Japanese, Ramen; Alcohol, Tapas/Small Plates; Classy, Desserts; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'
 
novJeudi='Classy, Hipster; Japanese, Ramen; Alcohol, Tapas/Small Plates; Classy, Desserts; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'
 
novVendredi='Japanese, Trendy; Alcohol, Upscale; Japanese, Ramen; Alcohol, Tapas/Small Plates; Classy, Desserts; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'
 
novSamedi='Japanese, Ramen; Alcohol, Tapas/Small Plates; Classy, Desserts; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'

novDimanche='Alcohol, Upscale; Classy, Upscale; Japanese, Ramen; Alcohol, Tapas/Small Plates; Classy, Desserts; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy'

decLundi='Alcohol, Sandwiches; Classy, Hipster; Alcohol, Burgers; Alcohol, American (New), Breakfast & Brunch, Classy; Alcohol, Upscale'
 
decMardi='Japanese, Trendy; Alcohol, Upscale'
 
decMercredi='Alcohol, Vegetarian; Alcohol, Upscale'
 
decJeudi='Japanese, Ramen; Classy, Hipster; Alcohol, Upscale'
 
decVendredi='Japanese, Trendy; Alcohol, Upscale'
 
decSamedi='Japanese, Ramen; Alcohol, Upscale'
 
decDimanche='Alcohol, Tapas/Small Plates; Alcohol, Upscale; Classy, Upscale; Alcohol, American (New), Breakfast & Brunch, Classy'
 
