# flake8: noqa
# pyright: # type: ignore

import pandas as pd
import numpy as np
import re
import sys
import locale
# from components import date_weekly
# from components import renomear
from components.fileManip import FileManip
from components.date_month import Date_month
from components.renomear import Renomear

from path_file import Path_file
from datetime import datetime
from components.variables import *

import numbers

import numpy as np


def convert_str_float(value):
    try:
        value = str(value)
        value = value.replace(' ', '')
        value = value.replace('.', '')
        value = value.replace(',', '.')
        value = float(value)
        value = round(value, 2)
    except ValueError:
        value = 0.0
    return value


def convert_to_date(value):
    try:
        value = pd.to_datetime(value, dayfirst=True)
    except (ValueError, TypeError):
        value = pd.Timestamp('2000-01-01')
    return value


class TableManip:
    def __init__(self) -> None:
        self.renomear = Renomear()
        self.df: pd.DataFrame = pd.DataFrame()
        self.dfNew: pd.DataFrame = pd.DataFrame()
        self.table: pd.DataFrame = pd.DataFrame()
        self.fileManip = FileManip()
        self.path_file = Path_file()
        self.date_month = Date_month()
        self.value = value
        self.list_one_two = list_one_two
        self.list_name_change = list_name_change
        self.list_one_two_three = list_one_two_three
        self.list_list_column_orden_total = list_list_column_orden_total
        self.dict_duplicate_sum = dict_duplicate_sum
        self.dict_duplicate_count = dict_duplicate_count
        self.column_clone = column_clone
        self.value_fixed_column = value_fixed_column
        self.number_Line = number_Line
        self.number_Column = number_Column

    def printVariaveis(self):
        print('###################### INICIO ##########################')
        print(
            column_Vendedor,
            column_Gerente,
            column_Supervisor,
            column_Cargo_Gerencia,
            column_Credito,
            column_Periodo_Valor_Qtd_Vendas,
            column_Periodo_Valor_Qtd_Vendas_Supervisor,
            column_Periodo_Valor_Qtd_Vendas_Gerencia,
            column_Qtd_Valor_Vend,
            column_1_Parcela_Referencia,
            column_Data_de_Entrega,
            column_Data_Cad_Adm,
            column_ATA_Entrega,
            column_Total_ATA_Entrega_Vend,
            column_Data_Semana,
            column_Periodo_final,
            column_Periodo_inicial,
            column_ATA,
            column_Cargo,
            column_Administradora,
            column_Tipo_Pagamento,
            column_Index,
            word_Vendedor,
            word_Supervisor,
            word__Sup,
            word__Ger,
            word__Qtd_Cotas,
            word_Qtd_Vendas,
            word_CADASTRO,
            word__Valor_Qtd_Vendas_Inicial,
            word__Valor_Qtd_Vendas_Final,
            word__Data_Inicial,
            word__Data_Final,
            word__Valor_Qtd_Vendas_Inicial_Supervisor,
            word__Valor_Qtd_Vendas_Final_Supervisor,
            word__Data_Inicial_Supervisor,
            word__Data_Final_Supervisor,
            word__Valor_Qtd_Vendas_Inicial_Gerencia,
            word__Valor_Qtd_Vendas_Final_Gerencia,
            word__Data_Inicial_Gerencia,
            word__Data_Final_Gerencia
        )
        print('###################### FIM ##########################')

    @property
    def merge(self):
        if self.dfNew.empty:
            self.dfNew = self.df
        else:
            self.dfNew = pd.merge(
                self.dfNew, self.df, how='outer')
        return self.dfNew

    @property
    def infTable(self):
        return self.value

    @infTable.setter
    def infTable(self, table):
        if isinstance(self.number_Line, str) and isinstance(self.number_Column, str):
            self.value = table.at[self.number_Line, self.number_Column]  # pelo nome
        elif isinstance(self.number_Line, int) and isinstance(self.number_Column, int):
            self.value = table.iat[self.number_Line, self.number_Column]  # pelo local
        else:
            print(
                f'line: {self.number_Line} {type(self.number_Line)}'
                f'colum: {self.number_Column} {type(self.number_Column)}'
            )

    @property
    def renemar_data(self):
        return None

    @renemar_data.setter
    def renemar_data(self, table):
        num_line, num_column = table.shape
        for line in range(num_line):
            for column in range(num_column):
                inf = table.iat[line, column]
                try:
                    inf = inf.replace('\n', '').replace(
                        '\t', '').replace('  ', '')
                    table.iat[line, column] = inf
                except AttributeError:
                    pass
        self.table = table

    @property
    def add_column_nan(self):
        return None

    @add_column_nan.setter
    def add_column_nan(self, list_names_columns):
        for name_column in list_names_columns:
            self.table[name_column] = np.nan

    @property
    def add_value_fixed_column(self):
        return None

    @add_value_fixed_column.setter
    def add_value_fixed_column(self, name_column):
        self.table[name_column] = self.value_fixed_column

    @property
    def add_column_clone(self):
        return None

    @add_column_clone.setter
    def add_column_clone(self, name_column):
        self.table[name_column] = self.table[word_Periodo]

    @property
    def add_column_clone_two_columns(self):
        return None

    @add_column_clone_two_columns.setter
    def add_column_clone_two_columns(self, list_name_column):
        name_ata = self.table[list_name_column[1]] + '/' + self.table[list_name_column[2]].astype(str)  # noqa
        self.table[list_name_column[0]] = name_ata

    @property
    def add_column_primary_key(self):
        return None

    @add_column_primary_key.setter
    def add_column_primary_key(self, name_column):
        quantity_line = self.table.shape[0]
        list_primary_key = []
        for key in range(1, quantity_line + 1):
            primary_key = f'{key:06}'
            list_primary_key.append(primary_key)
        self.table[name_column] = list_primary_key

    def create_list_qtd_data_full(self):
        column_qtd_cotas_inicial = [word__Valor_Qtd_Vendas_Inicial,
                                    word__Valor_Qtd_Vendas_Inicial_Supervisor,
                                    word__Valor_Qtd_Vendas_Inicial_Gerencia]
        column_qtd_cotas_final = [word__Valor_Qtd_Vendas_Final,
                                  word__Valor_Qtd_Vendas_Final_Supervisor,
                                  word__Valor_Qtd_Vendas_Final_Gerencia]
        column_data_incial = [word__Data_Inicial,
                              word__Data_Inicial_Supervisor,
                              word__Data_Inicial_Gerencia]
        column_data_final = [word__Data_Final,
                             word__Data_Final_Supervisor,
                             word__Data_Final_Gerencia]
        list_qtd_data = []
        list_qtd_data_gerente = []
        list_qtd_data_gerente_geral = []
        list_qtd_data_temp = []
        cont = 1
        cont_column = 0
        while True:
            column_qtd_inical = str(cont) + column_qtd_cotas_inicial[cont_column]
            column_qtd_final = str(cont) + column_qtd_cotas_final[cont_column]
            column_dt_inicial = str(cont) + column_data_incial[cont_column]
            column_dt_final = str(cont) + column_data_final[cont_column]
            # column existe na lista de colunas da tabela
            if column_qtd_inical in self.table.columns:
                list_qtd_data_temp.append([column_qtd_inical, column_qtd_final, column_dt_inicial, column_dt_final])  # noqa
                cont += 1
            else:
                # é vendedor?
                if cont_column == 0:
                    cont_column = 1
                    cont = 1
                    list_qtd_data = list_qtd_data_temp
                    list_qtd_data_temp = []
                elif cont_column == 1:
                    cont_column = 2
                    cont = 1
                    list_qtd_data_gerente = list_qtd_data_temp
                    list_qtd_data_temp = []
                else:
                    list_qtd_data_gerente_geral = list_qtd_data_temp
                    break

        # criar lista ordem reversa
        list_qtd_data = list_qtd_data[::-1]
        list_qtd_data_gerente = list_qtd_data_gerente[::-1]
        list_qtd_data_gerente_geral = list_qtd_data_gerente_geral[::-1]
        # Lista de nome coluna -> 5 Qtd. Cotas Inicial, 4...
        # '1 Qtd. Cotas Inicial'], ['5 Qtd. Cotas Inicial_Gerente', '4...
        # '1 Qtd.Cotas Inicial_Gerente']])
        list_qtd_data_full = [list_qtd_data, list_qtd_data_gerente, list_qtd_data_gerente_geral]
        return list_qtd_data_full

    def create_list_columns_ata_qtd_cotas_vendas(self, column_ata_mes_sma):
        new_name_column = word_Total + ' ' + column_ata_mes_sma
        new_name_column_vendedor = new_name_column + word__Vend
        new_name_column_supervisor = new_name_column + word__Sup
        new_name_column_gerencia = new_name_column + word__Ger
        list_column_ata = [new_name_column_vendedor,
                           new_name_column_supervisor,
                           new_name_column_gerencia]
        new_name_column_qtd_vendas = word_Qtd_Vendas + ' ' + column_ata_mes_sma
        new_name_column_qtd_vendas_vendedor = new_name_column_qtd_vendas + word__Vend
        new_name_column_qtd_vendas_supervisor = new_name_column_qtd_vendas + word__Sup
        new_name_column_qtd_vendas_gerencia = new_name_column_qtd_vendas + word__Ger
        list_column_qtd_vendas = [new_name_column_qtd_vendas_vendedor,
                                  new_name_column_qtd_vendas_supervisor,
                                  new_name_column_qtd_vendas_gerencia]
        new_name_column_qtd_cotas = column_ata_mes_sma + word__Qtd_Cotas
        new_name_column_qtd_cotas_vendedor = new_name_column_qtd_cotas + word__Vend
        new_name_column_qtd_cotas_supervisor = new_name_column_qtd_cotas + word__Sup
        new_name_column_qtd_cotas_gerencia = new_name_column_qtd_cotas + word__Ger
        list_column_qtd_cotas = [new_name_column_qtd_cotas_vendedor,
                                 new_name_column_qtd_cotas_supervisor,
                                 new_name_column_qtd_cotas_gerencia]
        return list_column_ata, list_column_qtd_vendas, list_column_qtd_cotas

    def create_list_columns_total(self, column_ata_mes_sma):
        new_name_column = word_Total + ' ' + column_ata_mes_sma
        new_name_column_vendedor = new_name_column + word__Vend
        new_name_column_supervisor = new_name_column + word__Sup
        new_name_column_gerencia = new_name_column + word__Ger
        if word_Sma_ in new_name_column:
            list_column_total = [
                new_name_column_vendedor, new_name_column_supervisor, new_name_column_gerencia
            ]
            return list_column_total
        new_name_column_qtd_vendas = word_Qtd_Vendas + ' ' + column_ata_mes_sma
        new_name_column_qtd_vendas_vendedor = new_name_column_qtd_vendas + word__Vend
        new_name_column_qtd_vendas_supervisor = new_name_column_qtd_vendas + word__Sup
        new_name_column_qtd_vendas_gerencia = new_name_column_qtd_vendas + word__Ger
        new_name_column_qtd_cotas = column_ata_mes_sma + word__Qtd_Cotas
        new_name_column_qtd_cotas_vendedor = new_name_column_qtd_cotas + word__Vend
        new_name_column_qtd_cotas_supervisor = new_name_column_qtd_cotas + word__Sup
        new_name_column_qtd_cotas_gerencia = new_name_column_qtd_cotas + word__Ger

        list_column_total = [
            new_name_column_vendedor, new_name_column_qtd_vendas_vendedor, new_name_column_qtd_cotas_vendedor,  # noqa
            new_name_column_supervisor, new_name_column_qtd_vendas_supervisor, new_name_column_qtd_cotas_supervisor,  # noqa
            new_name_column_gerencia, new_name_column_qtd_vendas_gerencia, new_name_column_qtd_cotas_gerencia  # noqa
        ]
        return list_column_total

    def discover_num_qtd_cotas(self, line, value_compare, num_qtd_cotas_temp, column_qtd_data):
        column_qtd_cotas_inicial = column_qtd_data[0]
        value_qci = self.table.iloc[line][column_qtd_cotas_inicial]
        #               5, 4, 3, 2, 1
        num_qtd_cotas = column_qtd_cotas_inicial[0]
        # se nao existir valro passa para o próximo nu_qtd_contas
        if str(value_qci).lower() == 'nan' or value_qci is None:
            # se chegou a 1 é o ultimo não existe próximo
            if num_qtd_cotas == '1':
                return num_qtd_cotas_temp, num_qtd_cotas_temp
            return None, num_qtd_cotas_temp
        value_qci = convert_str_float(value_qci)

        # receber o valor da coluna Qtd.
        column_qtd_cotas_final = column_qtd_data[1]
        value_qcf = self.table.iloc[line][column_qtd_cotas_final]
        value_qcf = convert_str_float(value_qcf)

        column_data_incial = column_qtd_data[2]
        value_di = self.table.iloc[line][column_data_incial]
        value_di = convert_to_date(value_di)

        column_data_final = column_qtd_data[3]
        value_df = self.table.iloc[line][column_data_final]
        value_df = convert_to_date(value_df)

        value_pr = self.table.iloc[line][column_1_Parcela_Referencia]
        value_pr = str(value_pr)
        if word_CADASTRO in value_pr:
            column_data = column_Data_Cad_Adm
        else:
            column_data = column_Data_de_Entrega
        value_data = self.table.iloc[line][column_data]
        value_data = convert_to_date(value_data)

        if value_compare >= value_qci and value_compare <= value_qcf and value_data <= value_df:
            # devido a mudança n categoria do tipo de pagamentos tem vendas antigas
            # que não se encaixa no inicio da função
            if value_data >= value_di:
                return num_qtd_cotas, num_qtd_cotas_temp
            num_qtd_cotas_temp = num_qtd_cotas
        # ultimo da fila 1
        if num_qtd_cotas == '1':
            return num_qtd_cotas_temp, num_qtd_cotas_temp
        return None, num_qtd_cotas_temp

    def data_column_Qtd_Valor_Vend(self, line, periodo_valor_qtd_vendas):
        #  se variavel for interavel
        if not isinstance(periodo_valor_qtd_vendas, (str, list, tuple)):
            periodo_valor_qtd_vendas = self.table.iloc[line][column_Periodo_Valor_Qtd_Vendas_Supervisor]  # noqa
            if not isinstance(periodo_valor_qtd_vendas, (str, list, tuple)):
                self.table.at[line, column_Qtd_Valor_Vend] = 'Periodo Nulo'
                return
        #      'Qtd Vendas'
        if word_Qtd_Vendas in periodo_valor_qtd_vendas:
            #                       'Qtd Valor Vend'
            self.table.at[line, column_Qtd_Valor_Vend] = word_Qtd_Vendas  # noqa
        else:
            self.table.at[line, column_Qtd_Valor_Vend] = 'Valor Vendas'

    def get_name_professional(self, line):
        vendedor = self.table.iloc[line][column_Vendedor]
        supervisor = self.table.iloc[line][column_Supervisor]
        cargo_gerencia = self.table.iloc[line][column_Cargo_Gerencia]
        list_professional = [vendedor, supervisor, cargo_gerencia]
        return list_professional

    def data_column_Total(self, profession, ata, column_prof, column_ata_mes_sma, line, column_Total):  # noqa
        key_prof_ata = str(profession) + str(ata)
        # evitar perda de tempo na resoma
        if key_prof_ata in self.dict_duplicate_sum:
            sum_profession = self.dict_duplicate_sum[key_prof_ata]
        else:
            sum_profession = self.table.loc[
                (self.table[column_prof] == profession) &
                (self.table[column_ata_mes_sma] == ata),
                column_Credito].apply(convert_str_float).sum()

            self.dict_duplicate_sum[key_prof_ata] = sum_profession
        #         Total ATA Entrega  0  |  Total ATA Entrega Ger  2
        self.table.at[line, column_Total] = (locale.format_string("%.2f", sum_profession, grouping=True))  # noqa
        return sum_profession

    def creat_data_columns_Porcentagem(self, num_ata_pag, column_num_ata_nparc, PK_Vend_ATA_Entrega):  # noqa
        key_prof_ata = str(num_ata_pag) + str(column_num_ata_nparc) + str(PK_Vend_ATA_Entrega)  # noqa
        # criar dicionario para evitar perda de tempo na resoma
        if key_prof_ata not in self.dict_duplicate_sum:
            sum_profession = self.table.loc[
                (self.table[column_num_ata_nparc] <= num_ata_pag) &
                (self.table[column_PK_Vend_ATA_Entrega] == PK_Vend_ATA_Entrega),
                column_Credito
            ].apply(convert_str_float).sum()
            self.dict_duplicate_sum[key_prof_ata] = sum_profession
        sum_profession = self.dict_duplicate_sum[key_prof_ata]
        return sum_profession

    def data_column_Qtd_Vendas(self, profession, ata, column_prof, column_ata_mes_sma, line, column_Qtd_Vendas):  # noqa
        key_prof_ata = str(profession) + str(ata)
        if key_prof_ata in self.dict_duplicate_count:
            count_profession = self.dict_duplicate_count[key_prof_ata]
        else:
            count_profession = self.table.loc[
                (self.table[column_prof] == profession) &
                (self.table[column_ata_mes_sma] == ata),
                column_Credito].count()
            self.dict_duplicate_count[key_prof_ata] = count_profession
        self.table.at[line, column_Qtd_Vendas] = (
            locale.format_string("%.2f", count_profession, grouping=True)
        )
        return count_profession

    def alter_value_line_total_sum(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        quantity_line = self.table.shape[0]
        list_qtd_data_full = self.create_list_qtd_data_full()
        # 0     column_ATA_Entrega =    'ATA Entrega'
        # 1     column_mes_ent =        'Mes Ent'
        # 2     column_sma_ent =        'Sma Ent'
        # 3     column_ata_cad_adm =    'ATA Cad Adm'
        # 4     column_mes_cad_adm =    'Mes Cad Adm'
        # 5     column_sma_cad_adm =    'Sma Cad Adm'
        for column_ata_mes_sma in list_columns_ata_mes_sma:
            list_column_ata, list_column_qtd_vendas, list_column_qtd_cotas = self.create_list_columns_ata_qtd_cotas_vendas(column_ata_mes_sma)  # noqa
            self.dict_duplicate_sum = {}
            self.dict_duplicate_count = {}
            # pecorrera linha por linha da tabela
            for line in range(quantity_line):
                list_professional = self.get_name_professional(line)
                ata = self.table.iloc[line][column_ata_mes_sma]
                for key_prof, profession in enumerate(list_professional):
                    column_Total = list_column_ata[key_prof]
                    column_Qtd_Vendas = list_column_qtd_vendas[key_prof]
                    if key_prof == 0:  # vendedor
                        column_prof = column_Vendedor
                        periodo_valor_qtd_vendas = self.table.iloc[line][column_Periodo_Valor_Qtd_Vendas]  # noqa
                        self.data_column_Qtd_Valor_Vend(line, periodo_valor_qtd_vendas)
                    elif key_prof == 1:  # supervisro
                        column_prof = column_Supervisor
                        periodo_valor_qtd_vendas = self.table.iloc[line][column_Periodo_Valor_Qtd_Vendas_Supervisor]  # noqa
                    elif key_prof == 2:  # gerencia
                        column_prof = column_Cargo_Gerencia
                        periodo_valor_qtd_vendas = self.table.iloc[line][column_Periodo_Valor_Qtd_Vendas_Gerencia]  # noqa
                    # descobrir se é por quantidade ou valor
                    periodo_valor_qtd_vendas = str(periodo_valor_qtd_vendas)

                    sum_profession = self.data_column_Total(profession, ata, column_prof, column_ata_mes_sma, line, column_Total)  # noqa

                    # 'Sma' tem na coluna ata? se sim retornar
                    if word_Sma_ in column_ata_mes_sma:
                        continue
                    count_profession = self.data_column_Qtd_Vendas(profession, ata, column_prof, column_ata_mes_sma, line, column_Qtd_Vendas)  # noqa
                    # se exitri palavra 'Qtd. Vendas' em periodo_valor_qtd_vendas
                    if word_Qtd_Vendas in periodo_valor_qtd_vendas:
                        value_compare = count_profession
                    else:
                        value_compare = sum_profession
                    num_qtd_cotas_temp = '0'
                    # vendedor 0  5 Qtd. Cotas Inicial, 4...  '1 Qtd. Cotas
                    # gerente 1  5 Qtd. Cotas Inicial_Gerente', '4.. '1 Qtd
                    # gerente 2  5 Qtd. Cotas Inicial_Gerente_Geral',.. 1 Q
                    for column_qtd_data in list_qtd_data_full[key_prof]:
                        num_qtd_cotas, num_qtd_cotas_temp = self.discover_num_qtd_cotas(line, value_compare, num_qtd_cotas_temp, column_qtd_data)  # noqa
                        if num_qtd_cotas is not None:
                            break
                    # ATA Entrega qtd cotas 1 | ATA Entrega qtd costa Ger 3
                    num_qtd_cotas = '{:g}'.format(float(num_qtd_cotas))
                    self.table.at[line, list_column_qtd_cotas[key_prof]] = num_qtd_cotas

    def create_columns_total(self):
        for column_ata_mes_sma in list_columns_ata_mes_sma:
            list_column_total = self.create_list_columns_total(column_ata_mes_sma)  # noqa
            self.list_list_column_orden_total.append(list_column_total)

    def add_value_pk_vend_ata_entrega(self):
        quantity_line = self.table.shape[0]
        PK_Vend_ATA_Entrega = 0
        disc_PK_Vend_ATA_Entrega = {}
        for line in range(quantity_line):
            ata_entrega = self.table.iloc[line][column_ATA_Entrega]
            vendedor = self.table.iloc[line][column_Vendedor]
            key_vend_ata = str(vendedor) + str(ata_entrega)
            if key_vend_ata not in disc_PK_Vend_ATA_Entrega:
                PK_Vend_ATA_Entrega += 1
                disc_PK_Vend_ATA_Entrega[key_vend_ata] = PK_Vend_ATA_Entrega
                # disc_PK_Vend_ATA_Entrega[key_vend_ata] = key_vend_ata
            PK_Vend_ATA_Entrega_temp = disc_PK_Vend_ATA_Entrega[key_vend_ata]
            self.table.loc[line, column_PK_Vend_ATA_Entrega] = PK_Vend_ATA_Entrega_temp

    @property
    def add_value_situacao_num_ATA(self):
        return None

    # name_column_situacao,     0
    # name_column_data_pag,     1
    # name_column_data_venc,    2
    # name_column_ata_pag,      3
    # name_column_ata_venc      4
    # mane_column_situacao_ata  5
    # name_name_column_num_ata_nparc       6

    @add_value_situacao_num_ATA.setter
    def add_value_situacao_num_ATA(self, list_list_columns_situacao_num_ATA):
        quantity_line = self.table.shape[0]
        for line in range(quantity_line):
            # ata_entrega = self.table.iloc[line]['ATA Entrega']
            # cliente = self.table.iloc[line]['Cliente']
            for list_columns_percentage in list_list_columns_situacao_num_ATA:
                situacao = self.table.iloc[line][list_columns_percentage[0]]
                if 'PAGA' not in situacao:
                    self.table.loc[line, list_columns_percentage[5]] = ''
                    self.table.loc[line, list_columns_percentage[6]] = np.nan
                    continue
                ata_pag = self.table.iloc[line][list_columns_percentage[3]]
                # verificar se existe ata_pag se não a data pag esta errada
                if pd.isna(ata_pag) or ata_pag is None:
                    self.table.loc[line, list_columns_percentage[5]] = word_Data_Pag_Errada
                    self.table.loc[line, list_columns_percentage[6]] = np.nan
                    continue
                ata_venc = self.table.iloc[line][list_columns_percentage[4]]
                if ata_pag == ata_venc:
                    self.table.loc[line, list_columns_percentage[5]] = word_Pag_Mesma_ATA
                    self.table.loc[line, list_columns_percentage[6]] = 0
                    continue
                data_pag = self.table.iloc[line][list_columns_percentage[1]]
                data_venc = self.table.iloc[line][list_columns_percentage[2]]
                data_pag = datetime.strptime(data_pag, '%d/%m/%Y')
                data_venc = datetime.strptime(data_venc, '%d/%m/%Y')
                if data_pag <= data_venc:
                    self.table.loc[line, list_columns_percentage[5]] = word_Pag_Adiantado_ATA
                    num_month_full = self.date_month.sum_less_month(1, ata_pag, ata_venc)
                    self.table.loc[line, list_columns_percentage[6]] = num_month_full
                    continue
                self.table.loc[line, list_columns_percentage[5]] = word_Pag_Atrasado_ATA
                num_month_full = self.date_month.sum_less_month(-1, ata_pag, ata_venc)
                self.table.loc[line, list_columns_percentage[6]] = num_month_full

    @property
    def add_value_num_ATA_atrasada(self):
        return None

    @add_value_num_ATA_atrasada.setter
    def add_value_num_ATA_atrasada(self, list_list_columns_num_ATA_atrasado):
        self.dict_duplicate_vend_ata = {}
        num_ata_nparc_dict_1 = 0
        num_ata_nparc_dict_2 = 0
        quantity_line = self.table.shape[0]
        for line in range(quantity_line):
            PK_Vend_ATA_Entrega = str(self.table.iloc[line][column_PK_Vend_ATA_Entrega])
            for list_columns_num_ATA_atrasado in list_list_columns_num_ATA_atrasado:
                num_ata_nparc = self.table.iloc[line][list_columns_num_ATA_atrasado[0]]
                if np.isnan(num_ata_nparc):
                    continue
                num_ata_nparc = int(num_ata_nparc)
                if num_ata_nparc <= 0:
                    continue
                key_vend_ata = PK_Vend_ATA_Entrega + list_columns_num_ATA_atrasado[0]
                if key_vend_ata in self.dict_duplicate_vend_ata:
                    list_num_ata_nparc_dict = self.dict_duplicate_vend_ata[key_vend_ata]
                    num_ata_nparc_dict_1 = list_num_ata_nparc_dict[0]
                    num_ata_nparc_dict_2 = list_num_ata_nparc_dict[1]
                    if num_ata_nparc == 1:
                        num_ata_nparc_dict_1 = int(num_ata_nparc_dict_1) + 1
                    elif num_ata_nparc == 2:
                        num_ata_nparc_dict_2 = int(num_ata_nparc_dict_2) + 1
                else:
                    num_ata_nparc_dict_1 = 0
                    num_ata_nparc_dict_2 = 0
                    if num_ata_nparc == 1:
                        num_ata_nparc_dict_1 = 1
                    elif num_ata_nparc == 2:
                        num_ata_nparc_dict_2 = 1
                self.dict_duplicate_vend_ata[key_vend_ata] = [num_ata_nparc_dict_1, num_ata_nparc_dict_2]  # noqa
        for line in range(quantity_line):
            PK_Vend_ATA_Entrega = str(self.table.iloc[line][column_PK_Vend_ATA_Entrega])
            for list_columns_num_ATA_atrasado in list_list_columns_num_ATA_atrasado:
                key_vend_ata = PK_Vend_ATA_Entrega + list_columns_num_ATA_atrasado[0]
                if key_vend_ata in self.dict_duplicate_vend_ata:
                    num_ata_nparc_dict_1 = str(self.dict_duplicate_vend_ata[key_vend_ata][0])
                    num_ata_nparc_dict_2 = str(self.dict_duplicate_vend_ata[key_vend_ata][1])
                    num_ata_nparc_dict = num_ata_nparc_dict_1 + ' 2º ATA. '
                    num_ata_nparc_dict += num_ata_nparc_dict_2 + ' 3º ATA. '
                    self.table.loc[line, list_columns_num_ATA_atrasado[1]] = num_ata_nparc_dict  # noqa

    @property
    def add_value_porcentagem(self):
        return None

    # name_column_1_porc_ata,           0
    # name_column_2_porc_ata,           1
    # name_column_3_porc_ata            2
    # name_column_num_ata,              3
    # column_num_ata_nparc_atrasado     4

    @add_value_porcentagem.setter
    def add_value_porcentagem(self, list_list_columns_percentage):
        quantity_line = self.table.shape[0]
        self.dict_duplicate_sum = {}
        for line in range(quantity_line):
            PK_Vend_ATA_Entrega = self.table.iloc[line][column_PK_Vend_ATA_Entrega]
            self.renomear.inf = self.table.iloc[line][column_Total_ATA_Entrega_Vend]
            Total_ATA_Entrega_Vend = float(self.renomear.valor())
            for list_columns_percentage in list_list_columns_percentage:
                column_num_ata_nparc = list_columns_percentage[3]
                # column_num_ata_nparc_atrasado = list_columns_percentage[4]
                # num_ata_nparc_atrasado = self.table.iloc[line][column_num_ata_nparc_atrasado]
                for num_ata_pag in range(3):  # 0, 1, 2
                    sum_profession = self.creat_data_columns_Porcentagem(num_ata_pag, column_num_ata_nparc, PK_Vend_ATA_Entrega)  # noqa
                    porcentagem = round(sum_profession / Total_ATA_Entrega_Vend * 100, 1)
                    self.table.loc[line, list_columns_percentage[num_ata_pag]] = porcentagem

    @property
    def add_value_ata_pag_atrasados(self):
        return None

    @add_value_ata_pag_atrasados.setter
    def add_value_ata_pag_atrasados(self, list_list_columns_ata_pag_atrasado_n_ata):
        quantity_line = self.table.shape[0]
        for line in range(quantity_line):
            for list_columns_ata_pag_atrasado_n_ata in list_list_columns_ata_pag_atrasado_n_ata:
                ata_pag_parc = self.table.iloc[line][list_columns_ata_pag_atrasado_n_ata[0]]
                if ata_pag_parc is None or isinstance(ata_pag_parc, float) or pd.isna(ata_pag_parc) or ata_pag_parc == ' - ':  # noqa
                    continue
                list_new_ata_pag_parc = self.date_month.sum_month_ata_pag_parc(ata_pag_parc)
                # list_new_ata_pag_parc = [str(value) if not isinstance(value, str) else value for value in list_new_ata_pag_parc]  # noqa
                # self.table.loc[line, [column_ata_pag_atrasado_1_mes, column_ata_pag_atrasado_2_meses]] = list_new_ata_pag_parc  # noqa
                self.table.loc[line, list_columns_ata_pag_atrasado_n_ata[1]] = str(list_new_ata_pag_parc[0])  # noqa
                self.table.loc[line, list_columns_ata_pag_atrasado_n_ata[2]] = str(list_new_ata_pag_parc[1])  # noqa

    @property
    def add_value_pagar_comissao(self):
        return None

    # mane_column_comissao_atrasada,
    # name_column_1_porc_ata,
    # name_column_2_porc_ata,
    # name_column_3_porc_ata

    @add_value_pagar_comissao.setter
    def add_value_pagar_comissao(self, list_list_columns_comissao_atrasada):
        quantity_line = self.table.shape[0]
        for line in range(quantity_line):
            for list_columns_comissao_atrasada in list_list_columns_comissao_atrasada:
                porc_ata_1 = float(self.table.iloc[line][list_columns_comissao_atrasada[1]])
                if porc_ata_1 >= porcentagem_Vendas:
                    self.table.loc[line, list_columns_comissao_atrasada[0]] = list_columns_comissao_atrasada[1]  # noqa
                    continue
                porc_ata_2 = float(self.table.iloc[line][list_columns_comissao_atrasada[2]])
                if porc_ata_2 >= porcentagem_Vendas:
                    self.table.loc[line, list_columns_comissao_atrasada[0]] = list_columns_comissao_atrasada[2]  # noqa
                    continue
                porc_ata_3 = float(self.table.iloc[line][list_columns_comissao_atrasada[3]])
                if porc_ata_3 >= porcentagem_Vendas:
                    self.table.loc[line, list_columns_comissao_atrasada[0]] = list_columns_comissao_atrasada[3]  # noqa

    @ property
    def del_column(self):
        return None

    @ del_column.setter
    def del_column(self, name_column):
        self.table.drop(name_column, axis=1, inplace=True)

    @ property
    def rename_name_column_destiny(self):
        return None

    @ rename_name_column_destiny.setter
    def rename_name_column_destiny(self, name_column):
        self.table = self.table.rename(columns={word_Periodo: name_column})  # noqa

    @ property
    def rename_value_column_before(self):
        return None

    @ rename_value_column_before.setter
    def rename_value_column_before(self, name_column):
        num_line, num_column = self.table.shape
        for line in range(num_line):
            inf = self.table.iat[line, self.table.columns.get_loc(name_column)]
            inf_re = re.search(r'^(.*?) ' + word_a, inf)
            if inf_re:  # só ira alterar se encontrou a value separate
                inf = inf_re.group(1)
            self.table.iat[line, self.table.columns.get_loc(name_column)] = inf

    @ property
    def rename_value_column_after(self):
        return None

    @ rename_value_column_after.setter
    def rename_value_column_after(self, name_column):
        num_line, num_column = self.table.shape
        for line in range(num_line):
            inf = self.table.iat[line, self.table.columns.get_loc(name_column)]
            inf_re = re.search(word_a + r' (.*)$', inf)
            if inf_re:  # só ira alterar se encontrou a value separate
                inf = inf_re.group(1)
            self.table.iat[line, self.table.columns.get_loc(name_column)] = inf

    @ property
    def create_table(self):
        return None

    @ create_table.setter
    def create_table(self, Name_columns):
        self.table = pd.DataFrame()  # tabela vazia
        for column in Name_columns:
            self.table[column] = None

    @ property
    def add_line_dictionary(self):
        return None

    @ add_line_dictionary.setter
    def add_line_dictionary(self, line_dictionary):
        # self.table = self.table.append(line_dictionary, ignore_index=True)
        new_line = pd.DataFrame([line_dictionary])
        self.table = pd.concat([self.table, new_line], ignore_index=True)

    @ property
    def rename_name_column(self):
        return None

    @ rename_name_column.setter
    def rename_name_column(self, list_name_column):
        self.table = self.table.rename(columns={list_name_column[0]: list_name_column[1]})

    def rename_list_name_column(self, list_name_column, word):
        for name_column in list_name_column:
            new_name_column = name_column + ' ' + word
            self.table = self.table.rename(columns={name_column: new_name_column})

    @ property
    def rename_name_column_indix(self):
        return None

    @ rename_name_column_indix.setter
    def rename_name_column_indix(self, list_index_name_column):
        index_column = list_index_name_column[0]
        name_column = list_index_name_column[1]

        try:
            self.table.columns.values[index_column] = name_column
        except IndexError:
            print('ERROR: IndexError. if not install: pip install lxml')
            sys.exit()

    @ property
    def merge_table_ata_table_weekly(self):
        return self.table

    @ merge_table_ata_table_weekly.setter
    def merge_table_ata_table_weekly(self, table_ata):
        nun_line_weekly = len(self.table)
        for line_weekly in range(nun_line_weekly):
            data_weekly = self.table.iloc[line_weekly][column_Data_Semana]
            data_weekly = datetime.strptime(data_weekly, '%d/%m/%Y')
            nun_line_ATA = len(table_ata)
            for line_ATA in range(nun_line_ATA):
                data_ATA_final = table_ata.iloc[line_ATA][column_Periodo_final]
                data_ATA_final = datetime.strptime(data_ATA_final, '%d/%m/%Y')
                if data_weekly > data_ATA_final:
                    continue
                data_ATA_inicial = table_ata.iloc[line_ATA][column_Periodo_inicial]
                data_ATA_inicial = datetime.strptime(data_ATA_inicial, '%d/%m/%Y')
                if data_weekly < data_ATA_inicial:
                    continue
                dado_ATA = table_ata.iloc[line_ATA][column_ATA]
                self.table.loc[line_weekly, column_ATA] = dado_ATA

    @ property
    def add_columns_full(self):
        return None

    @ add_columns_full.setter
    def add_columns_full(self, table_configPag):
        # tableManip = TableManip()
        name_columns = table_configPag.columns.tolist()
        quantity_line_1 = self.table.shape[0]
        quantity_line_2 = table_configPag.shape[0]
        # tableManip.table = self.table
        list_columns_add = []
        # add colunas na table_full
        for name_column in name_columns:
            if name_column in [column_Cargo, column_Administradora, column_Tipo_Pagamento]:  # noqa
                continue
            self.add_value_fixed_column = name_column
            # todas as cols configPagamento menos cargo, admin, tipoPag e index
            list_columns_add.append(name_column)
        # self.table = tableManip.table
        # add valores as colunas
        for key_1 in range(quantity_line_1):
            administradora_1 = self.table.iloc[key_1][column_Administradora]
            cargo_1 = self.table.iloc[key_1][column_Cargo]
            for key_2 in range(quantity_line_2):
                administradora_2 = table_configPag.iloc[key_2][column_Administradora]
                cargo_2 = table_configPag.iloc[key_2][column_Cargo]
                tipo_pagamento_2 = table_configPag.iloc[key_2][column_Tipo_Pagamento]
                if administradora_1 == administradora_2 and cargo_1 == cargo_2 and '1' in tipo_pagamento_2:
                    for column in list_columns_add:
                        self.table.loc[key_1, column] = table_configPag.iloc[key_2][column]
                    break

    @ property
    def data_duplicate_change(self):
        return None

    @ data_duplicate_change.setter
    def data_duplicate_change(self, column):
        for name in self.list_name_change:
            self.table[column] = self.table[column].replace(name[0], name[1])

    @ property
    def row_duplicate_column(self):
        return None

    # descobir se na lista de coluna não existem valores repetidos
    # nas tres colunas
    @ row_duplicate_column.setter
    def row_duplicate_column(self, column):
        duplicatas = self.table.duplicated(subset=column, keep=False)
        self.table_duplicate = self.table[duplicatas]

    @ property
    def list_columns_one_two_three(self):
        return None

    # cria uma lista dos valores identicos nas tres colunas passadas
    @ list_columns_one_two_three.setter
    def list_columns_one_two_three(self, column_name):
        df = self.table_duplicate[column_name]
        df = df.sort_values(by=[column_name[0], column_name[1]])
        data_column_0 = ''
        data_column_1 = ''
        list_data_column_2 = []
        for index, row in df.iterrows():
            if data_column_0 == '':
                data_column_0 = row[column_name[0]]
                data_column_1 = row[column_name[1]]
            if data_column_0 == row[column_name[0]] and data_column_1 == row[
                    column_name[1]]:
                list_data_column_2.append(row[column_name[2]])
            else:
                self.list_one_two_three.append([
                    data_column_0, data_column_1, list_data_column_2])
                data_column_0 = row[column_name[0]]
                data_column_1 = row[column_name[1]]
                list_data_column_2 = []
                list_data_column_2.append(row[column_name[2]])
        self.list_one_two_three.append([
            data_column_0, data_column_1, list_data_column_2])

    @ property
    def edit_data_column_3(self):
        return None

    # só ira renomear se as tres colunas mostra alguma valor identico
    @ edit_data_column_3.setter
    def edit_data_column_3(self, column_name):
        Admin = column_name[0]
        Cargo = column_name[1]
        Table_rec = column_name[2]
        list_rename = ['IMOVEL 50%', 'IMOVEL 100%', ' IMOVEL RODOBENS',
                       '"D" - EXCEÇÃO', 'MOTO', 'CAMINHÃO', 'IMOVEL']
        for administradora, cargo, listTabela in self.list_one_two_three:
            nome_new = ''
            original = True
            meet_rename = False
            list_name_change = []
            list_name_change.append(administradora)
            for tabela_recebimento in listTabela:
                for rename in list_rename:
                    if rename in tabela_recebimento:
                        nome_new = administradora + f' ({rename})'
                        list_name_change.append(nome_new)  # outra tabela
                        meet_rename = True
                        break
                if meet_rename is False:
                    if original is True:
                        ''' o origina que nao ira mexer só um original'''
                        original = False
                    else:
                        ''' nao pertence as condições ascima criar'''
                        nome_new = Admin + f' (DUPLIC {Table_rec})'
                        list_name_change.append(nome_new)  # outra tabela
                        meet_rename = True
                if meet_rename is True:
                    self.table.loc[(self.table[Admin] == administradora) & (
                        self.table[Cargo] == cargo) & (
                        self.table[Table_rec] == tabela_recebimento),
                        Admin
                    ] = nome_new
                    meet_rename = False
            # server para altera a outra tabela
            self.list_name_change.append(list_name_change)

    @ property
    def edit_data_column_all(self):
        return None

    @ edit_data_column_all.setter
    def edit_data_column_all(self, name_colunms):
        cargo = name_colunms[0]
        admin = name_colunms[1]
        tipo_pag = name_colunms[2]
        dt_pag = name_colunms[3]
        dia_pag = name_colunms[4]
        p1_recebera = name_colunms[5]
        d_recebera = name_colunms[6]
        fat_recebera = name_colunms[7]
        index = name_colunms[8]
        list_columns = [
            index
        ]
        # iloc = self.table.iloc
        for column in list_columns:
            self.table = self.table.drop(columns=column)
        name_columns = self.table.columns.tolist()
        del name_columns[2]  # remover tipo_pagamento da lista
        self.table.reset_index(drop=True, inplace=True)  # reiniciar index
        '''Excluir linhas: Vazias, RECEBERA nas tres condições tenha NÂO e
        que se repete em CARGO, ADMIN, DT_PAG, DIA_PAG'''
        quantity_line = self.table.shape[0]
        list_line = []
        for key in range(quantity_line - 1, -1, -1):

            # Vazias
            value = self.table.iloc[key][cargo]
            if isinstance(value, numbers.Number):
                if np.isnan(value):
                    list_line.append(key)
            # RECEBERA nas tres condições tem NÂO
            elif (self.table.iloc[key][p1_recebera] == 'NÃO') and (
                self.table.iloc[key][d_recebera] == 'NÃO') and (
                self.table.iloc[key][fat_recebera] == 'NÃO'
            ):
                list_line.append(key)
            # Repete em CARGO, ADMIN, DT_PAG, DIA_PAG alem diferente 'DIA DA SE
            elif key != 0:
                iloc = self.table.iloc
                if (iloc[key][cargo] == iloc[key - 1][cargo]) and (
                    iloc[key][admin] == iloc[key - 1][admin]) and (
                    iloc[key][dia_pag] == iloc[key - 1][dia_pag]) and (
                    iloc[key][dt_pag] == iloc[key - 1][dt_pag]) and (
                    iloc[key][dt_pag] != 'DIA DA SEMANA'
                ):
                    list_line.append(key)
        # Excluir linhas
        for line in list_line:
            self.table = self.table.drop(line)
        # reiniciar index
        self.table.reset_index(drop=True, inplace=True)  # reiniciar index
        '''Alterar valor tipo_pagamento'''
        quantity_line = self.table.shape[0]
        iloc = self.table.iloc
        for key in range(quantity_line):
            line1 = self.table.iloc[key][tipo_pag]
            self.table.loc[self.table.index[key], tipo_pag] = line1[:2]
            if key != quantity_line - 1:
                line2 = self.table.iloc[key + 1][tipo_pag]
            # line_cargo = self.table.iloc[key][cargo]
            change = True
            data_change = ''
            if '5º' in line1:
                change = False
            elif '4º' in line1:
                if '5º' in line2:
                    change = False
                else:
                    data_change = ' 5º'
            elif '3º' in line1:
                if '4º' in line2:
                    change = False
                elif '5º' in line2:
                    data_change = ' 4º'
                else:
                    data_change = ' 4º 5º'
            elif '2º' in line1:
                if '3º' in line2:
                    change = False
                elif '4º' in line2:
                    data_change = ' 3º'
                elif '5º' in line2:
                    data_change = ' 3º 4º'
                else:
                    data_change = ' 3º 4º 5º'
            elif '1º' in line1:
                if '2º' in line2:
                    change = False
                elif '3º' in line2:
                    data_change = ' 2º'
                elif '4º' in line2:
                    data_change = ' 2º 3º'
                elif '5º' in line2:
                    data_change = ' 2º 3º 4º'
                else:
                    data_change = ' 2º 3º 4º 5º'
            if change is True:
                data_change = line1[:2] + data_change
                self.table.loc[self.table.index[key], tipo_pag] = data_change

    @ property
    def list_columns_one_two(self):
        return self.list_one_two

    @ list_columns_one_two.setter
    def list_columns_one_two(self, column_name):
        duplicatas_rows_cargo_nome = self.table_duplicate[column_name]
        nome_before = ''
        list_cargo = []
        for index, row in duplicatas_rows_cargo_nome.iterrows():
            if nome_before == '':
                nome_before = row[column_name[0]]
            if nome_before == row[column_name[0]]:
                list_cargo.append(row[column_name[1]])
            else:
                self.list_one_two.append([nome_before, list_cargo])
                nome_before = row[column_name[0]]
                list_cargo = []
                list_cargo.append(row[column_name[1]])
        self.list_one_two.append([nome_before, list_cargo])

    @ property
    def edit_data_column_2(self):
        return None

    @ edit_data_column_2.setter
    def edit_data_column_2(self, column_name):
        for nome, listCargo in self.list_one_two:
            nome_new = ''
            original = True
            list_name_change = []
            list_name_change.append(nome)
            for cargo in listCargo:
                if 'CONSULTOR' in cargo:
                    nome_new = nome + ' (CONSULTOR)'
                    list_name_change.append(nome_new)
                elif 'VENDEDOR' in cargo:
                    nome_new = nome + ' (VENDEDOR)'
                    list_name_change.append(nome_new)
                else:
                    if original is True:
                        ''' o origina que nao ira mexer'''
                        nome_new = nome
                        original = False
                    else:
                        ''' nao pertence as condições ascima criar'''
                        nome_new = nome + ' (DUPLIC CARGO)'
                        list_name_change.append(nome)
                if nome_new != nome:
                    self.table.loc[
                        (self.table[column_name[0]] == nome) & (
                            self.table[column_name[1]] == cargo),
                        column_name[0]
                    ] = nome_new
            self.list_name_change.append(list_name_change)
