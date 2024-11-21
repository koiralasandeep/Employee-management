# 8-2. String Modification Methods

<details>
  <summary>
   💡 Remember 
  </summary>
  We cannot actually modify a string. Strings are immutable.<br>
  We can create a copy of the string.
</details>

## a. lower()
- This creates a all lowercase version of the string
- Numbers and special characters remain unchanged
```python
string = 'HeLLO343'
new_string = string.lower()
```

## b. upper()
- This creates a all uppercase version of the string
- Numbers and special characters remain unchanged
```python
string = 'hello'
new_string = string.upper()
```

## c. lstrip()
- Strips all the leading characters specified in ()
- If the () are empty, it will strip leading spaces
```python
# To strip all the leading *
string1 = '    hello     '
string2 = '****hello****'
new_string = string1.lstrip()
new_string = string2.lstrip('*')
```

## d. rstrip()
- Strips all the trailing characters specified in ()
- If the () are empty, it will strip trailing spaces
```python
# To strip all the trailing *
string1 = '    hello    '
string2 = '****hello****'
new_string = string1.rstrip()
new_string = string2.rstrip('*')
```

## e. strip()
- Strips all the leading and trailing characters specified in ()
- If the () are empty, it will strip leading and trailing spaces
```python
# To strip all the leading and trailing *
string1 = '    hello    '
string2 = '****hello****'
new_string = string1.strip()
new_string = string2.strip('*')
```

## f: @TODO: Check out these methods and write down what they do
- title()
- join()
- center()
- capitalize()
- casefold()
