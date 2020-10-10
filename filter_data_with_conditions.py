'''
How to filter the data using differnt conditions

'''
import pandas as pd

# read the csv file. 
df = pd.read_csv ('sample.csv')
print (df)
'''
       Name            Email        Phone     City
0     Rajiv  rajiv@email.com  78787878787  Dharwad
1    Ramnik   ramnik@abc.net   8989898989   Nipani
2  Shailaja   shaila@kgl.com   7816671766    Kagal
..
..
6      Andy G  andy.g@ank.co.uk    9878676447     Noida

'''

# Select rows with a filter applied on a single column
new_df = df[df['Name'].str.contains('Raj')]
print (new_df)
'''
  Name            Email        Phone      City
0      Rajiv  rajiv@email.com  78787878787   Dharwad
3  Rajeshwar       raj@in.net  97771554676  Kolhapur
'''

# Select rows with a filter applied on a muliple columns
new_df = df[df['Name'].str.contains('Raj') & df['City'].str.contains('kolhapur', case=False)]
print (new_df)
'''
        Name       Email        Phone      City
3  Rajeshwar  raj@in.net  97771554676  Kolhapur
'''

# Select rows with a filter applied on a muliple columns with negative condition. 
new_df = df[df['Name'].str.contains('Raj') & ~df['City'].str.contains('kolhapur', case=False)]
print (new_df)
'''
    Name            Email        Phone     City
0  Rajiv  rajiv@email.com  78787878787  Dharwad
'''