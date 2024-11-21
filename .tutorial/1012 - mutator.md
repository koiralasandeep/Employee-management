# 10-6. Mutator Methods
These methods let us modify the attributes. These are void methods.

### a. Defining mutator methods
- Coding convention encourages to define mutator methods with the prefix **set**
- All method definitions will be INSIDE the class

  
```python
# Defining a public mutator method
def set_name(self, new_name):
  self.__name = new_name

# Defining a protected mutator method
def _set_name(self, new_name):
  self.__name = new_name

# Defining a private mutator method
def __set_name(self, new_name):
  self.__name = new_name
```
### b. Calling the public mutator methods
- Method calls will be outside the class definition
- We must use the object name to call the method
```python
# Outside the class
new_name = input("Enter the new name: ")
student1.set_name(new_name)

# @TODO - Print the name
# Hint: Must use the accessor method
```

### c. Calling the private mutator methods
- Method calls will be INSIDE the class definition, usually made by other methods.
- For the scope of this class, we will not be using these

<details>
  <summary>
    👉 Try this
  </summary>
  create a public mutator method named set_major and set the private method attribute major that is bound to self to the new major that the user passed
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  Inside class definition,<br>
  def set_major(self, new_major):
  self.__major = new_major (use an indent)
</details>


<details>
  <summary>
    👉 Try this
  </summary>
  Set the major for student1 to HIST using the mutator method
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  Outside class definition, after creating student1 object<br>
  student1.set_major("HIST"):
</details>


<details>
  <summary>
    🚩 Chapter Take away:
  </summary>
  1. Every method inside a class must have first parameter as self<br>
  2. To call any method, you must first create the object and use object to call that method
</details>