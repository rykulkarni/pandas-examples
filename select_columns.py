'''
How to select specific columns and create new data frame

'''
import pandas as pd

# read the excel file. 
df = pd.read_excel ('sample.xlsx')
print (df)
'''
       Name            Email        Phone     City
0     Rajiv  rajiv@email.com  78787878787  Dharwad
1    Ramnik   ramnik@abc.net   8989898989   Nipani
2  Shailaja   shaila@kgl.com   7816671766    Kagal
'''

# Select specific columns from the data frame and create new data frame. 
new_df = df[['Name','City']]
print (new_df)
'''
       Name     City
0     Rajiv  Dharwad
1    Ramnik   Nipani
2  Shailaja    Kagal
'''
