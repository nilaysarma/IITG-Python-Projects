# Week 2 Lab: Compute Energy
# Description: : A python script which takes input for mass (m) of an object and outputs the energy computed using E=m*c*c*. Here, c is the speed of light, that is, c=300000000 meters per second. The program should exit on typing 'q'

c = 300000000

while True:
    m = input("Mass: ")
    if(m == "q"):
        break
    E = float(m) * c * c

    print(f"Energy: {E} Joules")
