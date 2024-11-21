# 9-14. Dictionary Comprehension

## Example 1: 
To create a dictionary with 10 items where values are the square of the keys with only even keys

<details>
  <summary>
    Without comprehension
  </summary>

  ```python
  dict = {}
  for i in range(20):
    if i%2 == 0:
      dict[i] = i**2
  suchi_print(dict)
  ```
</details>


<details>
  <summary>
    Using Comprehension
  </summary>
  
  ```python
  dict = {i:i**2 for i in range(20) if i%2 == 0}
  suchi_print(dict)
  ```
</details>


## Example 2: 
Create a dictionary using two lists

<details>
  <summary>
    Without comprehension
  </summary>

  ```python
  header = ['name', 'cwid', 'major', 'gpa']
  student = ['Suchi','100','COSC', 3.98]
  stu_dict = {}
  for ind, val in enumerate(header):
    stu_dict[val] = student[ind]
  suchi_print(stu_dict)
  ```
</details>


<details>
  <summary>
    Using Comprehension
  </summary>
  
  ```python
  stu_dict = {key:val for key, val in zip(header, student)}
  suchi_print(stu_dict)
  ```
</details>


<details>
  <summary>
    👉 Try this: 9-14
  </summary>

  Create a dictionary with values as cubes of keys, but keys must be divisible by 4 using comprehension
</details>


<details>
  <summary>
    👀 Answer
  </summary>
  
  ```python
  newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
  ```
</details>
