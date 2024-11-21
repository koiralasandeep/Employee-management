# 3-4. Nested IF Statement
When an if a statement is present inside another if statement, it is called a nested IF statement.  

This situation occurs when you have to filter a variable multiple times.  
In nested IF statements, you should always take care of the indentation to define the scope of each statement. You can have as many levels of nesting as required  

But it makes the program less optimized, and as a result, can be more complex to read and understand.  
Therefore, you should always try to minimize the use of nested IF statements.

### Syntax:
```python
if condition1:
  # Executes if condition1 is true
  if condition2:
    # Executes if condition2 is true
  else:
    # Executes if condition2 is false
else:
  # Executes if condition1 is false
  if condition3:
    # Executes if condition3 is true
  else:
    # Executes if condition3 is false
```

### Example:

```python
year = int(input("Enter the year: " ))
if year%4 == 0:  
  print("It is a leap year")
  if year < 2024:
    print("It is in the past")
  else:
    print("It is not in the past")
else:
  print("It is not a leap year")
  if year > 1997:
    print("Generation Z")
  else:
    print("Not Generation Z")
```
<details>
  <summary>
    🔎 Closer look:
  </summary>
  The user input year is converted to integer<br>
  % is an operator that calculates the remainder when two numbers are divided<br>
  So, if we want to know whether the year is leap year, it must be divisible by 4<br>
  That means the remainder must be zero when divided by 4<br>
  We check if the year is a leap year<br>
  If that is True, then we check if the year is less than 2024<br>
  If that is True, the print statement displays It is in the past<br>
  Otherwise, the print statement displays It is not in the past<br>
  If it is not a leap year<br>
  We check if the year is later than 1997<br>
  If True, the print statement displays Generation Z<br>
  Otherwise, the print statement displays Not Generation Z
</details>

<details>
  <summary>
    🖨 Output test cases:
  </summary>
  When we enter the year 2000,<br>
  Because, it is a leap year and is earlier than 2024, the output will be:<br>
  It is a leap year<br>
  It is in the past<br><br>
  When we enter the year 2028,<br>
  Because, it is a leap year and is later than 2024, the output will be:<br>
  It is a leap year<br>
  It is not in the past<br><br>
  When we enter the year 2001,<br>
  Because, it is not a leap year and is later than 1997, the output will be:<br>
  It is not a leap year<br>
  Not Generation Z<br><br>
  When we enter the year 1995,<br>
  Because, it is not a leap year and is earlier than 1997, the output will be:<br>
  It is not a leap year<br>
  Generation Z<br><br>
</details>


<details>
  <summary>
    👉 3-4. Try this
  </summary>
  Accept user's input for a number<br>
  Check if the number is an even number<br>
  If yes, check if the number is divisible by 3<br>
  If yes, print The number is divisble by 6<br>
  Otherwise, print The number is not divisible by 6<br><br>
  But if the number is not an even number<br>
  Print Odd number
</details>


<details>
  <summary>
    👀 Answer
  </summary>

  ```python
    num = int(input("Enter the number: " ))
    if num % 2 == 0:  
      if num % 3 == 0:
        print("The number is divisble by 6")
      else:
      print("The number is not divisble by 6")
    else:
      print("Odd number")
```
</details>