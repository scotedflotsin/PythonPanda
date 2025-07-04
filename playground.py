import pandas as pd

# rad data from CSV file

##df = pd.read_csv('Data/sales_data_sample.txt', encoding="latin1")

df = pd.read_json("Data/sample_Data.json")



print(df)


