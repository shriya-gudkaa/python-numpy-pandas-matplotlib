"""
NumPy Rounding Functions
Description: Demonstrates round(), floor(), ceil(), and trunc()
to modify decimal values in arrays using different rounding methods.
"""

import numpy as np

arr = np.array([1.2, 2.5, 3.7])

# round() → nearest value
print("Round:", np.round(arr))
print("Round (1 decimal):", np.round(arr, 1))
print()

# floor() → round down
print("Floor:", np.floor(arr))
print()

# ceil() → round up
print("Ceil:", np.ceil(arr))
print()

# trunc() → remove decimal part
print("Trunc:", np.trunc(arr))