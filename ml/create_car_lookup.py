
import pandas as pd

df = pd.read_csv("dataset/used_cars.csv")

# Extract brand from car name
df["Brand"] = df["Name"].str.split().str[0]

# Extract numeric specifications
df["Mileage"] = df["Mileage"].str.extract(r"(\d+\.?\d*)").astype(float)
df["Engine"] = df["Engine"].str.extract(r"(\d+\.?\d*)").astype(float)
df["Power"] = df["Power"].str.extract(r"(\d+\.?\d*)").astype(float)

# Keep only the required car details
lookup = df[
    [
        "Name",
        "Brand",
        "Fuel_Type",
        "Transmission",
        "Mileage",
        "Engine",
        "Power",
        "Seats"
    ]
].drop_duplicates(subset=["Name"])

# Remove records with incomplete specifications
lookup = lookup.dropna(
    subset=["Mileage", "Engine", "Power", "Seats"]
)

# Save lookup file
lookup.to_csv("dataset/car_specs.csv", index=False)

print("Car specification lookup created!")
print("Total car variants:", len(lookup))
print(lookup.head())
