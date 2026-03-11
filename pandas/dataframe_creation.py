"""
Pandas DataFrame Creation
Description: Different ways to create a DataFrame
"""
import pandas as pd
import numpy as np

# 1 Creating dataframe from series
my_series = pd.Series([10,20,30])
my_series2 = pd.Series([40,50,60])
df_series = pd.DataFrame({"column1":my_series,
                          "column2":my_series2})
print("DataFrame from Series:")
print(df_series)

# 2 Creating dataframe from dictionary
my_dict = {"name":["shriya","riya","pal"],
           "age":[18,20,26]}
df_dict = pd.DataFrame(my_dict)
print("DataFrame from Dictionary:")
print(df_dict)

# 3 Creating dataframe from numpy array
array_data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
df_array = pd.DataFrame(array_data, columns=["A", "B", "C"])
print("DataFrame from NumPy array:")
print(df_array)

# 4 Creating DataFrame from another DataFrame
s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]) 
df = pd.DataFrame(s) 
df1 = df   # Assign DataFrame to another variable  
print("DataFrame from another DataFrame:")
print(df1) 
