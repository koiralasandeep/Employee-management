# 9-4. Modifying Dictionary Elements

## a. Modifying dictionary elements given the key
```python
student = {"name": "John Decker", 
            "cwid": "1007845"}
student["name"] = "Josh Decker"
student["major"] = "COSC"
suchi_print(student)
```

## b. Modifying dictionary elements given the value

For modifying elements using the value we must use a for loop

```python
student = {"name": "John Decker", 
            "cwid": "1007845"}

old_name = input("Whose name do you want to change? : ")
new_name = input("What do you want to change it to? : ")

# suchi_print(student)

for key, value in student.items():
  if value == old_name:
    student[key] = new_name
    
# suchi_print(student)
```
- We will see more such examples later on
  
<details>
  <summary>
    💡 Note:
  </summary>
  We will see more on items() method later on
    
</details>
