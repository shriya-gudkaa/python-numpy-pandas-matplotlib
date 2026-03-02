"""
NumPy Concatenation and Splitting
Description: Joining and splitting NumPy arrays
"""

import numpy as np

# Create sample arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

# Concatenate
concat = np.concatenate((a,b))
print("\nConcatenated 1D array:",concat)

# Vertical Stack
v_stack = np.vstack((a,b))
print("\nVertical Stack:\n", v_stack)

# Horizontal Stack 
h_stack = np.hstack((a, b))
print("\nHorizontal Stack:", h_stack)

# Append
append_array = np.append(a, [7, 8])
print("\nAfter Append:", append_array)


# Splitting (1D)
x = np.array([1, 2, 3, 4, 5, 6])
split = np.split(x, 2)
print("\nSplit arrays:",split)

array_s = np.array_split(x,4)
print("\nSplit array into unequal parts:",array_s)



# 2d array
arr2d = np.arange(16).reshape(4, 4)
print("\nOriginal 2D array:\n", arr2d)

# Vertical split
upper, lower = np.vsplit(arr2d, 2)
print("\nVertical Split - Upper:\n", upper)
print("Vertical Split - Lower:\n", lower)

# Horizontal split
left, right = np.hsplit(arr2d, 2)
print("\nHorizontal Split - Left:\n", left)
print("Horizontal Split - Right:\n", right)

# 2D Stack Examples

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

print("\n2D Array 1:\n", arr1)
print("2D Array 2:\n", arr2)

# Vertical stack (row-wise)
vstack_2d = np.vstack((arr1, arr2))
print("\n2D Vertical Stack:\n", vstack_2d)

# Horizontal stack (column-wise)
hstack_2d = np.hstack((arr1, arr2))
print("\n2D Horizontal Stack:\n", hstack_2d)

# Stack with new axis
stack_axis0 = np.stack((arr1, arr2), axis=0)
print("\nStack with axis=0:\n", stack_axis0)

stack_axis1 = np.stack((arr1, arr2), axis=1)
print("\nStack with axis=1:\n", stack_axis1)