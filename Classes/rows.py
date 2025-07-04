# head() and tail()



# head(n)   it will display the starting rows on the basis of the value of n otherwise return first 5 rows
# tail(n)    it will display the ending rows on the basis of the value of n otherwise return last 5 rows

import pandas as pd



df = pd.read_csv("/Users/harsh/PythonPanda/Data/sales_data_sample.csv", encoding="latin1")
print(df.head())



print("First rows of data:")
print(df.head())

print("Last rows of data:")

print(df.tail())