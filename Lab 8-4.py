#1. Create a Python file named lab_8-4.py
#2. Write the while-loop version of the following for-loop program.
from re import I


def sum_to(n):
   total = 0
   for i in range(n+1):
     total += i
     return total
#3. The function should be able to have an integer passed to it and 
# return the sum of all the values from 1 to that integer

#Original Code
print("----------------------------------------")
def sum_to(n):
   total = 0
   for i in range(n+1):
     total += i
     return total
print("I have Provided the answer below: ")
print("----------------------------------------")

#Revised Code:

#define function
def sum_to(numbers):
    #sum will be counted
   total_number = 0
   i = 0
   #while one conditional i is less than the numbers 
   while i <= int(numbers):
      i += 1  # Conditionals for the while loop
      total_number += i
   return total_number 
#print (sum)
print(sum_to(34))