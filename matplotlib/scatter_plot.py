""" 
The scatter() function is used to create a scatter plot, which shows the relationship 
between two variables. 
"""

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5] 
y = [10, 15, 13, 17, 20] 
plt.scatter(x, y) 
plt.title("Scatter Plot Example") 
plt.xlabel("X values") 
plt.ylabel("Y values") 
plt.show()