## Object-Oriented Programming Concepts in Python

This project illustrates the fundamental Object-Oriented Programming (OOP) concepts in Python: encapsulation, inheritance, and polymorphism. We'll use a simple example of a `Vehicle` class and its subclasses to demonstrate these concepts.

### Encapsulation

Encapsulation is the concept of hiding an object's internal state and requiring access through defined methods. In Python, this is typically achieved using private attributes and getter/setter methods.

```python
# vehicle.py

class Vehicle:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    # Getter methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    # Setter methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model
```

### Inheritance

Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass). In our example, we have a `Car` class and a `Motorcycle` class that inherit from the `Vehicle` class.

```python
# vehicle.py continued

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

class Motorcycle(Vehicle):
    def __init__(self, make, model, engine_size):
        super().__init__(make, model)
        self.engine_size = engine_size
```

### Polymorphism

Polymorphism is the ability to present the same interface for different data types. In Python, it's often achieved through method overriding. We'll demonstrate this with a common `start_engine` method for both `Car` and `Motorcycle` classes.

```python
# vehicle.py continued

class Car(Vehicle):
    # ...

    def start_engine(self):
        return f"{self.get_make()} {self.get_model()} engine started."

class Motorcycle(Vehicle):
    # ...

    def start_engine(self):
        return f"{self.get_make()} {self.get_model()} engine started."
```

### Usage

You can use this code in a Python script as follows:

```python
# main.py

from vehicle import Car, Motorcycle

# Create instances of Car and Motorcycle
car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", "1200cc")

# Access attributes using getter methods
print(f"Car Make: {car.get_make()}, Model: {car.get_model()}, Doors: {car.num_doors}")
print(f"Motorcycle Make: {motorcycle.get_make()}, Model: {motorcycle.get_model()}, Engine Size: {motorcycle.engine_size}")

# Start engines using polymorphism
print(car.start_engine())
print(motorcycle.start_engine())
```

### Output

```
Car Make: Toyota, Model: Camry, Doors: 4
Motorcycle Make: Harley-Davidson, Model: Sportster, Engine Size: 1200cc
Toyota Camry engine started.
Harley-Davidson Sportster engine started.
```

This example demonstrates encapsulation through private attributes and getter/setter methods, inheritance with the `Car` and `Motorcycle` classes inheriting from `Vehicle`, and polymorphism with the `start_engine` method behaving differently for each subclass.

## Abstraction

Abstraction in object-oriented programming allows you to define a blueprint for classes where certain methods must be implemented by any child classes derived from the abstract class. In Python, you can create abstract classes using the `ABC` module and the `@abstractmethod` decorator.

## Abstract Class

### `Polygon` (Abstract Base Class)

The `Polygon` class is an abstract base class (ABC) that defines one abstract method:
- `printNumberOfSides(self)`: An abstract method representing the number of sides of the polygon. The `pass` keyword indicates that the method should be implemented in child classes.

## Child Class

### `Triangle` (Child Class of `Polygon`)

The `Triangle` class inherits from the abstract class `Polygon`. It provides a concrete implementation of the abstract method `printNumberOfSides(self)`. In this case, it specifies that a triangle has 3 sides.

## Usage

To use this code, follow these steps:

1. Import the `ABC` module and the `abstractclassmethod` annotation:

   ```python
   from abc import ABC, abstractclassmethod
   ```

2. Create an instance of the `Triangle` class:

   ```python
   shape1 = Triangle()
   ```

3. Call the `printNumberOfSides()` method on the instance:

   ```python
   shape1.printNumberOfSides()
   ```

This will print "This polygon has 3 sides." to the console, demonstrating how the abstract class enforces the implementation of the abstract method in the child class.
