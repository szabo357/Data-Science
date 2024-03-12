import numpy as np

# Example 1
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe dictionary
for country, capital in europe.items() :
    print("the capital of " + country + " is " + capital)


np_height = [74, 74, 72, 73, 74, 75, 75, 73]
arr =np.array(np_height)
