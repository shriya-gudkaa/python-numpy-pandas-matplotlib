"""
Matplotlib Histogram
Description: Shows the distribution of data using plt.hist()
"""
import matplotlib.pyplot as plt 
import numpy as np

data = np.random.randn(100)
plt.hist(data, bins=20, color='skyblue', edgecolor='black') # Plots a histogram showing the distribution of data.
plt.xlabel("value")
plt.ylabel("frequency")
plt.title("Hist Graph")
plt.grid(True)
plt.show()