import pandas as pd
import numpy as np
import re


class TableManip:  
    def __init__(self) -> None:
        self.df = None
        self.dfNew = None
        self.nameNumberLine = None
        self.nameNumberColumn = None
        self.value = None
        self.table = None
        self.value_separate = None
        self.value_fixed_column = None
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
    # def column_home_values(self):
    #     return None
    
    # @column_home_values.setter
    # def column_home_values(self, column_home_value):
    #     self.column_home_value = column_home_value

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
        if self.dfNew is None:
            self.dfNew = self.df
        else:
            self.dfNew = pd.merge(
                self.dfNew, self.df, how='outer')  # type: ignore
        return self.dfNew

    @property
    def infTable(self):
        return self.value

    @infTable.setter
    def infTable(self, table):
        if type(self.nameNumberLine) == str and type(self.nameNumberColumn) == str:
            self.value = table.at[self.nameNumberLine, self.nameNumberColumn]  # pelo nome
        elif type(self.nameNumberLine) == int and type(self.nameNumberColumn) == int:
            self.value = table.iat[self.nameNumberLine, self.nameNumberColumn]  # pelo local
        else:
            print(
                f'line: {self.nameNumberLine} {type(self.nameNumberLine)}'
                f'colum: {self.nameNumberColumn} {type(self.nameNumberColumn)}'
                )

    @property
    def renemar_data(self):
        return self.table

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
        return self.table

    @add_column_nan.setter
    def add_column_nan(self, name_column):
        self.table[name_column] = np.nan

    @property
    def add_value_fixed_column(self):
        return self.table

    @add_value_fixed_column.setter
    def add_value_fixed_column(self, name_column):
        self.table[name_column] = self.value_fixed_column

    @property
    def add_column_clone(self):
        return self.table

    @add_column_clone.setter
    def add_column_clone(self, name_column):
        self.table[name_column] = self.table[self.column_clone]

    @property
    def del_column(self):
        return self.table

    @del_column.setter
    def del_column(self, name_column):
        self.table.drop(name_column, axis=1, inplace=True)

    @property
    def rename_name_column_destiny(self):
        return self.table

    @rename_name_column_destiny.setter
    def rename_name_column_destiny(self, name_column):
        self.table = self.table.rename(columns={self.rename_name_column_origin: name_column})
     
    @property
    def rename_value_column_before(self):
        return self.table

    @rename_value_column_before.setter
    def rename_value_column_before(self, name_column):
        num_line, num_column = self.table.shape
        for line in range(num_line):
            inf = self.table.iat[line, self.table.columns.get_loc(name_column)]
            inf_re = re.search(r'^(.*?) '+ self.value_separate, inf)
            if inf_re:  # só ira alterar se encontrou a self.value_separate
                inf = inf_re.group(1)
            self.table.iat[line, self.table.columns.get_loc(name_column)] = inf

    @property
    def rename_value_column_after(self):
        return self.table

    @rename_value_column_after.setter
    def rename_value_column_after(self, name_column):
        num_line, num_column = self.table.shape
        for line in range(num_line):
            inf = self.table.iat[line, self.table.columns.get_loc(name_column)]
            inf_re = re.search(self.value_separate + r' (.*)$', inf)
            if inf_re:  # só ira alterar se encontrou a self.value_separate
                inf = inf_re.group(1)
            self.table.iat[line, self.table.columns.get_loc(name_column)] = inf
