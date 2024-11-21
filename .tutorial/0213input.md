# 2-13. Input Function
If we need the user to interact with our program by providing some data, we must use input function

### Syntax:
a. <variable_name> = input() or  
b. <variable_name> = input(\<string\>)

## a.
```python
name = input()
print(name)
```

<details>
  <summary>
    🔎 Closer look
  </summary>
  name = input() - prompt the user to enter a value and we store that in a variable called name<br>
  print(name) - we print the user entered value
</details>


<details>
  <summary>
    🚩 2-13a. To remember
  </summary>
  input is a value returning function<br>
  so you must always have collect the value (entered by the user) in a variable
</details>


## b. 
We can send a string inside the parantheses to give some instructions to the user on what he/she is expected to enter

```python
name = input("Enter your name: ")
print(name)
```

<details>
  <summary>
    👉 2-13b. Try this
  </summary>
  ask the user to enter age and print it
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  age = input("Enter age: ")
</details>


## c. Datatype

input() function always returns a string

```python
height = input("Enter your height: ")
print(type(height))
```

<details>
  <summary>
    👉 2-13c. Try this
  </summary>
  ask the user to enter age and add 1 to it and print Next year, you will be __ years old
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  age = input("Enter age: ")<br>
  age = float(age)<br>
  age = age + 1<br>
  print(f"Next year, you will be {age} years old")
</details>


<details>
  <summary>
    🚩 2-13c. To remember
  </summary>
  input() function always returns a string
</details>