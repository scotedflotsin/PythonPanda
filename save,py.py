import pandas as pd



data = {
    "name": ["harsh0", "harsh1", "harsh2", "harsh3", "harsh4", "harsh5"],
    "age": [12,34,56,77,67,56],
    "city": ["kanpur", "mumbai", "delhi", "Berlin", "London", " America"]
}


df = pd.DataFrame(data)



print(df)


df.to_csv("MineGenerated/sample_Data.csv",index=False)
df.to_json("MineGenerated/sample_Datajson.json")
df.to_excel("MineGenerated/sample_DataEx.xlsx",index=False)



# read the following file

excelMineGeneratedFile = pd.read_excel("MineGenerated/Sample_DataEx.xlsx")



print("Excel file data is hare\n",excelMineGeneratedFile)

