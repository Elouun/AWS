restaurant = 'Select * from Business where name = "?n"'

user = 'select * from Users where name = "?n"'

review_by_user = 'SELECT * FROM Users u,Reviews r where u.user_id = r.user_id and name= "?n"'