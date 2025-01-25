# Week 3 Lab: Password Strength Checker with Feedback Loop
# Description: A password strength checker that evaluates a given password while reinforcing the understanding of fundamental data types like int, float, bool, string, and list. The program should provide real-time feedback and allow users to retry until they create a strong password.

# List to store history of entered passwords
password_history = []

while True:
    # Prompt the user to enter a password
    password = input("Enter a password: ")
    password_history.append(password)   # Add the passwords to the password_history list

    # Analyze password properties
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "@#$%^&*()!_?/-" for char in password)

    # Determine password strength & provide feedback
    if length < 6:
        print("Weak password. Try using numbers and special characters.")
    elif has_lower and has_upper and has_digit and has_special:
        print("Strong password! Great job!")
        break   # Exit the loop if the password is strong
    elif has_lower and has_digit:
        print("Medium password. Try adding a special character for a stronger password.")
    else:
        print("Weak password. Make sure it includes a mix of uppercase, lowercase, numbers, and special characters.")

# Print the password history list
print("\nPassword history:")
for i, pwd in enumerate(password_history, 1):
    print(f"{i}: {pwd}")