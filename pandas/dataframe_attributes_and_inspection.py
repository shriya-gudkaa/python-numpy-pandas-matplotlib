"""
Pandas DataFrame Attributes
Description: Inspecting structure and basic information of a DataFrame
"""

import pandas as pd

data = {
    "Name": ["Shriya", "Riya", "Pal"],
    "Age": [18, 17, 18],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print("DataFrame")
print(df)
print()

# Shape returns number of rows and columns
print("Shape of DataFrame:", df.shape)

# Columns shows column labels
print("Columns:", df.columns)

# Index shows row labels
print("Index:", df.index)

# dtypes shows data type of each column
print("Data Types:\n", df.dtypes)

print()

# head() displays first 5 rows (by default)
print("First rows using head():")
print(df.head())

print()

# tail() displays last 5 rows (by default)
print("Last rows using tail():")
print(df.tail())

print()

# info() gives summary of DataFrame including column types and non-null values
print("DataFrame Info:")
df.info()

print()

# describe() gives statistical summary of numeric columns
print("Statistical Summary:")
print(df.describe())