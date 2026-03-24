"""
NumPy File Handling
Demonstrates save(), load(), savetxt(), and loadtxt()
"""

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40])

# Binary File 
# save() save array in .npy format
np.save("data.npy", arr)

# load() load array from .npy file
loaded_npy = np.load("data.npy")
print("Loaded from .npy file:", loaded_npy)
print()

# Text File 
# savetxt() save array in .txt format
np.savetxt("data.txt", arr)

# loadtxt() load array from .txt file
loaded_txt = np.loadtxt("data.txt")
print("Loaded from .txt file:", loaded_txt)

