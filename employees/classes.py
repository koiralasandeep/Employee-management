class Employee():
  def __init__(self, empid, name, department, salary, email):
    self.__empid = empid
    self.__name = name
    self.__department = department
    self.__salary = salary
    self.__email = email
  def get_empid(self):
    return self.__empid
  def get_name(self):
    return self.__name
  def get_department(self):
    return self.__department
  def get_salary(self):
    return self.__salary
  def get_email(self):
    return self.__email

  def set_name(self, name):
    self.__name = name

  def set_department(self, new_dep):
    self.__department = new_dep

  def set_salary(self, new_salary):
    self.__salary = new_salary

  def __str__(self):
    return f"Employee ID: {self.__empid}, Name: {self.__name}, Department:{self.__department}, Salary: {self.__salary}, Email: {self.__email}"
    

