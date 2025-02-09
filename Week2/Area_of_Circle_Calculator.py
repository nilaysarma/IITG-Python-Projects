# Week 2 Lab: Area of Circle Calculator
# Description: : A Python script that takes input for the radius of a circle and computes its area using the formula A=π*r**r, where π is a constant (use an approximation like 3.14159). The program should display the computed area

pi = 3.14159
radius = float(input("Radius: "))
area = pi * radius ** 2
print(f"Area: {area} square units")