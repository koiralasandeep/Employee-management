# 5-13. Globals

## a. Global Variables
A global variable is created outside all the functions   
It is accessible to **ALL** the functions in a program

```python
var = 10  # Create a global variable

def function1():
  print(var)

def function2():
  print(var)

function1()
function2()
```

To assign a value to a global variable

```python
var = 0  

def function1():
  print(f'The global variable is {var}.')

def function2():
  global var  # global keyword tells the interpreter to assign a value to the global variable var
  var = int(input('Enter a number: '))

function1()
function2()
function1()
```

## Issues with global variables:

### Global variables make debugging difficult
Any statement in a program file can change the value of a global variable. If you find that the wrong value is being stored in a global variable, you have to track down every statement that accesses it to determine where the bad value is coming from. In a program with thousands of lines of code, this can be difficult.

### Global variable dependency makes code portability difficult
Functions that use global variables are usually dependent on those variables. If you want to use such a function in a different program, most likely you will have to redesign it so it does not rely on the global variable.

### Global variables make a program hard to understand
A global variable can be modified by any statement in the program. If you are to understand any part of the program that uses a global variable, you have to be aware of all the other parts of the program that access the global variable.


## b. Global Constants
A global constant is a global name that references a value that cannot be changed.  

```python
INTEREST_RATE = 3.4

```

<details>
  <summary>
    👍 5-a: Rule of Thumb:
  </summary>
  Global variables and global constants are created at ZERO indent position
</details>