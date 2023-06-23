import pandas as pd

# Create a pandas DataFrame with the waste data
data = pd.DataFrame({
    'Type of Waste': ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic'],
    'Source': ['Residential', 'Commercial', 'Industrial'],
    'Quantity (kg)': [1500, 800, 1200, 500, 2000, 1000, 500, 600, 800, 300, 100, 200]
})

# Write the DataFrame to a CSV file
data.to_csv('waste_data.csv', index=False)