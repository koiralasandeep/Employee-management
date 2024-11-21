# 5-10. Making Changes to Parameters

We have seen that when an argument is passed to a function, the function parameter variable will reference the argument’s value<br><br>
But, any changes that are made to the parameter variable inside the function will not affect the argument

```python

def main():
  value = 99
  print(f'Before change me call: {value}')
  change_me(value)
  print(f'After change me call: {value}')

def change_me(arg):
  arg = 0
  print(f'Inside change me function: {arg}')
 
main()
```

<details>
  <summary>
    🔎 Closer look
  </summary>
The main function creates a local variable named value with value 99<br>
The print statement 'Before change me call: 99'<br>
The value variable is passed as an argument to the change_me function<br>
This means that in the change_me function, the arg parameter will also reference the value 99<br>
Inside the change_me function, the arg parameter is assigned the value 0<br>
This reassignment changes arg, but it does not affect the value variable in main<br>
The two variables now reference different values in memory. The print statement  'Inside change me function: 0'<br>
And the function ends<br>
Control of the program then returns to the main function<br>
The print statement displays 'After change me call: 99'<br>
This proves that even though the parameter variable arg was changed in the change_me function, the argument (the value variable in main) was not modified.
</details>

<details>
  <summary>
    🚩 5-10 To remember
  </summary>
  This form of argument passing, where a function cannot change the value of an argument that was passed to it, is called pass by value
</details>


So far we have seen that the calling function can communicate with the called function, but the called function cannot use the argument to communicate with the calling function.<br><br>
Later in this chapter, we will see how to write a function that can communicate with the part of the program that called it by returning a value