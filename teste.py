# Criar um dicionário vazio para armazenar as listas
az = {}

# Adicionar listas ao dicionário usando letras do alfabeto como chaves
for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    az[letra] = []

# Adicionar uma lista adicional para 'lista'
az['lista'] = []

# Obter uma lista de todas as chaves no dicionário
keys = list(az.keys())

az[keys[0]].append(11111)
az[keys[0]].append(12222)

print(az['A'])
