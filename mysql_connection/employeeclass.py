import mysql.connector

class Employee():
  def __init__(self, host, user, password, database):
    self.conn = mysql.connector.connect(
      host = host,
      user = user,
      password = password,
      database = database
    )
    self.cursor = self.conn.cursor()
    self.create_table()

  def create_table(self):
    employee_create = 'create table employee(emp_id int(10) PRIMARY KEY AUTO_INCREMENT, emp_name varchar(30), emp_dept varchar(30), emp_salary decimal(10,2))'
    self.cursor.execute(employee_create)
    self.conn.commit()

  def insert_employee(self, emp_name, emp_dept, emp_salary):
    employee_insert = 'insert into employee(emp_name, emp_dept, emp_salary) values(%s, %s, %s)'
    data = (emp_name, emp_dept, emp_salary)
    self.cursor.execute(employee_insert, data)
    self.conn.commit()
    print('Employee inserted successfully')

  def retrive_employee(self):
    self.cursor.execute('select * from employee')
    result = self.cursor.fetchall()
    for i in result:
      print(i)

  def update_salary(self, employee_id, new_salary):
    update_query = 'update employee set emp_salary=%s where emp_id=%s'
    data = (new_salary, employee_id)
    self.cursor.execute(update_query, data)
    self.conn.commit()
    print('Salary updated successfully')

  def delete_employee(self, emp_id):
    delete_employee = 'delete from employee where emp_id=%s'
    data = (emp_id,)
    self.cursor.execute(delete_employee, data)
    self.conn.commit()
    print('Employee deleted successfully')

  def close_connection(self):
    self.cursor.close()
    self.conn.close()
    print('Database connection closed')

if __name__ == '__main__':
  con = Employee(host='localhost', user='root', password='12345', database='demo')

  con.insert_employee('John', 'IT', 40000)
  con.insert_employee('Lisa', 'IT', 50000)
  con.insert_employee('Gauri', 'Medical', 80000)
  con.insert_employee('Jack', 'HR', 45000)
  con.insert_employee('Shreya', 'Civil', 37000)
  con.insert_employee('Mala', 'Architect', 58000)

  print('Employee Data')
  con.retrive_employee()

  print('\nUpdate salary')
  con.update_salary(3, 74000)
  print('After update Employee data')
  con.retrive_employee()

  print('\ndelete employee')
  con.delete_employee(5)
  print('After deleted Employee data')
  con.retrive_employee()

  print()
  con.close_connection()