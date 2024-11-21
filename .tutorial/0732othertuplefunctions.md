# 7-32. Some Tuple Functions

## len() Function

## Find the number of elements in a tuple
Syntax: <variable_name> = len(<tuple_name>) - returns an integer

```python
favorite_actors = ("George Clooney", "Tom Hanks", "Henry Cavill")
number_of_actors = len(favorite_actors)
print(number_of_actors)
```

<details>
  <summary>
   👉 Try this: 7-32a
  </summary>
Find the number of elements in this tuple<br>
employee = ["28678", "Bob Singer", "HR", [90, 95, 67], ["Manager", "Supervisor", "Team Leader"]]
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
elements = len(employee)
print(elements)
```
</details>

## b. min, max, sum

Syntax:  
32b1. `max(<tuple_name>)` - returns the maximum element of the tuple  
32b2. `min(<tuple_name>)` - returns the minimum element of the tuple  
32b3. `sum(<tuple_name>)` - returns the sum of elements of the tuple

```python
scores_tuple = (99, 98, 96, 94, 100, 92, 90)
maximum_score = max(scores_tuple)
print(maximum_score)

gpa = (3.45, 2.37, 3.22, 4.0)
minimum_gpa = min(gpa)
print(minimum_gpa)

scores = (99, 98, 96, 94, 100, 92, 90)
total_score = sum(scores)
print(total_score)
```
**NOTE 📝** :
These functions is used only if values are **_all_** numeric or all strings

<details>
  <summary>
   👉 Try this: 7-32b
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
