# 8-8. Searching and Replacing

## a. endswith(substring)
Checks if a string ends with a specified substring
```python
substring = "00"
string = "45678200"
search_test = string.endswith(substring)
```

## b. startswith(substring)
Checks if a string starts with a specified substring
```python
substring = "400"
string = "4000045"
search_test = string.startswith(substring)
```

## c. find(substring)
- Checks to see if a given substring (needle) is present in the string (haystack)
- If found, it will return the index of the FIRST occurence
- If not found, it will return -1


```python
substring = "8"
string = "4000045"
search_test = string.find(substring)
```

<details>
  <summary>⚠️ Important Note:</summary>find() method will always return an integer
</details>

## d. replace(old, new)
Creates a copy of the original string after replacing _all occurences_ of a specified substring with a new substring

```python
string = "Univ of Louisiana Monroe"
find = "Univ"
replace = "University"
new_string = string.replace(find, replace)
```

<details>
  <summary>💡 Note:</summary>This will be a case-sensitive search
</details>