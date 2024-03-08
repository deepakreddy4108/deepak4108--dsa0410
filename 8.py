import pandas as pd

# Assuming you have a DataFrame named sales_data
# Example data (replace this with your actual DataFrame)
sales_data = pd.DataFrame({
    'ProductID': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'ProductName': ['ProductA', 'ProductB', 'ProductC', 'ProductA', 'ProductB', 'ProductC', 'ProductA', 'ProductB', 'ProductC'],
    'QuantitySold': [10, 15, 8, 12, 20, 5, 18, 10, 7],
    'Date': pd.to_datetime(['2024-02-01', '2024-02-01', '2024-02-01', '2024-02-02', '2024-02-02', '2024-02-02', '2024-02-03', '2024-02-03', '2024-02-03'])
})

# Filter data for the past month
start_date = pd.Timestamp.now() - pd.DateOffset(days=30)
filtered_data = sales_data[sales_data['Date'] >= start_date]

# Group by product and sum the quantities sold
product_sales = filtered_data.groupby('ProductName')['QuantitySold'].sum()

# Find the top 5 products
top_5_products = product_sales.nlargest(5)

# Display the results
print("Top 5 products sold the most in the past month:")
print(top_5_products)
