# 6-5. Processing Records
A record is a complete set of data about an item, and a field is an individual piece of data within a record.  
For example:  

267898  
John Doe  
HIST  
3.5  

All four lines together is a student record, and each line is called a field

## a. Adding data to a record
If we want to add another record, we have to add four lines with a newline after each line  

```python
f = open("students.txt", "a")
cwid = input("Student CWID: ")
name = input("Student Name: ")
major = input("Student Major: ")
gpa = input("Student GPA: ")
f.write(name + '\n' + major + '\n' + gpa + '\n')
f.close()  
```

<details>
  <summary>
    👉 Try this: 6-5a
  </summary>
  In a while loop keep adding student records in the above format, until user doesn't want to add any more. Choose your loop variable and exit condition for the while loop
</details>

<details>
  <summary>
    👀 Answer:
  </summary>

  ```python
  f = open("students.txt", "a")
  done = "n"
  while done != "n":
    cwid = input("Student CWID: ")
    name = input("Student Name: ")
    major = input("Student Major: ")
    gpa = input("Student GPA: ")
    f.write(name + '\n' + major + '\n' + gpa + '\n')
    done = input("Enter more? (y/n): ")
  f.close()  
  ```  
</details>


## b. Looking up
If we want to search the student record for a given cwid, we must check every fourth line and match it with the user entered cwid  
We can use a for loop to go over the lines in the file  
But for loop goes over every line, so we must skip three lines

```python
user_input = input("Enter CWID to lookup: ")
found = False # Let's assume we won't find the student in the file
f = open("students.txt", 'r')
for each_line in f:
  stu_id = each_line
  name = f.readline().rstrip('\n') # we read the next line to get the name and remove the newline character
  major = f.readline().rstrip('\n') # we read the next line to get the major and remove the newline character
  gpa = f.readline().rstrip('\n') # we read the next line to get the gpa and remove the newline character
  if stu_id.rstrip("\n") == user_input:
    print("Name:",name)
    print("Major:", major)
    print("GPA:", gpa)
    found = True
    break # we found what we are looking for, so stop reading the file

# outside the for loop
f.close()
if found == False:
  print("Student Not Found")
```

<details>
  <summary>
    🔍 Closer look
  </summary>
  We open the file in read mode because we are just looking up data<br>
  When we use a for loop over a file pointer, the loop variable stores each line<br>
  when the for loop starts, the first line has the cwid so we strip newline character and store in cwid variable<br>
  since we know the next line is the name, we use the readline() method to get that value and strip the newline character from it<br>
  the next line is the major, we use the readline() method to get that value and strip the newline character from it<br>
  the next line is the gpa, we use the readline() method to get that value and strip the newline character from it<br>
  we check if the cwid from the file matches the user entered cwid<br>
  if it matches, we print the name, major and gpa<br>
  break statement stops the for loop from executing any further<br>
  if match is not found, the loop continues to execute<br>
  and since we have already read the gpa, the next line will be stored in the loop variable (which is the cwid)<br>
  and the process repeats until a break statement is encountered or all the lines in the file are read
</details>

## c. Displaying
To display all the data in a tabular format
```python
f = open("students.txt", 'r')
for each_line in f:
  stu_id = each_line.rstrip("\n")
  name = f.readline().rstrip('\n') # we read the next line to get the name
  major = f.readline().rstrip('\n') # we read the next line to get the major
  gpa = f.readline().rstrip('\n') # we read the next line to get the gpa
  print(f'{stu_id : ^8} | {name: <20} | {major: ^6} | {gpa: >5} |')
  
f.close()
```

## d. Modifying
Modifying any data in a record involves both reading from and writing to the file  
Since we don't have a file open mode to do both, we read from one file and write to another file
For example, if you want to modify the name of a student  
First you open the students file in a read mode  
Open another temporary file in write mode  
Ask the user to give the CWID of the student whose name needs to be modified   
Using the for loop, we will try to find that CWID in the first record,  
If that CWID is Not found, we write the whole record to a new file without making any changes  
If the cwid is found, then we ask the user to provide the new name  
Now we will write the old cwid, new name, old major and old gpa to the new file  
Outside the for loop, close both the input file and output file  
Using the os module, delete the students file and rename the temporary file to students file
```python
import os
user_input = input("Enter student ID: ")

infile = open("students.txt", 'r')
outfile = open("temp.txt", "w")
for stu_id in infile:
  name = f.readline()
  major = f.readline()
  gpa = f.readline()
  if stu_id.rstrip('\n') != user_input:
    outfile.write(stu_id + name + major + gpa)
  else:
    new_name = input("Enter new name: ")
    outfile.write(stu_id + new_name + "\n" + major + gpa)
infile.close()
outfile.close()

os.remove("students.txt")
os.rename("temp.txt", "students.txt")
```

## e. Deleting
To delete a student (4 lines from the file)
Deleting a record involves both reading from and writing to the file  
Since we don't have a file open mode to do both, we read from one file and write to another file
First you open the students file in a read mode  
Open another temporary file in write mode  
Ask the user to give the CWID of the student who needs to be deleted   
Using the for loop, we will try to find that CWID in the first record,  
If that CWID is Not found, we write the whole record to a new file  
If the cwid is found, then skip writing that entire record to the new file  
Outside the for loop, close both the input file and output file  
Using the os module, delete the students file and rename the temporary file to students file
```python
import os
user_input = input("Enter Student ID to delete: ")

infile = open("students.txt", 'r')
outfile = open("temp.txt", "w")
for stu_id in f:
  if stu_id.rstrip('\n') != user_input:
    outfile.write(stu_id + f.readline() + f.readline() + f.readline())
infile.close()
outfile.close()

os.remove("students.txt")
os.rename("temp.txt", "students.txt")
```