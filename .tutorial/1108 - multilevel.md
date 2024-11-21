# 11-7. Multi-Level Inheritance

![Image](../.tutorial/images/multi-level-inhertiance.png)

- Grandchild class can access its own attributes, and both child and parent class' attributes and methods
- Child class can access its own and its parent's attributes and methods
- Parent class can access only its attributes and methods

## Creating multi-level inheritance

```python
class Parent():
  def __init__(self):
    print('Parent Init')

class Child(Parent):
  pass

class Grandchild(Child):
  pass
```

Now let's create objects an see how they behave

```python
p = Parent()
# c = Child()
# g = Grandchild()
```

