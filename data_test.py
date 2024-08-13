import pandas as pd 
from data import data
import plotly.express as px
import numpy as np

data = pd.read_csv('Data.csv', header = 1)
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)

print(data)

df_2_1 = data

print(df_2_1.loc[0])
jan = df_2_1.loc[0]
length = jan.count()
jan = jan[(length - 122):(length - 61)]
new = pd.DataFrame([jan])
print(new)


