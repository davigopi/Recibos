import pandas as pd
import numpy as np
import re
from time import sleep
import locale


class TableManip:
    def __init__(self) -> None:
        self.df: pd.DataFrame = pd.DataFrame()
        self.dfNew: pd.DataFrame = pd.DataFrame()
        self.nameNumberLine = 0
        self.nameNumberColumn = 0
        self.value = None
        self.table: pd.DataFrame = pd.DataFrame()
        self.value_separate = ''
        self.value_fixed_column = ''  # por padrao ''
        self.column_clone = ''
        self.rename_name_column_origin = ''

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
        if isinstance(self.nameNumberLine, str) and isinstance(
                self.nameNumberColumn, str):
            self.value = table.at[
                self.nameNumberLine, self.nameNumberColumn]  # pelo nome
        elif isinstance(self.nameNumberLine, int) and isinstance(
                self.nameNumberColumn, int):
            self.value = table.iat[
                self.nameNumberLine, self.nameNumberColumn]  # pelo local
        else:
            print(
                f'line: {self.nameNumberLine} {type(self.nameNumberLine)}'
                f'colum: {self.nameNumberColumn} {type(self.nameNumberColumn)}'
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
        self.table[name_column] = self.table[self.column_clone]

    @property
    def add_column_clone_two_columns(self):
        return None

    @add_column_clone_two_columns.setter
    def add_column_clone_two_columns(self, list_name_column):
        self.table[list_name_column[0]] = self.table[
            list_name_column[1]] + '/' + self.table[
                list_name_column[2]].astype(str)

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

    @property
    def alter_value_line_total_sum(self):
        return None

    @alter_value_line_total_sum.setter
    def alter_value_line_total_sum(self, name_column):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        quantity_line = self.table.shape[0]
        for key in range(4, 8):
            new_name_column = name_column[0] + ' ' + name_column[key]
            new_name_column_gerente = new_name_column + ' Sup'
            self.table[new_name_column] = ''
            self.table[new_name_column_gerente] = ''
            for line in range(quantity_line):
                vendedor = self.table.iloc[line][name_column[1]]
                gerente = self.table.iloc[line][name_column[2]]
                ata = self.table.iloc[line][name_column[key]]
                sum_value = self.table.loc[
                    (self.table[name_column[1]] == vendedor) &
                    (self.table[name_column[key]] == ata),
                    name_column[3]
                ].apply(lambda x: float(
                    x.replace(' ', '').replace('.', '').replace(',', '.')
                )).sum()
                # .apply(lambda x: locale.atof(x)).sum()
                sum_value_gerente = self.table.loc[
                    (self.table[name_column[2]] == gerente) &
                    (self.table[name_column[key]] == ata),
                    name_column[3]
                ].apply(lambda x: float(
                    x.replace(' ', '').replace('.', '').replace(',', '.')
                )).sum()
                # .apply(lambda x: locale.atof(x)).sum()
                sum_value = locale.format_string("%.2f", sum_value, grouping=True)
                sum_value_gerente = locale.format_string("%.2f", sum_value_gerente, grouping=True)
                self.table.at[line, new_name_column] = sum_value
                self.table.at[line, new_name_column_gerente] = sum_value_gerente

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
        self.table = self.table.rename(
            columns={self.rename_name_column_origin: name_column})

    @ property
    def rename_value_column_before(self):
        return None

    @ rename_value_column_before.setter
    def rename_value_column_before(self, name_column):
        num_line, num_column = self.table.shape
        for line in range(num_line):
            inf = self.table.iat[line, self.table.columns.get_loc(name_column)]
            inf_re = re.search(r'^(.*?) ' + self.value_separate, inf)
            if inf_re:  # só ira alterar se encontrou a self.value_separate
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
            inf_re = re.search(self.value_separate + r' (.*)$', inf)
            if inf_re:  # só ira alterar se encontrou a self.value_separate
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
        self.table = self.table.rename(
            columns={list_name_column[0]: list_name_column[1]})

    @ property
    def rename_name_column_indix(self):
        return None

    @ rename_name_column_indix.setter
    def rename_name_column_indix(self, list_index_name_column):
        index_column = list_index_name_column[0]
        name_column = list_index_name_column[1]
        self.table.columns.values[index_column] = name_column
