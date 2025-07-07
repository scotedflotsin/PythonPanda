import pandas as pd



data = {"day": ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday"],
        "time": [34,45,56,34,56,75]
        }

# making dataframe

df = pd.DataFrame(data)

print(df)