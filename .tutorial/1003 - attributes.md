# 10-2. Class Attributes

## Creating class Attributes
- Think of class attributes as global variables
- Defined inside a class
### 2a. Defining public class attributes
```python
college = "ULM"  
```

### 2b. Defining protected class attributes
```python
_dept = "comp sci"  
```

### 2c. Defining private class attributes
```python
__FILENAME = "books.csv" 
```

<details>
  <summary>
    💡 Note:
  </summary>
  Leading and trailing double underscores indicate that attributes (or methods) are private<br>
  Leading and trailing single underscore indicate that attributes (or methods) are protected<br>
  Private and protected entities should not be accessed or modified from outside the class
</details>

## Accessing class attributes
To access class attributes, we can use the object name or the class name  

**Syntax:**  
<obj_name>.<class_attr_name>  
_or_  
<class_name>.<class_attr_name>

### 2d. Accessing public class attributes

```python
print(student1.college)
print(Student.college)
```

### 2e. Accessing protected class attributes

```python
print(student1._dept)
print(Student._dept)
```

### 2f. Accessing private class attributes

```python
print(student1.__FILENAME)
print(Student.__FILENAME)
```

<details>
  <summary>
    💡 To know:
  </summary>
  Private or protected attributes can be accessed by<br>
  mangling the attributes<br>
  print(student1._Student__FILENAME)<br>
  But a responsible programmer shouldn't do that<br>
</details>


<details>
  <summary>
    🚩 To Remember:
  </summary>
All the objects will have the same value for a given class attribute
</details>


```python
student2 = Student()
print(student2.college)
```

<details>
  <summary>
    👉 Try this
  </summary>
  create a protected class attribute named college_code and set it to "1315"
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  Inside class definition,<br>
  _college_code = "1315"
</details>

<details>
  <summary>
    👉 Try this
  </summary>
  print the class attribute named college_code outside the class
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  Outside class definition,<br>
  print(Student._college_code) or <br>
  print(student1._college_code)
</details>
