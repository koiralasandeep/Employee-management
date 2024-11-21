# 2-12. Converting Datatypes To Boolean
To convert a float, integer or string to boolean, we use the bool() function  
**Syntax**: bool(<other_datatype_variable>)

### a. Float to Boolean

```python
my_gpa = 3.58

# @TODO: Write a print statement to print the type of my_gpa

# We can convert this to a boolean
my_gpa = bool(my_gpa)

# @TODO: Write a print statement to print the my_gpa

# @TODO: Write a print statement to print the type of my_gpa
```
<details>
  <summary>
    🚩 To remember:
  </summary>
  Any float other than 0.0 when converted to boolean will evaluate to True, 0.0 will evaluate to False
</details>

### b. Integer to Boolean

```python
score = 98

# @TODO: Write a print statement to print the type of score variable

# We can convert this to a float
score = bool(score)

# @TODO: Write a print statement to print the score variable


# @TODO: Write a print statement to print the type of score variable
```

<details>
  <summary>
    🚩 To remember:
  </summary>
  Any integer other than 0 when converted to boolean will evaluate to True, 0 will evaluate to False
</details>

### c. String to Boolean

```python
my_string = "Hello World"

# Write a print statement to print the type of my_string variable

# We can convert this to a boolean
my_string = bool(my_string)

# Write a print statement to print the my_string variable


# Write a print statement to print the type of my_string variable
```
<details>
  <summary>
    🚩 To remember:
  </summary>
  When you convert a string to a boolean, empty string evaluates to False and any other string evaluates to True
</details>