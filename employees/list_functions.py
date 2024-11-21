from validations import generate_email, generate_next_id, validate_first_name, validate_last_name, validate_depth, add_employee_salary


def file_to_list():
  employees = []
  try:
    with open("employees/employees2.txt","r") as fp:
      for line in fp:
        employees.append(line.rstrip("\n"))

  except:
    print("File not found")

  return employees


def list_to_file(employees):
  with open('employees/employees2.txt','w') as infile:
    for item in employees:
      infile.write(item + '\n')
  return employees



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
        while continue_input != "n" and continue_input != "N":
          add_employee(employees)
          continue_input = input("Do you want to add another employee? Y or N  ")


    elif choice == "2":
      empid = input("Enter ID to lookup: ")
      found, idx = lookup_employee(employees, empid)

    elif choice == "3":
      employees = update_employee_name(employees)

    elif choice == "4":
      employees = update_employee_salary(employees)

    elif choice == "5":
      employees = update_employee_department(employees)

    elif choice == "6":
      display_employees(employees)

    elif choice == "7":
      employees = delete_employee(employees)

    elif choice == "x":
      print("Goodbye")
      break

    else:
      print("Invalid Choice")


  list_to_file(employees)


def add_employee(employees):
  print("\n---Adding Employee---\n")
  empid = generate_next_id(employees)


  fn = validate_first_name()
  ln = validate_last_name()
  department = validate_depth()
  salary = add_employee_salary()
  email = generate_email(ln,fn,employees)

  name = fn +" "+ ln
  employees.append(empid)
  employees.append(name)
  employees.append(department)
  employees.append(salary)
  employees.append(email)
  return employees


def lookup_employee(employees, empid):
  if empid in employees:
    index_position = employees.index(empid)
    print("\nName:", employees[index_position +1])
    print("Department:", employees[index_position +2])
    print("Salary:", employees[index_position +3])
    print("Email:", employees[index_position + 4],"\n")
    return True, index_position
  else:
    print("\n---Employee not found---\n")
    return False, 0


def update_employee_name(employees):
  print("\n---Updating Name ---\n")
  empid = input("Enter employee ID : ")
  found, idx = lookup_employee(employees, empid)
  if found:
    employees[idx+1] = validate_first_name() + " " + validate_last_name()
  return employees


def update_employee_department(employees):
  print("\n---Updating Employee Department---\n")
  empid = input('Enter employee ID: ')
  found, idx = lookup_employee(employees, empid)
  if found:
    employees[idx+2] = validate_depth()
  return employees


def update_employee_salary(employees):
  print("\n---Updating Employee Salary---\n")
  empid = input('Enter employee ID: ')
  found, idx = lookup_employee(employees, empid)
  if found:
    employees[idx+3] = add_employee_salary()
  return employees


def display_employees(employees):
  idslice = employees[::4]
  for id in idslice:
    idx = employees.index(id)
    print(f'{employees[idx] : <10} | {employees[idx+1] : <20} | {employees[idx+2] : ^10} | {employees[idx+3] : <10} | {employees[idx+4] : <20}')


def delete_employee(employees):
  print("\n---Deleting Employee ---\n")
  empid = input("Enter employee ID: ")
  found, idx = lookup_employee(employees, empid)
  if found:
    for i in range(4):
      del employees[idx]
  return employees




