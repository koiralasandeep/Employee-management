# 11-1. Single Inheritance

## a. Creating a child for an existing parent
In Python, a child is created by using parent class' name in parantheses

![Image](../.tutorial/images/single-inheritance.png)
```python
class Student():
  def __init__(self):
    print("This is Student init")

class CINS_Student(Student): 
  pass

# CINS_Student is the child of Student
# Student is the Parent of CINS_Student
```

Let us create an object of Student (which is the parent)

```python
student1 = Student()
```

- Obviously, the parent's init gets called and the print statement is executed
- Now let us create an object of the child, which is CINS_Student

```python
# This class doesn't have an init method, so nothing must be displayed, BUT ... WAIT!!

cins = CINS_Student()
```
 
<details>
  <summary>
    🤓 Inference: 
  </summary>
  Because, there is a parent-child relationship, the child "inherited" the parent's init method!
</details>