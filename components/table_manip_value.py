import pandas as pd
import numpy as np
import numbers
from time import sleep
from datetime import datetime


class Table_manip_value():
    def __init__(self) -> None:
        self.table: pd.DataFrame = pd.DataFrame()
        self.table_2: pd.DataFrame = pd.DataFrame()
        self.table_duplicate: pd.DataFrame = pd.DataFrame()
        self.list_one_two = []
        self.list_one_two_three = []
        self.list_name_change = []

    @property
    def tables(self):
        return None

    @tables.setter
    def tables(self, table):
        self.table = table

    @property
    def tables_2(self):
        return None

    @tables_2.setter
    def tables_2(self, table):
        self.table_2 = table

    @property
    def row_duplicate_column(self):
        return None

    @row_duplicate_column.setter
    def row_duplicate_column(self, column):
        duplicatas = self.table.duplicated(subset=column, keep=False)
        self.table_duplicate = self.table[duplicatas]

    @ property
    def list_columns_one_two(self):
        return self.list_one_two

    @list_columns_one_two.setter
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

    @property
    def edit_data_column_2(self):
        return None

    @edit_data_column_2.setter
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

    @property
    def data_duplicate_change(self):
        return None

    @data_duplicate_change.setter
    def data_duplicate_change(self, column):
        for name in self.list_name_change:
            self.table[column] = self.table[column].replace(name[0], name[1])

    @ property
    def list_columns_one_two_three(self):
        return self.list_one_two_three

    @list_columns_one_two_three.setter
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

    @property
    def edit_data_column_3(self):
        return None

    @edit_data_column_3.setter
    def edit_data_column_3(self, column_name):
        Admin = column_name[0]
        Cargo = column_name[1]
        Table_rec = column_name[2]
        # df = self.table[column_name]
        # colunm_admin_cargo = column_name[0]+column_name[1]
        # df = df.sort_values(by=[column_name[0], column_name[1]])
        # df[(colunm_admin_cargo)] = df.apply(
        #     lambda row: row[column_name[0]] + row[column_name[1]], axis=1)
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

    @property
    def edit_data_column_all(self):
        return None

    @edit_data_column_all.setter
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
            # if key == 0:
            #     continue

            line1 = self.table.iloc[key][tipo_pag]
            # print(f'{key} ,({line1})')
            # print(self.table.head(n=0))
            self.table.loc[self.table.index[key], tipo_pag] = line1[:2]
            if key != quantity_line - 1:
                line2 = self.table.iloc[key + 1][tipo_pag]
            line_cargo = self.table.iloc[key][cargo]
            change = True
            data_change = ''
            if '5º' in line1:
                # self.table.loc[self.table.index[key], cargo] = line_cargo + ' 5'
                change = False
            elif '4º' in line1:
                # self.table.loc[self.table.index[key], cargo] = line_cargo + ' 4'
                if '5º' in line2:
                    change = False
                else:
                    data_change = ' 5º'
            elif '3º' in line1:
                # self.table.loc[self.table.index[key], cargo] = line_cargo + ' 3'
                if '4º' in line2:
                    change = False
                elif '5º' in line2:
                    data_change = ' 4º'
                else:
                    data_change = ' 4º 5º'
            elif '2º' in line1:
                # self.table.loc[self.table.index[key], cargo] = line_cargo + ' 2'
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

    # @property
    # def add_data_weekly(self):
    #     return None

    # @add_data_weekly.setter
    # def add_data_weekly(self, list_colunms):
    #     quantity_line = self.table_2.shape[0]
    #     for key in range(quantity_line):
    #         for column in list_colunms:
    #             line = self.table_2.iloc[key][column]
    #             print(line)

    # @property
    # def add_column_day_week(self):
    #   return None

    # @add_column_day_week.setter
    # def add_column_day_week(self, name_colunms):
    #   dt_entrega = name_colunms[0]
    #   dt_cad_adm = name_colunms[1]
    #   quantity_line = self.table.shape[0]
    #   self.table['Semana ' + dt_entrega] = np.nan
    #   self.table['Semana ' + dt_cad_adm] = np.nan
    #   for key in range(quantity_line):
    #     date1 = iloc[key][dt_entrega]
    #     date2 = iloc[key][dt_cad_adm]
    #     dates = [date1, date2]
    #     for date in dates:
    #       date = datetime.strptime(date, "%d/%m/%Y")
    #       day_week = date.weekday()
    #       day_week = (day_week + 1) % 7
    #       week_month = (date.day + day_week - 1) // 7 + 1

    @ property
    def return_table(self):
        return self.table

    @ property
    def return_table_duplicate(self):
        return self.table_duplicate
