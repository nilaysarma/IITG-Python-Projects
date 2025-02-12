# Week 5 Lab: : Prime Number Checker
# Description: Create a Python program that takes a number as input and checks whether it is prime or not. A prime number is a positive integer greater than 1 that is divisible only by 1 and itself.

num = int(input("Enter a number: "))

if num > 1:
    i = 2
    is_prime = True
    while i <= int(num ** 0.5):
        if num % i == 0:
            is_prime = False
            break
        i += 1
    
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
else:
    print(f"{num} is not a prime number.")
