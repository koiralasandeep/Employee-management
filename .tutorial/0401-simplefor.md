# 4-1. Simple For Loop

**Syntax:**
```python
# Using range function
for [loop_variable] in range([start], [stop], [step]):
  [statement 1]
  [statement 2]

# Iterating over a file
for [line] in [file_pointer]:
  [action to do with each line]

# Many more ...
```

## a. Range Function

The in-built range() function in Python generates a sequence of numbers  

```python
for num in range(5):
  print(num)
```
<details>
  <summary>
    🔎 Closer look:
  </summary>
  In the above statement, range(5) generates a sequence of five numbers starting with zero, that is 0, 1, 2, 3, 4<br>
  The variable num is called a loop variable<br>
  When the for loop starts, the num variable stores the value 0<br>
  The print(num) displays 0<br>
  The control goes back to the for loop and this time num stores the value 1<br>
  The print statement displays it<br>
  This keeps happening until there are no more numbers left in the sequence<br>
  Hence the output is<br><br>
  0<br>
  1<br>
  2<br>
  3<br>
  4<br>
</details>

### Let's slow it down:

```python
from time import sleep # Don't worry about this statement
for num in range(5):
  print(num)
  sleep(5) # Don't worry about this statement
```

### Example, let's say a runner has to run around a track, say, 5 times. How does he keep track of what lap number he is in? How do we write for loop in Python for that?

```python
for lap in range(5):
  print(lap)
```

Well in real life, lap numbers start at 1 not at 0. So, how do we change the range function?

```python
for lap in range(1, 6):
  print(lap)
```

<details>
  <summary>
    🔎 Closer look:
  </summary>
  In the range function, 1 is start and 6 is end.<br>
  Loop runs until the variable lap is equal to end-1<br>
  So the sequence generated is 1, 2, 3, 4, 5
</details>

### Other variations of the range function:

```python
# Using start, stop and step
for num in range(2, 17, 3):
  print(num)
```

<details>
  <summary>
    🔎 Closer look:
  </summary>
  In the range function, 2 is start, 17 is end and 3 is step<br>
  So the sequence generated is 2, 5, 8, 11, 14<br>
  Loop runs until the variable num is equal to end-1, that is why 17 is not displayed
</details>

```python
# Using start, stop and negative step
for num in range(25, 2, -4):
  print(num)
```

<details>
  <summary>
    🔎 Closer look:
  </summary>
  When using negative step, the sequence is generated in descending order<br>
  In the range function, 25 is start, 2 is end and -4 is step<br>
  So the sequence generated is 25, 21, 17, 13, 9, 5<br>
  Loop runs until the variable num is equal to end-1<br>
  Start must be greater than end when using negative step
</details>



<details>
  <summary>
    💡 Note:
  </summary>
  We don't necessarily have to use the loop variable    
</details>

Let's modify our example, say the runner has to run around a track, say, 10 times. Each time he finishes a lap, he must eat a banana and we print `Eat a banana`

```python
for lap in range(10):
  print("Eat a banana")

# Notice, we didn't use the loop variable anywhere inside our loop
```

<details>
  <summary>
    👉 Try this 4-1a:
  </summary>
  Ask a user to enter a whole number. Write a for loop so a runner has to run around a track, the user specified number of times. Each time he finishes a lap, he must eat a banana and we print Eat a banana.
</details>

<details>
  <summary>
    👀 Answer 4-1a:
  </summary>
  
  ```python
  num = int(input("Enter number of laps: ")) # convert user value to int
  for lap in range(num):
    print("Eat a banana")
  ```
</details>

## b. Accumulator variable

Well, lets change our scenario, how about the runner eats a banana only for the even laps that he runs. How do we print the number of bananas he ate?

```python
num_of_bananas = 0 # We assign 0 to a variable BEFORE the for loop
for lap in range(1, 11):
  if lap%2 == 0:  # Check if remainder is zero when divided by 2
    num_of_bananas += 1   # We add 1 to the variable only when it is even lap
print(num_of_bananas)

# num_of_bananas is called an accumulator variable
```

<details>
  <summary>
    👉 Try this 4-1b:
  </summary>
  A runner runs each lap and eats the lap number of bananas. That is, first lap, he eats one banana, second lap, he eats two bananas, so on. How many bananas does he eat after running 5 laps?
</details>

<details>
  <summary>
    👀 Answer 4-1b:
  </summary>

  ```python
num_of_bananas = 0
for lap in range(1, 6):
    num_of_bananas += lap
  
print(num_of_bananas)
  ```
</details>


