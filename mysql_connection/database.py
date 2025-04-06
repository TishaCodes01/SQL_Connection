import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='12345')
mycursor = conn.cursor()
mycursor.execute('create database demo')
