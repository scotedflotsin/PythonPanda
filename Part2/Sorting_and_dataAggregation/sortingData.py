import pandas as pd



# data sorting e.g Alphabetic order
# sorting value in one or more column


# df.sort_values(bg="Column name", True/False, inplace = True)



data = {
    "name": ["Arun", "Varun","Karan"],
    "age": [10, 20, 8],
    "salary": [40000, 30000, 1200000]
}


df = pd.DataFrame(data)

df.sort_values(by=["age", "salary"], ascending=[True, True], inplace=True)
print(df)

