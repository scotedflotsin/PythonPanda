import pandas as pd


# NaN not a number
# None for object data type
# first to identify the location where data is null


# isNull()
# true NaN is missing
# false nothing is not missing


# apply


data = {"name": ["Ram",None,"Ghansyam", "Ramu", "","Arya","Raj","Simran"],
        "age": [12,45,56,67,18,18,34,56],
        "salary": [40000,50000,None, 40000, 100000, 400000, 40040, 50000],
        "performaceScore": [23,45,34,5,5,34,5,56]
      }



df = pd.DataFrame(data)

print(df)


print(df.isnull().sum())  # count of missing value
print(df.isnull())
