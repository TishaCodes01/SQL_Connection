import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='12345', database='demo')

mycursor = conn.cursor()

mycursor.execute('show databases')

for i in mycursor:
  print(i)

print('\nStudent table values')


#fetching student details
mycursor.execute('select * from student')
result = mycursor.fetchall()
for i in result:
  print(i)

#creating books table
books_create = 'create table books(book_id int(10) primary key, name varchar(30), price float(10))'
mycursor.execute(books_create)
print('table create successfully')

#inserting values to table
books_insert = ('insert into books values(%s, %s, %s)')
data = [
  (1, 'good in a coffin', 489.43),
  (2, 'a love treaty', 287.98),
  (3, 'the intelligent investor', 549.99)
]
mycursor.executemany(books_insert, data)
conn.commit()
print('\nData inserted successfully\n')

#fetching books detail
mycursor.execute('select * from books')
result2 = mycursor.fetchall()
for i in result2:
  print(i)

#updating table
update_books = 'update books set price=699.89 where book_id=3'
mycursor.execute(update_books)
conn.commit()
print('\nData updated successfuly\n')

mycursor.execute('select * from books')
result3 = mycursor.fetchall()
for i in result3:
  print(i)

#deleting data
delete_book = 'delete from books where book_id=2'
mycursor.execute(delete_book)
conn.commit()
print('\nData deleted successfully\n')

mycursor.execute('select * from books')
result4 = mycursor.fetchall()
for i in result4:
  print(i)

# drop table query
mycursor.execute('drop table books')
conn.commit()
print('\nTable books deleted')

conn.close()