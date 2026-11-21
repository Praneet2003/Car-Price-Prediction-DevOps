
import pandas as pd

df = pd.read_csv("dataset/used_cars.csv")

print("Dataset Shape:", df.shape)

print("\nUnique Fuel Types:")
print(df["Fuel_Type"].unique())

print("\nUnique Transmission Types:")
print(df["Transmission"].unique())

print("\nUnique Owner Types:")
print(df["Owner_Type"].unique())

print("\nUnique Locations:")
print(df["Location"].unique())

print("\nSample Mileage Values:")
print(df["Mileage"].head(15).tolist())

print("\nSample Engine Values:")
print(df["Engine"].head(15).tolist())

print("\nSample Power Values:")
print(df["Power"].head(15).tolist())

print("\nUnique Seats:")
print(df["Seats"].unique())

print("\nSample Car Names:")
print(df["Name"].head(20).tolist())
