# 7-13. Modify Elements in a List 

## a. Change Value At Given Index

Syntax: <list_name>[\<index\>] = <new_value>

```python
# To change the value at index position 2 to Tom Cruise

favorite_actors = ["George Clooney", "Tom Hanks", "Henry Cavill"]
favorite_actors[2] = "Tom Cruise"
suchi_print(favorite_actors)
```


<details>
  <summary>
   👉 Try this: 7-13
  </summary>
Change the value at index 3 to PHP<br>
programming_languages = ["JavaScript", "Python", "Java", "C++"]
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
programming_languages[3] = "PHP"
```
</details>

## a. Change Value At Of An Element

Syntax: <list_name>[\<index\>] = <new_value>

```python
# To change the value Tom Hanks to Brad Pitt

favorite_actors = ["George Clooney", "Tom Hanks", "Henry Cavill"]
# first check if Tom Hanks is there
if "Tom Hanks" in favorite_actors:
  # Get the index
  position = favorite_actors.index("Tom Hanks")
  favorite_actors[position] = "Brad Pitt"
  suchi_print(favorite_actors)
```