# Conditionals - If (Lecture 17)
# Lecture Link: https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13270028#content

# Set-up
variable1 = 10
variable2 = 20

# If Condition
if variable1 < variable2: 
    print(variable1 + " is less than " + variable2) # or print(10 is less than 20) - without the variables
    # Anything below this line that is not indented is shown regardless of what happens with the if statement
    # Multiple statements & statements can be put within a conditional statement


# Conditionals - If/Else (Lecture 18)
# Lecture Link: https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13270030#content

# Set-up
number1 = 1
number2 = 2
number3 = 3

# Else/if - Addition
if number1 + number2 == number3:
    print("Correct numbers")
elif number1 + number2 != number3:
    print("Try again")    