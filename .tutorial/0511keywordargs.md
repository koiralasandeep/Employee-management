# 5-11. Keyword Arguments
We have seen how arguments are passed by position to parameter variables in a function.<br>
In addition to this form of argument passing, we can specify which parameter variable the argument should be passed to<br>

`parameter_name=value`<br>

parameter_name is the name of a parameter variable<br>
value is the value being passed to that parameter<br><br>
An argument that is written in accordance with this syntax is known as a **keyword argument**

### Let us see our Try this example:

```python
def create_multiple(number, multiple):
  resultant = number * multiple
  print(resultant)

def main():
  n = int(input("Enter number: "))
  m = int(input("Enter multiple: "))
  
  # Passing by position
  create_multiple(n, m)

  # Passing by keyword - one way
  create_multiple(number = n, multiple = m)

  # Passing by keyword - another way
  create_multiple(multiple = m, number = n)

main()
```

<details>
  <summary>
    🔎 Closer look
  </summary>
When we called create_multiple using positional arguments, n was passed to number and m was passed to multiple, simply based on their respective positions<br>
But, when we use keyword arguments we can specify, which argument can be passed to which parameter<br>
In this case, we don't have to follow the same order<br>
</details>