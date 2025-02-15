import re

def camel_to_snake(camel_case: str) -> str:
    if not camel_case[0].islower():
        return "Invalid input. Please enter a camelCase variable name (starting with a lowercase letter)."

    # Convert camelCase to snake_case
    snake_case = re.sub(r'([A-Z])', r'_\1', camel_case).lower()
    return snake_case

# Get user input
camel_case_input = input("Enter a camelCase variable name: ")

# Check if the input is a valid camelCase format
if not camel_case_input.isalnum() or "_" in camel_case_input:
    print("Invalid input. Only use letters and numbers, and avoid underscores.")
else:
    print("Snake case:", camel_to_snake(camel_case_input))
