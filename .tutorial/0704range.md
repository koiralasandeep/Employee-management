# 7-4. Creating List Using range() function

<details>
  <summary>
   💡 7-4 Remember:
  </summary>
   range() function returns an object that holds a series of values<br><br>
  When you pass three arguments to the range function<br>
  - the first argument is the starting value<br>
  -  the second argument is the ending limit<br>
  -  and the third argument is the step value
</details>

We can use the built-in list() function to convert a range of elements to a list

Syntax: <list_name> = list(range(\<start\>, \<stop\>, \<step\>))

```python
numbers = list(range(5))
print(numbers)

# another example
numbers = list(range(1, 10, 2))
suchi_print(numbers)
```

<details>
  <summary>
   👉 Try this: 7-4
  </summary>
  Using list and range functions, can you create a list like this<br>
  [3, 8, 13, 18, 23, 28]
</details>


<details>
  <summary>
   👀 Answer
  </summary>

  ```python
  my_list = list(range(3,30,5))
  ```
  Infact, it doesn't have to be 30 in the second argument, it could be 29 or 30 or 31 or 32 or 33
</details>
