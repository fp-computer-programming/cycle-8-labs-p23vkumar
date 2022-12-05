#1. Create a Python file named lab_10-2


#2. Write a function that will take a list of names and write the body of
#an email to invite them to a party
def List_Of_names(name):
    for x1 in name:
        #3. The body should be something like this: 
##"Hi name, You're invited to my party on Friday!" Where name is the name of each person 
#in the list.
        print("Hi" + " " + x1 + " " + ",You're invited to my party on Saturday!")

print(List_Of_names(['Vishnu', 'Eric', 'Bob'])) #4. The function should use a for loop and print each invitation after it is generated. 
#There should be at least 3 names in the list.

