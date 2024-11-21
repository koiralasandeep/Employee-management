# 4-3. Nested for loops

When a for loop is inside another for loop, it is called nested for loop  

Let's change the previous scenario, where the runner has to run the red track 5 times and each time he runs the red track, he has to run the blue track 3 times. Each time he runs the red track, he has to eat a banana and each time he runs the blue track he eats a strawberry. How many bananas and how many strawberries does he eat? How to write Python for loops for this?

```python
for red_lap in range(1, 6):
  print("Eat a banana")
  for blue_lap in range(1, 4):
    print("Eat a strawberry")

print(f'{red_lap} bananas')
print(f'{red_lap * blue_lap} strawberries')
```

- New scenario 1:
  - The runner has to run the red track 5 times
  - Each time he runs the red track,
    - he eats a banana
    - he has to run the blue track 3 times - each lap around blue track he eats a strawberry
    - he finishes running blue track and then goes to green track
    - he has to run the green track 2 times - each lap around green track he eats a blueberry
  - How many bananas, strawberries and blueberries does he eat? How to write Python for loops for this?

- New scenario 2:
  - The runner has to run the red track 5 times
  - Each time he runs the red track,
    - he eats a banana
    - he has to run the blue track 3 times - each lap around blue track he eats a strawberry
    - each time he runs the blue track he has to run the green track 2 times - each lap around green track he eats a blueberry
  - How many bananas, strawberries and blueberries does he eat? How to write Python for loops for this?