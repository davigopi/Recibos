import pandas as pd
import datetime
from components.tableManip import TableManip
from dateutil.relativedelta import relativedelta


class Date_weekly:
    def __init__(self, *args, **kwargs) -> None:
        self.dias_week = [
            'Segunda-feira',
            'Terça-feira',
            'Quarta-feira',
            'Quinta-feira',
            'Sexta-feira',
            'Sábado',
            'Domingo',
        ]
        self.meses = {
            '01': 'JANEIRO',
            '02': 'FEVEREIRO',
            '03': 'MARÇO',
            '04': 'ABRIL',
            '05': 'MAIO',
            '06': 'JUNHO',
            '07': 'JULHO',
            '08': 'AGOSTO',
            '09': 'SETEMBRO',
            '10': 'OUTUBRO',
            '11': 'NOVEMBRO',
            '12': 'DEZEMBRO'
        }
        self.year_weekly = []
        self.calend = []
        self.table: pd.DataFrame = pd.DataFrame()

    # 1º PASSO reconhecer os anos traves dos meses informados
    @property
    def year_weeklys(self):
        return None

    @year_weeklys.setter
    def year_weeklys(self, month):
        months = month
        # Obtém o ano atual
        year_current = datetime.datetime.now().year
        year_salve = year_current
        self.year_weekly.append(year_salve)
        data_months = datetime.datetime.now()
        while months > 0:
            data_months = data_months - relativedelta(months=1)
            year_data_months = data_months.year
            if year_salve != year_data_months:
                year_salve = year_data_months
                self.year_weekly.append(year_salve)
            months -= 1

    # 2º PASSO Criar a estrutura de dados com todos os dias de um year
    @property
    def create_weekYear_week_date(self):
        return None

    @create_weekYear_week_date.setter
    def create_weekYear_week_date(self, none):
        self.calend = []
        for years in self.year_weekly:
            data = datetime.date(years, 1, 1)  # primeiro dia do year
            iniciar_weeks = False
            while data.year == years:
                num_week = data.isocalendar()[1]
                if num_week == 1:
                    iniciar_weeks = True
                if iniciar_weeks is True:
                    num_dia_week = data.weekday()
                    dia_week = self.dias_week[num_dia_week]
                    data_formatada = data.strftime("%d/%m/%Y")
                    self.calend .append([num_week,
                                         dia_week,
                                         data_formatada
                                         ])
                data += datetime.timedelta(days=1)

    # 3º PASSO Organiza a estruturas por semanais colocando em listas
    @property
    def edit_weekYear_week_date_separate_week(self):
        return None

    @edit_weekYear_week_date_separate_week.setter
    def edit_weekYear_week_date_separate_week(self, none):
        calend = []
        calend_interno = []
        for num_week, dia_week, data in self.calend:
            calend_interno.append([num_week, dia_week, data])
            if dia_week == 'Domingo':
                calend.append(calend_interno)
                calend_interno = []
        if calend_interno != []:
            calend.append(calend_interno)
        self.calend = calend

    # 4º PASSO edita os valores da week anual para week mensal
    @property
    def edit_weekYear_week_date_separate_weekMonth(self):
        return None

    @edit_weekYear_week_date_separate_weekMonth.setter
    def edit_weekYear_week_date_separate_weekMonth(self, none):
        calend = []
        calend_interno = []
        ultimo_month = '01'
        variavel = 0
        for week_list in self.calend:
            for num_week, dia_week, data in week_list:
                calend_interno.append([dia_week, data])
                ''' O padrão ISO 8601 se o primeiro dia do year for uma
                quinta-feira, a week anterior é considerada a primeira'''
                if dia_week == 'Quinta-feira':
                    month = data.split("/")[1]
                    year = data.split("/")[2]
            if month != ultimo_month:
                variavel = num_week - 1
                ultimo_month = month
            if num_week == 1:
                variavel = 0
            num_week -= variavel
            name_month = self.meses.get(month)
            week_mth_year = str(num_week) + 'ª/' + name_month + '/' + year  # type: ignore # noqa
            mth_year = name_month + '/' + year  # type: ignore
            calend.append([calend_interno, week_mth_year, mth_year])
            calend_interno = []
        self.calend = calend
        # print(self.calend)

    # 5º PASSO organizar as informações em uma unica lista
    @property
    def edit_weekMonth_week_date(self):
        return self.calend

    @edit_weekMonth_week_date.setter
    def edit_weekMonth_week_date(self, none):
        calend = []
        for calend_interno, week_mth_year, mth_year in self.calend:
            for weekly, day in calend_interno:
                calend.append([week_mth_year, day, weekly, mth_year])
        self.calend = calend

    # 6º PASSO criar uma biblioteca com as informações e logo depois a tabela
    @property
    def create_table_weekMonth_week_date(self):
        return None

    @create_table_weekMonth_week_date.setter
    def create_table_weekMonth_week_date(self, List_colunms):
        tableManip = TableManip()
        # criar uma tabela vazia com as list_columns
        #        'N Semana Mes',   'Data semana',  'Dia semana', 'Mes ano'
        tableManip.create_table = List_colunms
        for week_mth_year, day, weekly, mth_year in self.calend:
            new_line = {List_colunms[0]: week_mth_year,
                        List_colunms[1]: day,
                        List_colunms[2]: weekly,
                        List_colunms[3]: mth_year, }
            tableManip.add_line_dictionary = new_line
        self.table = tableManip.table

    @property
    def return_year_weekly(self):
        return self.year_weekly

    @property
    def return_calend(self):
        return self.calend

    @property
    def return_table(self):
        return self.table


if __name__ == '__main__':
    # Criar o calendário para o year desejado (por exemplo, 2024)
    date_weekly = Date_weekly()
    date_weekly.year_weeklys = 24  # OBS VER PORQUE NAO ESTA PUZANDO AUTOMATICO
    date_weekly.create_weekYear_week_date = None
    date_weekly.edit_weekYear_week_date_separate_week = None
    date_weekly.edit_weekYear_week_date_separate_weekMonth = None
    date_weekly.edit_weekMonth_week_date = None
    date_weekly.create_table_weekMonth_week_date = None

    # Exemplo de como acessar os dias do calendário
    weekMonth_week_date = date_weekly.return_calend
    year_weekly = date_weekly.return_year_weekly
    table = date_weekly.return_table
    for var in weekMonth_week_date:
        print(var)
    print(year_weekly)
    print(table)
