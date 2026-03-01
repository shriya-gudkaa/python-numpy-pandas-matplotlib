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
