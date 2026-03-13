import pandas as pd
import numpy as np

# Creating a dictionary containing employee information
d = {
    'EmpId': ['E01','E02','E03','E04'],
    'EmpName': ['Raj','Atul','Reena','Ayushi'],
    'Department': ['IT','IT','HR','Accounts']
}

# Creating a DataFrame from the dictionary
# Custom row labels (index) are also provided
df = pd.DataFrame(d, index=['First','Second','Third','Fourth'])

print("Initial DataFrame:\n", df)
print()

# Adding rows to the DataFrame

# The loc[] attribute can be used to add a new row

df.loc['Fifth', :] = ['E05', 'Nakul', 'HR']
print("After adding 'Fifth' row:")
print(df)

# Adding another row using loc
df.loc['Sixth'] = ['E06', 'Rahul', 'Accounts']
print("After adding 'Sixth' row:")
print(df)

# Modifying or adding a value in a specific column

# Here we assign a value to the EmpId column for a new row label
# If the row label does not exist, Pandas will create it
df.EmpId['Seventh'] = 'E07'

print("After modifying/adding 'Seventh' row:")
print(df)


# Adding a new column to the DataFrame

# Creating a new column named 'City'
# np.nan is used to represent missing values

df['City'] = ['New Delhi', np.nan, np.nan, np.nan, np.nan, np.nan]

print("After adding 'City' column:")
print(df)