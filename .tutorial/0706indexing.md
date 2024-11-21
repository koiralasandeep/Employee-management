# 7-6. Indexing

## a. Indexing

- We can access the individual elements in a list is with an index
- Each element in a list has an index that specifies its position in the list
- Indexing starts at 0, so the index of the first element is 0, the index of the second element is 1, and so forth.
- The index of the last element in a list is 1 less than the number of elements in the list
- Syntax: \<variable_name\> = \<list_name\>[\<index_position\>]

```python
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
# To get the first element we put the index in square brackets
first = row_1[0]
print(first)
```

<details>
  <summary>
   🚩 7-6a To Remember:
  </summary>
  Indexing in lists/tuples ALWAYS starts at 0
</details>


## b. Negative Indexing

- We can also use negative indexes with lists to identify element positions relative to the end of the list
- The Python interpreter adds negative indexes to the length of the list to determine the element position
- The index −1 identifies the last element in a list, −2 identifies the next to last element, and so forth

```python
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
# To get the last element using negative index
last = row_1[-1]
print(last)
```

### See image below

![Image](../.tutorial/images/list_indexes.svg)


<details>
  <summary>
   👉 7-6b Try this: 
  </summary>
  In the row_1 list, can you print USD using<br>
  1. positive index<br>
  2. negative index
</details>


<details>
  <summary>
   👀 Answer
  </summary>

  ```python
  element_positive_index = row_1[2]
  element_negative_index = row_1[-3]
  print(element_positive_index)
  print(element_negative_index)
  ```
  📝 You may choose any variable names as long as the list name and indexes are correct 🙂
</details>

## What happens when you use an index that doesn't exist?

```python
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
var = row_1[5]
print(var)

# Exception is raised
```

<details>
  <summary>
   🚩 7-6 To Remember:
  </summary>
  An exception is raised when we access an index that doesn't exist in the list/tuple
</details>