# Week 4 Lab: Exam Grading
# Description: A Python Program which asks the instructor to enter a student's details (namely, Name, Roll Number), and the score secured by the student in three subjects (namely in Physics, Chemistry and Maths). The program should then process this data and compute the grade for each subject and also the overall grade. The output should be presented in the terminal as neatly structured like a grade card.

print("-" * 20)
name = input("Enter Student name: ")
roll = int(input("Enter Roll No. "))
maths_score = float(input("Enter marks in Maths: "))
physics_score = float(input("Enter marks in Physics: "))
chemistry_score = float(input("Enter marks in Chemistry: "))

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

maths_grade = grade(maths_score)
physics_grade = grade(physics_score)
chemistry_grade = grade(chemistry_score)
overall_grade = grade((maths_score + physics_score + chemistry_score) / 3)

print("-"  * 20 + "\nHere is the Grade Card:\n" + "-" * 20)
print("Student Name: ", name)
print("Student Roll: ", roll)
print("Grade in Maths: ", maths_grade)
print("Grade in Physics: ", physics_grade)
print("Grade in Chemistry: ", chemistry_grade)
print("Overall Grade: ", overall_grade)
print("-" * 20)
print("Thank you!")
