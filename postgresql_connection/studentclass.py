import psycopg2

class Student():
  def __init__(self, host, dbname, user, password, port):
    self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
    self.mycursor = self.conn.cursor()
    print('connection established')

  def create_table(self):
    create_student = '''create table student(id int primary key,
                        name varchar(30),
                        age int,
                        sex varchar(2),
                        department varchar(30))'''
    self.mycursor.execute(create_student)
    self.conn.commit()
    print('\nStudent table created successfully')

  def insert_student(self, stu_id, name, age, sex, department):
    student = 'insert into student values(%s, %s, %s, %s, %s)'
    data = (stu_id, name, age, sex, department)
    self.mycursor.execute(student, data)
    self.conn.commit()
    print('\nStudents inserted successfully')
    
  def retrive_student(self):
    self.mycursor.execute('select * from student')
    result = self.mycursor.fetchall()
    for i in result:
      print(i)

  def update_age(self, stu_id, age):
    self.mycursor.execute('update student set age=%s where id=%s', (age, stu_id))
    self.conn.commit()
    print('\nStudent updated successfully')

  def delete_student(self, stu_id):
    self.mycursor.execute('delete from student where id=%s', (stu_id,))
    self.conn.commit()
    print('\nStudent deleted successfully')

  def drop_student(self):
    self.mycursor.execute('drop table student')
    self.conn.commit()
    print('Student table dropped successfully')

  def close_connection(self):
    self.mycursor.close()
    self.conn.close()
    print('Connection closed')

if __name__ == '__main__':
  con = Student(host='localhost', dbname='demo', user='postgres', password='12345', port=5432)

  con.create_table()

  con.insert_student(105, 'Eva', 22, 'F', 'Biology')
  con.insert_student(106, 'Frank', 28, 'M', 'Chemistry')
  con.insert_student(107, 'Grace', 30, 'F', 'Psychology')
  con.insert_student(108, 'Hannah', 26, 'F', 'Economics')
  con.insert_student(109, 'Ivy', 21, 'F', 'English Literature')
  con.insert_student(110, 'Jack', 27, 'M', 'Art History')

  print('\nStudent information')
  con.retrive_student()

  con.update_age(109, 23)

  con.delete_student(110)

  print('\nStudent information after updating and deleting records')
  con.retrive_student()

  print('\ndropping student table')
  con.drop_student()

  print('\nclosing connection')
  con.close_connection()
