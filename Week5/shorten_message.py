# Week 5 Lab: : Shortening text messages
# Description: When texting, it’s not uncommon to shorten words to save time or space, as by omitting vowels. Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def remove_vowels(text: str) -> str:
    vowels = "AEIOUaeiou"
    return "".join(char for char in text if char not in vowels)

# Get user input
message = input("Enter your message: ")

# Output the shortened message
print("Shortened message:", remove_vowels(message))
