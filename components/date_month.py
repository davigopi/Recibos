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
