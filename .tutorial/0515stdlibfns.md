# 5-15. Standard Library Functions
Python comes with a standard library of functions that have already been written for us  
These functions, also known as library functions, make a programmer’s job easier 

<details>
  <summary>
    💡 Remember
  </summary>
  We have ussed some Python’s library functions<br>
  print() - void function that takes arguments
  input() - value returning function that returns a string<br>
  range() - value returning function, returns a range
</details>

## Modules
- Many of the library functions are stored in files called modules   
- To be able to call a function stored in a module, we write an import statement at the top of the program  
- An import statement tells the interpreter the name of the module that contains the function 

## b. math Module:
One of the Python standard modules is named math    
It contains various mathematical functions that work with floating-point numbers  
To the math module’s functions we write an import statement at the top of the program  
This statement loads the contents of the math module into memory and makes all the functions in the math module available to the program

```python
import math
# to calculate the square root of a number
number = 35
square_root = math.sqrt(number)
print(square_root)
```

<details>
  <summary>
    🔎 Closer look
  </summary>
  sqrt() function is needed to calculate the square root of a number<br>
  this function is available in the math module<br>
  so, we import the math module<br>
  But to be able to call sqrt(), we must use the module name as a prefix<br>
  sqrt() returns a float, that is why we are able to store the value in a variable called square_root<br>
</details>

#### Because the internal workings of library functions cannot be seen, they are called black boxes

## Random module - Generating Random Numbers

## c. randint()
Random numbers are useful for lots of different programming tasks.  
Computer games that let the player roll dice use random numbers to represent the values of the dice 
Programs that show cards being drawn from a shuffled deck use random numbers to represent the face values of the cards


Python provides several library functions for working with random numbers.  
These functions are stored in a module named random in the standard library. 

```python
import random
# To generate a random integer between 1 and 100
number = random.randint (1, 100)
print(number)
```

<details>
  <summary>
    🔎 Closer look
  </summary>
  The randint function is in the random module, so we import it<br>
  when calling randint<br>
  - we must prefix the module name before the function name using a dot<br>
  - we must pass two integer arguments, that tell the function to give an integer random number in the range of 1 through 100<br>
  randint returns an integer, that can be assigned to a variable called number<br>
  to display a random number, it is not necessary to assign the random number to a variable, it can be sent to the  print function<br>
  print(random.randint (1, 100))
</details>


<details>
  <summary>
    👉 Try this
  </summary>
  Generate a random integer between two values that the user enters<br>
  Hint: When user enters data using input function, that data is a string, we must convert it to integer
</details>


<details>
  <summary>
    👀 Answer
  </summary>
  num1 = int(input("Enter first number: "))<br>
  num2 = int(input("Enter second number: "))<br>
  rand = random.randint(num1, num2)<br>
  print(rand)<br>
  # Assume that the user will enter numeric values and that the first number will be smaller than the second one
</details>


## d. randrange()
The randrange function takes the same arguments as the range function.  
It returns a randomly selected value from a sequence of values. 

```python
number = random.randrange(10)
print(number)
# The function will randomly select a number from [0,1,2,3,4,5,6,7,8,9]
```

```python
number = random.randrange(5,10)
print(number)
# The function will randomly select a number from [5,6,7,8,9]
```

```python
number = random.randrange(0, 101, 10)
print(number)
# The function will select a number from [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

<details>
  <summary>
    🚩 To remember
  </summary>
  randint and randrange return an integer
</details>


<details>
  <summary>
    👉 Try this
  </summary>
  Generate a random number between 1 and 13 and if it is 1, print Ace, 2 print Two.. , 3 print Three, so on, 11, print Jack, 12 print Queen and 13 print King
</details>


<details>
  <summary>
    👀 Answer
  </summary>
  rand = random.randrange(1, 14)<br>
  if rand == 1:<br>
  &ensp;print("Ace")<br>
  elif rand == 2:<br>
  &ensp;print("Two")<br>
  elif rand == 3:<br>
  &ensp;print("Three")<br>
  elif rand == 4:<br>
  &ensp;print("Four")<br>
  elif rand == 5:<br>
  &ensp;print("Five")<br>
  elif rand == 6:<br>
  &ensp;print("six")<br>
  elif rand == 7:<br>
  &ensp;print("Seven")<br>
  elif rand == 8:<br>
  &ensp;print("Eight")<br>
  elif rand == 9:<br>
  &ensp;print("Nine")<br>
  elif rand == 10:<br>
  &ensp;print("Ten")<br>
  elif rand == 11:<br>
  &ensp;print("Jack")<br>
  elif rand == 12:<br>
  &ensp;print("Queen")<br>
  elif rand == 13:<br>
  &ensp;print("King")<br>
</details>

## e. uniform() function
The uniform returns a random floating-point number between two specified floats

```python
number = random.uniform(1.0, 10.0)
print(number)
```

<details>
  <summary>
    👉 Try this
  </summary>
  Generate a random float between two values that the user enters<br>
  Hint: When user enters data using input function, that data is a string, we must convert it to float
</details>


<details>
  <summary>
    👀 Answer
  </summary>
  num1 = float(input("Enter first number: "))<br>
  num2 = float(input("Enter second number: "))<br>
  rand = random.uniform(num1, num2)<br>
  print(rand)<br>
  # Assume that the user will enter numeric values and that the first number will be smaller than the second one
</details>
