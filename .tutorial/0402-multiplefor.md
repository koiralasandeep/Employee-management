# 4-2. Multiple for loops


- Now imagine a scenario where there are two tracks, red and blue. The runner has to run the red track 5 times and eat a banana each time, then he runs the blue track 3 times and eats a strawberry each time. How many bananas and how many strawberries does he eat? How to write Python for loops for this?

```python
for lap in range(1, 6):
  print("Eat a banana")
print(lap)

for lap in range(1, 4):
  print("Eat a strawberry")
print(lap)
```
