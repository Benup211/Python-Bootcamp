from abc import ABC, abstractclassmethod
class Animal(ABC):
    @abstractclassmethod
    def eat(self,food):
        pass
    @abstractclassmethod
    def make_sound(self):
        pass
class Cat(Animal):
    def __init__(self, name, breed, age):
        self._name = name
        self._breed = breed
        self._age = age

    # Getters
    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    def get_age(self):
        return self._age

    # Setters
    def set_name(self, name):
        self._name = name

    def set_breed(self, breed):
        self._breed = breed

    def set_age(self, age):
        self._age = age

    # Implementation of abstract methods
    def eat(self, food):
        print(f"Serve me {food}.")

    def make_sound(self):
        print(f"Miaow! Nyaw! Nyaaaaa!")

    # Additional method
    def call(self):
        print(f"{self._name}, come on!")


class Dog(Animal):
    def __init__(self, name, breed, age):
        self._name = name
        self._breed = breed
        self._age = age

    # Getters
    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    def get_age(self):
        return self._age

    # Setters
    def set_name(self, name):
        self._name = name

    def set_breed(self, breed):
        self._breed = breed

    def set_age(self, age):
        self._age = age

    # Implementation of abstract methods
    def eat(self, food):

        print(f"Eaten {food}.")

    def make_sound(self):
        print(f"Bark! Woof! Arf!")

    # Additional method
    def call(self):
        print(f"Here {self._name}")

# Create instances of the Cat and Dog classes
dog1 = Dog("Isis", "Dalmatian", 5)
dog1.eat("Steak")        
dog1.make_sound()       
dog1.call()  
cat1 = Cat("Puss", "Persian", 4)
cat1.eat("Tuna")          
cat1.make_sound()       
cat1.call()             
           
