"""
NumPy Array Operations
Description: Basic operations performed on NumPy arrays
"""
import numpy as np

arr1 = np.array([10,20,30,40])
arr2 = np.array([1,2,3,4])

print("Array 1:\n",arr1)
print("Array 2:\n",arr2)

# 1. Mathematical Operations
print("Addition: ",np.add(arr1,arr2))
print("Subtraction: ",np.subtract(arr1,arr2))
print("Multiplication: ",np.multiply(arr1,arr2))
print("Division: ",np.divide(arr1,arr2))
print()

# 2. Aggregation Functions
print("Sum: ",np.sum(arr1))
print("Mean: ",np.mean(arr1))
print("Minimum: ",np.min(arr1))
print("Maximum: ",np.max(arr1))

# 3.Reshape
reshape_array = arr1.reshape(2,2)
print("Reshaped Array:\n", reshape_array)