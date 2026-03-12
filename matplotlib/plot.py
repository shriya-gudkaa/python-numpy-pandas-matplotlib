"""
Matplotlib Line Plot
Description: Draws a line connecting data points using plt.plot()
"""

# Draws a line (or multiple lines) connecting data points. 
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [2,4,6,8]

plt.plot(x,y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Plot")
plt.grid(True) # Adds a grid to the background of the plot.
plt.show() # Displays the window with the plot.