"""
Pandas Sorting and Aggregation
Description: Sorting data and performing aggregation operations
"""

import pandas as pd

data = {
    "Name": ["Shriya", "Riya", "Pal", "Aman"],
    "Age": [18, 20, 26, 22],
    "Marks": [85, 90, 88, 75]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()

# Sorting by column values
print("Sorted by Marks:")
print(df.sort_values(by="Marks"))
print()

# Sorting by index
print("Sorted by index:")
print(df.sort_index())
print()

# Aggregation functions
print("Sum of Marks:", df["Marks"].sum())
print("Mean Marks:", df["Marks"].mean())
print("Minimum Marks:", df["Marks"].min())
print("Maximum Marks:", df["Marks"].max())
print()
