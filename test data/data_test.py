import pandas as pd 
import plotly.express as px
import numpy as np

data = pd.read_csv('Data.csv', header = 1)
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)

print(data)

df_2_1 = data

# jan = df_2_1.loc[1]
# length = jan.count()
# jan = jan[(length - 122):(length - 61)]
# new = pd.DataFrame([jan])
# new = new.T
# print(new)

selected_month = "JAN"

for i in range(12):
        if df_2_1.loc[i]['Month'] == selected_month:
            month_data = df_2_1.loc[i]
            length = month_data.count()
            if month_data.iloc[-1] == 0:
                filtered_month_data = month_data[(length - 122):(length - 61)]
            else:
                filtered_month_data = month_data[(length - 61):length]

            df_2_2 = pd.DataFrame([filtered_month_data])
            df_2_2 = df_2_2.T
            df_2_2 = df_2_2.rename(columns={df_2_2.columns[0]: 'Consumption'})
            sorted_df = df_2_2.sort_values(by='Consumption', ascending=False)

print(df_2_2.columns)
print(data.columns)
print(type(df_2_2))
print(type(data))
print(df_2_2)
print(sorted_df)
