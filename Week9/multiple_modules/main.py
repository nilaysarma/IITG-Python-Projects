from mypackage.geometry import area_circle
from mypackage.matrix import add_matrix
import numpy as np

print("Area of circle: ", area_circle(5))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Matrix addition: \n", add_matrix(a, b))
