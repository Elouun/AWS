restaurant = 'Select * from Business where name = "?n"'
restaurantID = 'Select * from Business where business_id = "?n"'

user = 'select * from Users where name = "?n"'
userID = 'Selct * from Users where user_id = "?n"'

review_by_user = 'SELECT text,stars FROM Users u,Reviews r where u.user_id = r.user_id and name="?n" limit 5'
review_by_user_id = 'SELECT text,stars FROM Users u,Reviews r where u.user_id = r.user_id and user_id="?n" limit 5'


restauetoiles = 'select * from Business where stars = "?n"'

restauVille = 'select * from Business where city = "?n"'

restaualcoholterrasse = 'select * from Business where Alcohol = 1 and OutdoorSeating = 1 and city = "?n"'