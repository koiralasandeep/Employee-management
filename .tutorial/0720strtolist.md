# 7-20. Conversion - Strings and Lists

## String to List:

Syntax: \<list_name> = \<string>.split([\<delimiter_string\>])
## a. Without Using delimiter

```python
string1 = "Hello World"
list1 = string1.split()
suchi_print(list1)
```

## b. Using delimiter

```python
string1 = "1001,David Collins,HIST,3.79"
list1 = string1.split(",")
suchi_print(list1)
```

## c. List to String

Why convert list to a string?  
- In the case of storing or transmitting data, it is better to do it in the form of a string rather than a list.
- In the case of printing output to the console or a file, you have to format the data in a particular way. When we convert a list to a string, we can easily format the output using string manipulation techniques.
- Some libraries or APIs require data to be passed as a string instead of a list. In these cases, you have to convert your list to a string before passing it to the library or API.
  
```python
employee = ["1001", "David Collins", "HIST", "3.79"]
my_string = ",".join(employee)
```