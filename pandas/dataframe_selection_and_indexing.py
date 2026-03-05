"""
Pandas DataFrame Selection and Indexing
Description: Selecting columns and rows from a DataFrame
"""

import pandas as pd

data = {
    "Name": ["Shriya", "Riya", "Pal", "Aman"],
    "Age": [18, 20, 26, 22],
    "Marks": [85, 90, 88, 75]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print()


# Selecting a single column
print("Selecting 'Name' column:")
print(df["Name"])
print()


# Selecting multiple columns
print("Selecting Name and Marks columns:")
print(df[["Name", "Marks"]])
print()


# Selecting rows by index
print("Row at index 1:")
print(df.loc[1])
print()


# loc label-based selection
print("Using loc (rows 1 to 2):")
print(df.loc[1:2])
print()


# iloc position-based selection
print("Using iloc (first two rows):")
print(df.iloc[0:2])
print()


# Filtering with condition
print("Students with Marks > 85:")
print(df[df["Marks"] > 85])