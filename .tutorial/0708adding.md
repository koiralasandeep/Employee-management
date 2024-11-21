# 7-9. Adding elements to the list

Lists are mutable, so we can add, modify and delete elements

## a. Adding element at the end
- Syntax: <list_name>.append(<element_value>)
```python
# To add 70000 as the last element of the list

employee = ["28678", "Bob Singer", "HR", [90, 95, 67], ["Manager", "Supervisor", "Team Leader"]]
employee.append(75000)
suchi_print(employee)
```

<details>
  <summary>
   🚩 7-9a To Remember: 
  </summary>
  append method takes only one argument
</details>

## b. Adding element at a specified location
- Syntax: <list_name>.insert(<index>, <element_value>)
```python
# To add a 75000 at the third index position

employee = ["28678", "Bob Singer", "HR", [90, 95, 67], ["Manager", "Supervisor", "Team Leader"]]
employee.insert(3, 75000)
suchi_print(employee)
```

<details>
  <summary>
   🚩 7-9b To Remember: 
  </summary>
  The first argument passed to the index method must be an integer
</details>


<details>
  <summary>
   👉 7-9b Try this: 
  </summary>
Add a new value bob@company.com at fourth index position of the list<br>
employee = ["28678", "Bob Singer", "HR", [90, 95, 67], ["Manager", "Supervisor", "Team Leader"]]
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
employee.insert(4, "bob@company")
print(employee)
```
</details>


<details>
  <summary>
   🚩 7-9b2 To Remember: 
  </summary>
  If index doesn't exist, value is added at the end
</details>

```python
employee = ["28678", "Bob Singer", "HR", [90, 95, 67], ["Manager", "Supervisor", "Team Leader"]]
employee.insert(10, 75000) # index 10 is obviously out of the scope of this list, will it raise an exception?
suchi_print(employee)
```