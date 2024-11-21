# 11-2. Single Inheritance With Class Attributes

## Can we try with some attributes?
Create class attributes inside parent class

```python
class Student():
  college = "ULM" # I am a public class attribute
  _dept = "CINS" # I am a protected class attribute

class CINS_Student(Student): 
  pass
```

Let's access these attributes outside the class

```python
# Let's see parent behavior
student1 = Student()
print(student1.college)
print(student1._dept)
```

```python
# Let's see child behavior
cins_student1 = CINS_Student()
cins_student1.college
print(cins_student1._dept)
```

<details>
  <summary>
    👉 Inference: 
  </summary>
  The child inherited the parent's class attributes
</details>