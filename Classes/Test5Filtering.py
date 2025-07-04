#Gonna to learn how to run query
import pandas as pd


data = {"name": ["Ram","Alexgender","Ghansyam", "Ramu", "Ayushi","Arya","Raj","Simran"],
        "age": [12,45,56,67,18,18,34,56],
        "salary": [40000,50000,23000, 40000, 100000, 400000, 40040, 50000],
        "performaceScore": [23,45,34,5,5,34,5,56]

      }


fg = pd.DataFrame(data)

print(fg)


print("Gonna to access single column")

print("Single column")
col = fg["age"]
print(col)


print("Multiple columns")

cols = fg[["name", "age"]]
print(cols)



#>>>>>>>>>>>>>>>>>>>>>>>