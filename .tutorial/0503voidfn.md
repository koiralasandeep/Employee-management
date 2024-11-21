# 5-3. Writing Our First Void Function

A function that doesn't return any value to the calling after execution is called a void function.

## a. Defining the function
**Syntax:**  

def <function_name>():  

This is called a **function header**  
Set of statement(s) inside the function is called **function body**

<details>
  <summary>
    💡 Function naming conventions
  </summary>
  Same rules when naming variables apply here<br><br>
- cannot use Python’s keywords<br>
- cannot contain spaces<br>
- cannot use any special characters except underscore<br>
- can use numbers as long as it doesn't start with a number<br>
- uppercase and lowercase characters are distinct
</details>

```python
def first_function(): # function header or function signature
  # all statements must be indented and collectively called function body
  print("This is my first function!")
  print("Hip hip hooray")

```

<details>
  <summary>
    👍 5-3a Rule of thumb:
  </summary>
Always define a function at ZERO indent position<br>
  Until we get to chapter 10
</details>

## b. Calling a function
Remember, defining is not enough, we must call it  
We call a function by its name with parantheses next to it  
Function call will not be inside its definion (atleast until chapter 12)

```python
def main():
  first_function()

main()
```


<details>
  <summary>
    👉 5-3a Try this:
  </summary>
  Define a function named second_function and inside the function body have two print statements to print<br><br>
  I am in second function<br>
  I will call third function
</details>


<details>
  <summary>
    👀 Answer:
  </summary>
def second_function():<br>
&ensp;print("I am in main")<br>
&ensp;print("I will call third function")
</details>


<details>
  <summary>
    👉 5-3b Try this:
  </summary>
  Call the second_function in main() after the call to first_function
</details>


<details>
  <summary>
    👀 Answer:
  </summary>
def main():<br>
&ensp;first_function()<br>
&ensp;second_function()<br><br>
main()
</details>