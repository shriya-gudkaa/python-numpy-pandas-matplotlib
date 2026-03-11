"""
Pandas Handling Missing Data
Description: Detecting and handling missing values in a DataFrame
"""

import pandas as pd
import numpy as np

data = {
    "Name": ["Shriya", "Dhea", "Pal", "Shubh"],
    "Age": [18, np.nan, 26, 22],
    "Marks": [85, 90, np.nan, 75]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()


# Detect missing values
print("Checking missing values using isnull():")
print(df.isnull())
print()


# Detect non-missing values
print("Checking non-missing values using notnull():")
print(df.notnull())
print()


# Drop rows with missing values
print("DataFrame after dropna():")
print(df.dropna())
print()


# Fill missing values
print("DataFrame after fillna(0):")
print(df.fillna(0))

# Deleting Columns
print("Deletes entire columns")
del df['Age']
print(df)

# Deleting Rows and Columns using drop()
df_new = df.drop([3]) 
print(df_new)

print(df.drop('Name', axis=1)) 

# duplicated() checks for duplicate rows and returns True or False
print("Duplicate:")
df = pd.DataFrame({'A':[1, 1, 2]}) 
print(df.duplicated())
