# 9-8. Looping Through Dictionary

```python
student = {"name" : "John",
         "age" : 29,
         "gpa" : 3.45,
         "courses" : {"fall": ["math 101", 'engl 101'],
                      "winter" : ["math 201", 'engl 201'],
                      "spring" : ["math 201", 'engl 201'],
                      "summer" : ["math 201", 'engl 201'],
                      },
         "sports" : ("tennis", "badminton", "ping pong"),
         "colors" : ["red", "black", "yellow"],
         "favorites" : {"apple", "orange", "banana"}
         }

for key in student:
  print(f'{key} : {student[key]}')
```

<details>
  <summary>
    💡 Remember: In Lists
  </summary>
  When using a for loop on a lists, the loop variable stored the value
</details>

```python
import time

list = ["Mary Kay", "1007845", "CINS", 4.0]
for element in list:
  print(element)
  time.sleep(2)
```

<details>
  <summary>
    💡 Note: In Dictionaries
  </summary>
  When using a for loop on a dictionary, the loop variable stores the key
</details>

  
```python
import time

student = {"name": "Mary Kay",
               "cwid": "1007845",
               "major": "CINS",
               "gpa" : 4.0
             }
for element in student:
  print(element)
  time.sleep(2)
```