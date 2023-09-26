# Python has several structures to store collections or multiple items in a single variable: List, Dictionary, Tuples, and Set.
# For this course, we are just going to focus with list and dictionaries

# [Section] Lists
# Lists are very similar to arrays in JS in a sense that they can contain a collection of data and also access its element through the index.

# To create a list, the square brackets ([]) is used.
names = ["John", "Paul", "George", "Ringo"];
# This is an example of what we call String List.
programs = ['developer career', 'pi-shape', 'courses'];
# Example Number list:
durations = [260, 180, 20];
# Example of Boleean List / truth tables
truth_values = [True, False, True, True, False];

# Example of a list that contains elements with diffrent data type:
sample_list = ["Apple", 3, False, "Potato", 4, True];

print(sample_list);

# Get the size or the number of elements in our lists:
# The number of elements can be counted using the len() method;
# len(listName);
print(len(programs));

# Accessing values
	# List can be accessed by providing the index number of the element.
	# The index numbers in list starts with 0 and the last element will be len - 1, where len is the number of our elements.
	# listName[indexElement];
print(names[2]);
print(durations[2]);

# To access the last element on our array without using the negative index, we can actually use the len method of our list
print(truth_values[len(truth_values) - 1]);
print(names[len(names) - 1]);

# Access a range of values
# Syntax: listName[startingIndex: endingIndex]
#note ending index not included
#if the ending index is larger or greater than last index of list it will include all the last index element from starting element
print(names[0:3]);
print(names[0:100]);
#Update list
names[0]="John Doe";
print(names[0:3]);
#list manipulators
#list has methods that can be used to manupulate the elements with in
print(durations)
durations.append(301);
print(durations);
#Deleting an element from the list:del key word
del durations[1];
print(durations)
#check whether the element is part of the list or not
#we want to check whether 20 is included in duration array
print(20 in durations);
print(21 in durations);
#sort list-sort method,sort the list alphanumerically ascending by default
print(names);
names.sort();
print(names);

#clear or remove all the elements- the clear() method, this is used to empty the content of the lists
test_list=[1,3,5,7,9];
print(test_list);
test_list.clear();
print(test_list);

#[Section] Dictionaries
# Dictionaries are used to store values in key:value pairs,this is similar with objects in other programming languages
#Dictionary is collection which is ordere,changeable and does not allow duplicates:
person1={
    "name" : "Brandon",
    "age" : 28,
    "occupation": "student",
    "isEnrolled":True,
    "subjects":["Python", "SQL", "Django"]
}
#to get the number of key:value pairs in the dictionary,we also use len() method
print(len(person1));
#Accessing values in the dictionary
#to get the items in the dictionary, the key name can be referred using square notation
print(person1["isEnrolled"]);
print(person1["subjects"]);
#target the list value in the dictionary
print(person1["subjects"][1]);
# Get all the keys from the Dictionary - keys() method
print(person1.keys());
#Get all the value of the dict keys
print(person1.values());
#the items() methof will return each item in our dictionary, as a key-value pair in a list
print(person1.items());

#add new key value pair in the existing dictionary
#it can be done either putting a new index key and assigning a value or the update() method
person2={
    "name" : "chris",
    "age" : 28,
    "occupation": "instructor",
    "isEnrolled":False,
    "subjects":["Python", "SQL", "Django","JS","Java","PHP"]
}
print(person2);
person2["nationality"]="Filipino";
print(person2);

#using the update method
person2.update({"fave_food":"Sinigang"});
print(person2)

#Deleting entries can be done using the pop() method or the del keyword
person2.pop('fave_food');
print(person2)

del person2['nationality'];
print(person2)

#The clear() method empties the dictionary
person3={
    "name":"John",
    "age":18
}
print("####");
print(person3);
person3.clear();
print(person3)
print("####");

#looping through the dictionary
for keys in person2:
    print(f"The value of {keys} is {person2[keys]}");
print("####")
#Nested Dictionaries- dictionary 
person4={
    "name":"Monika",
    "age":20,
    "ocupation":"poet",
    "isEnrolled":True,
    "sugjects":["Python","SQL","Django"]
}
classRoom={
    "student1":person2,
    "student2":person4
}
print(classRoom["student1"]["subjects"][1]);

# [Section] Mini Exercise
# 1. Create a car dictionary with the following keys:
# brand, model, year of make, color
# 2. Print the following statement from the details:
# "I own a <Brand> <Model> and it was made in <Year of Make>"

car = {
    "brand":"Toyota",
    "model":"Camry",
    "Year_of_making":2018,
    "Color":"Blue"
}
print(f"I own a {car['brand']} {car['model']} and it was made in {car['Year_of_making']}");

# Functions are blocks of code that runs when called.
# A function can be used to get inputs, process the inputs, and return outputs.
# Imagine the process of learning: inputs like lessons are processed by the brain and with the processed data, a project is the output
# The "def" keyword is used to create a function. The syntax is: 
# def <function name>()

#defines a function call my_greeting
def my_greeting():
    #code to be run when function is called
    print("Hello User!")
#calling/Invoking a function- specify a function name and provide value if needed
my_greeting();

#parameter can be added to functions to have more control to what the inpputs for the function will be
def greet_user(username):
    print(f"Hello {username}!");
# Arguments are the values that are substituted to the parameters
greet_user('benup')
greet_user('ghimire')

#return statements-the return keyword allow function to returns values
#last command to be executed for return command
#any command added after return statement is ignored
def addition(num1,num2):
    return num1+num2
sum=addition(5,10);
print(f"The sum is {sum}");

#[Section] lambda functions:
# A lambda function is a small anonymous function that can be used for callbacks
    # It is just like any normal python function, except that it has no name when defining it, and it is contained in one line of code.
    # A lambda function can take any number of arguments, but can only have one expression.
multiply=lambda a,b:a*b
print(multiply(3,2))
print(multiply(5,6))


# Classes would serve as blueprints to describe the concept of objects
# Each object has characteristics (properties) and behaviors (objects)
# Imagine the concept of a car; a car has a brand, model, year_of_make and is able to drive, brake, turn
# To create a class, the "class" keyword is used along with the class name that starts with an uppercase character
# class ClassName():
# properties that all Car objects must have are defined in a method called init
# Any number of parameters to .__init__() can be passed but the first parameter should always be self
class Car():
    def __init__(self,brand,model,year_of_make):
        self.brand=brand;
        self.model=model;
        self.year_of_make=year_of_make;
        self.fuel="Gasoline"
        self.fuel_level=20
    def fill_fuel(self):
        print(f"Current fuel level :{self.fuel_level}");
        print(f"filling up the fuel tank ..");
        self.fuel_level=100;
        print(f"New fuel level :{self.fuel_level}");
new_car=Car('Nissan','GT-R',2019)
print(f"My car is {new_car.brand} {new_car.model}");
new_car.fill_fuel();


