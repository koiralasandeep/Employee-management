# 2-17. Formatting with F-strings
F-string is a special type of string literal that allow you to format values in a variety of ways in a print statement  
By using **f**, short for format, and curly braces, **{ }**, we can print the value of the variable

## a. Placeholder Values
```python
name = "John Smith"
print(f'My name is: {name}')
```

<details>
  <summary>
    🚩 To remember
  </summary>
  {name} is called a placeholder for the value of name
</details>

<details>
  <summary>
    👉 2-17a. Try this
  </summary>
  Write one print statement to display<br>
  Name: John Smith<br>
  Major: CINS<br><br>
  name = "John Smith"<br>
  major = "CINS"<br>
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print(f'Name: {name}\nMajor: {major}')
</details>

## b. Placeholder Expressions
We can also use expressions inside {}

```python
num = 80
print(f'The square of {num} is: {num ** 2})
```

<details>
  <summary>
    👉 2-17b. Try this
  </summary>
  Using placeholder expressions<br>
  Print the remainder the given number when divided by 7<br>
  It should display:<br><br>
  The remainder of 80/7 is 3<br><br>
  num = 80
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print(f'The remainder of {num}/7 is {num%7}')
</details>

## c. Formatting Values - Precision

**Syntax:** {<variable_name>: .\<number-of-decimals>f}  

- We can use the . as format specifier to round float varaibles  
- The number following the . specifies desired digits after the decimal places  
- The f after that specifies that it is a float

```python
my_float = 587435684235 / 63

print(f'Unformatted float: {my_float}')

# To format a float to two decimal points
print(f'Formatted float: {my_float: .2f}')
```

<details>
  <summary>
    👉 2-17c. Try this
  </summary>
  Format the float to three decimal points<br>
  The output should be<br><br>
  Three decimal point float:  9324375940.238<br><br>
  my_float = 587435684235 / 63
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print(f'Three decimal point float: {my_float: .3f}')
</details>


## d. Formatting Values - Comma
We can insert comma separators for accounting numbers by using the , specifier  
**Syntax:** {<variable_name> : ,}

```python
my_float = 587435684235 / 63

print(f'Unformatted float: {my_float}')
print(f'Comma formatted float: {my_float: ,}')
```

### Using both specifiers - precisiona and comma
```python
# To format a float to two decimal points and comma separator

print(f'Comma formatted float: {my_float: ,.2f}')
```

<details>
  <summary>
    👉 2-17d. Try this
  </summary>
  Format the above float to comma separated and with no decimal point<br>
  The output should be<br><br>
  Sales revenue: $ 9,324,375,940
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print(f'Sales revenue: $ {my_float : ,.0f}')
</details>

## e. Formatting Values - Type

| Type Character | Effect |
| ---------- | ------ |
| d or D |  Causes text to be formatted as integer |
| f |  Causes text to be formatted as float |
| % | Causes text to be formatted as a percentage |
| e | Causes text to be formatted in scientific notation |

### 1. Formatting integers
So far we have seen formatting floats  
We can format integers using the d or D designator  

```python
number_of_people = 452302

# To format an integer
print(f'Number of people: {number_of_people:d}')
```

<details>
  <summary>
    🚩 To remember
  </summary>
  When we use d or D, we cannot user the . (precision) designator
</details>


<details>
  <summary>
    👉 2-17e1. Try this
  </summary>
  Write a print statement to format<br>
  the number of people with comma separation<br>
  The output should be<br><br>
  Number of people: 452,302<br><br>
  number_of_people = 452302
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print(f'Number of people: {number_of_people: ,d}')
</details>

### 2. Formatting as a percentage
We use **%** as format specifier to display a float as a percentage
```python
  my_float = 0.25

  # To format a float as a percentage
  print(f'Formatted float: {my_float: %}')

  # To format a float as a percentage with 0 decimal places
  print(f'Formatted float: {my_float: .0%}')

```

<details>
  <summary>
    👉 2-17e2. Try this
  </summary>
  Write a print statement to format
  the given float as a percentage with 1 decimal place<br><br>
  interest_rate = 0.25
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  print(f'{interest_rate: .1%}')
  ```
</details>


### 3. Formatting in scientific notation
We use **_e_** to specify the scientific notation 

```python
number_of_stars = 456987123023155

# To format a float using scientific notation
print(f'Number of stars: {number_of_stars: e}')
```

<details>
  <summary>
    👉 2-17e3. Try this
  </summary>
  Write a print statement to format<br>
  as a scientific notation with 2 decimal places<br>
  The output should be<br><br>
  Number of stars:  4.57e+14<br><br>
  number_of_stars = 456987123023155
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  
  ```python
  print(f'Number of stars: {number_of_stars: .2e}')
  ```
</details>

## f. Formatting Values - Width
**Syntax:** {<variable_name : <number_of_characters_side>}  
No specifier, we simply put a number after the :   
That will format the placeholder to span that many characters  

```python
product = "Sony TV"
sales = 568495.5638

# To format the variable to span 20 characters
print(f'{product}: {sales: 20}')
```

### Multiple specifiers: width and precision

```python
product = "Sony TV"
sales = 568495.5638

# To format sales to span 20 characters and two decimal places
# Notice the \t for tab space
print(f'{product}\t{sales: 20.2f}')

