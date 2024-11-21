# 7-28. Accessing elements of a tuple using index

## a. Positive Index
Syntax: \<tuple_name>[\<position-1\>] 
- we use square brackets for index in tuples also  
- this returns a value, so print it or save it in a variable

```python
# To print the fourth element
student = (123678, "James Smith", "COSC", 3.67, [90, 95, 67])
suchi_print(student[3])
```

<details>
  <summary>
    🚩 Remember:
  </summary>
  Exception is raised if you use an index that is not in the tuple
</details>


<details>
  <summary>
    👉 Try this 7-27a:
  </summary>
  Print the FOURTH element of the student tuple<br>
  <code>student = [123678, "James Smith", "COSC", 3.67, [90, 95, 67], ('Basketball', 'Soccer')]</code>
</details>

<details>
  <summary>
    👀 Answer:
  </summary>
  print(student[3])
</details>

## b. Negative Index: 
Gets index from the end of the tuple  
Syntax: \<tuple_name\>[-\<position\>]

```python
student = (123678, "James Smith", "COSC", 3.67, [90, 95, 67], "08/01/2005")
# # To get the last element we just use -1
print(student[-1])
```

<details>
  <summary>
    👉 Try this 7-28b:
  </summary>
  Print the value COSC from the student tuple using negative index<br>
  <code>student = [123678, "James Smith", "COSC", 3.67, [90, 95, 67], ('Basketball', 'Soccer')]</code>
</details>

<details>
  <summary>
    👀 Answer:
  </summary>
  print(student[-4])
</details>
