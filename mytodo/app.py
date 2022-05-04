from chalice import Chalice
import pymysql
import logging
import json
import sys

app = Chalice(app_name='test')
db_name = 'sys'
db_user = 'root'
db_pass = 'adminadmin'
rds_host = 'db-yummy.c13ygo7twrsm.eu-west-3.rds.amazonaws.com'
db_port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=db_user, passwd=db_pass, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


@app.route('/', methods=["GET"])
def default():
    return "Yummy'dvice"

@app.route('/save_data', methods=["GET"])
def save_data():

        with conn.cursor() as cur:
            cur.execute("INSERT INTO test (clef, valeur) VALUES (%s, %s)", (1,2))
            conn.commit()

@app.route('/get_data')
def get_data():

        with conn.cursor() as cur:    
            cur.execute("select * from test")
            formulas = cur.fetchall() 
        return json.dumps(formulas, indent=4)
                
