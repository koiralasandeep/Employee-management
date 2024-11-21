# 11-6. Parent's Access To Child's Methods (or attributes)


```python
class Student():
  def method1(self):
    print("This is student method1")

class CINS_Student(Student):
  def method2(self):
    print("This is CINS student method1")

cins = CINS_Student()
cins.method1()
cins.method2()

# Now uncomment these lines and see

# student = Student()
# student.method1()
# student.method2()

```

<details>
  <summary>
    🤓 Inference:
  </summary>
  In inheritance, child can access parent's attributes and methods but a parent cannot access a child's methods or attributes
</details>