import time


class Date_month:
    def __init__(self, *args, **kwargs) -> None:

        self.meses_int = {
            1: 'JANEIRO',
            2: 'FEVEREIRO',
            3: 'MARÇO',
            4: 'ABRIL',
            5: 'MAIO',
            6: 'JUNHO',
            7: 'JULHO',
            8: 'AGOSTO',
            9: 'SETEMBRO',
            10: 'OUTUBRO',
            11: 'NOVEMBRO',
            12: 'DEZEMBRO'
        }

        self.meses_ext = {
            'JANEIRO': 1,
            'FEVEREIRO': 2,
            'MARÇO': 3,
            'ABRIL': 4,
            'MAIO': 5,
            'JUNHO': 6,
            'JULHO': 7,
            'AGOSTO': 8,
            'SETEMBRO': 9,
            'OUTUBRO': 10,
            'NOVEMBRO': 11,
            'DEZEMBRO': 12
        }

    def sum_less_month(self, valor_sum_less, ata_pag, ata_venc):
        num_month_full: int = 0
        num_month = int(valor_sum_less)
        for chave, valor in self.meses_int.items():
            if valor in ata_pag:
                break
        new_month = chave
        new_year = int(ata_pag[-4:])
        while True:
            num_month_full += num_month
            new_month = new_month + num_month
            if new_month > 12:
                new_month = 1
                new_year = new_year + 1
            elif new_month < 1:
                new_month = 12
                new_year = new_year - 1
            else:
                new_year = new_year
            new_month_in_full = self.meses_int[new_month]
            test_ata_pag = new_month_in_full + '/' + str(new_year)
            if test_ata_pag == ata_venc:
                break
        num_month_full *= -1
        return num_month_full

    def sum_month_ata_pag_parc(self, ata_pag_parc):
        for chave, valor in self.meses_int.items():
            if valor in ata_pag_parc:
                break
        list_new_ata_pag_parc = []
        valor_sum = 1
        while True:
            new_month = chave + valor_sum
            new_year = int(ata_pag_parc[-4:])
            if new_month > 12:
                new_month = new_month - 12
                new_year = new_year + 1
            else:
                new_year = new_year
            new_month_in_full = self.meses_int[new_month]
            new_ata_pag_parc = new_month_in_full + '/' + str(new_year)
            list_new_ata_pag_parc.append(new_ata_pag_parc)
            if valor_sum == 1:
                valor_sum = 2
                continue
            break
        return list_new_ata_pag_parc
    
    def list_month_year(self, date):
        list_month_year = []
        month = int(date.month())
        year = int(date.year())
        n_months = 60
        while True:
            word_month_year = self.meses_int[month] + ' de ' + str(year)
            list_month_year.append(word_month_year)
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            n_months -= 1
            if n_months == 0:
                break
        return list_month_year

    def discover_n_months(self, month_year, date):
        n_months = 0
        month_ext = ''
        year_ext = ''
        n_space = 0
        for letter in month_year:
            if letter == ' ':
                break
            month_ext += letter
        for letter in month_year:
            if letter == ' ':
                n_space += 1
                continue
            if n_space <= 1:
                continue
            year_ext += letter
        month_int = self.meses_ext[month_ext]
        year_int = int(year_ext)
        month =date.month()
        year = date.year()
        while True:
            if month == month_int and year == year_int:
                break
            n_months += 1
            month_int += 1
            if month_int > 12:
                month_int = 1
                year_int += 1
        return n_months

    def discover_month_year(self, ata_month_year):
        month_condition = False
        year_ext = ''
        month_ext = ''
        for letter in ata_month_year:
            if letter == ' ':
                month_condition = True
                continue
            if month_condition:
                year_ext += letter
            else:
                month_ext += letter
        month_int = self.meses_ext[month_ext]
        year_int = int(year_ext)
        return month_int, year_int