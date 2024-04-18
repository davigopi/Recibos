import pandas as pd

# Suponha que você tenha um DataFrame chamado df
df = pd.DataFrame({'A': ['foo', 'bar', 'baz'], 'B': ['123', '456', '789']})

# Juntando as colunas 'A' e 'B' em uma nova coluna 'C'
df['C'] = df['A'] + df['B']

# Exibindo o DataFrame com a nova coluna 'C'
print(df)
