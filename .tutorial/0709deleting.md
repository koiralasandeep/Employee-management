# 7-10. Deleting Elements From List

## a. Deleting element using value
Syntax: <list_name>.remove(<value>)


```python
# To remove Javascript from the list
# value must be a case-sensitive match

programming_languages = ["JavaScript", "Python", "Java", "C++"]
programming_languages.remove("JavaScript")
suchi_print(programming_languages)
```

<details>
  <summary>
   🚩 7-10a To Remember: 
  </summary>
  Exception is raised if value is not in the list
</details>

 

<details>
  <summary>
   👉 Try this: 7-10a
  </summary>
Delete the programming language Java<br>
programming_languages = ["JavaScript", "Python", "Java", "C++"]
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
employee.remove("Java")
print(employee)
```
</details>


## b. Deleting element using index
Syntax: del <list_name>[\<index\>]

```python
programming_languages = ["JavaScript", "Python", "Java", "C++"]
del programming_languages[3]
suchi_print(programming_languages)

# Exception is raised if index is not in the list
```


<details>
  <summary>
   👉 Try this: 7-10b
  </summary>
Delete the element at index 1<br>
programming_languages = ["JavaScript", "Python", "Java", "C++"]
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
del employee[1]<br>
print(employee)
  ```
</details>