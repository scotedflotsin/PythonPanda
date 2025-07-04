import pandas as pd


data = {"name": ["Ram","Alexgender","Ghansyam", "Ramu", "Ayushi","Arya","Raj","Simran"],
        "age": [12,45,56,67,18,18,34,56],
        "salary": [40000,50000,23000, 40000, 100000, 400000, 40040, 50000],
        "performaceScore": [23,45,34,5,5,34,5,56]
      }





df = pd.DataFrame(data)


# modification


# .loc[]
# df.loc[row_index, "Column Name"] = new value

df.loc[0, "salary"] = 550000
print(df)


