## Python User Input

To take user input in Python, we can use the `input()` function. Here's the syntax:

```python
input_string = input("Please enter a value: ")

```

The `input()` function takes an argument which is the prompt string. The user is prompted to enter a value, and this value is returned as a string.

To take integer input, we can use the `int()` function to convert the string input to an integer. Here's an example:

```python
input_string = input("Please enter an integer: ")
integer_input = int(input_string)

```

To take decimal input, we can use the `float()` function to convert the string input to a float. Here's an example:

```python
input_string = input("Please enter a decimal: ")
decimal_input = float(input_string)

```

## Control structures

In Python, control structures are used to control the flow of a program.

 The selection control structure is implemented using the `if`, `elif`, and `else` statements, which allow the program to execute different blocks of code depending on the condition. 

The repetition control structure is implemented using the `while` and `for` loops, which allow the program to execute a block of code multiple times. 

Additionally, the `break` and `continue` statements are used to control the flow of the loops, allowing the program to exit the loop or skip an iteration based on the specified condition. Understanding these control structures is essential to writing effective and efficient Python code.

### Selection Control

In Python, we can use the `if`, `elif`, and `else` statements to implement selection control. Here's the syntax:

```python
if condition:
    # code to be executed if condition is true
elif condition2:
    # code to be executed if condition2 is true
else:
    # code to be executed if both condition and condition2 are false

```

The `elif` block can be repeated as many times as needed to handle all possible conditions.

### Repetition Control

In Python, we can use the `while` and `for` loops to implement repetition control. Here's the syntax for each:

```python
# while loop
while condition:
    # code to be executed while condition is true

# for loop
for variable in iterable:
    # code to be executed for each element of iterable

```

The `while` loop will continue to execute as long as the condition is true. The `for` loop will iterate over each element of the iterable object.

### Breaks and Continues

In Python, we can use the `break` and `continue` statements to control the flow of loops. Here's the syntax:

```python
# break statement
while condition:
    if some_condition:
        break

# continue statement
for variable in iterable:
    if some_condition:
        continue
    # code to be executed if some_condition is false

```

The `break` statement will immediately exit the loop when it is encountered. The `continue` statement will skip the current iteration of the loop and move on to the next one.