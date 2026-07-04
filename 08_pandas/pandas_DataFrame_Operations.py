import pandas as pd

df = pd.read_csv('student.csv')
print(df)

# selecting a single row by index label
print(df.loc[0])

# selecting multiple rows by index label
print(df.loc[[0,2, 3]])

# select a single row by integer index
print(df.iloc[2])

# select multiple rows by integer index
print(df.iloc[2])

# Adding a new column in dataframe
df['phone_no'] = [10, 20, 30, 40]
print(df)

# Deleting the column
df = df.drop(columns=['phone_no'])
print(df)

# Adding a new column in dataframe where tou want
df.insert(3, 'phone_no', [10, 29, 30, 40])
print(df)

# rename the column name
df = df.rename(columns={"age" : "student_age"})
print(df)

# Deleting the column
del df['phone_no']
print(df)

# deleting a particular row from dataframe
df = df.drop(3)
print(df)

# Adding a new row in existing dataframe
df.loc[3] = [4, 'pinki', 28, 'Female', 'Bangalore']
print(df)

# update the values
df.loc[2, 'student_age'] = 71
print(df)

#updating the multiple values
df.loc[[0, 2], 'address'] = ['andaman', 'nicobar']
print(df)