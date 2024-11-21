# 2-1. Print Function

We use print to display data to the user  
**Syntax:**  
print("\<whatever you want to print\>") _or_  
print('\<whatever you want to print\>') _or_  
print("""\<whatever you want to print\>""")


## a. Printing phrases
```python
print("Hello World") # We can use single quotes also
```

#### Any statement that starts after a # in python is called a comment and will not be executed

<details>
  <summary>
    👉 Try this:
  </summary>
  Display  I am Mary's cat
</details>

<details>
  <summary>
    👀 Answer:
  </summary>
  print("I am Mary's cat") # you cannot use single quotes because the string has single quote in it 
</details>


<details>
  <summary>
    👉 Try this:
  </summary>
  Display  Mary said, "Hello There!"
</details>

<details>
  <summary>
    👀 Answer:
  </summary>
  print('Mary said, "Hello There!"') # you cannot use double quotes because the string has double quote in it 
</details>

## b. Printing paragraphs
We use ''' or """ when we need to display large amount of text that might contain single or double quotes
```python
print(""" This is paragphic data with "  
and '  and 
this won't break the code.
It also allows me to display in multiple lines""")
```

## c. Multiple print statements 
Each print statement displays data in new line
```python
print("Hello")
print("World")
```

<details>
  <summary>
    👉 Try this:
  </summary>
  Using multiple print statements display<br><br>
  Alabama<br>
  Arizona<br>
  Alaska<br>
  Arkansas
</details>

<details>
  <summary>
    👀 Answer:
  </summary>
  print("Alabama")<br>
  print('Arizona')<br>
  print("Alaska")<br>
  print("Arkansas")<br>
</details>


## d. Printing multiple values
We can use comma-separated values in the same print statement  
They will be separated by space by default when displayed

```python
print("Hello","world","there","!")
```

<details>
  <summary>
    👉 Try this:
  </summary>
  Print four strings Lord, of, the, Rings so it will look like<br><br>
  Lord of the Rings
</details>

<details>
  <summary>
    👀 Answer:
  </summary>
  # you may use single or double quotes<br>
  print("Lord", "of", 'the', 'Rings') 
</details>