import pandas as pd

# Read the waste data from the CSV file
data = pd.read_csv("waste_data.csv")

# Group the data by waste type and calculate the total quantity
grouped_data = data.groupby("Waste Type").agg({"Quantity": "sum"}).reset_index()

"""# Debugging code: print out the grouped data and its shape
print(grouped_data)
print(grouped_data.shape)"""

# Calculate the total waste quantity
total_waste = grouped_data["Quantity"].sum()

# Calculate the percentage of each waste type
grouped_data["Percentage"] = grouped_data["Quantity"] / total_waste * 100

# Analyze plastic waste
plastic_waste = grouped_data.loc[grouped_data["Waste Type"] == "Plastics"]

# Print the results
print("Total Waste Quantity:", total_waste)
print(plastic_waste)
print("Plastic Waste Quantity:", plastic_waste["Quantity"].values[0])
print("Plastic Waste Percentage:", plastic_waste["Percentage"].values[0])

# Save the analysis to a new CSV file
grouped_data.to_csv("waste_analysis.csv", index=False)