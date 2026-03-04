"""
Pandas Series Creation
Description: Different ways to create a Pandas Series
"""

import numpy as np
import pandas as pd

#1. Creating series from python List
my_list = [10,20,30,40]
my_series = pd.Series(my_list)
print("Series from list:")
print(my_series)

#2. Creating series from python Dictionary
my_dict = {"A":10,"B":20,"C":30}
my_series = pd.Series(my_dict)
print("Series from dictionary:")
print(my_series)

#3. Creating series from numpy array
array = np.array([10,20,30,40])
my_series = pd.Series(array)
print("Series from NumPy array:")
print(my_series)