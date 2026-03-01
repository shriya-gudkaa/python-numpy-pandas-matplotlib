"""
NumPy Statistical Functions
Description: Statistical and cumulative operations in NumPy
"""
import numpy as np 

arr = np.array([10,20,30,40,50])
print("Original array: ",arr)

# 1. Basic Statistical Functions
print("Mean: ",np.mean(arr))
print("Median: ",np.median(arr))
print("Standard deviation: ",np.std(arr))
print("Variance Value: ", np.std(arr))
print("Minimum Value: ",np.min(arr))
print("Maximum Value: ",np.max(arr))

print()

# 2. Position of Min and Max
print("Index of Maximum (argmax):", np.argmax(arr))
print("Index of Minimum (argmin):", np.argmin(arr))

print()

# 3. Cumulative Functions
print("Cumulative Sum:", np.cumsum(arr))
print("Cumulative Product:", np.cumprod(arr))

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print("2D Array:\n", arr2)

""" axis = 0 (column-wise)
    axis = 1 (row-wise)
    Standard Deviation """

print("Standard Deviation (axis=0):", np.std(arr2, axis=0))
print("Standard Deviation (axis=1):", np.std(arr2, axis=1))

# Variance
print("Variance (axis=0):", np.var(arr2, axis=0))
print("Variance (axis=1):", np.var(arr2, axis=1))