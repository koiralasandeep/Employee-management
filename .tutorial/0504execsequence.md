# 5-4. Execution Sequence
A Python program begins at the first statement and executes each statement sequentially  

## a. Using Functions
<details>
  <summary>
    🚩 Remember
  </summary>
  A good practice is to write a Python program in main.py
</details>

- The main() function is defined in main.py  
- Then, the main() function is called  
- All the statements in the program should be inside the main() definition  
- main() function can also call other functions  
- When a function call is encountered, the execution **"jumps to"** the function definition of that function  
- It will execute all the statements until there are no more or until a special keyword **return** is encountered  
- Then the control comes back to the calling function  
Any statement written after a **return** statement will not be executed

<details>
  <summary>
    🤓 Recipe book
  </summary>
  <a href="/.tutorial/cake.jpg">Recipe</a>
</details>

```python
# Write a program to make Recipe 1 from the cake recipe book

# Without functions

print('Chocolate cake with buttercream icing')
print('Prepare the batter')

# Chocolate Batter
print('Beat eggs and butter')
print('Add sugar and beat some more')
print('Mix in flour, chocolate powder and baking powder') 
      
print('Bake the batter at 350o for 30 min')    
print('Prepare icing')

# Buttercream icing
print('Take butter at room temperature')
print('Add powdered sugar and mix them together')

# Vanilla Flavor
print('Split open the vanilla bean')
print('Use the back of the knife to get the seeds out')
print('Crush the seeds to extract the vanilla flavor')

print('Mix in vanilla flavor')

print('Apply icing to cake')

## -----------------------------

# Let's transform the above program to use functions
# Write main function first

```

<details>
  <summary>
  🔎 Closer look
  </summary>
  First the main function is called when Python encounters main()<br>
  The control jumps to the first line inside the main definition<br>
  This prints Chocolate cake with buttercream icing<br>
  Next control goes to the next line, which prints Prepare the batter<br>
  The next line is a function call to chocolate_batter()<br>
  In other words main function is calling chocolate_batter function<br>
  So, the control jumps to the first line of the function body of chocolate_batter<br>
  Which prints Beat eggs and butter<br>
  The control then goes to the next line which prints Add sugar and beat some more<br>
  Then the control goes to the next line which prints Mix in flour, chocolate powder and baking powder<br>
  Since there are no more statements after this, the control jumps to the next line of the calling function (main function)<br>
  The next line after the function call prints Bake the batter at 350o for 30 min<br>
  And the control goes to the next line which prints Prepare icing<br>
  The next line is a function call to buttercream_icing or main is calling buttercream_icing<br>
  So the control jumps to the first line of the function body which prints Take butter at room temperature<br>
  The control moves to the next line which prints Add powdered sugar and mix them together<br>
  In the next line, buttercream_icing is calling the function vanilla_flavor<br>
  So the control jumps to the first line in that function, which prints Split open the vanilla bean<br>
  The control goes to the next line which prints Use the back of the knife to get the seeds out<br>
  The control goes to the next line which prints Crush the seeds to extract the vanilla flavor<br>
  After this there are no more statements to execute, so the control goes back to the calling function, buttercream_icing<br>
  The next line in this function prints Mix in vanilla flavor<br>
  After this, there are no more statements in buttercream_icing, so the control jumps to the calling function, main<br>
  The next line in main prints Apply icing to cake<br>
  There are no more statements in main function, so the programs ends its execution.
</details>

<details>
  <summary>
    Recipe 1 (Chocolate cake with buttercream icing) using functions
  </summary> 
  
  ```python
  def main():
    print('Chocolate cake with buttercream icing')
    print('Prepare the batter')
    chocolate_batter()
    print('Bake the batter at 350o for 30 min')
    print('Prepare icing')
    buttercream_icing()
    print('Apply icing to cake')

  def chocolate_batter():
    print('Beat eggs and butter')
    print('Add sugar and beat some more')
    print('Mix in flour, chocolate powder and baking powder')

  def buttercream_icing():
    print('Take butter at room temperature')
    print('Add powdered sugar and mix them together')
    vanilla_flavor()
    print('Mix in vanilla flavor')

  def vanilla_flavor():
    print('Split open the vanilla bean')
    print('Use the back of the knife to get the seeds out')
    print('Crush the seeds to extract the vanilla flavor')

  main()

  ```
</details>



<details>
  <summary>
  🚩 5-4a. Remember:
  </summary>
  The function definition MUST appear before main() function call<br>
  Cannot use the same function name for two functions defined in the same file
</details>

<details>
  <summary>
  👉 5-4a. Try this
  </summary>
  Write a program to make Recipe 2 from the cake recipe book with functions. Define function(s) as needed
</details>

<details>
  <summary>
  👀 Answer
  </summary>

  ```python
  
  def vanilla_flavor():  # We have already written this function
    print('Split open the vanilla bean')
    print('Use the back of the knife to get the seeds out')
    print('Crush the seeds to extract the vanilla flavor')
  
  def vanilla_batter():
    print('Beat eggs and butter')
    print('Add sugar and beat some more')
    vanilla_flavor()
    print('Mix in flour, vanilla flavor and baking powder')

  def creamcheese_icing():
    print('Take creamcheese and beat it')
    print('Add powdered sugar and beat some more')
    print('Mix in almond flavor')
  
  def main():
    print('Vanilla cake with creamcheese icing')
    print('Prepare the batter')
    vanilla_batter()
    print('Bake the batter at 350 degrees for 30 min')
    print('Prepare icing')
    creamcheese_icing()
    print('Apply icing to cake')
  ```
 
</details>

## b. Functions inside Modules
We can also place our functions in separate files  

For example, all functions related to   
- icings can be placed in icing.py aka icing **module**    
- batter can be placed in batter.py aka batter **module**
  
In such cases, we will have to import the functions in main.py using import statement

```python
# Using import

# Method 1: Using comma separated names to import only the functions we need
from icing import vanilla_icing, creamcheese_icing
from batter import chocolate_batter, vanilla_batter

# Method 2: Using * to import ALL the functions
from icing import *
from batter import *

# Method 3
import icing
import batter
# In this method, the function call will have a prefix of the filename it is located in

# For example:
icing.vanilla_icing()
batter.chocolate_batter()
```

[Check out recipes using modules](https://replit.com/@SuchiRodda/Modules)
