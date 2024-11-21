# 2-5. Python Datatype - String

Any alphanumeric character or text enclosed in single quotes or double quotes (or in some instances ''', three single quotes or """ three double quotes) is referred to as a string  
For example:
- "Apple"
- 'Suchi says, "Welcome to Python Programming"'
- "Sally's best friend is Suzy"
- ''' "This is very interesting", said Suchi's student. I'm excited to learn more about how to write paragraphs spanning multiple lines, consisting of single and double quotes using three single quotes in Python. '''
- "67859" (even though this looks numeric, because we enclosed it in double quotes, Python treats it as a string)

## a. Define/declare an empty string
To define/declare a string whose value we don't know yet, we can use the str()  
**Syntax**: <variable_name> = str()

```python
my_string = str()
```
## b. Assigning a string value to a variable

```python
my_string = 'Suchi says, "Welcome to Python Programming"'
```

## c. Printing string variable
We can use the print function

```python
print(my_string)
```

## 3d. Converting other datatypes to string

You can convert any other data type into a string using the str() function.

```python
my_variable = 2.7
print(type(my_variable))
print(my_variable)
converted_to_string = str(my_variable)
print(type(converted_to_string))
print(converted_to_string)
```
<details>
  <summary>
    🚩 To remember:
  </summary>input() statement in Python always stores the user entered value in a string even though it might all be numeric
</details>