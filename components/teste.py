from datetime import datetime
import calendar
from time import sleep


def semana_do_mes(data):
  # Obter o dia da semana (0 = segunda-feira, 6 = domingo)
  dia_da_semana = data.weekday()

  # Ajustar o dia da semana para começar do domingo (0 = domingo, 6 = sábado)
  dia_da_semana = (dia_da_semana + 1) % 7

  # Calcular o número da semana do mês
  print('dia_da_semana', dia_da_semana)
  print('data.day', data.day)
  print('(data.day + dia_da_semana - 1) // 7 ', ((data.day + dia_da_semana - 1) // 7))

  semana_do_mes = (data.day + dia_da_semana - 1) // 7 + 1

  return semana_do_mes


# Exemplo de uso
data_exemplo = datetime(2024, 3, 31)  # Data de exemplo (15 de março de 2024)
semana = semana_do_mes(data_exemplo)
print(f"A data {data_exemplo.strftime('%d/%m/%Y')} pertence à semana {semana} do mês.")


print('#################################')


import datetime

# Definindo os nomes dos dias da semana
dias_semana = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado',
    'Domingo',
]


# Criar a estrutura de dados com todos os dias de um ano
def criar_calendario(list_ano):
  calendario = []
  for anos in list_ano:
    data = datetime.date(anos, 1, 1)  # primeiro dia do ano
    iniciar_semanas = False
    while data.year == anos:
      num_semana = data.isocalendar()[1]
      if num_semana == 1:
        iniciar_semanas = True
      if iniciar_semanas is True:
        num_dia_semana = data.weekday()
        dia_semana = dias_semana[num_dia_semana]
        data_formatada = data.strftime("%d/%m/%Y")
        calendario.append([num_semana,
                          dia_semana,
                          data_formatada
                           ])
      data += datetime.timedelta(days=1)
  return calendario


# Organiza a estruturas por semans
def separa_calendario_semanas(calendario_ano):
  calendario = []
  calendario_interno = []
  for num_semana, dia_semana, data in calendario_ano:
    calendario_interno.append([num_semana, dia_semana, data])
    if dia_semana == 'Domingo':
      calendario.append(calendario_interno)
      calendario_interno = []
  if calendario_interno != []:
    calendario.append(calendario_interno)
  return calendario


# edita os valores da semana anual para semana mensal
def editar_calendario_semanas_mes(calend_ano_semanas):
  calendario = []
  calendario_interno = []
  ultimo_mes = '01'
  variavel = 0
  for semana_list in calend_ano_semanas:
    for num_semana, dia_semana, data in semana_list:
      calendario_interno.append([dia_semana, data])
      ''' O padrão ISO 8601 se o primeiro dia do ano for uma quinta-feira,
      a semana anterior é considerada a primeira'''
      if dia_semana == 'Quinta-feira':
        mes = data.split("/")[1]
    if mes != ultimo_mes:
      variavel = num_semana - 1
      ultimo_mes = mes
    if num_semana == 1:
      variavel = 0
    num_semana -= variavel
    calendario.append([calendario_interno, num_semana])
    calendario_interno = []
  return calendario


# Criar o calendário para o ano desejado (por exemplo, 2024)
ano_desejado = [2023, 2024]
calendario_ano = criar_calendario(ano_desejado)
calend_ano_semanas = separa_calendario_semanas(calendario_ano)
calend_ano_semanas_mes = editar_calendario_semanas_mes(calend_ano_semanas)

# Exemplo de como acessar os dias do calendário
for semana in calend_ano_semanas_mes:
  print(semana)


print('##########################')

# data = datetime.datetime.now().date()
# print(data.isocalendar())
print(calendar.monthrange(2024, 2)[1])
