# 4-4. While loop
A while loop is a repetitive structure that is used when the number of times the loop needs to run is determined at run-time  
For example, in our runner example, instead of giving the runner a specific number of laps to run, what if, the runner is asked to run laps until the user says "stop" and eat a banana for each lap?

## Syntax:
```python
[initial_condition]  
while [check_condition]:  
  [perform_actions]  
  [change_conditon]
```

<details>
  <summary>
    🔎 Closer look:
  </summary>
  While loop has 3 important components to work<br>
  Otherwise, the program will run indefinitely
</details>

```python
action = "run" # initial condition
while action != "stop": # checking the condition so it evaluates to True
  print("Eat a banana")
  action = input("Continue? (run/stop): ")
```

<details>
  <summary>
    👉 Try this 4-4:
  </summary>
  Write a while loop that will continue to execute until user enters x or X.
</details>

<details>
  <summary>
    👀 Answer 4-4:
  </summary>

  ```python
  user_input = "1" # Initial condition - Choose anything except x or X
  while user_input != "x" and user_input != "X": # check the condition
    user_input = input("Enter your choice: ") # Change the condition
  ```
</details>