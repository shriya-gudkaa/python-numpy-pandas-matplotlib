"""
NumPy Indexing and Slicing
Description: Accessing and slicing elements in NumPy arrays
"""

import numpy as np

arr = np.array([10,20,30,40,50])
print("Original array: ",arr)

#1. Basic Indexing
print("First element: ",arr[0])
print("Last element: ",arr[-1])

#2. 1D Slicing
print("Every element: ",arr[:])
print("First 3 elements: ",arr[0:3])
print("every 2 element: ",arr[::2])

print()

# Create sample 2D array
arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]
                 ])

print("Original 2D array:\n",arr2)

# 3. 2D Indexing
print("Element at row 1, column 2: ",arr2[1,2])

# 4. 2D Slicing

# array[row_start:row_end, col_start:col_end]
print("First row:", arr2[0, :])

print("First column:", arr2[:, 0])

print("Rows 0 to 1, Columns 0 to 1:\n", arr2[0:2, 0:2])

print("Rows 1 to 2, Columns 1 to 2:\n", arr2[1:3, 1:3])

print("All rows, Columns 1 to 2:\n", arr2[:, 1:3])

print("Rows 1 to end, All columns:\n", arr2[1:, :])

print("Last two rows:\n", arr2[-2:, :])

print("Last column:\n", arr2[:, -1])

#5. Boolean Masking
print("Elements greater than 5:", arr2[arr2 > 2])