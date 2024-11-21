# 9-10, 9-11. Pickling and Unpickling Dictionaries

Serializing an object is the process of converting an object to a stream of bytes that can be saved to a file for later retrieval.  
In Python, object serialization is called **pickling**.  
We need to import the pickle module for pickling and unpickling

## 10. Pickling a dictionary
Must open file in wb mode - write in binary
  
```python
import pickle

student1 = {
  "name" : "John",
  "age" : 29,
  "gpa" : 3.45,
  "courses" : {"fall": ["math 101", 'engl 101'],
               "winter" : ["math 201", 'engl 201'],
               "spring" : ["math 201", 'engl 201'],
               "summer" : ["math 201", 'engl 201']
              },
  "sports" : ("tennis", "badminton", "ping pong"),
  "colors" : ["red", "black", "yellow"],
  "favorites" : ["apple", "orange", "banana"]
  }
  
with open("student.txt", "wb") as fp:
  pickle.dump(student, fp)
```

<details>
  <summary>
    💡 Note
  </summary>
  When you open a file that doesn't exist, in wb mode, Pyhton creates it
</details>


## 9-11. Unpickle a dictionary
Must open file in rb mode - read in binary

```python
with open("student.txt", "rb") as fp:
  student = pickle.load(fp)

suchi_print(student)
```

<details>
  <summary>
    💡 Note
  </summary>
  We can pickle and unpickle lists and tuples too
</details>