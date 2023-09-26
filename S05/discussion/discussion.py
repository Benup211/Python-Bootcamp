class SampleClass():
    #the class constructor or initialization method is called by python everytime an instance of the class is created
    #"self" parameter is a refrence to the current instance of the class, and is used to access variables that belongs to the class
    def __init__(self,year):
        self._year=year;
    def show_year(self):
        print(f"This year is:{self._year}");
obj = SampleClass(2023);
# to display the properties and methods of an object instance, the "dot notation" is used
obj.show_year();

#[Section] fundamental of oop
#four fundamentals principles in OOP
#Encapsulation
#Inheritance 
#Ploymorphism
#Abstraction

#Data Encapsulation->Data hiding,only access attribute through method of class
#the attribute of a class will be hidden from ther classes and can only be accessed only through the methods of their current class.
# the prefix underscore "_name" is used as a warning for developers that means:
# "Please be careful about this attribute or method, dont use it outside of the declared class"
class Person():
    def __init__(self):
        #protected attribute_name
        self._name="John Doe";
        #protected attribute _age
        self._age=0;
    #setter method "set_name"
    def set_name(self,name):
        self._name=name;    
    #getter method "get name"
    def get_name(self):
        print(f"Name of Person:{self._name}");
    #setter method "set_age"
    def set_age(self,age):
        self._age=age;    
    #getter method "get name"
    def get_age(self):
        print(f"Name of Person:{self._age}");
p1= Person();
p1.get_name();
p1.set_name("Bob Doe");
p1.get_name();
p1.get_age();
p1.set_age(20);
p1.get_age();

#[SECTION] Inheritance
#Inheritance->transfer characteristics of a class to other class that are derived from it
# syntax: class Childclassname(Parentclassname)

class Employee(Person):
    def __init__(self,employeeId):
        #super can be used to invoke immediate parent class constructor
        super().__init__()
        #attribute unique to the employee class
        self._employeeId=employeeId;
    #getter method
    def get_employeeId(self):
        print(f"The employee ID is {self._employeeId}");
    #setter method
    def set_employeeId(self,employeeId):
        self._employeeId=employeeId;
    #details method
    def get_detials(self):
        print(f"{self._employeeId} belongs to {self._name}");
print("#"*50)
emp1=Employee("Emp-001");
emp1.get_detials();
emp1.set_name("dob");
emp1.set_age(21);
emp1.get_detials();
print("#"*50)
class Student(Person):
    def __init__(self,studentNo, course, year_level):
        # super() can be used to invoke immediate parent class constructor
        super().__init__()
        # attributes unique to the Employee class
        self._studentNo = studentNo
        self._course = course
        self._year_level = year_level
    
    # getters
    def get_studentNo(self):
        print(f"Student number of Student is {self._studentNo}")

    def get_course(self):
        print(f"Course of Student is {self._course}")

    def get_year_level(self):
        print(f"The Year Level of Student is {self._year_level}")

    # setters
    def set_studentNo(self, studentNo):
        self._studentNo = studentNo
    
    def set_course(self, course):
        self._course = course
    
    def set_year_level(self, year_level):
        self._year_level = year_level

    # custom method
    def get_details(self):
        print(f"{self._name} is currently in year {self._year_level} taking up {self._course}.")

# Test cases:
print("#"*50)
student1 = Student("stdt-001", "Computer Science", 1)
student1.set_name("Brandon Smith")
student1.set_age(18)
student1.get_details()
print("#"*50)

#[SECTION] polymorphism
#Polymorphism->many form of a method
#A child class inherits all the methods from the parent class.However, in some situations, the method inherited from the parent class doesn't quite fit into the child class

#function and objects
#A function can be created that can take any object, allowing for polymorphism
class Admin():
    def is_admin(self):
        print(True);
    def user_type(self):
        print("Admin user");
class Customer():
    def is_admin(self):
        print(False);
    def user_type(self):
        print("Regular User");
#Define a test function that will take an object
def test_function(obj):
    obj.is_admin();
    obj.user_type();
#Create object instance for Admin and Customer
user_admin=Admin();
user_customer=Customer();
#pass the created instance to the test function
test_function(user_admin);
test_function(user_customer);


#Abstraction->allows you to create a set of methods that must be created within any child classes built from abstract class
# Abstraction
# An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.

# By default, Python does not provide abstact classes. Python comes with a module that will let us create abstract classes.

# import the ABC model and the annotcation abcstractclassmethod
from abc import ABC, abstractclassmethod

# Abstract class

class Polygon(ABC):

    # Create an abstract method
    @abstractclassmethod
    def printNumberOfSides(self):
        # pass keyword denotes that the method will do nothing.
        pass


# Child class of the Abstract Class

class Triangle(Polygon):
    def __init__(self):
        super().__init__()

    def printNumberOfSides(self):
        print(f"This polygon has 3 sides.")


shape1 = Triangle()

shape1.printNumberOfSides();