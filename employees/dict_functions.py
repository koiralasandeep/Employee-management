import pickle
import os
from suchi.suchi_pretty_print import suchi_print

from employees.validations import add_employee_salary, generate_email, validate_depth, validate_first_name, validate_last_name


def employee_operations():
  employees = file_to_dictionary()
  choice = ""
  while choice.lower() != 'x':
    print("\n\n--Employee Management--\n")
    print("1.Add Employee")
    print("2.Lookup Employee")
    print("3.Update Employee Name")
    print("4.Update Employee Salary")
    print("5.Update Employee Department")
    print("6.Display Employee")
    print("7.Delete Employee")
    print("x.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        continue_input = "y"
        while continue_input.lower() != "n":
          add_employee(employees)
          continue_input = input("Do you want to add another employee? Y or N  ")
    elif choice == "2":       
      empid = input("Enter employee ID to lookup: ")
      lookup_employee(employees, empid)

    elif choice == "3":
      employees = modify_name(employees)

    elif choice == "4":
      employees = modify_salary(employees)
      
    elif choice == "5":
      employees = modify_department(employees)
      
    elif choice == "6":
      display_employees(employees)
    
    elif choice == "7":
      employees = delete_employee(employees)
    
    elif choice.lower() == "x":
      print("Goodbyee")
    else:
      print("Invalid Choice")
  
  
  
  
  dictionary_to_file(employees)

def file_to_dictionary():
  if os.path.getsize("employees/employees4.pkl") == 0:
    return {}
  try:
    with open("employees/employees4.pkl","rb")as fp:
      employees = pickle.load(fp)
    return employees
  except FileNotFoundError:
    print("File Not Found")
    return{}

def get_next_empid_dict(employees):
  if len(employees) == 0:
    return 3001
  k = employees.keys()
  maximum = max(k) + 1
  return maximum
  
def add_employee(employees):
  empid = get_next_empid_dict(employees)
  fn = validate_first_name()
  ln = validate_last_name()
  email = generate_email(ln,fn, employees)
  department = validate_depth()
  salary = add_employee_salary()
  name = fn + " " + ln
  new_employee = {"name":name,"department":department,"email":email,"salary":salary}
  employees[empid] = new_employee
  return employees

def lookup_employee(employees, empid):
  empid = int(empid)
  for key, value in employees.items():
    if key == empid:
      print("Name:", value.get("name","-"))
      print("Department:", value.get("department","-"))
      print("Salary:",value.get("salary","-"))
      print("Email:",value.get("email","-"))
      return True
  print("Employee Not Found")
  return False

def modify_name(employees):
  empid= int(input("ENter the employee ID: "))
  found = lookup_employee(employees, empid)
  if found:
    fn = validate_first_name()
    ln = validate_last_name()
    full_name = fn + " " + ln
    employees[empid]["name"]= full_name
    print("NAME mODIFIED sUCCESFULLY")
  return employees

def modify_department(employees):
  empid= int(input("ENter the employee ID: "))
  found = lookup_employee(employees, empid)
  if found:
    department = validate_depth()
    employees[empid]["department"]= department
    print("Department Modified!!")
  return employees

def modify_salary(employees):
  empid= int(input("ENter the employee ID: "))
  found = lookup_employee(employees, empid)
  if found:
    salary = add_employee_salary()
    employees[empid]["salary"]= salary
    print("Department Modified!!")
  return employees


def display_employees(employees):
  print(f"{'ID':^7} | {'Name':<25} | {'Department':^10} | {'Salary':>6} | {'Email':<20}")
  for empid, value in employees.items():
    name = value.get("name","-")
    dept = value.get("department","-")
    salary = value.get("salary","-")
    email = value.get("email","-")
    print(f"{empid:^7} | {name:<25} | {dept:^10} | {salary:>6} | {email:<20}")



def delete_employee(employees):
  empid = int(input("Enter the employee   ID: "))
  found = lookup_employee(employees, empid)
  if found:
    del employees[empid]
    print("Successfull")
  return employees


def dictionary_to_file(employees):
  with open("employees/employees4.pkl","wb") as fp:
    pickle.dump(employees, fp)
  





  