
import pandas as pd

# Load dataset
df = pd.read_csv("dataset/used_cars.csv")

# Drop unnecessary columns
df = df.drop(columns=["Unnamed: 0", "New_Price"])

# Extract car brand from Name
df["Brand"] = df["Name"].str.split().str[0]

# Drop original Name column
df.drop(columns=["Name"])

# Convert Mileage into numeric values
df["Mileage"] = df["Mileage"].str.extract(r"(\d+\.?\d*)").astype(float)

# Convert Engine into numeric values
df["Engine"] = df["Engine"].str.extract(r"(\d+\.?\d*)").astype(float)

# Convert Power into numeric values
df["Power"] = df["Power"].str.extract(r"(\d+\.?\d*)").astype(float)

# Replace invalid Seats values
df.loc[df["Seats"] == 0, "Seats"] = None

# Handle missing values
for col in ["Mileage", "Engine", "Power", "Seats"]:
    df[col] = df[col].fillna(df[col].median())

# Save cleaned dataset
df.to_csv("dataset/cleaned_cars.csv", index=False)

print("Data Cleaning Completed!")
print("\nCleaned Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nCleaned Dataset:")
print(df.head())

print("\nData Types:")
print(df.dtypes)
