# Python Collections and Functions README

## Collections in Python

Python provides several data structures to store collections or multiple items in a single variable. In this course, we will focus on two of these: **Lists** and **Dictionaries**.

### Lists

Lists in Python are similar to arrays in other programming languages. They can contain a collection of data and allow access to elements by their index.

To create a list, use square brackets `[]`. Here are some examples:

```python
names = ["John", "Paul", "George", "Ringo"]
programs = ['developer career', 'pi-shape', 'courses']
durations = [260, 180, 20]
truth_values = [True, False, True, True, False]
sample_list = ["Apple", 3, False, "Potato", 4, True]
```

You can access list elements using their index:

```python
print(names[2])  # Accessing the third element "George"
```

You can also access the last element of a list using the `len` method:

```python
print(names[len(names) - 1])  # Accessing the last element "Ringo"
```

To access a range of values, use slicing:

```python
print(names[0:3])  # Accessing elements from index 0 to 2
```

Lists have methods for manipulation, such as `append`, `del`, `in`, and `sort`. For example:

```python
durations.append(301)  # Add 301 to the end of the durations list
del durations[1]       # Delete the element at index 1
print(20 in durations) # Check if 20 is in the list
names.sort()           # Sort the names list alphabetically
```

### Dictionaries

Dictionaries are used to store key-value pairs. They are similar to objects in other programming languages.

Here's an example of a dictionary:

```python
person1 = {
    "name": "Brandon",
    "age": 28,
    "occupation": "student",
    "isEnrolled": True,
    "subjects": ["Python", "SQL", "Django"]
}
```

You can access values in a dictionary by specifying the key:

```python
print(person1["isEnrolled"])    # Accessing the value associated with the key "isEnrolled"
print(person1["subjects"])      # Accessing a list value in the dictionary
print(person1["subjects"][1])   # Accessing the second element of the subjects list
```

Dictionaries also have methods like `keys()`, `values()`, `items()`, `update()`, `pop()`, `del`, and `clear` for various operations.

## Functions in Python

Functions are blocks of code that execute when called. They can take parameters and return values.

Here's an example of defining and using a function:

```python
def my_greeting():
    print("Hello User!")

my_greeting()  # Calling the function
```

You can define functions with parameters and return values:

```python
def greet_user(username):
    print(f"Hello {username}!")

greet_user('benup')
```

Functions can also use the `return` keyword to return values:

```python
def addition(num1, num2):
    return num1 + num2

sum = addition(5, 10)
print(f"The sum is {sum}")
```

### Lambda Functions

Lambda functions are small anonymous functions that can be used for simple tasks. They are defined using the `lambda` keyword and can take any number of arguments but have only one expression.

Here's an example:

```python
multiply = lambda a, b: a * b
print(multiply(3, 2))  # Output: 6
```

## Classes and Objects

In Python, classes serve as blueprints to describe the concept of objects. Each object has properties and behaviors. You can create classes and instantiate objects from them.

Here's an example of defining a `Car` class:

```python
class Car:
    def __init__(self, brand, model, year_of_make):
        self.brand = brand
        self.model = model
        self.year_of_make = year_of_make
        self.fuel = "Gasoline"
        self.fuel_level = 20

    def fill_fuel(self):
        print(f"Current fuel level: {self.fuel_level}")
        print("Filling up the fuel tank...")
        self.fuel_level = 100
        print(f"New fuel level: {self.fuel_level}")

new_car = Car('Nissan', 'GT-R', 2019)
print(f"My car is {new_car.brand} {new_car.model}")
new_car.fill_fuel()
```

This README covers the basics of collections, functions, lambda functions, and classes in Python. It serves as a reference for the concepts and code examples presented in the course.