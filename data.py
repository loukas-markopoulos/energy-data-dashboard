import pandas as pd
import numpy as np 

df = pd.read_csv('Example Data.csv')

del df['Consumer Name']

data = np.array(df)

print(f'{data}')