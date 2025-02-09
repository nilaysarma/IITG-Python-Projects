# Week 4 Lab: String Length Comparison
# Description: Prompt the user to enter two strings. Write a Python program to compare the lengths of the two strings and print a message indicating which string is longer, or if they are of equal length.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) > len(string2):
    print("The first string is longer.")
elif len(string1) < len(string2):
    print("The second string is longer.")
else:
    print("Both strings are of equal length.")
