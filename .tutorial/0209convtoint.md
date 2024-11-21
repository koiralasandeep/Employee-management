# 2-9. Converting Datatypes To Integer
To convert a string, float or boolean to integer, we use the int() function  
**Syntax**: int(<other_datatype_variable>)

### a. String to Int

```python
my_phone = "3185551234"

# @TODO: Write a print statement to print the my_phone_number variable

# We can convert this to an integer
my_phone_number = int(my_phone)

# @TODO: Write a print statement to print the my_phone_number variable

# @TODO: Write a print statement to print the type of my_phone_number variable

```
<details>
  <summary>
    🚩 To remember:
  </summary>
  You can convert a string to an integer only if ALL the characters are numeric
</details>

### b. Float to Int

```python
gpa = 3.5

# @TODO: Write a print statement to print the type of gpa variable

# We can convert this to an integer
# and store in the same variable if we want to
gpa = int(gpa)

# Write a print statement to print the gpa variable


# Write a print statement to print the type of gpa variable
```
<details>
  <summary>
    🚩 To remember:
  </summary>
  When you convert a float to an integer, the numbers after the decimal point are stripped<br>
  The number will NOT be rounded to the nearest whole number
</details>


### c. Boolean to Int

```python
valid = True

# Write a print statement to print the type of valid variable


# We can convert this to an integer
valid_int = int(valid)

# Write a print statement to print the valid_int variable


# Write a print statement to print the type of valid_int variable
```
<details>
  <summary>
    🚩 To remember:
  </summary>
  When you convert a boolean to an integer, True is converted to 1 and False is converted to 0
</details>