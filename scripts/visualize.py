import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background')


# Read the merged data
df = pd.read_csv("data/merged_data.csv")

# Convert Date column to datetime, ignoring errors for bad values
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows where Date could not be parsed
df = df.dropna(subset=['Date'])

# Ensure Close column is numeric
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Optional: Fill NaN in sentiment columns with 0
for col in ['Positive', 'Negative', 'Neutral']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Sort by Date
df = df.sort_values(by='Date')

# Plot
plt.figure(figsize=(14,6))
sns.lineplot(x="Date", y="Close", data=df, label="Crude Oil Price", marker='o')

if 'Positive' in df.columns:
    sns.lineplot(x="Date", y="Positive", data=df, label="Positive News", marker='o')
if 'Negative' in df.columns:
    sns.lineplot(x="Date", y="Negative", data=df, label="Negative News", marker='o')
if 'Neutral' in df.columns:
    sns.lineplot(x="Date", y="Neutral", data=df, label="Neutral News", marker='o')

plt.xticks(rotation=45)
plt.title("Commodity Price vs Market News Sentiment")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.show()
