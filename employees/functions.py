import employees.validations
import os



#Function header for add_employee
def add_employee():
  print("Adding Employee") #function body for add employee
  emp_id = employees.validations.generate_employee_id()

  fn = employees.validations.validate_first_name()

  ln = employees.validations.validate_last_name()

  dep = employees.validations.validate_depth()

  emp_salary = employees.validations.add_employee_salary()

  email = employees.validations.generate_email(ln,fn,employees)

  first_last = fn + " " + ln



  try:
    with open('employees/employees1.txt','a') as infile:
      infile.write(emp_id+"\n")
      infile.write(first_last+"\n")
      infile.write(dep + "\n") 
      infile.write(emp_salary+"\n")
      infile.write(email+"\n")

  except FileNotFoundError:
    print("File Not Found")




# Function Header for lookup_employee
def lookup_employees(emp_id):
  print("Lookup Employee")# Function Body for lookup_employee
  found = False
  try:
    with open('employess/employees1.txt','r') as fl:
      for each_line in fl:
        i_d = each_line.rstrip("\n")
        name = fl.readline().rstrip("\n")
        dp = fl.readline().rstrip("\n")
        sl = fl.readline().rstrip("\n")
        em = fl.readline().rstrip("\n")

        if i_d == emp_id:
          print(f"Name: {name} \nDepartment: {dp} \nSalary: {sl} \nEmail: {em}")
          found = True
          break
    return found

  except FileNotFoundError:
    print("File Not Found")
    return False





# Function Header for update_employee_name
def update_employee_name():
  print("Updating Employee Name")   # Function Body for update_employee_name
  emp_id = input("Enter your employee id: ")
  look = lookup_employees(emp_id)
  if not look:
    print("Employee Not Found")
    return
  try: 
    with open("employees/employees1.txt", "r") as infile, open('emplyees/temp.txt', 'w') as outfile:
      for line in infile:
        i_d = line.rstrip("\n")
        name = infile.readline().rstrip("\n")
        dp = infile.readline().rstrip("\n")
        sl = infile.readline().rstrip("\n")
        em = infile.readline().rstrip("\n")
        if emp_id != i_d:
          outfile.write(i_d + "\n" + name + "\n" + dp +"\n" + sl + "\n" + em + "\n")
        else:
          name_1 = str(employees.validations.validate_first_name())
          name_2 = str(employees.validations.validate_last_name())
          outfile.write(i_d + "\n" + name_1 +" "+ name_2 + "\n" + dp +"\n" + sl + "\n" + em + "\n")
  except FileNotFoundError:
    print("File Not Found")

  os.remove("employees.txt")
  os.rename("temp.txt","employees1.txt")





# Function Header for update_employee_salary
def update_employee_salary():
  print("Updating Employee Salary")     # Function Body for update_employee_salary
  emp_id = input("Enter your employee id: ")
  look = lookup_employees(emp_id)
  if not look:
    print("Employee Not Found")
    return

  try:
    with open("employees/employees1.txt", "r") as infile, open('employees/temp.txt', 'w') as outfile:
      for line in infile:
        i_d = line.rstrip("\n")
        name = infile.readline().rstrip("\n")
        dp = infile.readline().rstrip("\n")
        sl = infile.readline().rstrip("\n")
        em = infile.readline().rstrip("\n")
        if emp_id != i_d:
          outfile.write(i_d + "\n" + name + "\n" + dp +"\n" + sl + "\n" + em + "\n")
        else:
          vs = str(employees.validations.add_employee_salary())
          outfile.write(i_d + "\n" + name + "\n" + dp +"\n" + vs + "\n" + em + "\n")

  except FileNotFoundError:
    print("File Not Found")


  os.remove("employees/employees1.txt")
  os.rename("employees/temp.txt","employees/employees1.txt")




# Function Header for update_employee_dept
def update_employee_dept():
  print("Updating Employee Department")     # Function Body for update_employee_dept
  emp_id = input("Enter your employee id: ")
  look = lookup_employees(emp_id)
  if not look:
    print("Employee not found")
    return

  try:
     with open("employees/employees1.txt", "r") as infile, open('employees/temp.txt', 'w') as outfile:
      for each_line in infile:
        i_d = each_line.rstrip("\n")
        name = infile.readline().rstrip("\n")
        dp = infile.readline().rstrip("\n")
        sl = infile.readline().rstrip("\n")
        em = infile.readline().rstrip("\n")

        if emp_id != i_d:
          outfile.write(i_d + "\n" + name + "\n" + dp +"\n" + sl + "\n" + em + "\n")
        else:
          vd = str(employees.validations.validate_depth())
          outfile.write(i_d + "\n" + name + "\n" + vd +"\n" + sl + "\n" + em + "\n")

  except FileNotFoundError:
    print("File Not Found")

  os.remove("employees/employees1.txt")
  os.rename("employees/temp.txt","employees/employees1.txt")




# Function Header for display_employees
def display_employees():
  print("Displaying Employees")
  print(f'\n{"ID":^8} | {"Name":<25} | {"Salary":>10} | {"Dept":^6} | {"Email":<20}')
  with open('employees/employees1.txt','r') as infile:
    for line in infile:
      employee_id = line.rstrip("\n")
      employee_name = infile.readline().rstrip("\n")
      employee_dept = infile.readline().rstrip("\n")
      employee_salary = infile.readline().rstrip("\n")
      employee_email = infile.readline().rstrip("\n")


      print(f'{employee_id:^8} | {employee_name:<25} | {employee_salary:>10} | {employee_dept:^6} | {employee_email:<20} ')




# Function Header for delete_employee
def delete_employee():
  print("Delete Employee")# Function Body for delete_employee
  emp_id = input("Enter your employee id: ")
  look = lookup_employees(emp_id)
  if not look:
    print("Employee not found")
    return
  try:
    with open("employees/employees1.txt", "r") as infile, open('employees/temp.txt', 'w') as outfile:
      for each_line in infile:
        i_d = each_line.rstrip("\n")
        name = infile.readline().rstrip("\n")
        dp = infile.readline().rstrip("\n")
        sl = infile.readline().rstrip("\n")
        em = infile.readline().rstrip("\n")

        if emp_id != i_d:
          outfile.write(i_d + "\n" + name + "\n" + dp +"\n" + sl + "\n" + em + "\n")

  except FileNotFoundError:
    print("File Not Found")

  os.remove("employees/employees1.txt")
  os.rename("employees/temp.txt","employees/employees1.txt")



def employee_operations():
  uc = ""
  while uc.lower() != 'x':
    print("\n\n--Employee Management--\n")
    print("1.Add Employee")
    print("2.Lookup Employee")
    print("3.Update Employee Name")
    print("4.Update Employee Salary")
    print("5.Update Employee Department")
    print("6.Display Employee")
    print("7.Delete Employee")
    print("x.Exit")

    uc = input("Enter your choice ")
    if uc == "1":
      continue_input = "y"
      while continue_input != "n" and continue_input != "N":
        add_employee()
        continue_input = input("Do you want to add another employee? Y or N  ")




    elif uc =="2":
      emp_id = input("Enter your employee id: ")
      found = lookup_employees(emp_id)


      if  not found:
        print("Employee Not Found")

    elif uc == "3":
      update_employee_name()
    elif uc == "4":
      update_employee_salary()
    elif uc == "5":
      update_employee_dept()
    elif uc == "6":
      display_employees()
    elif uc == "7":
      delete_employee()
    elif uc == "x":
      print("Goodbye")
    else:
      print("Invalid Choice")

