#1. Create a Python file named lab_8-8.py
#2. Using the nested list rows from the 
#"Nested Data" slide, write a function that prints 
#each person's name

#Original Code

#create a function for list
def rows_name(rows):
    #original list for rows
    rows = [["Darick", "Eugene", "Kyle", "Azaan"],["Ryan", "Phil", "Eman", "Alex", "Nicholas"],
   ["Christian", "Josh", "Matt", "Francesco"],
   ["Patrick", "Nico", "Trevayne"]]
   #create two for conditionals for ranges
    for row in rows:
        for name in row:
            print(name)
print(rows_name('Vishnu'))

#• BONUS: Make each name be possessive. Remember, 
#if a name ends in s, only add an apostrophe. 
#If the name does not end in s, add, 's.
