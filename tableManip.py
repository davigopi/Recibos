import pandas as pd


class TableManip:  
    def __init__(self) -> None:
        self.df = None
        self.dfNew = None
        self.nameNumberLine = None
        self.nameNumberColumn = None
        self.value = None

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
    def merge(self):
        if self.dfNew is None:
            self.dfNew = self.df
        else:
            self.dfNew = pd.merge(
                self.dfNew, self.df, how='outer')  # type: ignore
        return self.dfNew

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
    def infTable(self):
        return self.value

    @infTable.setter
    def infTable(self, table):
        if type(self.nameNumberLine) == str and type(self.nameNumberColumn) == str:
            self.value = table.at[self.nameNumberLine, self.nameNumberColumn]  # pelo nome
        elif type(self.nameNumberLine) == int and type(self.nameNumberColumn) == int:
            self.value = table.iat[self.nameNumberLine, self.nameNumberColumn]  # pelo local
        else:
            print('Indefinido ->', self.nameNumberLine, type(self.nameNumberLine), "###", self.nameNumberColumn, type(self.nameNumberColumn))
