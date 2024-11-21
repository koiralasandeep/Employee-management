# 9-13. Set Comprehension
Comprehension is a concise way of coding in Python   


## Example:

In the given set, how to get only CINS courses and store in a set?
```python
courses = {'CINS 3002', 'CINS 2020', 'ACCT101', 'COSC2000'}
```

<details>
  <summary>
    Without Comprehension
  </summary>

  ```python
  new_courses = set()
  for each_course in courses:
    if each_course[:4] == 'CINS':
      new_courses.add(each_course)
  print(new_courses)
  ```
</details>

<details>
  <summary>
    With Comprehension
  </summary>

  ```python
  new_courses = {each_course for each_course in courses if each_course[:4] == 'CINS'}
  print(new_courses)
  ```
</details> 

Set comprehension is very similar to list comprehension, except that we use curly braces  

<details>
  <summary>
    👉 Try this: 9-13
  </summary>

  Given a set
  ```python
  projects = {'Spring Valley', 'Compete', 'Riverfront', 'Spintron'}
  ```
  Using set comprehension, create a set with project names all in lowercase
</details>


<details>
  <summary>
    👀 Answer
  </summary>

  Given a set
  ```python
  lowercase_projects = {p.lower() for p in projects}
  ```
</details>
