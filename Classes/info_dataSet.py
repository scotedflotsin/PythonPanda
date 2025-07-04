import pandas as pd

# 1- columns rows?
# 2- What type of?
# 3- missing data?
#
# info() is a method
#
# 1- no .of rows and column
# 2- column names
# 3- non-null counts
# 4- int64 float64 object
# 5- memory usage of the data frame


# getting the file and accessing the file information

fileData = pd.read_csv("/Users/harsh/PythonPanda/Data/sales_data_sample.csv",encoding = "latin1")
print(fileData.info())