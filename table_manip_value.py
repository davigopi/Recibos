class Table_manip_value():
    def __init__(self) -> None:
        self.table = None
        self.table_duplicate = None
        self.list_one_two = []
        self.list_one_two_three = []
        self.list_name_change = []

    @property
    def tables(self):
        return self.table
    
    @tables.setter
    def tables(self, table):
        self.table = table

    @property
    def row_duplicate_column_1(self):
        return self.table_duplicate
    
    @row_duplicate_column_1.setter
    def row_duplicate_column_1(self, column):
        duplicatas = self.table.duplicated(subset=[column], keep=False)
        self.table_duplicate  = self.table[duplicatas]

    @property
    def row_duplicate_column_2(self):
        return self.table_duplicate
    
    @row_duplicate_column_2.setter
    def row_duplicate_column_2(self, column):
        duplicatas = self.table.duplicated(
            subset=[column[0], column[1]], keep=False)
        self.table_duplicate  = self.table[duplicatas]

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
        return self.table

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
                    self.table.loc[(self.table[column_name[0]] == nome) &
                                   (self.table[column_name[1]] == cargo),
                                   column_name[0]] = nome_new
            self.list_name_change.append(list_name_change)

    @property
    def data_duplicate_change(self):
        return self.table
    
    @data_duplicate_change.setter
    def data_duplicate_change(self, column):
        for name in self.list_name_change:
            self.table[column] = self.table[column].replace(name[0], name[1])

    @ property
    def list_columns_one_two_three(self):
        return  self.list_one_two_three
    
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
            if data_column_0 == row[column_name[0]] and data_column_1 == row[column_name[1]]:
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
        return self.table

    @edit_data_column_3.setter
    def edit_data_column_3(self, column_name):
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
                        nome_new = column_name[0] + f' (DUPLIC {column_name[2]})'
                        list_name_change.append(nome_new)  # outra tabela
                        meet_rename = True
                if meet_rename is True:
                    self.table.loc[
                        (self.table[column_name[0]] == administradora) &
                        (self.table[column_name[1]] == cargo) &
                        (self.table[column_name[2]] == tabela_recebimento),
                        column_name[0]] = nome_new
                    meet_rename = False
            # server para altera a outra tabela
            self.list_name_change.append(list_name_change)

if __name__ == '__main__':
    import main
