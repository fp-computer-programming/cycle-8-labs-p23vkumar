#1. Create a Python file named lab_8-1
#2. Write a function in that uses the for loop and the range function to find the sum of all 
#the numbers up to and including the number the user input

def sum_range(numbers):
    #3. The function should return the final total of the sum of all of the 
#items in the list
    sum = 0
    for numbers in range(numbers + 1):
        sum += numbers
    return sum 

#4. Add a statement that prompts the user to input an integer
x1 = input("Enter Number: ")
#6. Add a statement to print the variable to see the final 

#print(function)
print(sum_range(int(x1)))    