# 2-14. Operators

## a. Arithmetic Operators

| Operator      | Description |
| ----------- | ----------- |
| +      | Addition       |
| -   | Subtraction        |  
| *   | Multiplication        |  
| /   | **Division** - Divides one number with another and gives the result as floating point        |  
| //   | **Integer Division** -  Divides one number with another and gives the result as an integer       |  
| %   | **Remainder** -  Divides one number with another and gives the remainder        |  
| **   | **Exponent** -  Raises a number to a power        |  

<details>
  <summary>
    👉 2-14a. Try this
  </summary>
  Write code to solve this problem. If you have 25 cookies and 7 people, how many cookies will you have left, after each person gets the same number of cookies? How many cookies will each person get?
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  cookies = 25<br>
  people = 7<br>
  remaining_cookies = cookies % people # get remainder<br>
  cookies_per_person = cookies // people # get integral quotient<br>
  print(f"Remaining Cookies: {remaining_cookies}")<br>
  print(f"Cookies per person: {cookies_per_person}")
</details>

### Operator Precendence
The order in which a mathematical expression is calculated in Python is similar to that we learned in Algebra  
The acronym PEMDAS stands for Parentheses, Exponents, Multiplication/Division, Addition/Subtraction 

<details>
  <summary>
    👍 2-14a. Rule of Thumb
  </summary>
  To remember PEMDAS use the mnemonic "Please Excuse My Dear Aunt Sally"
</details>

<details>
  <summary>
    👉 2-14a2. Try this
  </summary>
  Write code to get user input a value in centigrade and convert it to fahrenheit. <a href="/c-to-f.png">See Formula</a>
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  user_centigrade = input("Enter temperature in centigrade: ")<br>
  user_centigrade = float(user_centigrade)<br>
  fahrenheit = user_centigrade * (9/5) + 32 <br>
  print(f"Temperature in fahrenheit: {fahrenheit}")<br>
  # When testing this program, enter only numeric values for temperature
</details>


## b. Assignment Operators

| Operator      | Description |
| ----------- | ----------- |
| +=   | **Increment** -  Adds a value to a number and stores it in the number on the left        |  
| -=   | **Decrement** -  Subtracts a value to a number and stores it in the number on the left        |  
| *=   | _a *= b_ means a = a * b        |
| /=   | _a /= b_ means a = a / b        |

```python
# In 2-13c. Try this Answer
# We incremented user's age by 1

age = input("Enter age: ")
age = float(age)
age = age + 1
print(f"Next year, you will be {age} years old")
```

Instead of age = age + 1, we can concisely use age += 1

<details>
  <summary>
    👉 2-14b. Try this
  </summary>
  Write a program to decrement a user's age by 1 and print Last year you were __ years old
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  age = float(input("Enter age: ")) # you can convert to float in the same line<br>
  age -= 1<br>
  print(f"Last year, you were {age} years old")
</details>

## c. Comparison Operators

Comparison operators are used to compare two values  

| Operator      | Description |
| ----------- | ----------- |
| >   | Greater than        |  
| <   | Less than        |  
| ==  | Equal to        |
| >=  | Greater than or equal to |
| <=  | Less than or equal to   |
| !=  | Not equal to       |

```python
result = 5>7
print(result)
```

<details>
  <summary>
    🔎 Closer look
  </summary>
  python will compare if 5 is greater than 7<br>
  since 5 is not greater than 7, the result is false<br>
  it is stored in the result variable which is a boolean<br>
  print statement prints that boolean - False
</details>

### \>, <, >=, <= cannot be used to compare strings

<details>
  <summary>
    👉 2-14c. Try this
  </summary>
  Ask user to input his score and print if the entered score is less than or equal to 60
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  score = int(input("Enter score: ")) # convert to int <br>
  result = score<=60<br>
  print(result)
</details>

<details>
  <summary>
    🚩 2-14c. To remember
  </summary>
  >, <, >= and <= cannot be used when one side is a string
</details>

## d. Logical Operators

| Operator      | Description |
| ----------- | ----------- |
| and   | Returns True if all conditions are True        |  
| or   | Returns True if atleast one of the conditions is True         |  
| not  | Reverse the result        |

```python
result = 5<7 and 6<9
print(result)
```

<details>
  <summary>
    🔎 Closer look
  </summary>
  python will compare if 5 is less than 7, and it evaluates to True<br>
  then python will compare if 6 is greater than 9, and it evaluates to True<br>
  since both the conditions are True, the and operator will return True<br>
  that is stored in the result variable
  print statement prints that variable - True
</details>

```python
result = 5<7 and 6>9 and 7>10
print(result)
```

<details>
  <summary>
    🔎 Closer look
  </summary>
  python will compare if 5 is less than 7, and it evaluates to True<br>
  then python will compare if 6 is greater than 9, and it evaluates to True<br>
  then python will compare if 7 is greater than 10, and it evaluates to False<br>
  since all the conditions are not True, the and operator will return False<br>
  that is stored in the result variable
  print statement prints that variable - False
</details>

<details>
  <summary>
    👉 2-14d. Try this
  </summary>
  Ask user to input his score and print if the entered score is between 79 and 90, not including 79.<br>
  Hint: User score greater than 79 or score less than or equal to 90
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  score = int(input("Enter score: "))<br>
  result = score>79 or score<=90<br>
  print(result)
</details>

<details>
  <summary>
    🚩 2-14c,d. Remember
  </summary>
    The expressions using comparison and logical operators will evaluate to True or False<br>
    We will use these expressions in Chapter 3 - in if statement
  
</details>