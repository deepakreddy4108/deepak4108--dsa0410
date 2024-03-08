import pandas as pd

# Sample data (replace this with your actual DataFrame)
data = {'property ID': [1, 2, 3, 4, 5],
        'location': ['A', 'B', 'A', 'C', 'B'],
        'number of bedrooms': [3, 4, 5, 3, 4],
        'area in square feet': [1500, 1800, 2200, 1600, 2000],
        'listing price': [200000, 250000, 300000, 180000, 280000]}

property_data = pd.DataFrame(data)

# Average Listing Price of Properties in Each Location
average_price_by_location = property_data.groupby('location')['listing price'].mean()
print("Average Listing Price by Location:\n", average_price_by_location)

# Number of Properties with More Than Four Bedrooms
properties_more_than_four_bedrooms = property_data[property_data['number of bedrooms'] > 4]
num_properties_more_than_four_bedrooms = len(properties_more_than_four_bedrooms)
print("\nNumber of Properties with More Than Four Bedrooms:", num_properties_more_than_four_bedrooms)

# Property with the Largest Area
property_with_largest_area = property_data.loc[property_data['area in square feet'].idxmax()]
print("\nProperty with the Largest Area:\n", property_with_largest_area)
