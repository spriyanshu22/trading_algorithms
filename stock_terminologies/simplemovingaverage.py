# This code reads data from a csv file where the data for the close values is given 
# in column and then it calculated simple moving average for specified no of days 
import pandas as pd

# Define the number of days for the SMA
n = int(input("Enter the number of days for Simple Moving Average calculation: "))

 
df = pd.read_csv("data.csv")   #taking the data form csv file

sma = df['Close'].rolling(n).mean() #the rollong function creates as rolling window 
                                    #of specified size and mean calculates average of the close values

# Print the SMA values
print(sma)