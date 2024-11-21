# 11-4. Method Overriding (aka Polymorphism)

- Polymorphism allows subclasses to have methods with the same names as the methods in their superclasses.
- It gives the ability for a program to call the correct method depending on the type of object that is used to call it.

## 4a. Method overriding with init
Let's add an init to the child class definition

```python
class Student():
  def __init__(self):
    print("This is student init")

class CINS_Student(Student):
  pass
  # def __init__(self):
  #   print("This is CINS student init")

```

Call them outside the class
```python
student1 = Student()
cins_student = CINS_Student()

# Now uncomment the child's init and see what happens
```

<details>
  <summary>
    🤓 Inference: 
  </summary>
  When child has its own init, the parent's init is overridden and child uses its own init
</details>


## 4b. Let's add a method with same name to both parent and child

```python
class Student():
  def method1(self):
    print("This is student method1")

class CINS_Student(Student):
  def method1(self):
    print("This is CINS student method1")

student1 = Student()
student1.method1()

cins_student = CINS_Student()
cins_student.method1()

```

<details>
  <summary>
    🤓 Inference: 
  </summary>
  When child has a method with the same name of that of the parent, the parent's method is overridden
</details>
