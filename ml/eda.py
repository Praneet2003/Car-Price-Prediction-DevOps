
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/cleaned_cars.csv")

sns.set_theme(style="whitegrid")

# 1. Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Price"], bins=40, kde=True)
plt.title("Car Price Distribution")
plt.xlabel("Price (in Lakhs)")
plt.show()

# 2. Average Price by Fuel Type
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Fuel_Type", y="Price", errorbar=None)
plt.title("Average Price by Fuel Type")
plt.show()

# 3. Average Price by Transmission
plt.figure(figsize=(6, 5))
sns.barplot(data=df, x="Transmission", y="Price", errorbar=None)
plt.title("Average Price by Transmission")
plt.show()

# 4. Price vs Manufacturing Year
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Year", y="Price", alpha=0.5)
plt.title("Car Price vs Manufacturing Year")
plt.show()

# 5. Engine vs Price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Engine", y="Price", alpha=0.5)
plt.title("Engine Capacity vs Price")
plt.show()

# 6. Power vs Price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Power", y="Price", alpha=0.5)
plt.title("Power vs Price")
plt.show()

# 7. Top 10 Brands by Average Price
brand_price = (
    df.groupby("Brand")["Price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 5))
sns.barplot(data=brand_price, x="Price", y="Brand", errorbar=None)
plt.title("Top 10 Brands by Average Car Price")
plt.show()
