import pandas as pd



data = {"name": ["Ram","Alexgender","Ghansyam", "Ramu", "Ayushi","Arya","Raj","Simran"],
        "age": [12,45,56,67,18,18,34,56],
        "salary": [40000,50000,23000, 40000, 100000, 400000, 40040, 50000],
        "performaceScore": [23,45,34,5,5,34,5,56]

      }

# single condition
df = pd.DataFrame(data)

high_salary = df[df["salary"]>50000]

print(high_salary)

print(">>>>>>>>>>>>>>>>>>MULTIPLE CONDITIONS AND USING AND OPERATOR>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


#Multiple condition using AND
condition2 = df[(df["salary"] > 40000) & (df["age"] > 20)]
print(condition2)


# Or condition

print(">>>>>>>>>>>>>>>>>>MULTIPLE CONDITIONS AND USING OR OPERATOR>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

condition3 = df[(df["age"]>20) | (df["performaceScore"] > 20)]
print(condition3)
