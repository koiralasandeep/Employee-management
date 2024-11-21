# 7-24. List Slicing

A slicing expression selects a range of elements from a sequence.  

A slice is a span of items that are taken from a sequence.  

General synatx: \<slice_name\> = \<list_name\>[\<start\>:\<end\>:\<step\>]  

A slice from a list will be a list

```python
january_sales_data = [540.26, 626.09, 550.08, 600.26, 761.85, 707.5, 802.65, 736.12, 838.17, 857.73, 518.97, 826.85, 919.85, 555.68, 767.36, 754.61, 795.04, 776.61, 773.46, 975.42, 614.68, 808.86, 905.62, 617.78, 881.28, 767.0, 927.12, 506.16, 611.36, 992.22, 893.3]

# To get all data

print(january_sales_data[:])

# To get only first week data

print(january_sales_data[:7])

```

## Get student id slice
Consider another example where we read a file data of student records into a list and just get the student id slice

```python
from suchi_pretty_print import suchi_print
def main():
  try:
    f = open("data/students.txt", "r")
  except:
    print("File not found")
  else:

    students = []  # first create an empty list
    for line in f: # Use a for loop to go over file lines
      line = line.rstrip("\n") # remove the newline character
      students.append(line) # add each line to the end of the list
    suchi_print(students)

    # to get just the student ids, we get a slice
    id_slice = students[0::4]
    suchi_print(id_slice)

    # using this slice, we can also calculate the next student id

if __name__ == "__main__":
  main()

```

<details>
  <summary>
    🚩 To remember:
  </summary>
  Invalid indexes do not cause slicing expressions to raise an exception.<br>

  If the end index specifies a position beyond the end of the list, Python will use the length of the list instead.<br>

  If the start index specifies a position before the beginning of the list, Python will use 0 instead.<br>

  If the start index is greater than the end index, the slicing expression will return an empty list.<br>
</details>


<details>
  <summary>
  👉 Try this: 7-24 
  </summary>
  Print the slice that has elements Wednesday and Thursday<br>
  <code>weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]</code>
</details>

<details>
  <summary>
  👀 Answer 
  </summary>
  print(weeks[3:5])
</details>