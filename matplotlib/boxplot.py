"""
Matplotlib Boxplot
Description: Displays distribution of numerical data using a box-and-whisker plot.
"""
import matplotlib.pyplot as plt 
data = [10, 20, 30, 40, 50, 60, 100] 
plt.boxplot(data) 
plt.title("Boxplot Example") 
plt.show()
plt.savefig("my_boxplot.pdf") # Save as PDF 
# savefig() Saves the current figure to a file (e.g., PNG, JPG, PDF).

"""
The boxplot() function in Matplotlib is used to display the distribution of numerical 
data using a box-and-whisker plot. 
It visually shows: 
• Minimum value 
• First Quartile (Q1) 
• Median (Q2) 
• Third Quartile (Q3) 
• Maximum value 
• Outliers (if any) 
"""

