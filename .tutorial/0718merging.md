# 7-18. Merging two lists

## a. Using operator +

```python
l1 = [1, 5, 3, 7, 9]
l2 = ["alpha", "beta", "psi"]

l3 = l1 + l2
suchi_print(l3)

# l3 = l2 + l1
# suchi_print(l3)
```

 ## b. Using method

 ```python
 l1 = [1, 5, 3, 7, 9]
 l2 = ["alpha", "beta", "psi"]

 l1.extend(l2)
 suchi_print(l1)

 # l2.extend(l1)
 # suchi_print(l2)
 ```

<details>
  <summary>
   🎉 Fun exercise: 
  </summary>
See the difference between append and extend

```python
employee = ["28678", "Bob Singer", "HR"]
more_data = ["08/01/1982", "bob@company.com" ]
employee.extend(more_data)
# employee.append(more_data)
suchi_print(employee)
```

**HINT:** The `append()` method adds a list as a single element to the end of a list, whereas the `extend()` method concatenates the first list with another list.
</details>


<details>
  <summary>
    🚩 To Remember
  </summary>

`list3_name = <list1_name> + <list2_name>`
and 
`list1_name.extend(list2_name)`
are almost equivalent.
</details>