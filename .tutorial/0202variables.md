# 2-2. Python Variables

Variables are _containers_ to store values  
These values can be
- numberic
- alphabetic
- alphanumeric
- or a special type called Boolean (True/False)

## a. Defining a variable
A variable can be defined as follows  
**Syntax:** \<variable_name> = \<value> or \<expression>

```python
# assigning a value of 5 to a variable named var1
var1 = 5

# assigning an expression to a variable named var2
var2 = 4 + 5

```

## b. Printing a variable
To print the value stored in a variable, we use the print statement with the variable name inside the paranthesis  
**Syntax:** print(<variable_name>)

```python
# printing variables
print(var1)
print(var2)
```

<details>
  <summary>
    🚩 Important:
  </summary>
  You must print the variable name without any single or double quotes
</details>

## c. Variable naming rules
A valid variable name
- CANNOT have blank spaces, meaning, it has to be one word
- CANNOT be a python keyword

  (For example: if, for, while etc.). You can find the complete list [here](https://realpython.com/lessons/reserved-keywords/)
- CANNOT start with a number
- CANNOT have any special character except an underscore
- CAN have a mix of alphabetical or numerical characters or underscores 

## d. Variable naming convenions

### Variable names are case sensitive.  
Which means:  
`Age`, `age`, `aGe`, `AgE`, `agE`, `AGe`, `AGE` are all **different** variables

```python
age = 25
print(Age) # Will give an error

```

<details>
  <summary>
    👉 Try this:
  </summary>
  Fix the above print statement
</details>

<details>
  <summary>
    👀 Answer:
  </summary>
  print(age)
</details>

### Variable names can be as long as you want
But, it is a good practice to keep the length between 8 and 20 characters

### Varaible names can be anything
As long as they follow above rules  
But a good convention is to name variables descriptively

```python
i = 2.7
interest_rate_percent = 2.7

# both are valid names
# but which one is more descriptive?
```

### Variable naming styles
Different programmers choose different styles of variable naming.  
Two popular ones are:
1. **Camel Case:**

   First character is lower case, first character of each of the words will be uppercase and the rest will be lowercase

```python
# Style 1: Camel case
interestRatePercent = 2.7

```
2. **Snake Case:**

   All characters are lowercase, and each word is separated by an underscore

```python
# Style 2: Snake case
interest_rate_percent = 2.7
```

You choose your style!