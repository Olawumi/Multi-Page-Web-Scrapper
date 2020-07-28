from sqlalchemy import create_engine
import mysql.connector

connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'sakila')

cur = connection.cursor()

"""
cur.execute("select * from actor")
actor = cur.fetchall()
print(actor)
"""