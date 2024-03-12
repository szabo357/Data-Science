import pandas as pd


brics = pd.read_csv("datasets/brics.csv", index_col= 0)


# It prints only the header names
for val in brics :
    print(val)


# This prints the headers with the rows data.
for lab, row in brics.iterrows():
    print(lab)
    print(row)


# This only prints the capital of each row.
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])


# Adding a column to pandas DF. ( Not efficient in large datasets)
# for lab, row in brics.iterrows():
#     # - Creating a series on every iteration
#     brics.loc[lab, "name_length"] = len(row["country"])
# print(brics)


# Better approach on how to add a new column to df without a loop.
brics["name_length"] = brics["country"].apply(len)
print(brics)



# Import cars data
import pandas as pd
cars = pd.read_csv('datasets/cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)


for lab, row in cars.iterrows():
    print( lab + ": " + str(row["cars_per_cap"]) )


# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)