# 9-1,2. Creating Dictionary

## 9-1. Create an empty dictionary

Syntax: <dictionary_name> = {} or <dictionary_name> = dict()
```python
student = {}
student = dict()  
```
<details>
  <summary>
    💡 Remember this for future
  </summary>
  In the above code, we created student as an object of the class dict
</details>

## 9-2. Creating a dictionary with values
- Dictionary keys can be of any datatype that is immutable
- Values can be of any datatype, including a dictionary
### a. Method 1:
```python
student = {"name": "Mary Kay",
            "cwid": "1007845",
            "major": "CINS",
            3 : 3,
            "gpa" : 4.0
          }
suchi_print(student)
```

### b. Method 2: Using {} and keys in []
```python
student = {}
student["name"] = "Mary Kay"
student["cwid"] = "1007845"
suchi_print(student)
```

### c. Method 3: dict method and list of tuples
```python
name_tuple = ("name", "Mary Kay")
cwid_tuple = ("cwid", "1007845")
major_tuple = ("major", "CINS")
student_list = [name_tuple, cwid_tuple, major_tuple]
           
suchi_print(student_list)

# student = dict(student_list)
# suchi_print(student)
```
<details>
  <summary>
    💡 Note
  </summary>
  Each tuple should have exactly two elements
</details>