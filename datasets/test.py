# Initial testing code reading the cars dataset from datasets.
# extracting only the countries where drives_right is True
# Import cars data
import pandas as pd
cars = pd.read_csv('datasets/cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel =  cars[dr]

# Print sel
print(sel)