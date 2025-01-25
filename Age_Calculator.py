# Week 2 Lab: Age Calculator with Birthday Countdown

import datetime

Date_of_Birth = input("Enter your Date of Birth (DD-MM-YYYY): ")

Date_of_Birth = datetime.datetime.strptime(Date_of_Birth, "%d-%m-%Y").date()
Current_Date = datetime.date.today()
age = Current_Date.year - Date_of_Birth.year

print("Your Age is: ", age)

Next_Birthday = Date_of_Birth.replace(year=Current_Date.year)
if(Next_Birthday == Current_Date):
    print("Today is your birthday. Happy Birthday!")
    exit()
if Next_Birthday < Current_Date:
    Next_Birthday = Next_Birthday.replace(year=Current_Date.year + 1)
Days_Left = Next_Birthday - Current_Date

print("Your next birthday is on: ", Next_Birthday.strftime("%d-%m-%Y"))
print(Days_Left.days, " days left for your next birthday")