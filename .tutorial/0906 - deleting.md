# 9-6. Deleting Dictionary Elements

## a. Method 1 - using del statement
```python
student = {"name": "Suchi Rodda", "cwid": "1007845", "major": "COSC"}
suchi_print(student)
del student["major"]
# suchi_print(student)
```

## b. Method 2 - using pop() method
```python
student = {"name": "Suchi Rodda", "cwid": "1007845", "major": "COSC"}
student.pop('phone')
```
- Can we delete if the key doesn't exist?
```python
student = {"name": "Suchi Rodda", "cwid": "1007845", "major": "COSC"}
del student["phone"]
# student.pop('phone')
```

<details>
  <summary>
    💡 Note:
  </summary>
  Both del and pop() will raise an exception if the key is not found
</details>