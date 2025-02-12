# Week 5 Lab: Factorial Calculator
# Description: Using the understanding of looping, develop a Python program that calculates the factorial of a given number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"Factorial of {n} is {factorial}")
