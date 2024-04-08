from datetime
from dateutil.relativedelta import relativedelta

month = 24
months = month
# Obtém o ano atual
year_weekly = []
year_current = datetime.now().year
year_salve = year_current
year_weekly.append(year_salve)
data_months = datetime.now()
while months > 0:
    data_months = data_months - relativedelta(months=1)
    year_data_months = data_months.year
    if year_salve != year_data_months:
        year_salve = year_data_months
        year_weekly.append(year_salve)
    months -= 1
print(year_weekly)

# Exibe o ano atual
# print("Ano atual:", ano_atual)
