"""
NumPy Broadcasting
Description: Performing operations on arrays of different shapes
"""

import numpy as np

# Scalar Broadcasting
a = np.array([1, 2, 3])
print("Original array:", a)
print("After adding scalar 5:", a + 5)

print()

# 1D + 1D
b = np.array([10, 20, 30])
print("Array a:", a)
print("Array b:", b)
print("a + b:", a + b)

print()

# 1D + 2D Broadcasting
c = np.ones((3, 3))
d = np.array([1, 2, 3])

print("2D Array c:\n", c)
print("1D Array d:", d)
print("c + d:\n", c + d)

print()

#  Column Broadcasting
x = np.arange(3).reshape(3, 1)
y = np.arange(3)

print("x:\n", x)
print("y:", y)
print("x + y:\n", x + y)

print()
