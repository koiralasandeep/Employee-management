# 2-10. Converting Datatypes To Float
To convert a string, integer or boolean to float, we use the float() function  
**Syntax**: float(<other_datatype_variable>)

### a. String to Float

```python
my_gpa = "3.58"

# @TODO: Write a print statement to print the type of my_gpa

# We can convert this to a float
my_gpa = float(my_gpa)

# @TODO: Write a print statement to print the my_gpa

# @TODO: Write a print statement to print the type of my_gpa
```
<details>
  <summary>
    🚩 To remember:
  </summary>
  You can convert a string to an float only if ALL the characters are numeric, and one . (denoting the decimal point)
</details>

### b. Integer to Float

```python
score = 98

# @TODO: Write a print statement to print the type of score variable

# We can convert this to a float
score = float(score)

# @TODO: Write a print statement to print the score variable


# @TODO: Write a print statement to print the type of score variable
```

### c. Boolean to Float

```python
valid = True

# Write a print statement to print the type of valid variable

# We can convert this to a float
valid_float = float(valid)

# Write a print statement to print the valid_float variable


# Write a print statement to print the type of valid_float variable
```
<details>
  <summary>
    🚩 To remember:
  </summary>
  When you convert a boolean to a float, True is converted to 1.0 and False is converted to 0.0
</details>