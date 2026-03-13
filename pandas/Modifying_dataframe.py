
import pandas as pd
import numpy as np

d = {'EmpId' : ['E01','E02','E03','E04'],    
'EmpName' : ['Raj','Atul','Reena','Ayushi'],    
'Department' : ['IT','IT','HR','Accounts']}    
df = pd.DataFrame(d, index=['First','Second','Third','Fourth'])
print("df:\n", df)
print()
#Adding a Row
# “loc” attribute is also used to add a new row in DataFrame
df.loc['Fifth', : ] = ['E05', 'Nakul', 'HR']
print(df)

df.loc['Sixth']=['E06', 'Rahul', 'Accounts']
print(df)

# Modifying a Row
df.EmpId['Seventh'] = 'E07'
print(df)

# Adding a colum
#df['City'] = 'New Delhi'
df['City'] = ['New Delhi', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
print(df)