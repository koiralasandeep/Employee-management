import pickle
import os
# from employees.classes import Employee
from classes2 import Employee
from employees.validations import validate_first_name, validate_last_name, validate_depth, generate_email, add_employee_salary


def file_to_dictionary():
  if os.path.getsize("employees/employees5.class") == 0:
    return {}
  try:
    with open("employees/employees5.class","rb") as fp:
      employee_dic = pickle.load(fp)
      return employee_dic
  except:
    print("File Not Found")
    return {}

def employee_operations():
  employee_dic = file_to_dictionary() 
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
      display_employees(employee_dic)

    elif choice == "2":
      continue_input = "y"
      while continue_input.lower() != "n":
        add_employee(employee_dic)
        continue_input = input("Do you want to add another employee? Y or N  ")
    elif choice == "3":
      empid = input("Enter employee ID to lookup: ")
      lookup_employee(empid, employee_dic)
    elif choice == "4":
      employee_dic = update_employee_name(employee_dic)
    elif choice == "5":
      employee_dic = update_employee_salary(employee_dic)
    elif choice == "6":
      employee_dic = update_employee_department(employee_dic)
    elif choice == "7":
      employee_dic = delete_employee(employee_dic)
    elif choice.lower() == "x":
      print("Goodbye")
    else:
      print("Invalid Choice")

  dictionary_to_file(employee_dic)
  

def display_employees(employee_dic):
  if len(employee_dic) == 0:
    print("No Employee Found")
  for employee in employee_dic.values():
    print(employee)
    


def generate_next_empID_class(employee_dic):
  if len(employee_dic) == 0:
    return 3001
  k = employee_dic.keys()
  maximum = max(k) + 1
  return maximum

def add_employee(employee_dic):
  empid = generate_next_empID_class(employee_dic)
  fn = validate_first_name()
  ln = validate_last_name()
  email = generate_email(ln,fn, employee_dic)
  department = validate_depth()
  salary = add_employee_salary()
  name = fn + " " + ln

  employee = Employee(empid, name, 'phone', department, salary, email)
  employee_dic[empid]= employee
  return employee_dic


def lookup_employee(empid, employee_dic):
  empid = int(empid)
  if empid in employee_dic:
    print(employee_dic[empid])
    return True
  else:
    print("Employee Not Found")
    return False

def update_employee_name(employee_dic):
  empid = int(input("Enter your employee ID: "))
  print("Employee IDs in Dictionary:", list(employee_dic.keys()))
  found = lookup_employee(empid, employee_dic)
  if found:
    f_name = validate_first_name()
    l_name = validate_last_name()
    name = f_name + " " + l_name
    employee_dic[empid].set_name(name)
  return employee_dic

def update_employee_salary(employee_dic):
  empid = int(input("Enter your employee ID: "))
  found = lookup_employee(empid, employee_dic)
  if found:
    new_salary = add_employee_salary()
    employee_dic[empid].set_salary(new_salary)
  return employee_dic

def update_employee_department(employee_dic):
  empid = int(input("Enter your employee ID: "))
  found = lookup_employee(empid, employee_dic)
  if found:
    new_dep = validate_depth()
    employee_dic[empid].set_department(new_dep)
  return employee_dic

def delete_employee(employee_dic):
  empid = int(input("Enter your employee ID: "))
  found = lookup_employee(empid, employee_dic)
  if found:
    del employee_dic[empid]
    print("successfull")
  return employee_dic


def dictionary_to_file(employee_dic):
  with open("employees/employees5.class","wb") as fp:
    pickle.dump(employee_dic, fp)
  

  
    
    
    