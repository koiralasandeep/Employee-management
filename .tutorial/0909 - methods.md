# 9-9. Dictionary Methods

## a. copy()
Creates a copy of the dictionary

```python
student = {"name": "Suchi Rodda", "cwid": "1007845", "major":"COSC", "gpa":4.5}
new_student = student.copy()
suchi_print(new_student)
```

## b. clear()
Deletes all the elements in a dictionary

```python
student.clear()
suchi_print(student)
```

## c. get()
Gets the value associated with specified key
```python
name = student.get("name")

```

## d. update()
Adds new key-value pair or modify existing value in a dictionary

```python
# using dictionary
new_dictionary = {"gpa":4.0, 
                  "email":"rodda@ulm.edu"}
student.update(new_dictionary)
suchi_print(student)

# using a list of tuples
list_of_tuples = [("gpa", 4.0), 
                  ("email",  "rodda@ulm.edu")
                 ]
suchi_print(student)
```

## e. items()
Returns all the dictionary's keys and associated values

```python
print(student.items())
```

## f. keys()
Returns all the dictionaries keys as a sequence
```python
k = student.keys()
# suchi_print(k)
```

## g. values()
Returns all the dictionaries values as a sequence
```python
v = student.values()
suchi_print(v)
```

## h. pop()
Returns value associated with specified key and removes that key-value pair from the dictionary
```python
popped = student.pop("name")
suchi_print(student)
# raises exception is key not present
```

## i. popitem()
Returns the last key-value pair and removes that key-value pair from the dictionary

```python
popped_item = student.popitem()
# print(popped_item)
print(student)
```