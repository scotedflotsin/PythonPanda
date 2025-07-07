import pandas as pd



# getting data file for real aggregation data set

filePath = "../../Data/sample_Data.json"

Data = pd.read_json(filePath)

df = pd.DataFrame(Data)

print(df)



# Now we are going to implement aggregation

print(df.columns)

AvgPrice = df["price"].mean()
MinPrice = df["price"].min()
MaxPrice = df["price"].max()
SumPrice = df["price"].sum()

print(AvgPrice)
print(MinPrice)
print(MaxPrice)
print(SumPrice)


# Now task to show mobile name and price



name = df["name"]
price = df["price"]


NewDf = pd.DataFrame({"name":name,"price":price})
print(NewDf)



# Now task to get the mobile whose price is greater than 500
print("How many mobile's price ar greater than 500")
AbgMobileName = NewDf[NewDf["price"] > 500]

print(AbgMobileName)

