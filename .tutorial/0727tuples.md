# 7-27. Creating Tuples

## a. Creating an empty tuple
Syntax: <tuple_name> = tuple()
```python
scores = tuple()

# or

scores = ()

suchi_print(scores)
```

## b. Creating tuple with one element

```python
scores = (89, ) # must place a comma

suchi_print(scores)
```

## c. Creating tuple with elements/values
Syntax: <tuple_name> = (\<element1\>, \<element2\>,\<element3\> )
- Tuple elements are parantheses in brackets and separated by commas
- Elements can be of any datatype

### 1. Integer tuple
All elements are ints

```python
# Example of an integer tuple
even_numbers = (2, 4, 6, 8, 10)
suchi_print(even_number) 
```


### 2. float tuple
All elements are floats
```python
# Example of a float tuple
sales = (4.5, 5.6, 6.3, 7.8, 5.7)
suchi_print(sales)
```

### 3. string tuple
All elements are strings
```python
# Example of a string tuple
favorite_actors = ("George Clooney", "Tom Hanks", "Henry Cavill")
suchi_print(favorite_actors)
```

### 4. bool tuple (all elements are booleans)
```python
# Example of a bool tuple
bool_t = (True, False, False, True, True)
suchi_print(bool_t)
```

### e. Multiple Datatypes:
Tuples can have elements of any datatype including a list or a tuple

```python
# Multiple Datatypes in a tuple
student = (123678, "James Smith", "COSC", 3.67, [90, 95, 67], ("yellow", "blue", "orange"))
suchi_print(student)
```

## d. Creating tuples using range()

```python
numbers = tuple(range(5))
print(numbers)

# another example
numbers = tuple(range(1, 10, 2))
suchi_print(numbers)
```

## e. Creating tuple using repetition operator

```python
t1 = (7, ) * 6
suchi_print(t1)

# another example
t1 = (1, 3, 5) * 4
suchi_print(t1)
```

## Tuples are ordered

The order in which elements appear in a tuple is important

```python
favorite_actors1 = ("George Clooney", "Tom Hanks", "Henry Cavill")

favorite_actors2 = ("Tom Hanks", "George Clooney", "Henry Cavill")

if favorite_actors1 == favorite_actors2:
  print("Same Tuples")
else:
  print("Different tuples")
```

## Duplicity

Tuples can have the same value appear multiple times

```python
l1 = (1, 2, 3, 2, 3)

```
Values 2 and 3 are repeating
