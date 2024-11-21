# 5-8. Local Variables With Same Name

Different functions can have local variables with the same names because the functions cannot see each other's local variables

```python

def main():
  texas() # Call the texas function
  california() # Call the california function

# Definition of the texas function
def texas():
  birds = 5000  # a local variable named birds
  print(f'texas has {birds} birds.')

# Definition of the california function
def california():
  birds = 8000  # a local variable named birds
  print(f'california has {birds} birds.')

# Call the main function
main()
```

<details>
  <summary>
    🔎 Closer Look
  </summary> 
  Although there are two separate variables named birds in this program, only one of them is visible at a time because they are in different functions<br>
  When the texas function is executing, the birds variable with value 5000 is visible <br>
  When the california function is executing, the birds variable with value 8000 is visible
</details>