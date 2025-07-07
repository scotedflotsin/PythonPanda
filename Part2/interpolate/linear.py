import pandas as pd

data = {"name": ["Ram",None,"Ghansyam", "Ramu", None,"Arya","Raj","Simran"],
        "age": [12,45,None,67,None,18,34,56],
        "salary": [40000,50000,None, 40000, 100000, 400000, 40040, 50000],
        "performanceScore": [23,45,34,5,5,34,5,56]
      }



df = pd.DataFrame(data)
print("Before interpolate")

df["age"] = df["age"].interpolate(method = "linear")
df["salary"] = df["salary"].interpolate(method = "linear")

print("After interpolate")

print(df)
