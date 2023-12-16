from collections import defaultdict

# Define a lista de volares:
lista = [3, 2, 4, 7, 3, 8, 2, 3, 8, 1]

# Define o objeto que armazenará os índices de cada elemento:
# keys = defaultdict(list);

# Percorre todos os elementos da lista:
for key, value in enumerate(lista):
    print(key, value)
    # Adiciona o índice do valor na lista de índices:
    # keys[value].append(key)

# # Exibe o resultado:
# for value in keys:
#     if len(keys[value]) > 1:
#         print(value, keys[value])
    
    