# Week 11 Lab: Demonstrating Numba's Performance Over NumPy
# Objective: Show how numba accelerates numerical computations compared to NumPy.

# Tasks:
# 1. Write a function to compute the sum of squares of a large array using NumPy.
# 2. Write the same function using numba.jit for just-in-time (JIT) compilation.
# 3. Measure the execution time of both functions using timeit .
# 4. Plot a bar chart comparing execution times for different array sizes.
# 5. Make observations on when to use numba over numpy.

import numpy as np
import timeit
from numba import jit

# NumPy implementation
def sum_of_squares_numpy(arr):
    return np.sum(np.square(arr))

# Numba JIT-compiled implementation
@jit(nopython=True)
def sum_of_squares_numba(arr):
    total = 0.0
    for x in arr:
        total += x * x
    return total

# Generate a large random array
arr = np.random.rand(10**6)  # 1 million elements

# Run Numba function once to trigger JIT compilation
sum_of_squares_numba(arr)

# Measure execution time
numpy_timer = timeit.Timer(stmt="sum_of_squares_numpy(arr)", globals=globals())
numba_timer = timeit.Timer(stmt="sum_of_squares_numba(arr)", globals=globals())

numpy_time = numpy_timer.timeit(number=10)
numba_time = numba_timer.timeit(number=10)

print(f"NumPy execution time: {numpy_time:.6f} seconds")
print(f"Numba execution time: {numba_time:.6f} seconds")
