import pandas as pd
import matplotlib.pyplot as plt

# Load global temperature dataset
url = "https://raw.githubusercontent.com/datasets/global-temp/master/data/monthly.csv"
try:
    df = pd.read_csv(url)
except Exception as e:
    print(f"Error loading the data: {e}")

# Display the first few rows of the DataFrame to understand the structure
print(df.head())

# Check for missing values and verify data types to ensure data integrity
print(df.isnull().sum())
print(df.info())

# Convert 'Date' to datetime and set it as index
df['Date']=pd.to_datetime(df['Date'])
df.set_index('Date' , inplace=True)

# Plot mean global temperature over time
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Mean'], label='Mean Global Temperature' , color='b')
plt.title('Global Temperature Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature(°C)')
plt.legend()
plt.show()

# Optionally save the plot as an image file for future reference or sharing
plt.savefig('global_Temperature_plot.png')  # Saves the plot as a PNG file

# Calculate and plot 12-month rolling average
df['rolling_mean'] = df ['Mean'].rolling(window=12).mean()
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Mean'], label='Mean Global Temperature', color='b')
plt.plot(df.index, df['rolling_mean'], label='12-Month Rolling mean', color='r')
plt.title('Global Temperature with Rolling Mean')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()

# Save this plot as well for future reference
plt.savefig('global_Temperature_with_rolling_mean.png')  # Saves the plot as a PNG file