'''
How to load data from a file and create data frame.

- read the excel file and create a data frame. 
- read CSV file and create data frame. 
'''
import pandas as pd

# read the excel file. 
df = pd.read_excel ('sample.xlsx')

# Print the data frame 
print (df)

# read the csv file. 
df = pd.read_csv ('sample.csv')

# Print the data frame 
print (df)