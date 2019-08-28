# Check out the documentation on the Basic-Operators.md file in this folder

# Examples of operators
number = 1 + 2 # sets the value of number to 3 (1 + 2) - integer variable
print(number) # prints the value of the variable number, in this case 3

# Modulus operator
remainder = 11 % 3 # sets the value of the variable "remainder" to the remainder of 11 divided by 3
print(remainder)

# Types of operators in Python
# +. Addition
# -. Subtraction
# *. Multiplication
# /. Division
# %. Modulus - returns the remainder of a division
# Power operators
squared = 7 ** 2 # sets the value of "squared" (an integer variable) to the value of 7^2 - 49
cubed = 7 ** 3 # sets the value of "cubed" (an integer/float variable) to the value of 7^3 = 343
print(cubed + squared) # prints the value of cubed added to the value of squared

# Operators & Strings
# addition and strings
helloworld = "hello " + "world" #sets the value of the string variable "helloworld" to "hello + world" = "hello world"
print(helloworld) # prints the value of "helloworld", in this case hello world
# multiplication abd strings
lotsofstring = "string" * 10 # sets the value of "lotsofstring" to 10xstring
print(lotsofstring) # prints string x10 

# Operators can be used with lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)