# 7-5. Creating List Using Repetition Operator

<details>
  <summary>
    💡 7-5 Remember
  </summary>
  We learned that * can be a multiplication operator or a repetition operator
</details>

- Similarly, if we have a number and a sequence (like list or tuple), then \* acts as a repetition operator

```python
repeated_list = [7] * 6
suchi_print(repeated_list)
```

<details>
  <summary>
    🔍 Close Look:
  </summary>
  In line 1, the expression [7] * 6 makes six copies of the list [7] and joins them all together in a single list. The resulting list is assigned to the repeated_list variable<br><br>
  In line 2, the repeated_list variable is passed to the print function
</details>

<details>
  <summary>
   👉 Try this: 7-5
  </summary>
  Can you create a list like this?
  [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
</details>


<details>
  <summary>
   👀 Answer
  </summary>

  ```python
  my_list = [1, 2, 3] * 3
  ```
</details>

<details>
  <summary>
   🚩 7-5 To Remember:
  </summary>
  The number must be int, so convert any float or str to int before using it to repeat a string
</details>