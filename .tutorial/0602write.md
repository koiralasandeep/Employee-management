# 6-2. Writing to file
Before we can write to a file, we must open it in **w** mode  
When we open a file in write mode it is called an output file

**Syntax**: <file_pointer> = open("\<file_name\>", "w")

```python
fp = open('data.txt','w')
fp = open('files/data.txt','w') # the slash might be different in different operating systems
fp.close()
```
<details>
  <summary>
    🔍 Closer look
  </summary>
  fp is a variable and is called file pointer or file object<br>
  open() - is a built-in Python function to open a file<br>
  open takes atleast one required argument, file name (along with full path<br>
  file name must be specified in single or double quotes<br>
  second argument - mode is optional<br>
  if no mode is specified, the file is opened in read mode<br>
  if you want to specify the write mode, you must use "w" inside single or double quotes
</details>

In write mode, if the file doesn't exist Python will create the file 

## a. The write() method
```python
fp = open('states.txt', 'w')
fp.write('Alabama')
fp.write('Alaska')
fp.close()
```

In write mode the read position starts at 0, meaning each time, the data will be overwritten

<details>
  <summary>
    👉 Try this: 6-2a
  </summary>
  Open a file named products.csv in write mode, name the file pointer outfile<br>
  To this file write two values like this<br><br>
  Apples<br>
  Oranges<br><br>
  Close the file
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  
  ```python
  outfile = open("products.csv", "w")
  outfile.write("Apples")
  outfile.write("Oranges")
  outfile.close()
  ```
</details>

## b. Using newline characters (and tab characters)
```python
fp = open('states.txt', 'w')
fp.write('Alabama\tMontgomery\n')
fp.write('Alaska\tJuneau\n')
# or
# fp.write('Alabama\tMontgomery\nAlaska\tJuneau\n')
fp.close()
```
<details>
  <summary>
    💡 Remember
  </summary>
  \n - newline character<br>
  \t - tab character
</details>


## c. Concatenating strings and writing to file
```python
infile = open('states.txt', 'w')
more = "y"
while more != "n":
  state = input("Enter state: ")
  capital = input("Enter capital: ")
  string = state + '\t' + capital + '\n'
  infile.write(string)
  more = input("Do you want to enter more? (y/n): ")
infile.close()
```

<details>
  <summary>
    👉 Try this: 6-2c
  </summary>
  Open a file named states.csv in write mode, name the file pointer of<br>
  Using two input statements, ask user to enter a state and a capital 
  Write those two values like this<br><br>
  Alaska,Juneau<br>
  Close the file
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  of = open("states.csv", "w")
  state = input("Enter state: ")
  capital = input("Enter capital: ")
  string = state + ',' + capital + '\n'
  of.write(string)
  of.close()
  ```
</details>

We can only write string data to file  
So we have to convert other datatypes to strings before we write to the file

## d. Writing other datatypes
Using for loop to write numbers from 1 to 20
```python
file = open('numbers.txt', 'w')
for num in range(1, 21):
  file.write(num) # will give error
  # file.write(str(num)) # we must convert to string
file.close()
```

<details>
  <summary>
    👉 Try this: 6-2b
  </summary>
  To a file named scores.txt write 30 random floats between 50 and 100<br>⏩ Tutorial 5-15e for random number generation
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  import random
  f = open("scores.txt", "w")
  for i in range(30):
    score = random.uniform(50, 100)
    f.write(str(score) + '\n')
  f.close()
  ```
</details>

## e. Writing data in append mode
In append mode
- the file is created if it doesn't exist
- read position starts at the end of the file  
- new data will be appended to old data

**Syntax**: <file_pointer> = open("\<file_name\>", "a")

```python
infile = open('products.txt', 'a')
done = "n"
while done != "y":
  product = input("Enter product: ")
  price = input("Enter price: ")
  string = product + '\n' + price + '\n'
  infile.write(string)
  done = input("Are you done? (y/n): ")
infile.close()
```

<details>
  <summary>
    👉 Try this
  </summary>
  Until the user presses n<br>
  Using three input statements, ask user for student cwid, name, major and gpa
  To a file named students.txt write these values in four separate lines. Open the file in append mode<br>
  # Test your code with these four values<br>
  267898, John Doe, HIST, 3.5
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  
  ```python
  f = open("students.txt", "a")
  more = "y"
  while more != "n":
    cwid = input("Student CWID: ")
    name = input("Student Name: ")
    major = input("Student Major: ")
    gpa = input("Student GPA: ")
    string= cwid + '\n' + name + '\n' + major + '\n' + gpa + '\n'
    f.write(string)
    more = input("Enter more? (y/n): ")
  f.close()
  ```
</details>