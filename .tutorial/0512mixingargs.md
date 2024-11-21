# 5-12. Mixing Keyword and Positional Arguments

It is possible to mix positional arguments and keyword arguments in a function call<br>
But the positional arguments must appear first, followed by the keyword arguments

```python

def display_student(first_name, last_name, major, email):
  print(f'Name: {last_name}, {first_name}\nMajor: {major}\nEmail: {email}')

def main():
  f = input("First Name: ")
  l = input("Last Name: ")
  m = input("Major: ")
  e = input("Email: ")

  # Mixing positional and keyword arguments
  display_student(f, l, email = e, major = m)

  # or
  display_student(f, l, major = m, email = e)
```