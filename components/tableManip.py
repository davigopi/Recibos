import pandas as pd
import numpy as np
import re
import locale
from components.fileManip import FileManip
from path_file import Path_file


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
        self.list_columns_ata_mes_sma = []
        self.column_vendedor = ''
        self.column_gerente = ''
        self.column_cargo_gerente_geral = ''
        self.column_credito = ''
        self.periodo_valor_qtd_vendas = ''
        self.periodo_valor_qtd_vendas_Gerente = ''
        self.periodo_valor_qtd_vendas_Gerente_Geral = ''
        self.column_qtd_valor_vend = ''

        self.fileManip = FileManip()
        self.path_file = Path_file()
        self.arq_log = self.path_file.path_file_create_user('Appdata', 'log', 'Prob_data.txt')  # noqa
        self.fileManip.arq_log = self.arq_log  # type: ignore

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

    # name_column:
    # 0 column_total_vendidos = 'Total'
    # 1 column_vendedor = 'Vendedor'
    # 2 column_gerente = 'Gerente'
    # 3 column_credito = 'Crédito'
    # 4 periodo_valor_qtd_vendas = '1 Periodo valor qtd vendas'
    # 5 column_qtd_valor_vend = 'Qtd Valor Vend'
    # 6 column_cargo_gerente_geral = 'Cargo_Gerente_Geral'
    @alter_value_line_total_sum.setter
    def alter_value_line_total_sum(self, name_column):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        quantity_line = self.table.shape[0]
        # descobri os ' Qtd. Cotas Inicial' que existem na tabela
        list_qtd_data = []
        list_qtd_data_gerente = []
        list_qtd_data_gerente_geral = []
        list_qtd_data_temp = []
        column_qtd_cotas_inicial = [' Qtd. Cotas Inicial',
                                    ' Qtd. Cotas Inicial_Gerente',
                                    ' Qtd. Cotas Inicial_Gerente_Geral']
        column_qtd_cotas_final = [' Qtd. Cotas Final',
                                  ' Qtd. Cotas Final_Gerente',
                                  ' Qtd. Cotas Final_Gerente_Geral']
        column_data_incial = [' Data inicial',
                              ' Data inicial_Gerente',
                              ' Data inicial_Gerente_Geral']
        column_data_final = [' Data final',
                             ' Data final_Gerente',
                             ' Data final_Gerente_Geral']
        column_1p_referencia = '1P referencia'
        column_data_entrega = 'Data de Entrega'
        column_data_cad_adm = 'Data Cad. Adm'

        cont = 1
        cont_column = 0
        while True:
            column_qtd_inical = str(cont) + column_qtd_cotas_inicial[cont_column]  # noqa
            column_qtd_final = str(cont) + column_qtd_cotas_final[cont_column]  # noqa
            column_dt_inicial = str(cont) + column_data_incial[cont_column]
            column_dt_final = str(cont) + column_data_final[cont_column]
            # column existe na lista de colunas da tabela
            if column_qtd_inical in self.table.columns:
                list_qtd_data_temp.append([
                    column_qtd_inical,
                    column_qtd_final,
                    column_dt_inicial,
                    column_dt_final])
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
        list_qtd_data_full = [list_qtd_data,
                              list_qtd_data_gerente,
                              list_qtd_data_gerente_geral]
        # 0 column_ata_entrega = 'ATA Entrega'
        # 1 column_mes_ent = 'Mes Ent'
        # 2 column_sma_ent = 'Sma Ent'
        # 3 column_ata_cad_adm = 'ATA Cad Adm'
        # 4 column_mes_cad_adm = 'Mes Cad Adm'
        # 5 column_sma_cad_adm = 'Sma Cad Adm'
        for column_ata_mes_sma in self.list_columns_ata_mes_sma:
            # criar nome das novas colunas
            #                   'Total'
            new_name_column = name_column[0] + ' ' + column_ata_mes_sma
            new_name_column_gerente = new_name_column + ' Ger'
            new_name_column_gerente_geral = new_name_column + ' Ger Ger'
            new_name_column_qtd_cotas = column_ata_mes_sma + ' ' + 'qtd cotas'
            new_name_column_qtd_coats_gerente = new_name_column_qtd_cotas + ' Ger'  # noqa
            new_name_column_qtd_coats_gerente_geral = new_name_column_qtd_cotas + ' Ger Ger'  # noqa
            new_name_column_qtd_vendas = 'Qtd Vend ' + column_ata_mes_sma
            new_name_column_qtd_vendas_gerente = new_name_column_qtd_vendas + ' Ger'  # noqa
            new_name_column_qtd_vendas_gerente_geral = new_name_column_qtd_vendas + ' Ger Ger'  # noqa
            # list_name_columns = [
            #     new_name_column,  # Total ATA Entrega                       0
            #     new_name_column_qtd_cotas,  # ATA Entrega qtd cotas         1
            #     new_name_column_gerente,  # Total ATA Entrega Ger           2
            #     new_name_column_qtd_coats_gerente,  # ATA Entrega qtd costa Ger 3 # noqa
            #     new_name_column_qtd_vendas,  # Qtd Vend ATA entrega   4
            #     new_name_column_qtd_vendas_gerente  # Qtd Vend ATA entrega Ger 5 # noqa
            # ]
            list_column_ata = [new_name_column,
                               new_name_column_gerente,
                               new_name_column_gerente_geral]
            list_comumn_qtd_cotas = [new_name_column_qtd_cotas,
                                     new_name_column_qtd_coats_gerente,
                                     new_name_column_qtd_coats_gerente_geral]
            list_column_qtd_vendas = [new_name_column_qtd_vendas,
                                      new_name_column_qtd_vendas_gerente,
                                      new_name_column_qtd_vendas_gerente_geral]
            # pecorerar linha por linha da tabela
            for line in range(quantity_line):
                #                               'Vendedor'
                vendedor = self.table.iloc[line][self.column_vendedor]
                #                               'Gerente'
                gerente = self.table.iloc[line][self.column_gerente]
                cargo_gerente_geral = self.table.iloc[line][self.column_cargo_gerente_geral]  # noqa
                list_profession = [vendedor, gerente, cargo_gerente_geral]

                ata = self.table.iloc[line][column_ata_mes_sma]
                # num_ger = 0
                for key_prof, profession in enumerate(list_profession):
                    # soma da coluna 'Crédito' com  vendedor e a ata
                    # OBS: a soma é feio apenas no primeiro pagamento, ou seja,
                    # ata entrega, ata cad adm, sma entrega...
                    if profession == vendedor:
                        column_prof = self.column_vendedor
                        periodo_valor_qtd_vendas = self.table.iloc[line][self.periodo_valor_qtd_vendas]  # noqa
                    elif profession == gerente:
                        column_prof = self.column_gerente
                        periodo_valor_qtd_vendas = self.table.iloc[line][self.periodo_valor_qtd_vendas_Gerente]  # noqa
                    elif profession == cargo_gerente_geral:
                        column_prof = self.column_cargo_gerente_geral
                        periodo_valor_qtd_vendas = self.table.iloc[line][self.periodo_valor_qtd_vendas_Gerente_Geral]  # noqa
                    periodo_valor_qtd_vendas = str(periodo_valor_qtd_vendas)
                    if 'Qtd. Vendas' in periodo_valor_qtd_vendas:
                        self.table.at[line, self.column_qtd_valor_vend] = 'Qtd Vendas'  # noqa
                    else:
                        self.table.at[line, self.column_qtd_valor_vend] = 'Valor Vendas'  # noqa

                    sum_profession = self.table.loc[
                        (self.table[column_prof] == profession) &
                        (self.table[column_ata_mes_sma] == ata),
                        self.column_credito].apply(convert_str_float).sum()  # type: ignore # noqa
                    #         Total ATA Entrega  0  |  Total ATA Entrega Ger  2
                    self.table.at[line, list_column_ata[key_prof]] = (
                        locale.format_string(
                            "%.2f", sum_profession, grouping=True
                        )
                    )
                    # 'Sma' tem na coluna ata?
                    if 'Sma' in column_ata_mes_sma:
                        continue
                    count_profession = self.table.loc[
                        (self.table[column_prof] == profession) &
                        (self.table[column_ata_mes_sma] == ata),
                        self.column_credito].count()  # type: ignore
                    self.table.at[line, list_column_qtd_vendas[key_prof]] = (  # noqa
                        locale.format_string(
                            "%.2f", count_profession, grouping=True
                        )
                    )
                    # saber se vai compara como quantidade ou total
                    if 'Qtd. Vendas' in periodo_valor_qtd_vendas:
                        value_compare = count_profession
                    else:
                        value_compare = sum_profession
                    # vendedor 0  5 Qtd. Cotas Inicial, 4...  '1 Qtd. Cotas
                    # gerente 1  5 Qtd. Cotas Inicial_Gerente', '4.. '1 Qtd
                    # gerente 2  5 Qtd. Cotas Inicial_Gerente_Geral',.. 1 Q
                    num_cota_temp = 0
                    for column_qtd_data in list_qtd_data_full[key_prof]:
                        column_qtd_cotas_inicial = column_qtd_data[0]
                        value_qci = self.table.iloc[line][column_qtd_cotas_inicial]  # noqa
                        # passar para o proximo se o valor nao exitir
                        if column_qtd_data != list_qtd_data_full[key_prof][-1]:  # noqa
                            if str(value_qci).lower() == 'nan' or value_qci is None:  # noqa
                                continue
                        # receber o valor da coluna Qtd.
                        column_qtd_cotas_final = column_qtd_data[1]
                        column_data_incial = column_qtd_data[2]
                        column_data_final = column_qtd_data[3]
                        value_qcf = self.table.iloc[line][column_qtd_cotas_final]  # noqa
                        value_di = self.table.iloc[line][column_data_incial]
                        value_df = self.table.iloc[line][column_data_final]
                        value_qci = convert_str_float(value_qci)
                        value_qcf = convert_str_float(value_qcf)
                        value_di = convert_to_date(value_di)
                        value_df = convert_to_date(value_df)
                        value_pr = self.table.iloc[line][column_1p_referencia]
                        value_pr = str(value_pr)
                        if 'CADASTRO' in value_pr:
                            column_data = column_data_cad_adm
                        else:
                            column_data = column_data_entrega
                        value_data = self.table.iloc[line][column_data]
                        value_data = convert_to_date(value_data)
                        num_cota = column_qtd_cotas_inicial[0]
                        # if value_compare == 4639466:
                        #     print(f'{value_compare >= value_qci} -> {value_compare} >= {value_qci}')
                        #     if value_compare >= value_qci:
                        #         pass
                        if (
                            value_compare >= value_qci and
                            value_compare <= value_qcf and
                            value_data <= value_df
                        ):
                            # devido a mudança n categoria do tipo de
                            # pagamentos tem vendas antigas que não se
                            # encaixa no inicio da função
                            if value_data >= value_di:
                                break
                            num_cota_temp = num_cota
                        if num_cota == '1':
                            if (
                                value_compare >= value_qci and
                                value_compare <= value_qcf and
                                # value_data >= value_di and
                                value_data <= value_df
                            ):
                                text = f'cliente: {self.table.iloc[line]['Cliente']} \n'  # noqa
                                text += f'cargo: {self.table.iloc[line]['Cargo']} \n'  # noqa
                                text += f'Vendedor: {self.table.iloc[line]['Vendedor']} \n'  # noqa
                                text += f'{value_compare} >= {value_qci}  -> {value_compare >= value_qci} \n'  # noqa
                                text += f'{value_compare} <= {value_qcf}  -> {value_compare <= value_qcf}'  # noqa
                                # text += f'{value_data} >= {value_di}  -> {value_data >= value_di} \n'  # noqa
                                text += f'{value_data} <= {value_df}  -> {value_data <= value_df} \n'  # noqa
                                text += '\n'
                                self.fileManip.writeLog = text
                            if num_cota_temp != 0:
                                num_cota = num_cota_temp
                            else:
                                num_cota = 0
                            break

                    # ATA Entrega qtd cotas 1 | ATA Entrega qtd costa Ger 3
                    num_cota = '{:g}'.format(float(num_cota))
                    self.table.at[line, list_comumn_qtd_cotas[key_prof]] = num_cota  # noqa
                    # n_col = key_prof + 1 + num_ger
                    # self.table.at[line, list_name_columns[n_col]] = num_cota  # noqa
                # num_ger += 1

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
