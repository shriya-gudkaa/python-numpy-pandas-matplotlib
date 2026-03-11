"""
Pandas CSV Operations
Description: Working with CSV files
"""

import pandas as pd

df = pd.read_csv("albums.csv")

# Save DataFrame to CSV
df.to_csv("albums.csv", index=False)
print("DataFrame saved to students_output.csv")
print()

# Read CSV file
df_read = pd.read_csv("albums.csv")
print("Data read from CSV file:")
print(df_read)