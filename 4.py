import numpy as np

# Assuming house_data is a NumPy array with columns: [bedrooms, square_footage, sale_price]
# Adjust the column indices accordingly based on your actual data.

# Sample house_data (replace this with your actual data)
house_data = np.array([
    [3, 1500, 250000],
    [4, 1800, 300000],
    [5, 2000, 350000],
    [4, 1600, 280000],
    [3, 1400, 230000],
    [5, 2200, 400000],
])

# Step 1: Find indices of houses with more than four bedrooms
bedrooms_condition = house_data[:, 0] > 4
houses_more_than_four_bedrooms = house_data[bedrooms_condition]

# Step 2: Extract sale prices of houses with more than four bedrooms
sale_prices_more_than_four_bedrooms = houses_more_than_four_bedrooms[:, -1]

# Step 3: Calculate the average sale price
average_sale_price = np.mean(sale_prices_more_than_four_bedrooms)

# Step 4: Print or Use the Result
print("Average Sale Price of Houses with More Than Four Bedrooms:", average_sale_price)
