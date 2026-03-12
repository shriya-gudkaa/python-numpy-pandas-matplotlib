"""
Matplotlib Pie Chart
Description: Creates a pie chart using plt.pie()
"""

import matplotlib.pyplot as plt

sizes = [25,35,40]
labels = ["Apple" , "Banana" , "Cherry"]
plt.pie(sizes, labels=labels, autopct='%1.1f%%') #Creates a pie chart
plt.title("Fruit Share")
plt.show()

"""
• explode: A tuple or array indicating how much each slice should be offset from 
  the center. 
• colors: A list of colors for each slice. 
• autopct: A format string or function to display percentage values on the slices. 
• shadow: A boolean to add a shadow effect. 
• startangle: The starting angle of the first slice in degrees (default is 0).
"""