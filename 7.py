import pandas as pd

# Assuming you have a DataFrame named order_data
# Example data (replace this with your actual DataFrame)
order_data = pd.DataFrame({
    'CustomerID': [1, 1, 2, 3, 2, 3],
    'OrderDate': ['2022-01-01', '2022-01-02', '2022-01-01', '2022-01-03', '2022-01-02', '2022-01-04'],
    'ProductName': ['ProductA', 'ProductB', 'ProductA', 'ProductC', 'ProductB', 'ProductA'],
    'OrderQuantity': [2, 1, 3, 2, 4, 1]
})

# Convert 'OrderDate' column to datetime type
order_data['OrderDate'] = pd.to_datetime(order_data['OrderDate'])

# Calculate the total number of orders made by each customer
total_orders_by_customer = order_data.groupby('CustomerID')['OrderDate'].count()

# Calculate the average order quantity for each product
average_quantity_per_product = order_data.groupby('ProductName')['OrderQuantity'].mean()

# Find the earliest and latest order dates
earliest_order_date = order_data['OrderDate'].min()
latest_order_date = order_data['OrderDate'].max()

# Display the results
print("Total number of orders by each customer:")
print(total_orders_by_customer)

print("\nAverage order quantity for each product:")
print(average_quantity_per_product)

print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
