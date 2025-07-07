import pandas as pd
from numpy.ma.core import outer

# .merge(df1, df2, on="Column name", how="type of join")
students = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

marks = pd.DataFrame({
    "id": [1, 2, 4],
    "score": [90, 80, 70]
})

result = pd.merge(students, marks, on="id", how="inner")  # only matching ids
result2 = pd.merge(result, students, on="id", how="outer")
print(result)
print(result2)



# concatenation

finalDF = pd.concat([students, marks], axis=1)
print(finalDF)