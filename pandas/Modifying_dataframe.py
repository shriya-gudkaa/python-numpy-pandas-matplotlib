import pandas as pd
d = {'EmpId' : ['E01','E02','E03','E04'],    
'EmpName' : ['Raj','Atul','Reena','Ayushi'],    
'Department' : ['IT','IT','HR','Accounts']}    
df = pd.DataFrame(d, index=['First','Second','Third','Fourth'])
print("df:\n", df)
print()

# “loc” attribute is also used to add a new row in DataFrame
df.loc['Fifth', : ] = ['E05', 'Nakul', 'HR']
print(df)
