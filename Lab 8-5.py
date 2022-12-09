#1. Create a Python file named lab_8-5.py
#2. Write a function count_a(word) that takes in a string word and
#returns the number of a's in the word.
#3. The function should count both lowercase (a) and uppercase (A)

#create a function for the word in parameter
def count_a(word):
    #letter will be counted
    i = 0
    count = 0
    #print stament of the length of the word
    print(len(word))
    #While conditional statement  
    while i< len(word):
        #if statement to check lowercase a
        if word[i]=='a':
            count += 1
        elif word[i] == 'A': #if statement to check uppercase A
            count +=1
        i += 1
    #return the count of lower and uppercase a and A in the statement
    return count
#create a print statement with a word defined in the parameter
print(count_a('appreciAte'))       
