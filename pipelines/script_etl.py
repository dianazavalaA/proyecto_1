import pandas as pd

#Creación de dataframe
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df.to_csv('data_mkt.csv', index=False)