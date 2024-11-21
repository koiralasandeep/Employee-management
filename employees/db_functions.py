import sqlite3
from employees.validations import  validate_first_name, validate_last_name, generate_email, validate_depth, add_employee_salary
from suchi.suchi_pretty_print import suchi_print


conn = sqlite3.connect("employees/employees6.db")
cur = conn.cursor()


def employee_operations():
  tab = '''CREATE TABLE IF NOT EXISTS 
  employees (
  empid INTEGER PRIMARY KEY,
  name TEXT,
  department TEXT,
  salary REAL,
  email TEXT)'''
  cur.execute(tab)
  conn.commit()

  
  choice = ""
  while choice.lower() != 'x':
    print("\n\n--Employee Management--\n")
    print("1.Display Employee")
    print("2.Add Employee")
    print("3.Lookup Employee")
    print("4.Update Employee Name")
    print("5.Update Employee Salary")
    print("6.Update Employee Department")
    print("7.Delete Employee")
    print("x.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      display_employees(cur)
    elif choice == "2":
      continue_input = "y"
      while continue_input.lower() != "n":
        add_employee(conn,cur)
        continue_input = input("Do you want to add another employee? Y or N  ")
    elif choice == "3":
      empid = input("Enter employee ID to lookup: ")
      lookup_employee(cur, empid)
    elif choice == "4":
      update_employee_name(conn, cur)
    elif choice == "5":
      update_employee_salary(conn, cur)
    elif choice == "6":
      update_employee_department(conn, cur)
    elif choice == "7":
      delete_employee(conn, cur)
    elif choice == 'x':
      print('Thank You')
    else:
      print('Invalid Choice')

  conn.close()




def add_employee(conn, cur):
  fn = validate_first_name()
  ln = validate_last_name()
  email = generate_email(ln,fn, cur)
  department = validate_depth()
  salary = add_employee_salary()
  name = fn + " " + ln

  employee_data = (name,department,salary,email)
  insert_data = '''INSERT INTO employees(name,department,salary,email)
  VALUES(?,?,?,?)'''
  cur.execute(insert_data, employee_data)

  conn.commit()



def display_employees(cur):
  select = '''SELECT * FROM employees'''
  cur.execute(select)
  rows = cur.fetchall()
  print("{:<10} {:<20} {:<20} {:<10} {:<30}".format("Employee ID", "Name", "Department", "Salary", "Email"))

  for row in rows:
    empid, name, department, salary, email = row
    suchi_print("{:<10} {:<20} {:<20} {:<10} {:<30}".format(empid, name, department, salary, email))
  conn.commit()



def lookup_employee(cur, empid):
  select = '''SELECT * FROM employees WHERE empid = ?'''
  cur.execute(select, (empid,))
  row = cur.fetchone()
  if row is not None:
    empid, name, department, salary, email = row
    print("Employee ID:", empid)
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
    print("Email:", email)
    return True  # Employee found
  else:
    return False 



def update_employee_name(conn, cur):
  id = input("Enter your employee id: ")
  update_sql = '''UPDATE employees
  SET name = ?
  WHERE empid = ?'''
  new_name = validate_first_name() + " " + validate_last_name()
  cur.execute(update_sql,(new_name, id))

  row = cur.rowcount
  if row == 0:
    print('Employee Not Found')
  else:
    conn.commit()
    print('Employee Name Updated')
  


def update_employee_department(conn, cur):
  id = input("Enter your employee id: ")
  update_sql = '''UPDATE employees
  SET department = ?
  WHERE empid = ?'''
  new_department = validate_depth()
  cur.execute(update_sql,(new_department, id))

  row = cur.rowcount
  if row == 0:
    print('Employee Not Found')
  else:
    conn.commit()
    print('Employee Department Updated')



def update_employee_salary(conn, cur):
  id = input("Enter your employee id: ")
  update_sql = '''UPDATE employees
  SET salary = ?
  WHERE empid = ?'''
  new_salary = add_employee_salary()
  cur.execute(update_sql,(new_salary, id))

  row = cur.rowcount
  if row == 0:
    print('Employee Not Found')
  else:
    conn.commit()
    print('Employee Salary Updated')


  
def delete_employee(conn,cur):
  id = input("Enter your employee id: ")
  del_sql = '''DELETE FROM employees
  WHERE empid = ?'''
  cur.execute(del_sql, (id,))
  row = cur.rowcount
  if row == 0:
    print('Employee Not Found')
  else:
    conn.commit()
    print('Employee Deleted')
