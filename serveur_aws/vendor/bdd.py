import pymysql

# mysql --host=db-yummy.c13ygo7twrsm.eu-west-3.rds.amazonaws.com --user=root --password=adminadmin sys
# source "sqlfile.sql"


db_name = 'sys'
db_user = 'root'
db_pass = 'adminadmin'
rds_host = 'yummy.c13ygo7twrsm.eu-west-3.rds.amazonaws.com'
db_port = 3306

def connect():

    conn = None

    try:
        conn = pymysql.connect(host=rds_host, user=db_user, passwd=db_pass, db=db_name, connect_timeout=5)
        print("connexion reussie")
    
    except pymysql.MySQLError as e:
        
        print("connexion echouee")

    return conn

def request(sql, conn):

    with conn.cursor() as cur:    

        cur.execute(sql)
        res = cur.fetchall()
                       
        return res
