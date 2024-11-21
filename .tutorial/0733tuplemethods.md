# 7-33. Tuple Methods

Tuples are immutable, so we can't use the following methods on tuples

- append
- sort
- reverse
- extend
- copy
- clear

There are only two methods we can use on tuples

- index - returns the index of an element
- count - returns the number of occurences of an element in the tuple

```python

t = (67, 68, 78, 89, 34, 78, 45)
num = t.count(78)
print(num)

```

