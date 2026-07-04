import pandas as pd

# std_data = [(1, 'varun', 30, 'male', 'chandigarh'),
#             (2, 'ravi', 31, 'male', 'delhi'),
#             (3, 'preeti', 29, 'female', 'jaipur'),
#             (4, 'amrit', 32, 'male', 'mumbai')]
# df = pd.DataFrame(std_data, columns=['stud_ID', 'name', 'age', 'gender', 'address'])
# print(df)

df = pd.read_csv("student.csv")
print(df)

print(df.head()) # by default show top 5 rows
print(df.head(2)) # show top 2 rows

print(df.tail()) # by default show bottom 5 rows
print(df.tail(2)) # show bottom 2 rows

print(df.shape) # no of rows and number of columns

print(df.columns) # print the first main row that has column names

print(df.size)

print(df.values)

print(df.dtypes)

var = df['age']
print(var)

var = df[['age', 'address']]
print(var)

var = df.index
print(var)