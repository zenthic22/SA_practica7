import mysql.connector
from config.config import config

db = config['database']()

def dbConnection():
    try:
        mydb = mysql.connector.connect(
            host=db.host,
            user=db.user,
            password=db.password,
            database=db.database
        )
        return mydb, None
    except Exception as ex:
        return None, ex