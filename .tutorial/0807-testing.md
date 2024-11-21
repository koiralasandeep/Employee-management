# 8-7. String Testing Methods

## a. isalnum()
Tests if a string is alpha-numeric only, without any special characters
```python
# If string has any special characters, test fails
string = "heLlo1230"
test = string.isalnum()
```

## b. isalpha()
Tests if a string is alphabetic only, without any numbers or special characters
```python
# If string has any special characters or numbers, test fails
string = "James Ellis"
test = string.isalpha()
```

## c. isdigit()
Tests if a string is numeric only, without any alphabets or special characters
```python
# If string not strictly numeric, test fails (even decimal points will cause test to fail)
string = "3185627894"
test = string.isdigit()
```

### d. islower()
Tests if a string is all lowercase, it ignores numbers and special characters
```python
# If the string has even one upper-case character, test fails
string = "hello12*"
test = string.islower()
```

### e. isspace()
Tests if a string is all blank spaces
```python
# If the string is not ALL spaces, test fails
string = "         "
test = string.isspace()
```

### f. isupper()
Tests if a string is all uppercase, it ignores numbers and special characters
```python
# If the string has even one lower-case character, test fails
string = "ULM"
test = string.isupper()
```

<details>
  <summary>💡 Note</summary>They all start with is
</details>