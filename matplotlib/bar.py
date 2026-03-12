"""
Matplotlib Bar Chart
Description: Creates a vertical bar chart using plt.bar()
"""

# Creates a vertical bar chart.
import matplotlib.pyplot as plt

names = ['Sakhi', 'Shriya', 'Dhea'] 
values = [40, 70, 30] 
plt.bar(names, values) # # Creates a vertical bar chart.
plt.xlabel("Categories") # Add labels to the x-axis 
plt.ylabel("Values") # Add labels to the y-axis
plt.title("Bar Graph") 
plt.grid(True) 
plt.show()