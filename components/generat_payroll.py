# from asyncio.windows_events import NULL
# from networkx import generate_adjlist
from numpy import number
import pandas as pd
from pathlib import Path
import json
# import math
from time import sleep
from pathlib import Path
# import math


class Generat_payroll:
    def __init__(self, *args, **kwargs) -> None:
        self.arqTableTeste = Path()

        self.column_vendedor = ''
        self.column_administradora = ''
        self.column_dt_pag_por = ''
        self.column_1p_referencia = ''
        self.column_credito = ''
        self.data_ata_single = ''
        self.seller_single = ''
        self.data_date_pay = ''
        self.solumn_cadastro = ''

        self.quantity_line_full = 0
        self.quantity_line_ata = 0
        self.quantity_line_weekly = 0
        # quantity_line_table = 0
        self.sum_credito = 0

        self.list_columns_str_to_float = []
        self.list_columns_full_ata = []
        self.list_columns_full_weekly = []
        self.list_columns_full_ata_entrega = []
        self.list_columns_full_ata_cadastro = []
        self.list_qtd_cotas_parc = []
        self.list_qtd_cotas_inicial = []
        self.list_qtd_cotas_final = []
        self.name_columns_full = []
        self.list_ata = []
        self.list_weekly = []
        self.list_columns_full_ata_single = []
        self.table_single_ata = []
        self.list_single_administradora = []
        self.list_administradora_line = []
        self.list_administradora_line_sum = []
        self.list_administradora_sum_qtdcotasinicial = []
        self.list_administradora_sum_qtdcotasinicial_parc = []

        self.table_full_single_ata = []

        self.dic_qtd_cotas_parc = {}
        self.dic_months = {}
        self.dic_administradoras = {}

        self.table: pd.DataFrame = pd.DataFrame()
        self.table_full: pd.DataFrame = pd.DataFrame()
        self.table_full_ata: pd.DataFrame = pd.DataFrame()
        self.table_full_weekly: pd.DataFrame = pd.DataFrame()
        self.table_single_merge: pd.DataFrame = pd.DataFrame()
        self.table_seller_single: pd.DataFrame = pd.DataFrame()

    # converter em float as columns string

    @property
    def convert_str_float(self):
        return self.table

    @convert_str_float.setter
    def convert_str_float(self, table):
        for column in self.list_columns_str_to_float:
            table.loc[:, column] = (table[column].str.replace('.', ''))
            table.loc[:, column] = (table[column].str.replace(',', '.'))
            table.loc[:, column] = (table[column].astype(float))
            table.loc[:, column] = (table[column].round(2))
        self.table = table

    # ira criar duas lista de todos os vendedores clt e parceiros
    def columns_to_list_full_seller(self):
        self.list_seller_ata = self.table_full_ata[self.column_vendedor]
        self.list_seller_ata = self.list_seller_ata.unique()
        self.list_seller_ata.sort()
        self.list_seller_weekly = self.table_full_weekly[self.column_vendedor]
        self.list_seller_weekly = self.list_seller_weekly.unique()
        self.list_seller_weekly.sort()
        for column_ata in self.list_columns_full_ata:
            for line in range(self.quantity_line_ata):
                data_ata = self.table_full_ata.iloc[line][column_ata]
                if data_ata not in self.list_ata and not pd.isna(data_ata):
                    self.list_ata.append(data_ata)
        for column_weekly in self.list_columns_full_weekly:
            for line in range(self.quantity_line_weekly):
                data_weekly = self.table_full_weekly.iloc[line][column_weekly]
                if data_weekly not in self.list_weekly and not pd.isna(
                        data_weekly):
                    self.list_weekly.append(data_weekly)
        self.list_ata = sorted(
            self.list_ata,
            key=lambda x: (
                x.split('/')[1], self.dic_months[x.split('/')[0]]
            )
        )
        self.list_weekly = sorted(
            self.list_weekly, key=lambda x: (
                x.split('/')[2], self.dic_months[x.split('/')[1]], x.split('/')[0]
            )
        )

    # define se vendedor/parceiro a primeira é pela ata entrea/cadastro
    def columns_ata_full_seller_single(self):
        p1_referencia = (
            self.table_seller_single.iloc[1][self.column_1p_referencia]
        )
        if self.solumn_cadastro in p1_referencia:
            list = self.list_columns_full_ata_cadastro
        else:
            list = self.list_columns_full_ata_entrega
        self.list_columns_full_ata_single = list

    # Criar uma lista tabelas aparti do dado ata e colunas definidas
    def tables_columns_ata_seller_single(self):
        for ata in self.list_columns_full_ata_single:
            table = self.table_seller_single[
                self.table_seller_single[ata] == self.data_ata_single
            ]
            self.table_single_ata.append([table, ata])

    # ira mesclar todas as tabelas que tiver valor
    def tables_concat_seller_single(self):
        for table, ata in self.table_single_ata:
            if not table.empty:
                self.table_single_merge = pd.concat(
                    [self.table_single_merge, table]
                )

    # pegar informações de valores da administradoras
    def create_dictionary_datas(self):
        self.list_single_administradora = self.table_single_merge[
            self.column_administradora].unique()
        for administradora in self.list_single_administradora:
            for line in range(self.quantity_line_full):
                data_administradora = self.table_single_merge.iloc[
                    line][self.column_administradora]
                if data_administradora == administradora:
                    self.dic_administradoras[administradora] = {}
                    for qtd_cotas in self.list_qtd_cotas_parc:
                        data = self.table_single_merge.iloc[line][qtd_cotas]
                        if not pd.isna(data):
                            self.dic_administradoras[
                                administradora][qtd_cotas] = data
                    break

    # @property
    # def line_column_administradoras_sell_single(self):
    #     return self.list_administradora_line

    # @line_column_administradoras_sell_single.setter
    def table_list_administradora_add_line(self):
        for table, ata in self.table_single_ata:
            if not table.empty:
                quantity_line_table = table.shape[0]
                list_administradora = table[self.column_administradora].unique()
                # print(quantity_line_table, '!!!!', list_administradora, '!!!!!')
                # print(table)
                list_admnimistradora_line = []
                for data_administradora in list_administradora:
                    for line in range(quantity_line_table):
                        data_administradora_2 = table.iloc[
                            line][self.column_administradora]
                        if data_administradora == data_administradora_2:
                            list_admnimistradora_line.append(
                                [data_administradora, line])
                            break
                self.list_administradora_line.append(
                    [table, ata, list_admnimistradora_line])
        # print(self.list_administradora_line)

    def table_list_administradora_line_add_sum(self):
        for table, ata, list_admnimistradora_line in self.list_administradora_line:
            quantity_line_table = table.shape[0]
            sums = 0
            for line in range(quantity_line_table):
                value = table.iloc[line][self.column_credito]
                value = value.replace('.', '')
                value = value.replace(',', '.')
                value = float(value)
                sums += value
            self.list_administradora_line_sum.append([
                table,
                ata,
                list_admnimistradora_line,
                sums
            ])
            # self.sum_credito = table[self.column_credito].sum() #nao funciona

    def table_list_administradora_sum_add_qtdcotasinicial(self):
        for table, ata, list_admnimistradora_line, sums in self.list_administradora_line_sum:
            list_administradora_qtdcotas = []
            for administradora_line in list_admnimistradora_line:
                data_administradora = administradora_line[0]
                line = administradora_line[1]
                for column_qtd_cota_inicial in reversed(
                        self.list_qtd_cotas_inicial):
                    value = table.iloc[line][column_qtd_cota_inicial]
                    value = value.replace('.', '')
                    value = value.replace(',', '.')
                    value = float(value)
                    if sums >= value:

                        column_qtd_cota_final = self.dic_qtd_cotas_parc[column_qtd_cota_inicial][0]
                        value_end = table.iloc[line][column_qtd_cota_final]
                        value_end = value_end.replace('.', '')
                        value_end = value_end.replace(',', '.')
                        value_end = float(value_end)
                        list_administradora_qtdcotas.append([
                            data_administradora,
                            column_qtd_cota_inicial,
                            value,
                            column_qtd_cota_final,
                            value_end
                        ])
                        break
            self.list_administradora_sum_qtdcotasinicial.append([
                table,
                ata,
                sums,
                list_administradora_qtdcotas
            ])

        # for column_qtd_cota_inicial in self.list_qtd_cotas_inicial:
        #     data_qtd_cota_inicial = self.dic_administradoras.iloc[
        #         line_table][column_qtd_cota_inicial]
        #     if data_qtd_cota_inicial >= self.sum_credito:
        #         break
        # return column_qtd_cota_inicial

    def prints(self):
        # print(self.list_seller_weekly)
        # print(self.list_weekly)
        # print(self.list_columns_full_ata_single)
        # print(self.table_single_ata)
        # print(self.table_single_merge)
        # print(self.list_single_administradora)
        # dic_administradoras_json = json.dumps(
        #     self.dic_administradoras, indent=4)
        # print(dic_administradoras_json)

        for table, ata, sum_credito, list_administradora_qtdcotas in self.list_administradora_sum_qtdcotasinicial:
            quantity_line_table = table.shape[0]
            number_ata = ''
            for key in range(7):
                key_ata = str(key)
                if key == 1:
                    number_ata = key_ata
                else:
                    if key_ata in ata:
                        number_ata = key_ata
            list_administradora_qtdcotas_parc = []
            for administradora_qtdcotas in list_administradora_qtdcotas:
                administradora = administradora_qtdcotas[0]
                column_qtdcotainicial = administradora_qtdcotas[1]
                data_qtdcotainicial = administradora_qtdcotas[2]
                column_qtdcotafinal = administradora_qtdcotas[3]
                data_qtdcotafinal = administradora_qtdcotas[4]
                list_column_parc = self.dic_qtd_cotas_parc[column_qtdcotainicial]
                for key2, column_parc in enumerate(list_column_parc):
                    if key2 == 0:  # tira a primeira coluna qtdcotafinal
                        continue
                    if number_ata in column_parc[-2:]:
                        break
                for line in range(quantity_line_table):
                    data_administradora = table.iloc[
                        line][self.column_administradora]
                    if administradora == data_administradora:
                        break
                porcentagem_ata = table.iloc[line][column_parc]
                list_administradora_qtdcotas_parc.append([
                    administradora,
                    column_qtdcotainicial,
                    data_qtdcotainicial,
                    column_qtdcotafinal,
                    data_qtdcotafinal,
                    column_parc,
                    porcentagem_ata
                ])
            self.list_administradora_sum_qtdcotasinicial_parc.append([
                table,
                ata,
                sum_credito,
                list_administradora_qtdcotas_parc
            ])
            # print(number_ata)
        for table, ata, sum_credito, list_administradora_qtdcotas_parc in self.list_administradora_sum_qtdcotasinicial_parc:
            print(
                ata,
                '      total: ',
                sum_credito)
            for administradora_qtdcotas_parc in list_administradora_qtdcotas_parc:
                print(administradora_qtdcotas_parc)
            print(table)
            print('#######################')


