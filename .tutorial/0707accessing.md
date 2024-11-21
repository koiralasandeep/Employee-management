# 7-8. Accessing List Index Using Value

## Syntax: <list_name>.index(<element_value>)
- The index method is a value-returning method
```python
# To find the index position of James Smith in the list

student = [123678, "James Smith", "COSC", 3.67, [90, 95, 67]]
index_position = student.index("James Smith")

# This has to be case-sensitive
```

<details>
  <summary>
   🚩 7-8 To Remember: 
  </summary>
  If we look for a value that doesn't exist in the list, an exception is raised
</details>


<details>
  <summary>
   👉 Try this: 7-8
  </summary>
  In the list below, find the index position of 28678 and using that index, print the name<br>
<code>employee = ["28678", "Bob Singer", "HR", [90, 95, 67], ["Manager", "Supervisor", "Team Leader"]]</code>
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
empid_index = employee.index("28678")
employee_name = employee[empid_index+2]
print(employee_name)
```
</details>
