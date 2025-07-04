# 1- How big is your dataset
# 2- What are the names of columns

# shapes and columns = Return a tuple

import pandas as pd


data = {"name": ["Ram","Alexgender","Ghansyam", "Ramu", "Ayushi","Arya","Raj","Simran"],
        "age": [12,45,56,67,18,18,34,56],
        "salary": [40000,50000,23000, 40000, 100000, 400000, 40040, 50000],
        "performaceScore": [23,45,34,5,5,34,5,56]
        }

# getting new file for idea


jsonData = pd.read_json("/Users/harsh/PythonPanda/Data/sample_Data.json", encoding="utf-8")

print(jsonData.shape)
print(jsonData.columns)


df = pd.DataFrame(data)

print("Shape of: ", df.shape)  # output : (8, 4)
print("Columns: ", df.columns)
print(df.head())
