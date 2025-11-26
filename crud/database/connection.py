import mysql.connector

def get_connection():
    conex = mysql.connector.connect(user='root', password='Gb2410!', host='localhost', database='estac_mysql',
    auth_plugin='mysql_native_password')
    return conex