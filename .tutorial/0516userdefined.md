# 5-16. User-defined functions
We can write our own functions that return values to the calling function

```python
def validate_gpa():
  gpa = input("Enter the GPA: ")
  gpa = float(gpa)
  if gpa >= 0.0 and gpa <= 4.0:
    return gpa
  else:
    print("Invalid GPA entered")

def main():
  correct_gpa = validate_gpa()
  print(correct_gpa)

main()
```

Because the function is returning a value, we can collect it in a variable for future printing or other mathematical calculations

```python
def get_values():
  name = input("Enter the student name: ")
  major = input("Enter the student major: ")
  return name, major

def main():
  student_name, student_major = get_values()
  print(student_name)
  print(student_major)

main()
```

Because the function is returning two value, we are collecting them in two variables  

<details>
  <summary>
    💡 Note
  </summary>
  When we get to Chapter 7: Lists and Tuples, we will collect all returned values in one variable and that would be a tuple
</details>
