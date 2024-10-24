import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load global temperature dataset
url = "https://raw.githubusercontent.com/datasets/global-temp/master/data/monthly.csv"
try:
    df = pd.read_csv(url)
except Exception as e:
    print(f"Error loading the data: {e}")
    exit()  # Exit the script if data loading fails

# Display the first few rows of the DataFrame to understand the structure
print(df.head())

# Check for missing values and verify data types to ensure data integrity
print(df.isnull().sum())
print(df.info())

# Extract year from 'Year' column (which is in format 'YYYY-MM')
df['Year'] = df['Year'].str[:4]  # Extract only the year part
df['Year'] = pd.to_datetime(df['Year'], format='%Y', errors='coerce')  # Convert to datetime
df.set_index('Year', inplace=True)

# Calculate descriptive statistics
print("Descriptive Statistics:\n", df.describe())

# Add additional analysis: Calculate the change in mean temperature
df['Mean Change'] = df['Mean'].diff()  # Calculate the difference in mean temperature

# Linear Regression for trend analysis
X = np.array(range(len(df.index))).reshape(-1, 1)  # Independent variable
y = df['Mean'].values  # Dependent variable
model = LinearRegression()
model.fit(X, y)
df['Trend'] = model.predict(X)

# Plot mean global temperature over time
plt.figure(figsize=(12, 8))
plt.plot(df.index, df['Mean'], label='Mean Global Temperature', color='b', linewidth=2)
plt.plot(df.index, df['Trend'], label='Temperature Trend', color='orange', linestyle='--', linewidth=2)
plt.title('Global Temperature Over Time with Trend Line')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)  # Add grid for better readability
plt.savefig('global_temperature_plot_with_trend.png')  # Saves the plot as a PNG file
plt.show()

# Calculate and plot 12-month rolling average
df['rolling_mean'] = df['Mean'].rolling(window=12).mean()
plt.figure(figsize=(12, 8))
plt.plot(df.index, df['Mean'], label='Mean Global Temperature', color='b')
plt.plot(df.index, df['rolling_mean'], label='12-Month Rolling Mean', color='r')
plt.title('Global Temperature with Rolling Mean')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)  # Add grid for better readability
plt.savefig('global_temperature_with_rolling_mean.png')  # Saves the plot as a PNG file
plt.show()

# Display the change in mean temperature
print("Mean Temperature Change:\n", df['Mean Change'].dropna())