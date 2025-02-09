# Week 3 Lab: Vowel Remover
# Description: A Python script/code which:
# takes user input as a string,
# remove vowels from the string (take care if it is single character),
# output the vowel stripped string,
# The program should exit on typing q.

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    words = text.split()  # Split input into words
    result = []

    for word in words:
        if len(word) == 1 and word in vowels:
            result.append(word)  # Keep single-character vowels
        else:
            result.append("".join(char for char in word if char not in vowels))  # Remove vowels

    return " ".join(result)

while True:
    user_input = input("user input: ")
    
    if user_input.lower() == "q":
        break
    
    output = remove_vowels(user_input)
    print(f"output: {output}\n")
