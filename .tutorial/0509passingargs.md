# 5-9. Passing Arguments to Functions

Sometimes it is useful not only to call a function, but also to send one or more pieces of data into the function<br>
Pieces of data that are sent into a function are known as **arguments**<br>
The function can use its arguments in calculations or other operations<br>

```python
def show_double(number):
 result = number * 2
 print(result)

def main():
  value = 5
  show_double(value)

main()
```

<details>
  <summary>
    🔎 Closer look
  </summary>
  When this program runs, the main function is called<br>
  Inside the main function definition<br>
  a local variable named value created and assigned the integer value 5<br>
  Then the show_double function is called, with value in parantheses<br>
  Or, in correct words, show_double function is called with value as an argument<br>
  In the show_double function definition, the number variable will be assigned the same value as the value variable<br>
  Then a local variable named result is assigned the value of the expression number * 2<br>
  Because number references the value 5, this statement assigns 10 to result.<br>
  Then the result variable is displayed
</details>

## Passing multiple values
If you want to pass more arguments, you can do so by using comma separated variables in the function call  
Also, you must accept the same number of comma separated variables in the function defintion  
These two sets of variables may or may not have the same names  
The first argument is passed to the first parameter variable, the second argument is passed to the second parameter variable and so on
 
<details>
  <summary>
    🚩 To remember
  </summary>
  The variables inside the parantheses in a function call are called arguments or argument list<br>
  The variables inside the parantheses in a function definition are called parameters or parameter list<br>
  The number of arguments and parameters MUST match
</details>


<details>
  <summary>
    👉 Try this
  </summary>
  Define a function called create_multiple which accepts two paramters named, number and multiple<br>
  Inside the function body,<br>
  1. Create a local variable named resultant and assign it a value of expression number times multiple<br>
  2. Print the resultant variable
</details>


<details>
  <summary>
    👀 Answer
  </summary>
  def create_multiple(number, multiple):<br>
  &ensp;resultant = number * multiple<br>
  &ensp;print(resultant)
</details>


<details>
  <summary>
    👉 Try this
  </summary>
  In main() definition<br>
  1. Assign a local variable called n a value entered by the user input converted to integer<br>
  2. Assign another local variable called m, a value entered by the user input converted to integer<br>
  3. Call the create_multiple function with the arguments n and m in that order<br>
  4. Outside main() definition call the main() function
</details>


<details>
  <summary>
    👀 Answer
  </summary>
  def main():<br>
  &ensp;n = int(input("Enter number: "))<br>
  &ensp;m = int(input("Enter multiple: "))<br>
  &ensp;create_multiple(n, m)<br><br>
  main()
</details>