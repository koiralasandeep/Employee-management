# 7-30. Tuples: in Operator

## To check if a value is present in the tuple
Syntax: if <value> in <tuple_name>:
```python
# To check if George Clooney is in the tuple

favorite_actors = ("George Clooney", "Tom Hanks", "Henry Cavill")
if "George Clooney" in favorite_actors:
  print(True)
```

<details>
  <summary>
   👉 Try this: 7-30
  </summary>
Ask user of an actor name, check if it is in the list, if yes, get the index of that actor and print it else print - Actor not present<br>
  actors = ("George Clooney", "Tom Hanks", "Henry Cavill")
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

```python
actor = input("Enter an actor name: ")
if actor in actors:
  idx = actors.index(actor)
  print(idx)
else:
  print("Actor not present")
```
</details>