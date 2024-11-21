# 5-14. Value-Returning Functions
A value-returning function is a function that returns a value back to the part of the program that called it

```python
def function():
  number = input("Enter a number: ")
  return int(number)

a = function()
print(a)
b = a*a
print(b)
```

<details>
  <summary>
    🔎 Closer look
  </summary>
  A value-returning function is a special type of function<br>
  It is a group of statements that perform a specific task<br>
  When you want to execute the function, you call it<br>
  When a value-returning function finishes, it returns a value back to the part of the program that called it.<br>
  The value that is returned from a function can be used like any other value: it can be assigned to a variable, displayed on the screen, used in a mathematical expression (if it is a number), and so on.
</details>

Value-returning functions can be
- Standard Library Functions
- USer-defined Functions