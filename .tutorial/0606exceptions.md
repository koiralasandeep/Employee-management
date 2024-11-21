# 6-6. Exceptions
An exception is an error that occurs while a program is running  
In most cases, an exception causes a program to abruptly halt  
For example:


```python
def main():
  cookies = int(input('Enter number of cookies: '))
  people = int(input('Enter number of people: '))
  cookies_per_person = cookies/people
  
main()
```

<details>
  <summary>
    🔎 Closer look:
  </summary>
  The above code is syntactically and semantically correct<br>
  When you execute it and enter, say 10 cookies and 4 people<br>
  The program output is 2.5<br>
  But if you enter 10 cookies and 0 people<br>
  Then the program abruptly halts with mesage called "traceback" specifying that it is a "ZeroDivisionError"<br>
  Such errors happen only at run-time and are called Exceptions<br>
  There are many different types of exceptions<br>
  For example instead of a numeric value enter an alphabetic value for cookies or peopl<br>
  That causes a "ValueError" exception because we just tried to convert a string to int
</details>

A good programmer must prevent exceptions from being raised by careful coding.  
In the above program to prevent ZeroDivisionError, we can place an if statement.


```python
def main():
  cookies = int(input('Enter number of cookies: '))
  people = int(input('Enter number of people: '))
  if people > 0:
    cookies_per_person = cookies/people
  else:
    print("Invalid value for people, must be more than 0")

main()
```

But some exceptions cannot be avoided regardless of how carefully we write our program  
For example we cannot avoid the ValueError  
Python allows us to write code that responds to exceptions when they are raised  
Such code is called an exception handler and is written with the **try/except** statement  

There are several ways to write a try/except statement, but the following general format shows the simplest variation

## a. try/except statement

```python
try:
  # statement
  # statement
  except <Exception_Name>:
  # statement
```

<details>
  <summary>
    🔎 Closer look:
  </summary>
  First, the keyword try appears, followed by a colon<br>
  Next, a code block appears called the try suite<br>
  The try suite is one or more statements that can potentially raise an exception<br>
  After the try suite, an except clause appears<br>
  The except clause begins with the keyword except, optionally followed by the name of an exception, and ending with a colon<br>
  Beginning on the next line is a block of statements that is called a handler<br>
  When the try/except statement executes, the statements in the try suite begin to execute<br>
  The following describes what happens next:<br><br>

  If a statement in the try suite raises an exception that is specified by the ExceptionName in an except clause, then the handler that immediately follows the except clause executes. Then, the program resumes execution with the statement immediately following the try/except statement<br><br>

  If a statement in the try suite raises an exception that is not specified by the ExceptionName in an except clause, then the program will halt with a traceback error message<br><br>

  If the statements in the try suite execute without raising an exception, then any except clauses and handlers in the statement are skipped, and the program resumes execution with the statement immediately following the try/except statement
</details>

```python
try:
  fp = open('suchi.txt', 'r') # can potentially raise exception because this file doesn't exist, so place it in the try suite
  contents = fp.read()
  print(contents)
  fp.close()
except FileNotFoundError: # this handler handles the case when the file doesn't exist
  print("File doesn't exist")

```

## b. Handling Multiple Exceptions

```python
def main():
  try: # the three statements below can potentially raise exception(s), so place them in the try suite
    cookies = int(input('Enter number of cookies: '))
    people = int(input('Enter number of people: '))
    cookies_per_person = cookies/people
    print(f"Each person gets {cookies_per_person} cookies")
  except ZeroDivisionError: # this handler handles the case when people = 0
    print("Invalid value for people, cannot be 0")
  except ValueError: # this handler handles the case when cookies or people is not numeric
    print("Enter valid numeric value for cookies and people")

  # This statement executes whether or not an exception is raised
  print(f"Done with everything")

main()
```

<details>
  <summary>
    🚩 To remember:
  </summary>
  A try/except statement gracefully responds to exceptions
</details>

## c. Using One except Clause to Catch All Exceptions

```python
def main():
  try:
    cookies = int(input('Enter number of cookies: '))
    people = int(input('Enter number of people: '))
    cookies_per_person = cookies/people
    print(f"Each person gets {cookies_per_person} cookies")
  except: # generic handler
    print("An error occured")

main()
```

## d. Displaying an Exception’s Default Error Message

If you want to have just one except clause to catch all the exceptions that are raised in a try suite, you can specify Exception as the type

```python
def main():
  try:
    cookies = int(input('Enter number of cookies: '))
    people = int(input('Enter number of people: '))
    cookies_per_person = cookies/people
    print(f"Each person gets {cookies_per_person} cookies")
  except Exception as err: # storing the exception info in a variable called err
    print("An error occured", err)

main()
```

## e. The else clause

The try/except statement may have an optional else clause, which appears after all the except clauses. Here is the general format of a try/except statement with an else clause:

The block of statements that appears after the else clause is known as the else suite. The statements in the else suite are executed after the statements in the try suite, only if no exceptions were raised. If an exception is raised, the else suite is skipped

```python
try:
    statement
    statement
    etc.
 except ExceptionName:
    statement
    statement
    etc.
 else:
    statement
    statement
    etc.
```


```python
def main():
  try:
    cookies = int(input('Enter number of cookies: '))
    people = int(input('Enter number of people: '))
    cookies_per_person = cookies/people
  except Exception as err: # storing the exception info in a variable called err
    print("An error occured", err)
  else:
    print(f"Each person gets {cookies_per_person} cookies")

main()
```

## f. The finally Clause
The try/except statement may have an optional finally clause, which must appear after all the except clauses. Here is the general format of a try/except statement with a finally clause:

```python
try:
    statement
    statement
    etc.
except ExceptionName:
  statement
  statement
  etc.
finally:
  statement
  statement
  etc.
```

The block of statements that appears after the finally clause is known as the finally suite. The statements in the finally suite are always executed after the try suite has executed, and after any exception handlers have executed. The statements in the finally suite execute whether an exception occurs or not. The purpose of the finally suite is to perform cleanup operations, such as closing files or other resources. Any code that is written in the finally suite will always execute, even if the try suite raises an exception.


```python
try:
  fp = open('suchi.txt', 'r')
except Exception as err: # executes only if exception is raised
  print(err)
else: # executes only if no exception is raised
  contents = fp.read()
  print(contents)
  fp.close()
finally: # executes whether or not exception is raised
  print("Done with everything")
```