# Name:   Sandeep Koirala
# Date: 10/03/2024


from employees.validations import generate_email, get_next_emp_multi,validate_first_name, validate_last_name, add_employee_salary, validate_depth, generate_next_id

def file_to_list():
  employees=[]
  try:
    with open('employees/employees.txt','r') as infile:
      employees = [line.rstrip("\n").split(";") for line in infile]
  except:
    print("File not found")
    return []
  return employees

def list_to_file(employees):
  with open('employees/employees.txt','w') as outfile:
    for emp in employees:
      idx = employees.index(emp)
      outfile.write(employees[idx] [0] + ";" + employees[idx] [1] + ";" +  employees[idx] [2] + ";" + employees[idx][3] + ";" + employees[idx][4]+"\n")

def employee_operations():
  employees = file_to_list()
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
      found, idx = lookup_employee(employees, empid)
    elif choice == "6":
      display_employees(employees)
    elif choice == "3":
      employees = update_employee_name(employees)
    elif choice == "7":
      employees = delete_employee(employees)
    elif choice == "4":
      employees = update_employee_salary(employees)
    elif choice == "5":
      employees = update_employee_dept(employees)
    elif choice.lower() == "x":
      print("Goodbyee")
    else:
      print("Invalid Choice")




  list_to_file(employees)

def add_employee(employees):
  empid = get_next_emp_multi(employees)
  fn = validate_first_name()
  ln = validate_last_name()
  name = fn + " " + ln
  dept = validate_depth()
  salary = add_employee_salary()
  email = generate_email(ln,fn,employees)
  new_employee = [empid, name, dept, salary, email]
  employees.append(new_employee)
  return employees


def lookup_employee(employees, empid):
  for emp in employees:
    if empid in emp:
      idx = employees.index(emp)
      print("\nName:", employees[idx] [1])
      print("Department:", employees[idx] [2])
      print("Salary:", employees[idx] [3])
      print("Email:", employees[idx] [4])
      return True, idx
  print("\n--Employee Not Found--\n")
  return False, 0

def update_employee_name(employees):
  print("--Updating Name--")
  empid= input("Enter employee ID: ")
  found, idx = lookup_employee(employees, empid)
  if found:
    employees[idx][1] = validate_first_name() + " " + validate_last_name()
  return employees

def update_employee_salary(employees):
  print("--Updating Salary--")
  empid= input("Enter employee ID: ")
  found, idx = lookup_employee(employees, empid)
  if found:
    employees[idx][3] = add_employee_salary()
  return employees

def update_employee_dept(employees):
  print("--Updating Department--")
  empid= input("Enter employee ID: ")
  found, idx = lookup_employee(employees, empid)
  if found:
    employees[idx][2] = validate_depth()
  return employees


def delete_employee(employees):
  print("\n--Deleting Employee--\n")
  empid= input("Enter employee ID: ")
  found, idx = lookup_employee(employees, empid)
  if found:
    del employees[idx]
  return employees


def display_employees(employees):
  if len(employees) == 0:
    print("\n\t\t --- No Employee found --- ")
    return
  print(f"{'ID':^7} | {'Name':<25} | {'Department':^10} | {'Salary':>6} | {'Email':<20}")
  for emp in employees:
    idx = employees.index(emp)
    print(f"{employees[idx] [0]:^7} | {employees[idx] [1]:<25} | {employees[idx] [2]:^10} | {employees[idx][3]:>6} | {employees[idx][4]:<20}")
















