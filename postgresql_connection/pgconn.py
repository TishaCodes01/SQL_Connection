import psycopg2

conn = psycopg2.connect(host='localhost', dbname='demo', user='postgres', password='12345', port=5432)
mycursor = conn.cursor()

create_student = '''create table if not exists student(id serial primary key,
                    name varchar(30),
                    age int,
                    department varchar(30),
                    cgpa float)'''
mycursor.execute(create_student)
conn.commit()
print('student table created successfully')

insert_student = 'insert into student(name, age, department, cgpa) values(%s, %s, %s, %s)'
data = [('Alice', 21, 'IT', 9.4),
        ('Bob', 25, 'civil', 9.2),
        ('Lisa', 23, 'CSE', 8.7),
        ('Jack', 20, 'EC', 8.5)]
mycursor.executemany(insert_student, data)
conn.commit()
print('\nData inserted successfully')

print('\nRetrieving data')
mycursor.execute('select * from student')
result = mycursor.fetchall()
for i in result:
  print(i)

print('\nusing where clause')
mycursor.execute('select name, age from student where age>%s', (22,))
result = mycursor.fetchall()
for i in result:
  print(i)

print('\nusing orderby')
mycursor.execute('select * from student order by name desc')
result = mycursor.fetchall()
for i in result:
  print(i)

print('\nupdate query \nafter updating records are')
mycursor.execute('update student set department=%s where id=%s', ('mechanical',4))
conn.commit()
mycursor.execute('select * from student')
result = mycursor.fetchall()
for i in result:
  print(i)

print('\ndelete query \nrecords after deletion')
mycursor.execute('delete from student where age>%s',(22,))
mycursor.execute('select * from student')
result = mycursor.fetchall()
for i in result:
  print(i)

print('\nlimit and offset')
mycursor.execute('select * from student limit 1 offset 1')
result = mycursor.fetchone()
print(result)

print('\ndrop query')
mycursor.execute('drop table student')
conn.commit()
print('student table dropped successfully')

mycursor.close()
conn.close()