# 5-7. Local Variables snd scope

When we assign a value to a variable inside a function, we create **a local variable**   
A local variable created inside a function cannot be accessed by statements that are outside the function  

<details>
  <summary>
    💡 5-7 Note:
  </summary>The term local is meant to indicate that the variable can be used only locally, within the function in which it is created
</details>

```python

def get_name():
  # name is assigned a value by the user input
  name = input('Enter your name: ')
  
def main():
  get_name()
  print(f'Hello {name}.')

main()
 ```
<details>
  <summary>
    🔎 Closer look
  </summary>
  This program has two functions: main and get_name. In the function get_name, the name variable is assigned a value that is entered by the user, so the name variable is local to that function. This means that the name variable cannot be accessed by statements outside the get_name function.<br><br>

  The main function calls the get_name function. Then, the statement after the function call tries to access the name variable. This results in an error because the name variable is local to the get_name function, and statements in the main function cannot access it.
</details>

<details>
  <summary>
    🚩 5-7a To remember
  </summary>
  A local variable cannot be accessed by code at a point before the variable has been created.
</details>



## b. Scope
A variable’s scope is the part of a program in which the variable may be accessed. In the above example the scope of the variable name is the function get_name()  

<details>
  <summary>
    🚩 5-7b To remember
  </summary>
  A variable is visible only to statements in the variable’s scope.
</details>
