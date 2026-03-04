"""
Pandas Series Attributes and Operations
Description: Accessing Series properties and performing basic operations
"""

import pandas as pd

# Create a Series
data = [10, 20, 30, 40, 50]
s = pd.Series(data)

print("Original Series:")
print(s)
print()

# 1 Attributes
print("Values:", s.values)
print("Index:", s.index)
print("Data Type:", s.dtype)
print("Shape:", s.shape)
print("Size:", s.size)

# 2 Accessing Elements
print("First element:", s[0])
print("Last element:", s[4])

print()

# 3 Basic Functions
print("Sum:", s.sum())
print("Mean:", s.mean())
print("Maximum:", s.max())
print("Minimum:", s.min())