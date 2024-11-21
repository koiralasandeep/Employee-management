# 10-5. Accessor Methods
These methods let us access the method attributes from outside the class.  
 When a method uses the self parameter to create an attribute, the attribute belongs to the specific object that self references  
 These are value-returning methods.

### 5a. Defining public accessor methods
Coding convention encourages to define accessor methods with the prefix **get**  
All method definitions will be INSIDE the class
  
```python
# Defining a public acessor method
def get_name(self):
  return self.__name
```

### 5b. Calling the public accessor methods
Method calls will be outside the class definition  
We must use the object name to call the method
  
```python
# Outside the class
student1.get_name()
```

<details>
  <summary>
    🚩 Notice
  </summary>
  From its definition, it looks like get_name accepts one argument<br>
  But when we are calling it the parantheses are empty<br>
In the background, Python is passing student1 as the argument
</details>

### 5c. Defining protected accessor methods
Method definitions will be INSIDE the class definition

```python
def _get_name(self):
  return self.__name
```


### 5d. Calling protected accessor methods
Method calls should be INSIDE children classes (we will see this in next chapter)  
For the scope of this class, we will not be using these


### 5e. Defining private accessor methods
Method definitions will be INSIDE the class definition

```python
def __get_name(self):
  return self.__name
```

### 5f. Calling private accessor methods
Method calls will be INSIDE the class definition  
For the scope of this class, we will not be using these (other than init and str)


<details>
  <summary>
    👉 Try this
  </summary>
  create a public accessor method named get_title and return private method attribute title that is bound to self in the class definition for book 
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  Inside class definition of Book,<br>
  def get_title(self):
  return self.__title (use an indent before return)
</details>


<details>
  <summary>
    👉 Try this
  </summary>
  Obtain and print the title for book1 using the accessor method
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  Outside class definition, after creating student1 object<br>
  print(book1.get_title())
</details>