# 11-3. Single Inheritance With Methods

## Let's add methods in parent class

Define the methods inside the class
```python
class Student():
  # public method
  def parent1(self):
    print("Parent1")

  # protected method
  def _parent2(self):
    print("Parent2")

class CINS_Student(Student): 
  pass
```

Call them outside the class
```python
# parent behavior
student1 = Student()
student1.parent1()
student1._parent2()
```

```python
# child behavior
cins_student = CINS_Student()
cins_student.parent1()
cins_student._parent2()
```

<details>
  <summary>
    🤓 Inference: 
  </summary>
  The child also inherited the parent's public and protected methods
</details>