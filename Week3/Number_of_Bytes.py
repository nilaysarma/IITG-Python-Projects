# Week 3 Lab: Number of bytes calculator
# Description: A python script which takes input as number and outputs the number of bytes the number will require for its binary representation. The program should exit on typing 'q'.

import math

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    
    if user_input.lower() == "q":
        break

    try:
        num = int(user_input)  # Convert input to integer
        if num == 0:
            bytes_required = 1  # At least 1 byte is needed for zero
        else:
            bits_required = num.bit_length()  # Get number of bits needed
            bytes_required = math.ceil(bits_required / 8)  # Convert bits to bytes
        
        print(f"Bytes required: {bytes_required}\n")

    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

