import pandas as pd

data = {"name": ["Ram","Alexgender","Ghansyam", "Ramu", "Ayushi","Arya","Raj","Simran"],
        "age": [12,45,56,67,18,18,34,56],
        "salary": [40000,50000,23000, 40000, 100000, 400000, 40040, 50000],
        "performaceScore": [23,45,34,5,5,34,5,56]
      }


# way to adding column in dataset


df = pd.DataFrame(data)


# Square brc df["Name"] = SomeData


print(df)

# adding a column
df["Bonus"] = df["salary"] * 0.1
print(df)


print(">>>>>>>>>>> >>>>>>>>>>>>>>>>>> .>>>>>>>>>>>>>>>>>>>>")


# using insert() method

# df.insert[location, "Column name", data]



df.insert(2, "Hike", df["salary"]*0.2)

print(df)


# print("File creation and save")
#
# df.to_json("new_data.json", indent=4)
#
#
# fileOp = pd.read_json("new_data.json", encoding= "latin1")
#
# fileOp.to_excel("new_data.xlsx")
#
#
# print(fileOp)





# modification


# .loc[]
# df.loc[row_index, "Column Name"] = new value

df.loc[0, "salary"] = 550000
print(df)









