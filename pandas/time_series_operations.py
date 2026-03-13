"""
Pandas Time Series Operations
Description: Demonstrates date conversion, setting index, filtering by date,
and resampling time-series data.
"""

import pandas as pd

# Read CSV file
data = pd.read_csv("random_stock_market_dataset.csv")

print("Original DataFrame:")
print(data)
print()

# Display current data types
print("Current Data Types:")
print(data.dtypes)
print()

# Convert 'Date' column to datetime format
data["Date"] = pd.to_datetime(data["Date"])
print("Data Types after converting Date:")
print(data.dtypes)
print()

# Set 'Date' column as the index
data.set_index("Date", inplace=True)
print("DataFrame after setting Date as index:")
print(data)
print()

# Filter a specific date range
filtered = data.loc["2024-01-01":"2024-01-07"]
print("Filtered Data (2024-01-01 to 2024-01-07):")
print(filtered)
print()

# Resample data to calculate monthly averages
monthly = data.resample("M").mean()
print("Monthly Average:")
print(monthly)

"""
Common resampling rules:
D → Daily
W → Weekly
M → Monthly
Y → Yearly
"""