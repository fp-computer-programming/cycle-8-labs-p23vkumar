#1. Create a Python file named lab_8-6.py
#2. Write a function factorial(num) that takes 
# in a number num and returns the product of all numbers 
# from 1 up to and including num.

#define function factorial to take 
#in variable number within the parameter
def factorial(number):
    #define number 1 in the sequence
    x = 1
    #while condition  
    while number >= 1:
        #define factorial equation
        x = x * number 
        # number = number - 1 = equation within parameters as defined by original factorial equation
        number = number - 1
    #return x 
    return x

#create several test cases
print("The factorial of the provided numbers are: " + " ")
print(factorial(4)) #case 1
print(factorial(3)) #case 2 
print(factorial(12)) #Case 3
print(factorial(15)) #case 4
print(factorial(11)) #case 5
print(factorial(8)) #case 6
print(factorial(7)) #case 7
print(factorial(9)) #case 8