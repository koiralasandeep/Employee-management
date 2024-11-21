# 10-7. Creating a Dictionary of Objects
Dictionaries can store different datatypes  
They can also store objects

```python
student1 = Student("Mira", "COSC")
student2 = Student("Raven", "HIST")

obj_dictionary = {"30010100": student1,
                  "30010101" : student2]

print(obj_dictionary)
```

<details>
  <summary>
    👉 Try this
  </summary>
  Create a third student with your own values and add that student to the dictionary
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  Outside class definition,<br>
  student3 = Student("Frodo", "ART")
  obj_dictionary["30010102"] = student3
</details>