# 7-15. Find min, max, sum

Syntax:  
15a. `max(<list_name>)` - returns the maximum element of the list  
15b. `min(<list_name>)` - returns the minimum element of the list  
15c. `sum(<list_name>)` - returns the sum of elements of the list

```python
scores_list = [99, 98, 96, 94, 100, 92, 90]
maximum_score = max(scores_list)
print(maximum_score)

gpa_list = [3.45, 2.37, 3.22, 4.0]
minimum_gpa = min(gpa_list)
print(minimum_gpa)

scores_list = [99, 98, 96, 94, 100, 92, 90]
total_score = sum(scores_list)
print(total_score)
```
**NOTE 📝** :
These functions is used only if values are **_all_** numeric or all strings

<details>
  <summary>
   👉 Try this: 
  </summary>
Calculate the min, max and sum of the list

```python
sales_data = [100.45, 102.67, 230.22, 115.75, 201.33, 118.56]
```
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python  
max(sales_data)
min(sales_data)
sum(sales_data)
```
</details>
