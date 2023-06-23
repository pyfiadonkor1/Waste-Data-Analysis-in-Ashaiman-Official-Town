import pandas as pd
import matplotlib.pyplot as plt

# Read the waste data from the CSV file
data = pd.read_csv("waste_data.csv")

# Group the data by waste type and calculate the total quantity
grouped_data = data.groupby("Waste Type").agg({"Quantity": "sum"}).reset_index()

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

# Create a bar chart
bar_chart_data = data.groupby(["Date", "Waste Type"]).agg({"Quantity": "sum"}).reset_index()
bar_chart_data.pivot(index="Date", columns="Waste Type", values="Quantity").plot(kind="bar", stacked=True)
plt.xlabel("Date")
plt.ylabel("Quantity")
plt.title("Waste Collected by Date and Type")
plt.legend(title="Waste Type")
plt.show()

"""# Create a pie chart
grouped_data.plot(kind="pie", y="Percentage", autopct="%.1f%%", labels=grouped_data["Waste Type"],
            legend=False, title="Total Waste Quantity by Type")
plt.ylabel("")
plt.show()"""