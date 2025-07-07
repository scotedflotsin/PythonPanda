import pandas as pd



data = {"name": ["Ram",None,"Ghansyam", "Ramu", None,"Arya","Raj","Simran"],
        "age": [12,45,56,None,18,18,None,56],
        "salary": [40000,50000,None, 40000, 100000, 400000, 40040, 50000],
        "performaceScore": [23,45,34,5,5,34,5,56]
      }


df = pd.DataFrame(data)





# conditional filling
print("Filling age value in missing fields")


df["age"] = df["age"].fillna(df["age"].mean())
df["name"] = df["name"].fillna("Unknow")

print(df)











