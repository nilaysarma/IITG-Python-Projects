# Week 3 Lab: Case Altered
# Description: A python program (script) which asks for user input by showing the prompt user input. It reads the input, does some processing and outputs the message received as input but with the case altered.

while True:
    user_input = input("user input: ")
    if user_input == "q":
        break
    print("case altered: ", user_input.swapcase())