import numpy as np

# Example data (replace this with your actual dataset)
fuel_efficiency = np.array([25, 30, 28, 22, 35, 26, 31, 29])

# Calculate the average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", average_fuel_efficiency)

# Example fuel efficiency values for two car models
fuel_efficiency_model_A = 25
fuel_efficiency_model_B = 30

# Calculate the percentage improvement
percentage_improvement = ((fuel_efficiency_model_B - fuel_efficiency_model_A) / fuel_efficiency_model_A) * 100
print("Percentage Improvement:", percentage_improvement, "%")
