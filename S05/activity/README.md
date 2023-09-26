# Animal Class Hierarchy

This Python code defines a simple class hierarchy for animals, with a base abstract class `Animal` and two concrete subclasses: `Cat` and `Dog`. The code demonstrates object-oriented programming principles, abstract classes, and inheritance.

## Table of Contents

- [Introduction](#introduction)
- [Class Hierarchy](#class-hierarchy)
- [Usage](#usage)

## Introduction

The `Animal` class hierarchy is designed to represent basic animal characteristics and behaviors. It illustrates the use of abstract classes to define a common interface (`eat()` and `make_sound()`) for concrete subclasses (`Cat` and `Dog`).

## Class Hierarchy

### `Animal` (Abstract Base Class)

The `Animal` class is an abstract base class (ABC) that defines two abstract methods:
- `eat(self, food)`: Abstract method to represent an animal eating.
- `make_sound(self)`: Abstract method to represent an animal making a sound.

### `Cat` (Concrete Subclass of `Animal`)

The `Cat` class inherits from `Animal` and provides concrete implementations of the abstract methods. Additionally, it includes:
- Attributes: `name`, `breed`, and `age`.
- Getter and setter methods for attributes.
- An extra method, `call()`, to call the cat.

### `Dog` (Concrete Subclass of `Animal`)

The `Dog` class is similar to the `Cat` class but tailored for dogs. It also inherits from `Animal` and provides concrete implementations of the abstract methods. It includes attributes (`name`, `breed`, and `age`), getter and setter methods, and an extra `call()` method.

## Usage

To use this code, follow these steps:

1. Import the `Animal`, `Cat`, and `Dog` classes from the script where they are defined:

   ```python
   from animal_classes import Animal, Cat, Dog
   ```

2. Create instances of the `Cat` and `Dog` classes, specifying their name, breed, and age:

   ```python
   cat1 = Cat("Puss", "Persian", 4)
   dog1 = Dog("Isis", "Dalmatian", 5)
   ```

3. Interact with the created instances by calling their methods:

   ```python
   cat1.eat("Tuna")          # Cat-specific eat method
   cat1.make_sound()         # Cat-specific sound method
   cat1.call()               # Cat-specific method

   dog1.eat("Steak")         # Dog-specific eat method
   dog1.make_sound()         # Dog-specific sound method
   dog1.call()               # Dog-specific method
   ```