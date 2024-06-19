import pandas as pd

# Definindo as tabelas de exemplo
tabela1 = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})
tabela2 = pd.DataFrame({'coluna1': [3, 4, 5], 'coluna2': ['d', 'e', 'f']})

# Unindo as tabelas lado a lado (assumindo que as colunas sejam iguais)
tabela_unida = pd.concat([tabela1, tabela2], ignore_index=True)
print(tabela_unida)

# Realizando um inner join padrão (juntando linhas com valores iguais na coluna1)
tabela_unida = tabela1.merge(tabela2, on='coluna1')
print(tabela_unida)

# Realizando um left join (incluindo todas as linhas da tabela1 e as
# linhas correspondentes da tabela2)
tabela_unida = tabela1.merge(tabela2, how='left', on='coluna1')
print(tabela_unida)

# Realizando um right join (incluindo todas as linhas da tabela2 e as
# linhas correspondentes da tabela1)
tabela_unida = tabela1.merge(tabela2, how='right', on='coluna1')
print(tabela_unida)

# Realizando um outer join (incluindo todas as linhas de ambas as tabelas,
# com valores NaN nas colunas sem correspondência)
tabela_unida = tabela1.merge(tabela2, how='outer', on='coluna1')
print(tabela_unida)

# Realizando um cross join (criando um novo produto cartesiano com todas
# as combinações de linhas das tabelas)
tabela_unida = tabela1.merge(tabela2, how='cross')
print(tabela_unida)
