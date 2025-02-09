# Week 4 Lab: Temperature Converter
# Description: a Python program that prompts the user to enter a temperature and its unit (Celsius or Fahrenheit).Based on the unit provided, convert the temperature to the other unit and display the result. Use a string variable to store the unit.

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of the temperature (C/F): ")

if(unit == 'C' or unit == 'c'):
    temperature = (temperature * 9/5) + 32
    print("The temperature in Fahrenheit is: ", temperature)
elif(unit == 'F' or unit == 'f'):
    temperature = (temperature - 32) * 5/9
    print("The temperature in Celsius is: ", temperature)
else:
    print("Invalid unit entered. Please enter either 'C' or 'F'.")
