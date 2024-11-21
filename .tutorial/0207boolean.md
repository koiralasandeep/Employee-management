# 2-7. Python Datatype - Boolean
A data type that has a value True or False is called a boolean  
This looks like a string but is **NOT** a string  

## a. Create an empty boolean variable
We do this when we don't know the value  
**Syntax:** <variable_name> = bool()

```python
my_boolean = bool()
```
## b. Assigning a boolean value to a variable

```python
my_boolean = True
my_boolean = False
```

### Invalid booleans:

```python
# This is a string and not a boolean
my_not_a_boolean = "True"

# These are not valid booleans
my_wrong_bool1 = true # true is not the same as True
my_wrong_bool2 = false # false is not the same as False

```
<details>
  <summary>
    🚩 To remember:
  </summary>
  Python is case-sensitive
</details>  

## c. Printing a boolean variable
We use the print function  
**Syntax:** print(<variable_name>)

```python
 print(my_boolean)
```
