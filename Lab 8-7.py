#1. Create a Python file named lab_8-7.py
#2. Write a function is_palindrome(word) that takes in a string word
#and returns the true if the word is a palindrome, false otherwise.
#3. A palindrome is a word that is spelled the same forwards and backwards.


def is_palindrome(word):
    reverse = ""
    i = len(word) - 1
    while i >= 0:
        reverse += word[i]
        i = i - 1
    return reverse  == word
print(is_palindrome('racecar'))
print(is_palindrome('ZoZ'))
print(is_palindrome('apple'))
