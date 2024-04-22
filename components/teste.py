import pandas as pd

# DataFrame esquerdo
df1 = pd.DataFrame({
    'nome': ['davi', 'debora', 'samuel'],
    'idade': [25, 30, 28]
})
# DataFrame direito
df2 = pd.DataFrame({
    'coluna_comparada': ['davi gomes pinheiro', 'caio lima', 'samuel ferreira lessa'],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
})

# Adicionando uma nova coluna em df1 para verificar se o nome está em coluna_comparada
df1['nome_em_coluna_comparada'] = df1['nome'].apply(lambda x: x in df2['coluna_comparada'].values)

# Mesclando os DataFrames usando a nova coluna temporária
merged_df = df1.merge(
    df2,
    how='left',
    left_on='nome_em_coluna_comparada',
    right_index=True,
    indicator=True)

print(merged_df)
