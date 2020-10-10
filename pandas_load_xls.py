'''
How to load excel file and create data frame.

- read the excel file and create a data frame. 
'''
import pandas as pd

# read the excel file. 
df = pd.read_excel ('sample.xlsx')

# Print the data frame 
print (df)