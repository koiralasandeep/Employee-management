# 7-26. Multi-dimensional lists

- We know that lists can have any datatypes, including another list
- Such a list is called a multi-dimensional list

```python
student = [123678, "James Smith", "COSC", 3.67, [90, 95, 67]]
suchi_print(student)
```

<details>
  <summary>
    🔍 Close Look:
  </summary>
  student list has five elements<br>
  first element is an int<br>
  second and third are strings<br>
  fourth element is a float<br>
  the last element is a list
</details>

## How to access the second scores in the student list
```python
student = [123678, "James Smith", "COSC", 3.67, [90, 95, 67]]
# We know how to get the scores
scores = student[4]
# scores is a list, so to get the second score, we use index position 1
second_score = scores[1]
suchi_print(second_score)

# Or we can consolidate both these lines into one
suchi_print(student[4][1])
```

## Let's see another example
```python
student1 = [123678, "James Smith", "COSC", 3.67, [90, 95, 67]]
student2 = [987654, "John Decker", "HIST", 4.35, [89, 87, 90]]
students = [student1, student2]
```

<details>
  <summary>
    🔍 Close Look:
  </summary>
  students list has two elements, both lists<br>
  each of these lists has five elements, with fifth element a list<br>
  so, students is three levels deep, list inside a list inside a list 😲<br>
</details>


## So, how to get John Decker's gpa? 
```python

# because John Decker is the second student, we use index 1 to get John's data (stored in a list)
john = student[1]
suchi_print(john)

# john is a list and his gpa is the fourth element
# johns_gpa = john[3]
# suchi_print(gpa)

# to consolidate and eliminate creating more variables
# suchi_print(student[1][3])
```

## How to get James Smith's third score?
```python

# because James Smith is the first student, we use index 0 to get James' data (stored in a list)
james = student[0]
suchi_print(james)

# james is a list and his scores is the last element
# james_scores = james[-1]

# Now we need the third score in the scores list
# third_score = james_scores[2]
# suchi_print(third_score)

# to consolidate and eliminate creating more variables
# suchi_print(student[0][-1][2])
```

<details>
  <summary>
   👉 Try this: 7-26
  </summary>
  Can you get John Decker's first score
</details>


<details>
  <summary>
   👀 Answer
  </summary>
  print(students[1][-1][0])
</details>
