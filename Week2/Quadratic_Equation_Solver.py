# Week 2 Lab: Quadratic Equation Solver
# Description: A Python script that takes input for the coefficients aa, bb, and cc of a quadratic equation ax2+bx+c=0ax2+bx+c=0 and computes its roots using the quadratic formula. The program should display the computed roots.

import math

# Get user input
a = float(input("Coefficient a: "))
b = float(input("Coefficient b: "))
c = float(input("Coefficient c: "))

# Compute the discriminant
discriminant = b**2 - 4*a*c

# Compute the roots
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"Roots: {root}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"Roots: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i")
