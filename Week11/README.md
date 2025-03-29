# DA108 | Lab 11 Assignment

## Assignment 1: [Linear Algebra with NumPy and SciPy](NumPy_SciPy.ipynb)

**Objective:** Learn to use NumPy and SciPy for basic linear algebra operations.

### Tasks:
1. Create a 3×3 random matrix and compute its inverse using `numpy.linalg.inv()`.
2. Compute the dot product of two randomly generated vectors using `numpy.dot()`.
3. Perform matrix-vector multiplication with NumPy.
4. Solve a system of linear equations using `scipy.linalg.solve()`.
5. Compute the eigenvalues and eigenvectors of a given square matrix.

## Assignment 2: [Sound Processing with Librosa](Sound_Processing_Librosa.ipynb)

**Objective:** Work with audio files using Librosa to mix and manipulate sounds.

### Tasks:
1. Load a `.wav` file from [freesound.org](https://freesound.org) using `librosa.load()`.
2. Plot the waveform using `matplotlib.pyplot.plot()`.
3. Load another `.wav` file and mix it with the first one by summing the signals.
4. Normalize the mixed signal and save it back as a `.wav` file using `soundfile.write()`.
5. Play the mixed audio using an external library like `IPython.display.Audio()`.

## Assignment 3: [Image Processing (Grayscale & Black-White Conversion)](Image_Processing.ipynb)

**Objective:** Convert images into grayscale and binary (black and white) using OpenCV.

### Tasks:
1. Load a color image using `cv2.imread()`.
2. Convert the image to grayscale using `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`.
3. Convert the grayscale image to a binary black-and-white image using thresholding (`cv2.threshold()`).
4. Display the original, grayscale, and binary images using `matplotlib.pyplot.imshow()`.
5. Save the grayscale and black-and-white images using `cv2.imwrite`.

## Assignment 4: [Demonstrating Numba's Performance Over NumPy](Numba_Performance.py)

**Objective:** Show how `numba` accelerates numerical computations compared to NumPy.

### Tasks:
1. Write a function to compute the sum of squares of a large array using NumPy.
2. Write the same function using `numba.jit` for just-in-time (JIT) compilation.
3. Measure the execution time of both functions using `timeit`.
4. Plot a bar chart comparing execution times for different array sizes.
5. Make observations on when to use `numba` over `numpy`.