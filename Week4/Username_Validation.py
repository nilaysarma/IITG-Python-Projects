# Week 4 Lab: Username Validation
# Description: Prompt the user to enter a username. Write a Python program to check if the username meets the following criteria:
# - The username must be at least 5 characters long.
# - The username must not contain any special characters or spaces.
# If the username meets the criteria, print "Valid username." Otherwise, print "Invalid username."

import re

def is_valid_username(username):
    # Check length
    if len(username) < 5:
        return False
    
    # Check for special characters or spaces (allow only letters and numbers)
    if not re.match(r"^[A-Za-z0-9]+$", username):  
        return False
    
    return True

# Get user input
username = input("Enter a username: ")

# Validate and print result
if is_valid_username(username):
    print("Valid username.")
else:
    print("Invalid username.")
