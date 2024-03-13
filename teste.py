# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html

# %a Dia da semana como nome abreviado do local. Dom, Seg,…, Sábado (en_US); Então, Mo, …, Sa (de_DE)
# %A Weekday como nome completo do local. Domingo, segunda-feira,…, sábado (en_US); Sonntag, Montag, …, Samstag (de_DE)
# %w Dia da semana como um número decimal, onde 0 é domingo e 6 é sábado. 0, 1,…, 6
# %d Dia do mês como um número decimal preenchido com zeros. 01, 02,…, 31
# %b Mês como nome abreviado do local. Janeiro, fevereiro,…, dezembro (en_US); Janeiro, fevereiro, …, dez (de_DE)
# %B Mês como nome completo do local. Janeiro, fevereiro,…, dezembro (en_US); Janeiro, fevereiro, …, dezembro (de_DE)
# %m Mês como um número decimal preenchido com zeros. 01, 02,…, 12
# %y Ano sem século como um número decimal preenchido com zeros. 00, 01,…, 99
# %Y Ano com século como número decimal. 0001, 0002,…, 2013, 2014,…, 9998, 9999
# %H Hora (relógio de 24 horas) como um número decimal preenchido com zeros. 00, 01,…, 23
# %I Hora (relógio de 12 horas) como um número decimal preenchido com zeros. 01, 02,…, 12
# %p O equivalente local a AM ou PM. AM, PM (en_US); manhã, tarde (de_DE)
# %M Minuto como um número decimal preenchido com zeros. 00, 01,…, 59
# %S Segundo como um número decimal preenchido com zeros. 00, 01,…, 59
# %f Microssegundo como um número decimal, preenchido com zeros até 6 dígitos. 000000, 000001,…, 999999
# %z deslocamento UTC no formato ±HHMM[SS[.ffffff]] (string vazia se o objeto for ingênuo). (vazio), +0000, -0400, +1030, +063415, -030712.345216
# %Z Nome do fuso horário (string vazia se o objeto for ingênuo). (vazio), UTC, GMT
# %j Dia do ano como um número decimal preenchido com zeros. 001, 002,…, 366
# %U Número da semana do ano (domingo como o primeiro dia da semana) como um número decimal preenchido com zeros. Todos os dias de um ano novo anterior ao primeiro domingo são considerados na semana 0. 00, 01,…, 53
# %W Número da semana do ano (segunda-feira como o primeiro dia da semana) como um número decimal preenchido com zeros. Todos os dias de um ano novo anteriores à primeira segunda-feira são considerados na semana 0. 00, 01,…, 53
# %c Representação apropriada de data e hora do local. Terça-feira, 16 de agosto, 21:30:00 1988 (en_US); Di 16 de agosto 21:30:00 1988 (de_DE)
# %x Representação de data apropriada do local. 16/08/88 (Nenhum); 16/08/1988 (en_US); 16.08.1988 (de_DE)
# Representação de tempo apropriada do %X local. 21:30:00 (en_US); 21:30:00 (de_DE)
# %% Um caractere literal '%'. %
# %G Ano ISO 8601 com século representando o ano que contém a maior parte da semana ISO (%V). 0001, 0002,…, 2013, 2014,…, 9998, 9999
# %u Dia da semana ISO 8601 como um número decimal, onde 1 é segunda-feira. 1, 2,…, 7
# %V Semana ISO 8601 como um número decimal com segunda-feira como o primeiro dia da semana. A semana 01 é a semana que contém 4 de janeiro. 01, 02,…, 53
# %:z Deslocamento UTC no formato ±HH:MM[:SS[.ffffff]] (string vazia se o objeto for ingênuo). (vazio), +00:00, -04:00, +10:30, +06:34:15, -03:07:12.345216


# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)



# pip install pytz types-pytz
# from datetime import datetime

from pytz import timezone

data = datetime.now()
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1670849077))
# data_str_data = '2022/04/20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)

print('##################################')


# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
# pip install python-dateutil types-python-dateutil
from dateutil.relativedelta import relativedelta

from datetime import timedelta


fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(delta.days, delta.years)
# print(data_fim - delta)
# print(data_fim)
# print(data_fim + relativedelta(seconds=60, minutes=10))

# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)

print('##################################')

# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(type(data.strftime('%Y')), data.strftime('%Y'),
       data.year, type(data.year))
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)

print('##################################')



# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

list_parcelas = []

for data in data_parcelas:
    list_parcelas.append([data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}'])

print(list_parcelas)
print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)


print('###################################')

# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

print(calendar.calendar(2022))
print(calendar.month(2022, 12))
print(calendar.monthrange(2022, 12))  # dia da semana que inicia o mes
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
print(list(enumerate(calendar.day_name)))
print(calendar.day_name[numero_primeiro_dia])
print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])
list_day = []
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        list_day.append(day)
print(list_day)

print('################################')


# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, '')  # local padrao do sistema operacional
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(calendar.calendar(2022))
print(locale.getlocale())
