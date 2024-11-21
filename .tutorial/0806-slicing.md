# 8-6. String Slicing

## a. Using List slicing method
Just like lists we can slice strings

Syntax: <string_name>[\<start\>:\<stop\>:\<step\>]

```python
string = "ULM Rocks!"
slice = string[:3]

```
<details>
  <summary> 
    👉 Try this:
  </summary>

In the string given in the code below:
- the first 7 chars is CWID
- next 50 is name
- next 4 is major
- next 4 is gpa
Can you get all of data elements in a comma separated string?
It should output -  <code>4231560,Wes Kinney,COSC,4.00</code>
```python
string = "4231560                    Wes Kinney                    COSC4.00"
```
</details>

<details>
  <summary>
    👀 Answer: 
  </summary>

```python
cwid = string[:7] # To get the first 7 characters
name = string[7:57].strip() # Get 8th to 56th character, and remove the spaces
major = string[57:61]
gpa = string[61:]
joined_string = cwid + "," + name + "," + major + "," + gpa
print(joined_string)

# or, do all the above in one statement
# print(string[:7] + "," + string[7:57].strip() + "," + string[57:61] + "," + string[61:])
  ```
</details>


<details>
  <summary>💡 Remember</summary>If you try to access an index that doesn't exist, Python will raise an exception
</details>


## b. Using slice() method
```python
string = "ULM Rocks!"
s1 = slice(0,3)
slice = string[s1]
```
