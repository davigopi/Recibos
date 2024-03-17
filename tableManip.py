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
        self.column_home_value = None
        self.value_separate = None
        self.value_before_after = None
        self.column_fixed_value = None

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

    @property
    def column_home_values(self):
        return None
    
    @column_home_values.setter
    def column_home_values(self, column_home_value):
        self.column_home_value = column_home_value

    @property
    def column_fixed_values(self):
        return None
    
    @column_fixed_values.setter
    def column_fixed_values(self, column_fixed_value):
        self.column_fixed_value = column_fixed_value

    @property
    def value_separates(self):
        return None
    
    @value_separates.setter
    def value_separates(self, value_separate):
        self.value_separate = value_separate

    @property
    def value_before_afters(self):
        return None
    
    @value_before_afters.setter
    def value_before_afters(self, value_before_after):
        self.value_before_after = value_before_after

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
    def add_column(self):
        return self.table

    @add_column.setter
    def add_column(self, name_column):
        if self.column_fixed_value is not None:  # criar coluna com valor fixo
            self.table[name_column] = self.column_fixed_value
        elif self.column_home_value is None:
            self.table[name_column] = np.nan
        else:
            self.table[name_column] = self.table[self.column_home_value]

    @property
    def del_column(self):
        return self.table

    @del_column.setter
    def del_column(self, name_column):
        self.table.drop(name_column, axis=1, inplace=True)

    @property
    def rename_name_column(self):
        return self.table

    @rename_name_column.setter
    def rename_name_column(self, name_column):
        self.table = self.table.rename(
            columns={self.column_home_value: name_column})
    
    @property
    def rename_value_column(self):
        return self.table

    @rename_value_column.setter
    def rename_value_column(self, name_column):
        num_line, num_column = self.table.shape
        for line in range(num_line):
            inf = self.table.iat[line, self.table.columns.get_loc(name_column)]
            if self.value_before_after == 'before':
                inf_re = re.search(r'^(.*?) '+ self.value_separate, inf)
            elif self.value_before_after == 'after':
                inf_re = re.search(self.value_separate + r' (.*)$', inf)
            if inf_re:  # só ira alterar se encontrou a self.value_separate
                inf = inf_re.group(1)
            self.table.iat[line, self.table.columns.get_loc(name_column)] = inf
        print(self.table)