```

<details>
  <summary>
    👉 2-17f. Try this
  </summary>
  Write a print statement to<br>
  Print the product name and a colon<br>
  Format the float to span across 30 characters<br>
  with 3 decimal places and comma<br>
  The output should be<br><br>
  Sony TV &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;568495.5638<br><br>
  product = "Sony TV"<br>
  sales = 568495.5638
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  print(f'{product}\t{sales: 30,.3f}')
  ```
</details>

## g. Formatting Values - Alignment
We can use the >,<,^ specifiers to get right, left and center aligned data, respectively  

**Syntax:** {<variable_name> : <alignment_specifier>\<width>}
<details>
  <summary>
    🚩 To Remember
  </summary>
  When using alignment specifier width MUST be specified
</details>


| Alignment Character | Effect |
| ---------- | ------ |
| ^ |  Causes text to be center aligned |
| < |  Causes text to be left aligned |
| > | Causes text to be right aligned |

```python
my_float = 568495.5698

# To format a float to right align across 20 characters
print(f'Right-aligned float: {my_float: >20}')

```

<details>
  <summary>
    💡 2-17g. Note
  </summary>
  If width is specified alignment is not, then float or integer defaults to right
</details>


<details>
  <summary>
    👉 2-17g. Try this
  </summary>
  Write a print statement to<br>
  format the following float to <br>
  center align across 30 characters<br>
  print only two decimal places<br>
  and as a percentage<br>
  The output should be:<br><br>
  The percentage is:&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;84.24% <br><br>
  this_percentage = 0.842365
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  print(f'The percentage is: {this_percentage: ^30.2%}')
  ```
</details>



<details>
  <summary>
    👉 2-17g-2. Try this
  </summary>
  Given products and sales values below<br>
  Write two print statements to display the following<br>
  1. product name right aligned spanning 20 characters<br>
  2. a tab character, a colon, a space and $ symbol<br>
  3. the sales value right aligned spanning 15 characters
      comma separated, with no decimal places<br>
  The output should be<br><br>
               Sony TV&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;: $&ensp;&ensp;&ensp;568,496<br>
            Samsung TV&ensp;&ensp;&ensp;: $&ensp;&ensp;&ensp;425,678<br><br>
  product1 = "Sony TV"<br>
  sales1 = 568495.5638<br>
  product2 = "Samsung TV"<br>
  sales2 = 425678.2145<br>
</details>

<details>
  <summary>
    👀 Answer
  </summary>
  print(f'{product1 : >20}\t: ${sales1 : >15,.0f}')<br>
  print(f'{product2 : >20}\t: ${sales2 : >15,.0f}')
</details>

## h. Order of Designators
When using multiple designators in a format specifier, we have to use the correct order  
The order is [alignment </>/^] [width] [,] [.precision] [type d/e/f/%]  

<details>
  <summary>
    🤓 2-17h. To remember
  </summary>
  You may use the mnemonic<br><br>
  Andy Was Clearly Preoccupied Today<br><br>
  A - alignment<br>
  W - width<br>
  C - comma<br>
  P - precision<br>
  T - type
</details>

## i. Concatenation with F-strings
We can concatenate multiple f-strings in a single print statement
We can use + or a space

#### For example
In our previous example:  
We wrote TWO print statements to get the output  
Sony TV&ensp;&ensp;&ensp;&ensp;: $&ensp;&ensp;&ensp;&ensp;&ensp;568,496  
Samsung TV: $&ensp;&ensp;&ensp;&ensp;&ensp;425,678

Instead, we can write one print statement by simply using +
 ```python
product1 = "Sony TV"
sales1 = 568495.5638
product2 = "Samsung TV"
sales2 = 425678.2145

print(f'{product1 : >20}\t: ${sales1 : >15,.0f}\n'
      +
      f'{product2 : >20}\t: ${sales2 : >15,.0f}')
```

<details>
  <summary>
    👉 2-17i. Try this
  </summary>
  Given<br> 
  name1 = "Jon Snow"<br>
  major1 = "ACCT"<br>
  gpa1 = 3.54897<br>
  email1 = "snow@ed.edu"<br>
  name2 = "David Willis"<br>
  major2 = "HIST"<br>
  gpa2 = 3.858812<br>
  email2 = "willis@ed.edu"<br>
  Print the data in a tabular fashion like this<br><br>

  |        Name         | Major  |  GPA   |        Email        |
  |---------------------|--------|--------|----------------------|
  |Jon Snow             |  ACCT  |   3.54 | snow@ed.edu         |
  |David Willis         |  HIST  |   3.85 | willis@ed.edu        |

  Format as follows<br>
  name left aligned over 20 characters<br>
  major center aligned over 6 characters<br>
  gpa right aligned over 6 characters, rounded to two decimal points<br>
  email left aligned over 20 characters<br>
  
</details>

<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  print(f'{"Name": ^20}', f'{"Major": ^6}', f'{"GPA": ^6}', f'{"Email": ^20}', sep = ' | ') # header row<br>
  print("-" * 62) # line under the header, hyphen printed 62 times<br>
  print(f'{name1: <20}', f'{major1: ^6}', f'{gpa1: >6.2f}', f'{email1: <20}', sep = ' | ') # first data row<br>
  print(f'{name2: <20}', f'{major2: ^6}', f'{gpa2: >6.2f}', f'{email2: <20}', sep = ' | ') # second data row
  ```
</details>