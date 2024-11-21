# 9-7. Complex Dictionary

- Dictionary values can be str, int, float, bool, lists, tuples, dictionaries, and even nested dictionaries
- Dictionary keys can be any immutable datatype, including tuples

```python
student = {
  "age" : 29,
  "gpa" : 3.45,
  "name" : "John",
  "colors" : ["red", "black", "yellow"],
  "sports" : ("tennis", "badminton", "ping pong"),
  "favorites" : ["apple", "orange", "banana"],
  "courses" : {"fall": ["math 101", 'engl 101'],
               "winter" : ["math 201", 'engl 201'],
               "spring" : ["math 201", 'engl 201'],
               "summer" : ["math 201", 'engl 201'],
              }
          }
```

<details>
  <summary>
   🔍 Closer look 
  </summary>
  
  - student is a dictionary
  - student has seven key/value pairs
    - first key is a string age and value is an int 29
    - second key is a string gpa and value is a float 3.45
    - third key is a string name and value is a string John
    - fourth key is a string colors and value is a list with three elements
    - fifth key is a string sports and value is a tuple with three elements
    - sixth key is a string favorites and value is a list with three elements
    - seventh key is a string courses and value is a dictionary with four key/value pairs
      - first key is a string fall and its value is a list with two elements
      - second key is a string winter and its value is a list with two elements
      - third key is a string spring and its value is a list with two elements
      - fourth key is a string summer and its value is a list with two elements<br>    
</details>

## Some Examples
### Example 1: 
<details>
  <summary>
    Add blue to student's colors
  </summary>

  ```python
  student["colors"].append("blue")
  ```

<details>
  <summary>
   🔍 Closer look 
  </summary>
  
  - Students colors are in the key "colors"
  - But that element is a list
  - To add a new color to the existing list we use append() method
</details>

</details>



<details>
  <summary>
   👉 Try this: 9-7a 
  </summary>
  Add the color green at index 2 to the student's colors

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
  student["colors"].insert(2, "green")
  ```
</details>
</details>

### Example 2:
<details>
  <summary>
    Delete the color red from the student's colors
  </summary>

  ```python
  student["colors"].remove("red")
  ```
  But this will raise an exception if red is not in the student's colors, so check before you delete

  ```python
  if "red" in student["colors"]:
    student["colors"].remove("red")
  ```
</details>


### Example 3:
<details>
  <summary>
    Add a maymester term with acct 101 as a course
  </summary>
  
```python
student["courses"]["maymester"] = ["acct 101"]
```

<details>
  <summary>
   🔍 Closer look 
  </summary>
  
  - Students courses are in the key "courses"
  - But that element is a dictionary
  - To add a new course we must create a new key value pair
  - The key is a string maymester and the value is a list with one element acct 101     
</details>
</details>

### Example 4:
<details>
  <summary>
    Drop the math 101 in fall
  </summary>
  
```python
student["courses"]["fall"].remove("math 101")
```
</details>

<details>
  <summary>
   👉 Try this 
  </summary>
  
  Drop the course engl 201 from summer

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
  student["courses"]["summer"].remove("engl 201")
  ```
</details>
</details>


### Example 5:

<details>
<summary>
  Add a user entered course for winter
</summary>
  
```python
course = input("Enter the course to add: ")
student["courses"]["winter"].append(course)
```
</details>

<details>
  <summary>
   👉 Try this 
  </summary>
  Add a user entered course for spring<br>
  
  ```python
  course = input("Enter the course to add: ")
  ```

<details>
  <summary>
   👀 Answer 
  </summary>

  ```python
  student["courses"]["spring"].append(course)
  ```
</details>
</details>

### Example 6:

<details>
  <summary>
    Ask user for a term and a course and delete that course from that term
  </summary>

```python
term = input("Enter a term: (fall/winter/spring/summer) ")
if term in student["courses"]:
  course = input("Enter course to delete: ")
  if course in student["courses"][term]:
    student["courses"][term].remove(course)
  else:
    print("Student not enrolled in this course")
else:
  print("Student not enrolled for this term")
```
</details>


### Example 7:

<details>
<summary>
  Ask user for a term and a course and add that course to that term
</summary>

```python
term = input("Enter a term: (fall/winter/spring/summer) ")
course = input("Enter course to add: ")
if term in student["courses"]:
  if course not in student["courses"][term]:
    student["courses"][term].append(course)
  else:
    print("Student already enrolled in this course")
else:
  student["courses"][term] = course
```
</details>