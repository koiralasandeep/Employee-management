def generate_employee_id():
  try:
    infile = open('employees.txt','r')
  except FileNotFoundError:
    print("File Not Found")
  else:
    for line in infile:
      line1 = line.rstrip("\n")
      line2 = infile.readline().rstrip("\n")
      line3 = infile.readline().rstrip("\n")
      line4 = infile.readline().rstrip("\n")
    line5 = str(int(line)+1)
    return line5



def validate_first_name():
  valid = False
  while valid is False:
    fn = input("Enter your first name: ")
    if fn.replace(" ","").isalpha():
      valid = True
    else:
      print("Invalid First Name")

  return fn.title()


def validate_last_name():
  while True:
    ln = input("Enter your last name: ")
    if not any(map(str.isdigit,ln)):
      return ln.title()
    else:
      print("Invalid Last Name")


def validate_depth():
  valid = False
  while valid is False:
    dept = input("Enter employees department: ")
    if dept.isalpha():
      valid = True
    else:
      print("Invalid Department Entered")
  return dept[:4].upper()

def add_employee_salary():
  while True:
    salary = input("Enter your salary: ")
    if salary.isnumeric() and 35000<=int(salary)<=100000 and len(salary)!=0:
      return salary
    else:
      print("Invalid Salary Entered")

# def lookup_email(email, employees):
#   for employee in employees:
#     if email == employee[4]:
#       return True
#     return False

def lookup_email(email, cur):

  cur.execute("SELECT COUNT(*) FROM employees WHERE email = ?", (email,))
  count = cur.fetchone()[0]
  if count > 0:
    return True
  else:
    return False


def generate_email(ln, fn, cur):
  bemail = (ln[:4] + fn[0]).lower()
  email = bemail + "@company.com"
  i = 1
  while lookup_email(email, cur):
      email = f"{bemail}{i}@company.com"
      i += 1
  return email


def generate_next_id(employees):
  return str(int(employees[::5] [-1]) + 1) 

def get_next_emp_multi(employees):
  if len(employees) == 0:
    return "1001"
  next_empid = int(employees[-1][0]) + 1
  return str(next_empid)

