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
