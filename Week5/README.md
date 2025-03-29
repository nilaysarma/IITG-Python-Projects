# DA108 | Lab 05 Assignment

## Task A: [Download and Save Country Flags Using Python](Country_Flags.ipynb)

Objective: You will write a Python program that:
- Downloads a CSV file from the given URL and saves it to a specified path.
- Loads the CSV file and reads it line by line.
- Extracts the flag image URL from each row in the above CSV file.
- Downloads the flag image and saves it in a folder named "flags".

### To-Do List
- In the python code:
    - Use **requests** or **urllib** python package to download the CSV file from the URL: [raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Country_Flags.csv](https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Country_Flags.csv)
    - Use **csv** python module to read the file.
    - Use **os** python package to manage directory creation.
- Write the script:
    - Assign the CSV file URL to a variable.
    - Download and save the CSV file.
    - Read the CSV file line by line.
    - Extract the country name and flag image URL.
    - Download and save the flag images into a "flags" directory.

## Task B: [Nobel Prize Analysis Using Lists & Loops](Nobel_Prize_Analysis.ipynb)

Download and Load the Data
- Assign the CSV file URL: [raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Nobel%20Laureattes.csv](https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Nobel%20Laureattes.csv) to a variable.
- Download and save it as "nobel_laureates.csv" in a chosen directory.

Open and read the CSV file line by line (use `open()` and `.split()` methods).
- Extract relevant fields (e.g., Birth Country).

Count the Number of Nobel Prizes by Country Create two lists:
- One to store country names. Another to store corresponding prize counts.
- For each laureate, check if their country exists in the list:
    - If yes, increase its count.
    - If no, add it to the list with an initial count of 1.
- Find the Top 20 Countries with Most Nobel Prizes:
    - Use basic sorting techniques (e.g., Bubble Sort or Selection Sort).
    - Print the top 20 countries along with their respective prize counts.
---

### Submission Guidelines
- Create .ipynb files for each of the above two tasks.
- Add **comments** explaining how each data type is used.
- Ensure your code is **efficient, well-structured, and readable**.
- Push your solution into the Github repo for this course made by you.