"""
NumPy Universal Functions (Ufuncs)
Description: Mathematical operations applied element-wise on arrays
"""

import numpy as np

arr1 = np.array([1, 4, 9, 16])
print("Original Array:", arr1)

# 1. Square root
print("Square root: ",np.sqrt(arr1))

# 2. Exponential
print("Exponential (e^x):", np.exp(arr1))

# 3. Power
print("Power: ",np.power(arr1,3))

# 4. Rounding Functions
arr_round = np.array([1.2, 2.5, 3.7, 4.5])
print("Original for rounding:", arr_round)
print("Round:", np.round(arr_round))
print("Floor:", np.floor(arr_round))
print("Ceil:", np.ceil(arr_round))

# 5 Absolute Value
arr_abs = np.array([-5, -2, 0, 3])
print("Absolute Values:", np.abs(arr_abs))

# 6 Comparison Functions
arr2 = np.array([4, 2, 1 ,9])
print("\nComparison Operations:")

print("Greater (arr1 > arr2):", np.greater(arr1, arr2))

print("Less (arr1 < arr2):", np.less(arr1, arr2))

print("Equal (arr1 == arr2):", np.equal(arr1, arr2))