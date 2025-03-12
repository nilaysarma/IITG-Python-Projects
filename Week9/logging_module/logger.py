def log_message(message, filename="logfile.txt"):
    with open(filename, "a") as file:
        file.write(message + "\n")
