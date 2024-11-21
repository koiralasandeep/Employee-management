# 2-16. print using end, sep and escape characters

## a. Using end in print  
### Suppressing the ending newline
Each print statement always starts the display in a new line  

```python
# Execute the two statements below
print("Hello")
print("World")
```

To suppress the newline, we use a special argument called **end**  

```python
print("Hello", end = '')
print("World")
```

## b. Using end with argument 
When multiple arguments are passed to a print function, they are automatically separated by a space 
We can use the **end** to display anything we want after the last string

```python
print("Uno", "Dos", "Tres", end = ' ** ')
```

<details>
  <summary>
    👉 2-16b. Try this
  </summary>
  Write a print statement to display Uno Dos Tres |
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print("Uno", "Dos", "Tres", end = ' |')
</details>


## c. Using sep in Print
When multiple arguments are passed to a print function, they are automatically separated by a space  
If we don't want a space printed between the items, we can use a special argument called **sep**  
The specified string will be inserted between each items  

```python
name = "Johnny Vince"
major = "ACCT"
gpa = 3.54
print(name, major, gpa, sep = ' ** ')
```

<details>
  <summary>
    👉 2-16c. Try this
  </summary>
  Given<br>
  name = "Johnny Vince"<br>
  major = "ACCT"<br>
  gpa = 3.54<br>
  Write ONE print statement to display Johnny Vince, ACCT, 3.54
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print(name, major, gpa, sep = ', ')
</details>

## d. Escape Characters

| Escape Character | Effect |
| ---------- | ------ |
| \n |  Causes output to be advanced to the next line |
| \t |  Causes output to skip over to the next tab position |
| \\' |  Causes a single quote mark to be printed |
| \\" |  Causes a double quote mark to be printed |
| \\\ |  Causes a backslash character to be printed |

```python
# Execute these statements one at a time and see

print("Uno\nDos\nTres")
print("Uno\t\tDos\t\tTres")
print('I\'m taking CINS 3002')
print('The path is C:\\Users\\rodda')
```

<details>
  <summary>
    👉 2-16d. Try this
  </summary>
  Given<br>
  name = "Johnny Vince"<br>
  major = "ACCT"<br>
  gpa = 3.54<br>
  Write ONE print statement to display<br>
  Johnny Vince<br>
  ACCT<br>
  3.54
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print(name, major, gpa, sep = '\n')
</details>
