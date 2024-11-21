# 7-31. Tuples: for loop

## a. Loop through just tuple element values
Syntax: for <loop_variable> in <tuple_name>:
```python
programming_languages = ("JavaScript", "Python", "Java", "C++")
for language in programming_languages:
  print(language)
```

<details>
  <summary>
    🔍 Close Look:
  </summary>
  Second line has the for loop going over the tuple<br>
  Python will read it as, "As long as there are elements in the tuple keep going"<br><br>
  
  The first time for loop executes, it prints the first element - Javascript<br>
  And checks, are there more elements? YES!<br><br>
  Then it loops again, and this time it prints the second element - Python<br>
  And checks, are there more elements? YES!<br><br>
  Then it loops again, and this time it prints the third element - Java<br>
  And checks, are there more elements? YES!<br><br>
  Then it loops again, and this time it prints the fourth element - C++<br>
  And checks, are there more elements? NO!<br><br>
  So it stops and program execution ends<br>
</details>

<details>
  <summary>
   👉 Try this: 7-31
  </summary>
Use a for loop to print each element of the tuple<br>
employee = ("28678", "Bob Singer", "HR", [90, 95, 67], ["Manager", "Supervisor", "Team Leader"])
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

```python
for value in employee:
  print(value)
```

I have used value as my variable name, you may choose any name as long as the list name is correct
</details>


## b. Loop through tuple element values and indexes
Syntax: for <index_name>, <value_name> in enumerate(<tuple_name>):

```python
programming_languages = ("JavaScript", "Python", "Java", "C++")
for index, language in enumerate(programming_languages):
  print(index, '->', language)
```

<details>
  <summary>
   👉 Try this: 
  </summary>
Use a for loop to print each element and its index<br>
employee = ("28678", "Bob Singer", "HR", [90, 95, 67], ["Manager", "Supervisor", "Team Leader"])
</details>

<details>
  <summary>
   👀 Answer 
  </summary>

```python
for idx, value in enumerate(employee):
  print(idx, '->', value)
```

I have used idx and value as my variable names, you may choose any names as long as the list name is correct
</details>
