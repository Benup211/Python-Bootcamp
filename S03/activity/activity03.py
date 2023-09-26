# Activity:

def leap_year_checker():

    is_leap = True
    # Add your answer from here. don't modify the function name or the initial value of the is_leap variable.
    # This will be used for checking.
    # Do not modify the return statement.

    #Instructions
    
    # 1. Add the input() function to prompt the user to input a year. Convert the input to an integer using int() and store it in the variable year.
    # 2. Use the following logic to determine if the year is a leap year:
        # If the year is divisible by 4 and not divisible by 100, or
        # If the year is divisible by 400,
        # then it is a leap year. Otherwise, it's not.
    # 3. Store the result in the variable is_leap.
        # If the year is a leap year, the value of is_leap must be true.
        # If the year is not a leap year, the value of is_leap must be false.

    # Add code here
    year=int(input("Enter any year:"));
    if((year%4)!=0):
        is_leap=False;
    else:
        if((year%100)!=0):
            is_leap=True;
        else:
            if((year%400)!=0):
                is_leap=False;
            else:
                is_leap=True;



    # Do not edit
    return is_leap


def grade_classifier():

    grade = 0
    # Add your answer from here. don't modify the function name or the initial value of the grade variable. 
    # This will be used for checking.
    # Do not modify the return statement.
    
    #Instructions
    #1. Add the input() function to prompt the user to input a numerical score. Convert the input to a floating-point number using float() and store it in the variable score.

    # 2. Use the following logic to determine the letter grade based on the score:
        # If the score is 90 or above, assign the grade "S".
        # If the score is between 75 and 89 (inclusive), assign the grade "P".
        # Otherwise, assign the grade "F"
        # .
    # 3. Store the assigned grade in the variable grade.

    # Add code here
    score=float(input("Enter a numerical score:"));
    if(score>=90):
        grade="S";
    elif(score>=75 and score<=89):
        grade="P";
    else:
        grade="F";

    



    # Do not edit
    return grade


# Do not edit
if __name__ == '__main__':
    print(leap_year_checker())
    print(grade_classifier())