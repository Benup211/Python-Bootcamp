# Python allows for user inputs, with this, users can give inputs to the program

# [Section] input() method -  allows our users to give or to add input to our program.
#example:
username= input("Enter your name:\n")
print(f"Hello {username}! Welcome Back")
#default value for input is string
print(type(username))
# If you want to convert the data type of the inputted value into integer or int you have to use the int() method.
# It will convert the string into data type

#since the num1 and num2 is from the input method,its data type is string
num1 = int(input("Enter 1st number:\n"));
num2 = int(input("Enter 2nd number:\n"));
print(f"The sum of num 1 and num2 is {num1 + num2}");
#selection control structure
test_num=int(input("Please enter your test number:\n"))
if test_num>0:
    print("Number is positive")
elif test_num==0:
    print("Number is neutral")
elif test_num<0:
    print("Number is negative")
#repition control struction
#loop
#Repeat a block of code
#WHILE loop is used to execute a set of statement as long as condition is true
i=1
while(i<=5):
    print(f"Current count {i}!")
    i+=1
# For loops are used for iterating over a sequence
#FOR loop used in list and tuple
fruit=["apple","banana","cherry","mango"]
for indiv_fruits in fruit:
    print(indiv_fruits)
# range method in for loop
# to use for loop to iterate through values, the range method can be used.
for x in range(6):
	print(f"The current value of x is {x}!");
# If we have two arguments on our range method, the first argument will be the starting value and the second argument will be the stopping, and the increment will still be 1.
for x in range(6, 10):
	print(f"The current values is {x}!");

for y in range(6, 20,2):
	print(f"The current values y is {y}!");

#mini activity:
    #study continue and break
