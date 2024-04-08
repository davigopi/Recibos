import pandas as pd
import numpy as np
import re


class TableManip:
    def __init__(self) -> None:
        self.df: pd.DataFrame = pd.DataFrame()
        self.dfNew: pd.DataFrame = pd.DataFrame()
        self.nameNumberLine = None
        self.nameNumberColumn = None
        self.value = None
        self.table: pd.DataFrame = pd.DataFrame()
        self.value_separate = None
        self.value_fixed_column = ''
        self.column_clone = None
        self.rename_name_column_origin = None

    @property
    def dfNews(self):
        return None

    @dfNews.setter
    def dfNews(self, dfNew):
        self.dfNew = dfNew

    @property
    def dfs(self):
        return None

    @dfs.setter
    def dfs(self, df):
        self.df = df

    # @property
    # def tables(self):
    #     return None

    # @tables.setter
    # def tables(self, table):
    #     self.table = table

    @property
    def value_fixed_columns(self):
        return None

    @value_fixed_columns.setter
    def value_fixed_columns(self, value_fixed_column):
        self.value_fixed_column = value_fixed_column

    @property
    def column_clones(self):
        return self.column_clone

    @column_clones.setter
    def column_clones(self, column_clone):
        self.column_clone = column_clone

    @property
    def value_separates(self):
        return None

    @value_separates.setter
    def value_separates(self, value_separate):
        self.value_separate = value_separate

    @property
    def rename_name_column_origins(self):
        return None

    @rename_name_column_origins.setter
    def rename_name_column_origins(self, rename_name_column_origin):
        self.rename_name_column_origin = rename_name_column_origin

    @property
    def nameNumberlines(self):
        return None

    @nameNumberlines.setter
    def nameNumberlines(self, nameNumberLine):
        self.nameNumberLine = nameNumberLine

    @property
    def nameNumberColumns(self):
        return None

    @nameNumberColumns.setter
    def nameNumberColumns(self, nameNumberColumn):
        self.nameNumberColumn = nameNumberColumn

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
        if isinstance(self.nameNumberLine, str) and isinstance(self.nameNumberColumn, str):
            self.value = table.at[self.nameNumberLine, self.nameNumberColumn]  # pelo nome
        elif isinstance(self.nameNumberLine, int) and isinstance(self.nameNumberColumn, int):
            self.value = table.iat[self.nameNumberLine, self.nameNumberColumn]  # pelo local
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
    def add_column_nan(self, name_column):
        print(f'self.df {self.df}  {type(self.df)}')
        self.df[name_column] = np.nan

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
    def del_column(self):
        return None

    @del_column.setter
    def del_column(self, name_column):
        self.table.drop(name_column, axis=1, inplace=True)

    @property
    def rename_name_column_destiny(self):
        return None

    @rename_name_column_destiny.setter
    def rename_name_column_destiny(self, name_column):
        self.table = self.table.rename(
            columns={self.rename_name_column_origin: name_column})

    @property
    def rename_value_column_before(self):
        return None

    @rename_value_column_before.setter
    def rename_value_column_before(self, name_column):
        num_line, num_column = self.table.shape
        for line in range(num_line):
            inf = self.table.iat[line, self.table.columns.get_loc(name_column)]
            inf_re = re.search(r'^(.*?) ' + self.value_separate, inf)
            if inf_re:  # só ira alterar se encontrou a self.value_separate
                inf = inf_re.group(1)
            self.table.iat[line, self.table.columns.get_loc(name_column)] = inf

    @property
    def rename_value_column_after(self):
        return None

    @rename_value_column_after.setter
    def rename_value_column_after(self, name_column):
        num_line, num_column = self.table.shape
        for line in range(num_line):
            inf = self.table.iat[line, self.table.columns.get_loc(name_column)]
            inf_re = re.search(self.value_separate + r' (.*)$', inf)
            if inf_re:  # só ira alterar se encontrou a self.value_separate
                inf = inf_re.group(1)
            self.table.iat[line, self.table.columns.get_loc(name_column)] = inf

    @property
    def create_table(self):
        return None

    @create_table.setter
    def create_table(self, Name_columns):
        self.table = pd.DataFrame()  # tabela vazia
        for column in Name_columns:
            self.table[column] = None

    @property
    def add_line_dictionary(self):
        return None

    @add_line_dictionary.setter
    def add_line_dictionary(self, line_dictionary):
        # self.table = self.table.append(line_dictionary, ignore_index=True)
        new_line = pd.DataFrame([line_dictionary])
        self.table = pd.concat([self.table, new_line], ignore_index=True)

    @property
    def return_table(self):
        return self.table

    @property
    def return_df(self):
        return self.df
