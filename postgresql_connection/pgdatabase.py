import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres', password='12345', port=5432)
conn.autocommit = True

mycursor = conn.cursor()
mycursor.execute('CREATE DATABASE demo')

mycursor.close()
conn.close()