import mysql.connector

def get_connection():
    conex = mysql.connector(user='root', password='ACRIAR',
                            host='acriar', database='estacionamento')
    return conex