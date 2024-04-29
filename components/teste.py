import pandas as pd

# Suponha que você tenha dois DataFrames: df1 e df2
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# Concatenar os DataFrames verticalmente (adicionar linhas)
concatenated_df = pd.concat([df1, df2])

# Exibir o DataFrame concatenado
print(concatenated_df)
