# Example data (replace these with your actual item prices, quantities, discount rate, and tax rate)
item_prices = [2.5, 1.0, 3.5, 4.0]
quantities = [3, 2, 1, 4]
discount_rate = 10  # 10% discount
tax_rate = 8       # 8% tax

# Calculate the total cost before discounts and taxes
subtotal = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))

# Calculate the total discount
total_discount = (discount_rate / 100) * subtotal

# Calculate the discounted subtotal
discounted_subtotal = subtotal - total_discount

# Calculate the total tax
total_tax = (tax_rate / 100) * discounted_subtotal

# Calculate the final total cost
total_cost = discounted_subtotal + total_tax

# Display the results
print("Subtotal:", subtotal)
print("Total Discount:", total_discount)
print("Discounted Subtotal:", discounted_subtotal)
print("Total Tax:", total_tax)
print("Total Cost:", total_cost)
