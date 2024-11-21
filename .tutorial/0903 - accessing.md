# 9-3. Accessing Dictionary elements

```python
student = {"name": "John Decker", 
            "cwid": "1007845"}
print(student["cwid"])   
```
<details>
  <summary>
    💡 Note
  </summary>
  If the key is not found, Python raises an exception
</details>


Three ways to do address this key error

### a. Exception Handling
```python
try:
  print(student["major"])
except:
  print("Key not found")
```

### b. Using **in** operator
```python
if "major" in dictionary:
  print(student["major"])
else:
  print("Key not found")
```

### c. get() method
```python
major = student.get("major")
# print(major)
```