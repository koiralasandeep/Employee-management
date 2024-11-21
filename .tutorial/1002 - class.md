# 10-1. Classes and Objects

Class is a description of an object’s characteristics  
An object is an instance of a class  
To create a class, we write a class definition.  
A class definition is a set of statements that define a class’s **data attributes** and **methods**

### 1a. Creating class
Class definition will always be at zero indent  

**Syntax:** class <class_name>():
```python
class student():
  pass
# Good coding convention is to start class name with uppercase character, so let's fix it
```

### 1b. Now we create the object of this class
Must do it OUTSIDE the class definition  

**Syntax:** <obj_name> = <class_name>()  

```python
student1 = Student()
```

<details>
  <summary>
    👉 Try this
  </summary>
  create a class named book
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  class Book():<br>
  pass (put an indent before pass)
</details>


<details>
  <summary>
    👉 Try this
  </summary>
  create an object of the class book
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  book1 = Book() (do this OUTSIDE the class definition)
</details>