if __name__ == '__main__':
    from generat_payroll import Generat_payroll
    generat_payroll = Generat_payroll()

    pathTables = Path(__file__).parent.parent / 'tables'
    name_arq = 'table_teste.csv'
    arqTableTeste = pathTables / name_arq

    table_full = pd.read_csv(
        "tables\\tableMerge.csv",
        sep=';',
        encoding='utf-8',
        dtype=str
    )

    column_vendedor = 'Vendedor'
    column_administradora = 'Administradora'
    column_dt_pag_por = 'Dt pag. por'
    column_1p_referencia = '1P referencia'
    column_credito = 'Crédito'
    data_ata_single = 'MARÇO/2024'
    seller_single = 'MARIA ILLYEDJA RODRIGUES DE SOUZA '
    # seller_single = 'BRUNA ALINE DE AZEVEDO (ENIO)'
    data_date_pay = 'DIA DA SEMANA'
    solumn_cadastro = 'CADASTRO'

    list_qtd_cotas_inicial = [
        '1 Qtd. Cotas Inicial', '2 Qtd. Cotas Inicial', '3 Qtd. Cotas Inicial',
        '4 Qtd. Cotas Inicial', '5 Qtd. Cotas Inicial',
    ]
    list_qtd_cotas_final = [
        '1 Qtd. Cotas Final', '2 Qtd. Cotas Final', '3 Qtd. Cotas Final',
        '4 Qtd. Cotas Final', '5 Qtd. Cotas Final',
    ]

    list_columns_full_ata = [
        'ATA Entrega', 'ATA Cad Adm', 'ATA 2º Parc', 'ATA 3º Parc',
        'ATA 4º Parc', 'ATA 5º Parc', 'ATA 6º Parc'
    ]
    list_columns_full_weekly = [
        'Sem Ent', 'Sem Cad Adm', 'Sem 2º Parc', 'Sem 3º Parc',
        'Sem 4º Parc', 'Sem 5º Parc', 'Sem 6º Parc'
    ]
    list_qtd_cotas_parc = [
        '1 Qtd. Cotas Inicial', '1 Qtd. Cotas Final',
        '1 Parc 1', '1 Parc 2', '1 Parc 3', '1 Parc 4', '1 Parc 5',
        '1 Parc 6', '1 Parc 7', '1 Parc 8', '1 Parc 9', '1 Parc 10',
        '2 Qtd. Cotas Inicial', '2 Qtd. Cotas Final',
        '2 Parc 1', '2 Parc 2', '2 Parc 3', '2 Parc 4', '2 Parc 5',
        '2 Parc 6', '2 Parc 7', '2 Parc 8', '2 Parc 9', '2 Parc 10',
        '3 Qtd. Cotas Inicial', '3 Qtd. Cotas Final',
        '3 Parc 1', '3 Parc 2', '3 Parc 3', '3 Parc 4', '3 Parc 5',
        '3 Parc 6', '3 Parc 7', '3 Parc 8', '3 Parc 9', '3 Parc 10',
        '4 Qtd. Cotas Inicial', '4 Qtd. Cotas Final',
        '4 Parc 1', '4 Parc 2', '4 Parc 3', '4 Parc 4', '4 Parc 5',
        '4 Parc 6', '4 Parc 7', '4 Parc 8', '4 Parc 9', '4 Parc 10',
        '5 Qtd. Cotas Inicial', '5 Qtd. Cotas Final',
        '5 Parc 1', '5 Parc 2', '5 Parc 3', '5 Parc 4', '5 Parc 5',
        '5 Parc 6', '5 Parc 7', '5 Parc 8', '5 Parc 9', '5 Parc 10',
    ]

    dic_qtd_cotas_parc = {
        '1 Qtd. Cotas Inicial': [
            '1 Qtd. Cotas Final',
            '1 Parc 1', '1 Parc 2', '1 Parc 3', '1 Parc 4', '1 Parc 5',
            '1 Parc 6', '1 Parc 7', '1 Parc 8', '1 Parc 9', '1 Parc 10'
        ],
        '2 Qtd. Cotas Inicial': [
            '2 Qtd. Cotas Final',
            '2 Parc 1', '2 Parc 2', '2 Parc 3', '2 Parc 4', '2 Parc 5',
            '2 Parc 6', '2 Parc 7', '2 Parc 8', '2 Parc 9', '2 Parc 10'
        ],
        '3 Qtd. Cotas Inicial': [
            '3 Qtd. Cotas Final',
            '3 Parc 1', '3 Parc 2', '3 Parc 3', '3 Parc 4', '3 Parc 5',
            '3 Parc 6', '3 Parc 7', '3 Parc 8', '3 Parc 9', '3 Parc 10'
        ],
        '4 Qtd. Cotas Inicial': [
            '4 Qtd. Cotas Final',
            '4 Parc 1', '4 Parc 2', '4 Parc 3', '4 Parc 4', '4 Parc 5',
            '4 Parc 6', '4 Parc 7', '4 Parc 8', '4 Parc 9', '4 Parc 10'
        ],
        '5 Qtd. Cotas Inicial': [
            '5 Qtd. Cotas Final',
            '5 Parc 1', '5 Parc 2', '5 Parc 3', '5 Parc 4', '5 Parc 5',
            '5 Parc 6', '5 Parc 7', '5 Parc 8', '5 Parc 9', '5 Parc 10'
        ],
        '6 Qtd. Cotas Inicial': [
            '6 Qtd. Cotas Final',
            '6 Parc 1', '6 Parc 2', '6 Parc 3', '6 Parc 4', '6 Parc 5',
            '6 Parc 6', '6 Parc 7', '6 Parc 8', '6 Parc 9', '6 Parc 10'
        ]
    }
    dic_months = {
        'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4, 'MAIO': 5,
        'JUNHO': 6, 'JULHO': 7, 'AGOSTO': 8, 'SETEMBRO': 9, 'OUTUBRO': 10,
        'NOVEMBRO': 11, 'DEZEMBRO': 12
    }

    # variaveis criada atravez de outras

    list_columns_full_ata_entrega = [
        item for item in list_columns_full_ata if item != 'ATA Cad Adm']
    list_columns_full_ata_cadastro = [
        item for item in list_columns_full_ata if item != 'ATA Entrega']

    name_columns_full = table_full.columns.tolist()

    table_full_ata = table_full[table_full[column_dt_pag_por] != data_date_pay]
    table_full_weekly = table_full[
        table_full[column_dt_pag_por] == data_date_pay]
    table_seller_single = table_full[
        table_full[column_vendedor] == seller_single]

    quantity_line_full = table_full.shape[0]
    quantity_line_ata = table_full_ata.shape[0]
    quantity_line_weekly = table_full_weekly.shape[0]

    # exportar variaveis
    generat_payroll.arqTableTeste = arqTableTeste
    generat_payroll.table_full = table_full
    generat_payroll.column_credito = column_credito
    generat_payroll.column_administradora = column_administradora
    generat_payroll.column_vendedor = column_vendedor
    generat_payroll.column_dt_pag_por = column_dt_pag_por
    generat_payroll.column_1p_referencia = column_1p_referencia
    generat_payroll.data_ata_single = data_ata_single
    generat_payroll.seller_single = seller_single
    generat_payroll.data_date_pay = data_date_pay
    generat_payroll.solumn_cadastro = solumn_cadastro

    generat_payroll.list_qtd_cotas_inicial = list_qtd_cotas_inicial
    generat_payroll.list_qtd_cotas_final = list_qtd_cotas_final
    generat_payroll.list_columns_full_ata = list_columns_full_ata
    generat_payroll.list_columns_full_weekly = list_columns_full_weekly
    generat_payroll.list_columns_full_ata_entrega = (
        list_columns_full_ata_entrega)
    generat_payroll.list_columns_full_ata_cadastro = (
        list_columns_full_ata_cadastro)
    generat_payroll.list_qtd_cotas_parc = list_qtd_cotas_parc
    generat_payroll.name_columns_full = name_columns_full

    generat_payroll.quantity_line_full = quantity_line_full
    generat_payroll.quantity_line_ata = quantity_line_ata
    generat_payroll.quantity_line_weekly = quantity_line_weekly

    generat_payroll.dic_qtd_cotas_parc = dic_qtd_cotas_parc
    generat_payroll.dic_months = dic_months

    generat_payroll.table_full_ata = table_full_ata
    generat_payroll.table_full_weekly = table_full_weekly
    generat_payroll.table_seller_single = table_seller_single
    # fim da exportacao variavel
    list_columns_str_to_float = (list_qtd_cotas_inicial + list_qtd_cotas_final)
    list_columns_str_to_float.append(column_credito)
    generat_payroll.list_columns_str_to_float = list_columns_str_to_float
    generat_payroll.convert_str_float = table_full
    generat_payroll.table_full = generat_payroll.convert_str_float
    generat_payroll.columns_to_list_full_seller()
    generat_payroll.columns_ata_full_seller_single()
    generat_payroll.tables_columns_ata_seller_single()
    generat_payroll.tables_concat_seller_single()
    generat_payroll.create_dictionary_datas()
    generat_payroll.table_list_administradora_add_line()
    generat_payroll.table_list_administradora_line_add_sum()
    generat_payroll.table_list_administradora_sum_add_qtdcotasinicial()
    generat_payroll.prints()
