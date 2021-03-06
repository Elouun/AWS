import pymysql
import requests

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
        
        return "connexion echouee"
    
    if conn != None :
        return conn
    else :
        return "connexion echouee"

def reco(param, model):
    
    if model == "indian":
        link = "http://93.12.245.177:8000/recommandation_indian?reco="
    else :
        link = "http://93.12.245.177:8000/recommandation_french?reco="
        
    link = link + param
    
    print(link)
    
    res = requests.get(link)
    
    return res.text
    
def request(sql, conn):
    
    res = ""

    with conn.cursor() as cur:   

        cur.execute(sql)
        
        #cur.execute("select count(*) from Business")
        
        
        res = cur.fetchall()

    return res

def insert(sql, conn):
    
    with conn.cursor() as cur:    

        cur.execute(sql)

    conn.commit()      
