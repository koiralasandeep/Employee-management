# 8-10. String splitting

## split() method
split() method uses a delimiter to break a string down into list elements  
If no delimiter is specified, a space character is used as a delimiter

```python
from suchi_pretty_print import suchi_print

# with space as a delimiter
string = "My name is James Watson"
string_to_list = string.split()
suchi_print(string_to_list)

# with comma as a delimiter
string = "James Watson,1008976,COSC,4.0,watson@ulm.edu"
string_to_list = string.split(',')

```

<details>
  <summary>💡 Remember</summary>split() method always returns a list
</details>