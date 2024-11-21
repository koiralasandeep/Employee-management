# 11-5. Child Accessing Parent's Methods Instead of Overriding

## What if child wants to access both its methods and the parent's methods too?
- We use a special method called super()
- super() can be used only INSIDE the child class

```python
class Student():
  def method1(self):
    print("This is student method1")

class CINS_Student(Student):
  def method1(self):
    super().method1()
    print("This is CINS student method1")

cins_student = CINS_Student()
cins_student.method1()
```

<details>
  <summary>
    💡 Note: 
  </summary>
  Instead of super, we can use the parent class name to call its methods inside the child class<br>
  But, we have to pass self as the first argument

  ```python
  class Student():
    def method1(self):
      print("This is student method1")

  class CINS_Student(Student):
    def method1(self):
      Student.method1(self) # accessing using parent's name
      print("This is CINS student method1")

  cins_student = CINS_Student()
  cins_student.method1()

  ```
</details>


<details>
  <summary>
    👉 11-5: Try This:
  </summary>
  
  In the above example
  - Write an init in the parent class and print `Hello`
  - From the child class' init method, call the parent init
</details>


<details>
  <summary>
    👀 Answer:
  </summary>

  ```python
class Student():
  def __init__(self):
    print("Hello")

class CINS_Student(Student):
  def __init__(self):
    super().__init__() # accessing the parent's init
    
cins_student = CINS_Student()
```
</details>
