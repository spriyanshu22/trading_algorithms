# This code reads data from a csv file where the data for the 'Close' values is given 
# in column and then it calculated exponential moving average for specified no of days 
# the formula used is EMA(n) = close*(2/(n+1)) + EMA(n-1)*(2/(n+1))

import pandas as pd

# Define the number of days for the EMA
n = int(input("Enter the number of days for Exponential Moving Average calculation: "))

 
data = pd.read_csv("data.csv")   #taking the data form csv file


weight = 2 / (n + 1)  # Defining the smoothing factor

# Calculate the EMA using a for loop and mean()
ema = []
ema.append(data['Close'][0])    # setting the ema[0] (ema for first day) to closing value
for i in range(1, len(data)):
    ema.append(weight * data['Close'][i] + (1 - weight) * ema[i-1])

# Convert the ema list to a pandas Series
ema = pd.Series(ema)

# Print the EMA values
print(ema)