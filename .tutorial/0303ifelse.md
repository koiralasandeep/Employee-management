# 3-3. If-else Statement
The **if-else statements** are used to execute both the true part and the false part of a given condition.  

If the condition is true, the _if block_ code is executed otherwise, the _else block_ code is executed.

### Syntax:
```python
if condition:
  # Executes this block if the condition is true
else:
  # Executes this block if the condition is false
```

### Example:
```python
year = int(input("Enter a year: "))
if year > 2024:
  print("Inside IF block")
  print("This is the future Doc")
else:
  print("Inside ELSE block")
  print("Back to the future Doc")
```

<details>
  <summary>
    👉 3-3. Try this
  </summary>
  Accept user input for a score<br>
  Check if score is less than 60 and print Fail<br>
  otherwise, print Pass<br>
</details>


<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  score = int(input("Enter score: "))
  if score < 60:
    print("Fail")<br>
  else:
    print("Pass")
  ```
</details>