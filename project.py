import pandas as pd

# Load the dataset
file_path = "/mnt/data/powerconsumption.csv"
df = pd.read_csv("powerconsumption.csv")

# Display basic information and the first few rows
df.info(), df.head()

# Check for missing values, duplicates, and unique value counts for each column
missing_values = df.isnull().sum()
duplicates = df.duplicated().sum()
unique_values = df.nunique()

# Summary statistics for numerical columns
summary_stats = df.describe()

missing_values, duplicates, unique_values, summary_stats

# Step 1: Convert 'Datetime' to datetime format and extract time components
df['Datetime'] = pd.to_datetime(df['Datetime'])
df['Date'] = df['Datetime'].dt.date
df['Hour'] = df['Datetime'].dt.hour
df['Month'] = df['Datetime'].dt.month
df['Weekday'] = df['Datetime'].dt.day_name()

# Display updated DataFrame info and head
df.info(), df[['Datetime', 'Date', 'Hour', 'Month', 'Weekday']].head()

import seaborn as sns
import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt

# Set plotting style
sns.set(style="whitegrid")
plt.figure(figsize=(18, 12))

# Plot distributions
variables = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows']
for i, var in enumerate(variables):
    plt.subplot(3, 2, i+1)
    sns.histplot(df[var], kde=True, bins=50, color='skyblue')
    plt.title(f'Distribution of {var}')
    plt.xlabel(var)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Calculate correlation matrix
corr_matrix = df.corr(numeric_only=True)

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

#OBJECTIVE 1. Temperature vs Power Consumption (All 3 Zones)
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))
for i, zone in enumerate(['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']):
    plt.subplot(1, 3, i+1)
    sns.scatterplot(x='Temperature', y=zone, data=df)
    plt.title(f'Temperature vs {zone}')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Power Usage')

plt.tight_layout()
plt.show()

#OBJECTIVE 2. Humidity vs Power Consumption (All 3 Zones)

plt.figure(figsize=(15, 5))
for i, zone in enumerate(['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']):
    plt.subplot(1, 3, i+1)
    sns.scatterplot(x='Humidity', y=zone, data=df, color='purple')
    plt.title(f'Humidity vs {zone}')
    plt.xlabel('Humidity (%)')
    plt.ylabel('Power Usage')

plt.tight_layout()
plt.show()
#OBJECTIVE 3. Daily & Monthly Power Consumption Trends

# Grouping daily and monthly
daily = df.groupby('Date')[['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']].sum()
monthly = df.groupby('Month')[['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']].sum()

# Daily Trend
daily.plot(figsize=(15,6), title=" Daily Power Consumption Trends")
plt.ylabel("Power Usage")
plt.xlabel("Date")
plt.grid(True)
plt.show()

# Monthly Trend
monthly.plot(kind='bar', figsize=(12,6), title=" Monthly Power Consumption per Zone")
plt.ylabel("Total Power Usage")
plt.xlabel("Month")
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

#OBJECTIVE 4. Compare Average Power Usage Across Zones
avg_power = df[['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']].mean()

sns.barplot(x=avg_power.index, y=avg_power.values, palette='Set2')
plt.title('🔌 Average Power Consumption per Zone')
plt.ylabel('Average Power Usage')
plt.xlabel('Zone')
plt.show()

#OBJECTIVE 5. Wind Speed & Gas Diffusion Impact on Power
df['TotalPower'] = df['PowerConsumption_Zone1'] + df['PowerConsumption_Zone2'] + df['PowerConsumption_Zone3']

plt.figure(figsize=(14,6))

# Wind Speed
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='WindSpeed', y='TotalPower', color='teal')
plt.title("Wind Speed vs Total Power Consumption")
plt.xlabel("Wind Speed")
plt.ylabel("Power Usage")

# General Diffuse Flows
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='GeneralDiffuseFlows', y='TotalPower', color='orange')
plt.title("General Diffuse Flows vs Total Power Consumption")
plt.xlabel("Gas Diffusion (General Flows)")
plt.ylabel("Power Usage")

plt.tight_layout()
plt.show()
