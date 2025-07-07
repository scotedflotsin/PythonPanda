import pandas as pd

data = {"name": ["Ram","Alexgender","Ghansyam", "Ramu", "Ayushi","Arya","Raj","Simran"],
        "age": [12,45,56,67,18,18,34,56],
        "salary": [40000,50000,23000, 40000, 100000, 400000, 40040, 50000],
        "performaceScore": [23,45,34,5,5,34,5,56]
      }



finalDataSet = pd.DataFrame(data)


print("Remove the column")


# finalDataSet.drop(column = ["name","otherName", "MoreOtherName"], inplace = true)


finalDataSet.drop(columns=["salary"], inplace=True)

print(finalDataSet)

