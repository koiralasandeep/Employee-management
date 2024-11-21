# 9-0. Dictionary Characteristics

## Charactersitics:

### Mutability
- Dictionaries are mutable objects
- Which means you can add or delete or modify elements of a dictionary after it is created
- We will see in next sections how to do that

<details>
  <summary>
    💡 Note
  </summary>
  int, float, string, bool and tuples are immutable data types<br>
  lists and dictionaries (sets too) are mutable
</details>

### Order

<details>
  <summary>
    💡 Remember?
  </summary>
  Lists and Tuples are ordered
</details>

```python
list = ["Mary Kay", "kay@ulm.edu"]

list2 = ["kay@ulm.edu", "Mary Kay"]
suchi_print(list)

# if list == list2:
#   print("Same")
# else:
#   print("Not same")
```
But, elements in dictionary are unordered

```python
# Dictionaries don't care about order as long as the keys are the same

student = {"name" : "Mary Kay", "email" : "kay@ulm.edu"}
student2 = {"email" : "kay@ulm.edu", "name" : "Mary Kay"}
suchi_print(student)

# if student == student2:
#   print("Same")
# else:
#   print("Not same")
```

### Duplication
Keys in dictionaries cannot be duplicated
```python
student = {"name" : "Mary Kay",
            "email" : "kay@ulm.edu", "name" : "Mary Ann"}

suchi_print(student)
```