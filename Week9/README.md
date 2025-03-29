# DA108 | Lab 09 Assignment

## Task A: [Create a module compute_utils](compute_utils/compute_utils.py)

### Instructions:
1. Create a file called compute_utils.py
2. Implement the following inside the compute_utils.py. Feel free to write additional functions.

```py
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
```

3. Create another script main.py that:
    - Imports compute_utils module.
    - Calls each function with sample values and prints the results.

## Task B: [Creating a package with multiple modules](multiple_modules/mypackage/)

### Instructions:
1. Create a folder name mypackage.
2. Inside mypackage, create these modules:
    - geometry.py (contains functions for computing area of circle, square, rectangle, etc.)
    - matrix.py (contains functions for matrix addition, multiplication, inverse, etc.). You can use the numpy package inside matrix.py to operate on the matrices.
    - __init__.py (to make it a package)
3. Create main.py outside the package directory and use:
```py
from mypackage.geometry import area_circle
from mypackage.algebra import solve_linear

print("Area of circle: ", area_circle(5))
print("Solution to 2x + 4 = 0: ", solve_linear(2, 4))
```

## Task C: [Writing and importing custom logging module](logging_module)

### Instructions:
1. Create a module called logger.py with the following function.
```py
def log_message(message, filename="logfile.txt"):
    with open(filename, "a") as file:
        file.write(message + "\n")
```

2. Create another script app.py to import and use logger.py:
```py
from logger import log_message

log_message("Program started")
log_message("User logged in")
print("Logs written successfully.")
```

3. After running app.py, check if logfile.txt contains the log messages.

## Task D: [Build & Test the Package Locally](pypi)

### Understand the utility of the following commands.
```sh
pip install setuptools wheel twine
python setup.py sdist bdist_wheel
```
The above will create dist/ folder with distribution files.

### Test installation locally
Execute the below in the package repository (where you have the setup.py file)
```sh
pip install .
```
This above will install the package in your local system. You can then use it (let say the package name is mymathlib) as follows in any code.

### Publish to PyPI

1. Go to PyPI and create an account
2. Install twine in your local system if not install (uisng pip install twine)
3. Upload the package by executing the below in the terminal.
```sh
twine upload dist/*
```
4. Now any one can pip install your package!

This package is published on [PyPI](https://pypi.org/project/mymathlibrary) and can be installed by using pip:
```sh
pip install mymathlibrary
```