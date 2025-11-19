import mysql.connector

def get_connection():
    conex = mysql.connector.connect(user='root', password='Gb2410!', host='127.0.0.1', database='estac_mysql')
    return conex