# Simple calulator program to execute basic numerical commands

# Define function for addition
def addition(x,y):
    """x and y are the input variables 
    to add together and get the sum as output"""

    return x+y


# Define function for substraction
def substraction(x,y):
    """x and y are the input variables 
    to minus a value from the other and get the substrated value as output"""

    return x-y


# Define function for multiplication
def multiplication(x,y):
    """x and y are the input variables 
    to multiply together and get the multiplicated value as output"""

    return x*y


# Define function for division
def division(x,y):
    """x and y are the input variables 
    to divide one into the other and get the divided value as output"""

    return x/y


# Define function for exponent
def exponent(x,y):
    """x and y are the input variables 
    to raise to the other and get the exponented value as output"""

    return x**y

##########################################################
# Display Menu
print("Welcome to Calculator Made Easy like MREASY")
print("Select one of the avaliable options below and input only two numbers for each mathematical operation")
print("Enter 1 for addition")
print("Enter 2 for substraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
print("Enter 5 for exponent")

##########################################################
# Get user choice
choice = int(input("Enter your choice of operation (1/2/3/4/5): "))
if (choice > 5):
    print("Invalid entry, please enter a value within the stated range")
    choice = int(input("Enter your choice of operation (1/2/3/4/5): "))
else:
    print("Please enter two numbers to execute mathematical operation")
##########################################################
# Get user input for the two numbers

num1 = float(input("Enter your first value: "))
num2 =  float(input("Enter your second value: "))

###########################################################
## Looping through the matherical operation functions

if (choice==1):
    print(f"{num1} + {num2} = {addition(num1,num2)}")
elif (choice==2):
    print(f"{num1} - {num2} = {substraction(num1,num2)}")
elif (choice==3):
    print(f"{num1} * {num2} = {multiplication(num1,num2)}")
elif (choice==4):
    print(f"{num1} / {num2} = {division(num1,num2)}")
elif (choice==5):
    print(f"{num1} ** {num2} = {exponent(num1,num2)}")
else:
    print("Invalid input, please try again")







