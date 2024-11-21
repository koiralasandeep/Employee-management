# 7-25. List Comprehension

A list comprehension is a concise expression that creates a new list by iterating over the elements of an existing list or a file or any other sequence.  

Consider a list with each element having a tab character at the end and we are to create a new list which has elements without the tab characters

```python
student = ["23344\t", "Robert\t", "CINS\t", "3.88\t"]

# Without List comprehension
modified_student = []
for element in student:
  modified_student.append(element.rstrip("\t"))

# Using list comprehension
# modified_student = [element.rstrip("\t") for element in student]

print(modified_student)
```

Consider the example of reading a file

```python
def main():
  try:
    f = open("data/students.txt", "r")
  except:
    print("File not found")
  else:

    # Without List comprehension
    students = []  # first create an empty list
    for line in f: # Use a for loop to go over file lines
      line = line.rstrip("\n") # remove the newline character
      students.append(line) # add each line to the end of the list

    # Using List comprehension
    students = [line.rstrip("\n") for line in f]

    
    print(students)

if __name__ == "__main__":
  main()
```

<details>
  <summary>
    👉 Try this: 7-25
  </summary>
  Generate a list of 30 random floats between 500 and 1000, rounded to two decimal points, and write to a list named april_sales_data. Use list comprehension
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  from random import uniform
  april_sales_data = [round(uniform(500, 1000),2) for i in range(30)]
  ```
</details>


<details>
  <summary>
    👉 Try this: 7-25
  </summary>
  Using list comprehension, convert each month to all lower case and store in a list<br>
  <code>months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]</code>
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  months_in_lower = [each_month.lower() for each_month in months]
  ```
</details>



<details>
  <summary>
    👉 Try this: 7-25
  </summary>
  Using list comprehension, convert each element to float and store in a list<br>
  <code>int_list = [3, 6, 4, 8, 10, 4, 5, 8, 9, 1]</code>
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  float_list = [float(each_int) for each_int in int_list]
  ```
</details>

## b. Using IF in list comprehension

```python
# Create a list with only even numbers from this list
int_list = [3, 6, 4, 8, 10, 4, 5, 8, 9, 1]

# Without comprehension
even_number_list = []
for each_number in int_list:
  if each_number % 2 == 0:
    even_number_list.append(each_number)

# With comprehension
even_number_list = [each_number for each_number in int_list if each_number % 2 == 0]

suchi_print(even_number_list)

```

<details>
  <summary>
    👉 Try this: 7-25b
  </summary>
  Make a list of all sales less than 150.0 and print it - use list comprehension
  
  ```python
  sales_data = [100.45, 102.67, 230.22, 115.75, 201.33, 181.56]
  ```
</details>


<details>
  <summary>
    👀 Answer
  </summary>
  
  ```python
  sales_data = [100.45, 102.67, 230.22, 115.75, 201.33, 181.56]
  new_list = [amount for amount in sales_data if amount<150]
  print(new_list)
  ```
</details>