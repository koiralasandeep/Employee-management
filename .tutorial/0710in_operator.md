# 7-11. in operator

## To check if a value is present in the list
Syntax: if <value> in <list_name>:
```python
# To check if George Clooney is in the list

favorite_actors = ["George Clooney", "Tom Hanks", "Henry Cavill"]
if "George Clooney" in favorite_actors:
  print(True)
```
  
<details>
  <summary>
   👉 Try this: 7-11
  </summary>
Check if Tom Cruise is in the list, if yes, delete Tom Cruise from the list using the value, else print - Actor not present<br>
  favorite_actors = ["George Clooney", "Tom Hanks", "Henry Cavill"]
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
if "Tom Cruise" in favorite_actors:
  favorite_actors.remove("Tom Cruise")
else:
  print("Actor not present")
  ```
</details>