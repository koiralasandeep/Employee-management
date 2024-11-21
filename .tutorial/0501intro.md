# 5-1. Functions
- A function is a group of statements that exist within a program for the purpose of performing a specific task
- Most programs perform tasks are large enough to be broken down into several subtasks
- These subtasks in Python are called **Functions**
- These functions can be executed in the desired order to perform the overall task of the program  

<details>
  <summary>
    🤓 Example
  </summary>
  Think of a university<br>  
  Its functionality is so vast that it is divided into departments and each of these departments perform jobs that are specific to them<br><br>  
  &ensp; - Admissions handles all recruitment, prep etc<br></r>  
  &ensp; - Housing handles dorms etc<br>  
  &ensp; - Registrar handles are courses and add and drop etc<br>
  And many more.. <br>
  All these departments also pass information back and forth for their functioning
</details>

## Modularized Program
Any program that uses functions to accomplish a task is called a modularized program

### Without functions
```python
# Admissions
print("Admissions step 1")
print("Admissions step 2")
print("Admissions step 3")
print("Admissions step 4")

# Scholarship
print("Scholarship step 1")
print("Scholarship step 2")
print("Scholarship step 3")

# Enrollment
print("Enrollment step 1")
print("Enrollment step 2")
```

### With Functions

```python
# Admissions
def admissions():
  print("Admissions step 1")
  print("Admissions step 2")
  print("Admissions step 3")
  print("Admissions step 4")

# Scholarship
def scholarship():
  print("Scholarship step 1")
  print("Scholarship step 2")
  print("Scholarship step 3")

# Enrollment
def enrollment():
  print("Enrollment step 1")
  print("Enrollment step 2")



admissions()
scholarship()
enrollment()
```

## Benefits of using functions

1. Simpler Code
2. Code reuse
3. Better testing
4. Faster development
5. Easier facilitation of teamwork

