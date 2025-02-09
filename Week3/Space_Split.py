# Week 3 Lab: Space Split
# Description: Often while listening to a lecture on youtube we slow down/speed up the playback speed. The program should exit on typing 'q'. This program will do something similar but with text. The program should work as follows.
# output:
# user input: Hello! I am Tommy!
# output: Hello! ... I ... am ... Tommy!
# The program should exit on typing q

while True:
    user_input = input("user input: ")
    
    if user_input == "q":
        break
    
    words = user_input.split()  # Split input into words
    output = " ... ".join(words)  # Join words with " ... "
    
    print(f"output: {output}")
