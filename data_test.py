import pandas as pd 

data = pd.read_csv('Data.csv', header = 1)
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)

print(data)

print(data['Month'])

for column in data.columns:
    print(column)