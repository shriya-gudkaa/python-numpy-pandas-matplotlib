"""
NumPy Array Creation Functions
Author: Shriya Gudka
Description: Basic array creation methods in NumPy
"""
import numpy as np 

# 1. Create array from list

my_list = [10,20,30]
my_array = np.array(my_list)
print("converting list to array:\n",my_array)

# 2. Create zeros array

zeros_arr = np.zeros(5)
print("Zeros array:\n", zeros_arr)

# 3. Create ones array

ones_arr = np.ones(5)
print("Ones array:\n", ones_arr)

# 4. Create range array

arange_arr = np.arange(10)
print("Range array:\n",arange_arr)

arange_arr1 = np.arange(1,11,2)
print("array created with arange start-stop-step:\n",arange_arr1)

# 5. Create 2D array from list of lists
list_2d = [[1,2,3,4],
           [5,6,7,8]]

array_2d = np.array(list_2d)
print("2D Array from list of lists:\n", array_2d)


# 6. Create 2D zeros and ones arrays

zeros_2d = np.zeros((2, 3))
print("2D Zeros array:\n", zeros_2d)

ones_2d = np.ones((3, 2))
print("2D Ones array:\n", ones_2d)

# 7. Create array filled with specific value

full_array = np.full((3, 5), 3.14)
print("Array filled with 3.14:\n", full_array)

# 8. Create random array (uniform distribution)

random_array = np.random.random((3, 3))
print("Random 3x3 array (0 to 1):\n", random_array)

random_int = np.random.randint(1, 10, (3, 3))
print("Random integer array:\n", random_int)