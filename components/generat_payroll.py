# from numpy import append
import pandas as pd
import locale
import os
# import numpy as np
from pathlib import Path
from components.fileManip import PDF
# from fileManip import FileManip

# self.table_single_merge.to_csv(
#     "tables\\table_teste.csv",
#     index=False,
#     header=True,
#     sep=';'
# )


class Generat_payroll:
    def __init__(self, *args, **kwargs) -> None:

        self.model = ''

        self.stop_program = False

        self.profession = ''
        self.column_cargo = ''
        self.column_administradora = ''
        self.column_tabela = ''
        self.column_dt_pag_por = ''
        self.column_1p_referencia = ''
        self.column_1P_recebera = ''
        self.column_D_referencia = ''
        self.column_D_recebera = ''
        self.column_FAT_referencia = ''
        self.column_FAT_recebera = ''
        self.column_credito = ''
        self.column_comissao = ''
        self.column_situacao = ''
        self.column_ata_entrega = ''
        self.column_ata_cad_Adm = ''
        self.data_ata_single = ''
        self.seller_single = ''
        self.data_date_pay = ''
        self.column_cadastro = ''
        self.word = ''

        self.quantity_line_full = 0
        self.quantity_line_ata = 0
        self.quantity_line_weekly = 0
        self.sums = 0
        self.number = 0

        self.list_situacao_to_comission = []
        self.list_recebera_to_comission = []
        self.list_condition_ata = []
        self.list_cargo_not_calc_commis = []
        self.list_columns_end = []
        self.list_columns_new = []
        self.list_columns_ata_ent = []
        self.list_columns_ata_cad = []

        self.column_ata_qtd = []

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
        self.list_cols_full_ata_sing = []

        self.table_single_ata = []
        self.list_single_administradora = []
        self.list_administradora_line = []
        self.list_administradora_line_sum = []
        self.list_administradora_sum_qtdcotasinicial = []
        self.list_administradora_sum_qtdcotasinicial_parc = []
        self.list_table_column_comissao = []
        self.list_table_edit = []
        # self.list_table_column_define = []
        self.list_unique_information = []

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

        # path_tables = Path(__file__).parent
        # self.arqTableTeste = Path()
        # name_arq = 'table_teste1.csv'
        # self.arqTableTeste1 = path_tables / name_arq
        # name_arq = 'table_teste2.csv'
        # self.arqTableTeste2 = path_tables / name_arq
        # name_arq = 'table_teste3.csv'
        # self.arqTableTeste3 = path_tables / name_arq

    @property
    def num_columns(self):
        return self.number

    # recebe uma lista de texto para formar uma palavra que proc nas colunas
    @num_columns.setter
    def num_columns(self, list_text):
        for num in range(2, 100):
            column = list_text[0] + str(num) + list_text[1]
            if column not in self.table_full.columns:
                self.number = num - 1
                break

    @property
    def convert_str_float(self):
        return None

    @convert_str_float.setter
    def convert_str_float(self, table):
        for column in self.list_columns_str_to_float:
            if table[column].dtype == 'object':
                try:
                    table[column] = (table[column].str.replace('.', ''))
                    table[column] = (table[column].str.replace(',', '.'))
                    table[column] = (table[column].astype(float))
                    table[column] = (table[column].round(2))
                except KeyError:
                    continue
        self.table = table

    # 1º ira criar duas lista de todos os vendedores clt e parceiros
    def columns_to_list_full_seller(self):
        self.list_seller_ata = self.table_full_ata[self.profession]
        self.list_seller_ata = self.list_seller_ata.unique()
        self.list_seller_ata.sort()
        self.list_seller_weekly = self.table_full_weekly[self.profession]
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
                x.split('/')[2],
                self.dic_months[x.split('/')[1]], x.split('/')[0]
            )
        )
        # print(self.list_seller_weekly)
        # print(self.list_weekly)

    # 2º define se vendedor/parceiro a primeira é pela ata entrea/cadastro
    def columns_ata_full_seller_single(self):
        p1_referencia = str(
            self.table_seller_single.iloc[0][self.column_1p_referencia]
        )
        if self.column_cadastro in p1_referencia:
            self.list_cols_full_ata_sing = self.list_columns_full_ata_cadastro
            list_ata_cad = self.list_columns_ata_cad
        else:
            self.list_cols_full_ata_sing = self.list_columns_full_ata_entrega
            list_ata_cad = self.list_columns_ata_ent
        if self.profession == 'Gerente':
            self.column_ata_qtd = list_ata_cad[1]
        else:
            self.column_ata_qtd = list_ata_cad[0]

    # 3º Criar uma lista tabelas aparti do dado ata e colunas definidas
    def tables_columns_ata_seller_single(self):
        self.table_single_ata = []
        for ata in self.list_cols_full_ata_sing:
            table = self.table_seller_single[
                self.table_seller_single[ata] == self.data_ata_single
            ].copy()
            table.reset_index(drop=True, inplace=True)
            self.table_single_ata.append([table, ata])
        # informações unicas para o pdf
        self.list_unique_information.append(self.data_ata_single)
        # for table, ata in self.table_single_ata:
        #     if ata == 'ATA 2º Parc':
        #         print(ata)
        #         print(table)
        #         print('')
        #         print('')
        #         table.to_csv(
        #             arqTableTeste, index=False, header=True, sep=';'
        #         )

    # 4º ira mesclar todas as tabelas que tiver valor
    def tables_concat_seller_single(self):
        self.table_single_merge: pd.DataFrame = pd.DataFrame()
        for table, ata in self.table_single_ata:
            if not table.empty:
                self.table_single_merge = pd.concat(
                    [self.table_single_merge, table]
                )

    # 5º verificar se pertence ao cargo especifico para sair ou não
    def is_to_stop_program(self):
        self.stop_program = False
        cargo = self.table_single_merge.iloc[0][self.column_cargo]
        for cargo_not_calc_commis in self.list_cargo_not_calc_commis:
            if cargo_not_calc_commis in cargo:
                print(cargo)
                self.stop_program = True

    # 6º Todas as informações inicia e final dosvalores da administradoras
    def create_dictionary_datas(self):
        self.dic_administradoras = {}

        # list_dupla_administradora_cargo = self.table_single_merge[
        #     [self.column_administradora, self.column_tabela]
        # ].drop_duplicates()

        list_dupla_administradora_cargo = self.table_single_merge[
            [self.column_administradora, self.column_tabela]
        ].drop_duplicates().to_records(index=False).tolist()

        for administradora, tabela in list_dupla_administradora_cargo:
            # print(administradora)
            # print(tabela)
            # print('=============')
            # self.list_single_administradora = self.table_single_merge[
            #     self.column_administradora].unique()
            # for administradora in self.list_single_administradora:
            for line in range(self.quantity_line_full):
                data_administradora = self.table_single_merge.iloc[
                    line][self.column_administradora]
                data_tabela = self.table_single_merge.iloc[
                    line][self.column_tabela]
                if data_administradora == administradora and (
                        data_tabela == tabela):
                    key_dic = administradora + ' - ' + tabela
                    self.dic_administradoras[key_dic] = {}
                    for qtd_cotas in self.list_qtd_cotas_parc:
                        data = self.table_single_merge.iloc[line][qtd_cotas]
                        if not pd.isna(data):
                            self.dic_administradoras[key_dic][qtd_cotas] = data
                    break
        # for key, dic in self.dic_administradoras.items():
        #     print(key)
        #     for key2, value in dic.items():
        #         print(f'{key2} => {value}')
        # print(self.list_single_administradora)

    # 7º ira criar uma lista da administradora e sua linha
    def table_list_administradora_add_line(self):
        self.list_administradora_line = []
        for table, ata in self.table_single_ata:
            if not table.empty:
                quantity_line_table = table.shape[0]
                list_administradora = table[
                    self.column_administradora].unique()
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
        # for (table,
        #      ata,
        #      list_admnimistradora_line
        #      ) in self.list_administradora_line:
        #     print(f'ata -> {ata}')
        #     print(f'list_admnimistradora_line-> {list_admnimistradora_line}')
        #     print(table)
        #     print('')
        #     print('')

    # 8º Ira criar a soma de todos as vendas aparti da ATA especifica
    def table_list_administradora_line_add_sum(self):
        # OBS: infelizmente o comando self.sums =
        # table[self.column_credito].sum(), nao funciona
        self.list_administradora_line_sum = []
        for (
            table,
            ata,
            list_admnimistradora_line
        ) in self.list_administradora_line:
            quantity_line_table = table.shape[0]
            sums = 0
            sums_compliance = 0
            for line in range(quantity_line_table):
                value = table.iloc[line][self.column_credito]
                value = str(value)
                value = value.replace('.', '')
                value = value.replace(',', '.')
                value = float(value)
                sums += value
                if ata in [self.column_ata_entrega, self.column_ata_cad_Adm]:
                    sums_compliance = sums
                else:
                    name_column = ata
                    name_column = name_column.replace('ATA ', '')
                    name_column = 'Situação ' + name_column
                    situacao = table.iloc[line][name_column]
                    if situacao in self.list_situacao_to_comission:
                        sums_compliance += value

            self.list_administradora_line_sum.append([
                table,
                ata,
                sums,
                sums_compliance,
                list_admnimistradora_line,
            ])
        # for (table,
        #      ata,
        #      sums,
        #      sums_compliance,
        #      list_admnimistradora_line
        #      ) in self.list_administradora_line_sum:
        #     print('table_list_administradora_line_add_sum')
        #     print(f'ata -> {ata}')
        #     print(f'sums -> {sums}')
        #     print(f'Soma do confirmados -> {sums_compliance}')
        #     print(f'list_admnimistradora_line ->{list_admnimistradora_line}')
        #     print(f'table {table}')
        #     print('')
        #     print('')

    '''# 9º ira altera o numero da linha criado no 7º passo e vai colocar
    cota inical e cota final para cada administradora baseado na soma
    do 8º passo'''

    def table_list_administradora_sum_add_qtdcotasinicial(self):
        self.list_administradora_sum_qtdcotasinicial = []
        for (
            table,
            ata,
            sums,
            sums_compliance,
            list_admnimistradora_line
        ) in self.list_administradora_line_sum:
            list_administradora_qtdcotas = []
            for administradora_line in list_admnimistradora_line:
                data_administradora = administradora_line[0]
                line = administradora_line[1]
                for column_qtd_cota_inicial in reversed(
                        self.list_qtd_cotas_inicial):
                    # try:
                    value = table.iloc[line][column_qtd_cota_inicial]
                    value = str(value)
                    value = value.replace('.', '')
                    value = value.replace(',', '.')
                    value = float(value)
                    # except KeyError:
                    #     continue
                    # verifique se a soma do total é maior ou igual a regras
                    # caso não enconter nas regras e chegue a ultima coluna
                    # passe a ultima coluna como regra
                    c_1_q_c_i = self.list_qtd_cotas_inicial[0]
                    if sums >= value or column_qtd_cota_inicial == c_1_q_c_i:
                        column_qtd_cota_final = self.dic_qtd_cotas_parc[
                            column_qtd_cota_inicial][0]
                        value_end = table.iloc[line][column_qtd_cota_final]
                        value_end = str(value_end)
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
                sums_compliance,
                list_administradora_qtdcotas
            ])
        # for (table,
        #      ata,
        #      sums,
        #      sums_compliance,
        #      list_admnimistradora_line
        #      ) in self.list_administradora_sum_qtdcotasinicial:
        #     print('')
        #     print('')
        #     print('table_list_administradora_sum_add_qtdcotasinicial')
        #     print(f'ata -> {ata}')
        #     print(f'sums -> {sums}')
        #     text = 'list_admnimistradora_line ->'
        #     print(f'{text} {list_admnimistradora_line}')
        #     print(f'table {table}')
        #     print('')
        #     print('')

    '''10º  ira adicionar o valor da porcentagem de comissão baseado na soma
    total de vendas do 8º passo e coloca junta a lista '''

    def table_list_administradora_sum_add_full(self):
        self.list_administradora_sum_qtdcotasinicial_parc = []
        for (
            table,
            ata,
            sums,
            sums_compliance,
            list_administradora_qtdcotas
        ) in self.list_administradora_sum_qtdcotasinicial:
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
                list_column_parc = self.dic_qtd_cotas_parc[
                    column_qtdcotainicial]
                for key2, column_parc in enumerate(list_column_parc):
                    if key2 == 0:  # tira a primeira coluna qtdcotafinal
                        continue
                    new_column_parc = column_parc.replace(self.word, '')
                    if number_ata in new_column_parc[-2:]:
                        break
                for line in range(quantity_line_table):
                    data_administradora = table.iloc[
                        line][self.column_administradora]
                    if administradora == data_administradora:
                        break
                # print(column_parc)
                porcentagem_ata = table.iloc[line][column_parc]
                if pd.isna(porcentagem_ata):
                    porcentagem_ata = 0
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
                sums,
                sums_compliance,
                list_administradora_qtdcotas_parc
            ])
        # for (table,
        #      ata,
        #      sums,
        #      sums_compliance,
        #      list_administradora_qtdcotas_parc
        #      ) in self.list_administradora_sum_qtdcotasinicial_parc:
        #     print('table_list_administradora_sum_add_full')
        #     print(f'ata -> {ata}')
        #     print(f'sums -> {sums}')
        #     text = 'list_administradora_qtdcotas_parc - >'
        #     print(f'{text} {list_administradora_qtdcotas_parc}')
        #     print(f'table {table}')
        #     print('')
        #     print('')

    '''11º
    acrecenta sum_comissao, sum_comissao_compliance, percentage_compliance,
    vendedor, cargo,'''

    def add_column_comissao(self):
        sum_all_comissao = 0
        sum_all_comissao_gerente = 0
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        for (
            table,
            ata,
            sums,
            sums_compliance,
            list_administradora_qtdcotas_parc
        ) in self.list_administradora_sum_qtdcotasinicial_parc:
            table[self.list_columns_new[2]] = '0'
            vendedor = table.iloc[0][self.profession]
            cargo = table.iloc[0][self.column_cargo]
            sum_comissao = 0
            text = ata
            text = text.replace(' ', '')
            text = text.replace('ATA', '')
            text = text.replace('º', '')
            text = text.replace('Parc', '')
            text = text.replace('Entrega', '1')
            text = text.replace('CadAdm', '1')
            column_situacao_parc = self.column_situacao
            if text != '1':
                column_situacao_parc += ' ' + text + 'º Parc'
            if self.profession == 'Gerente':
                text += '_Gerente'
            quantity_line_table = table.shape[0]
            # print(self.column_ata_qtd)
            for line in range(quantity_line_table):
                text2 = table.iloc[line][self.column_ata_qtd]
                name_column = text2 + ' Parc ' + text
                data_percentual = table.iloc[line][name_column]
                if pd.isnull(data_percentual):
                    data_percentual = 0
                text_perc = str(data_percentual) + ' %'
                table.loc[line, self.list_columns_new[2]] = text_perc
                data_percentual = float(data_percentual) / 100
                # ['Entrega', 'Cad Adm', 'Parc', 'FAT']
                entrega = self.list_condition_ata[0]
                cad_adm = self.list_condition_ata[1]
                parc = self.list_condition_ata[2]
                fat = self.list_condition_ata[3]
                if entrega in ata or cad_adm in ata:
                    data_recebera = (
                        table.iloc[line][self.column_1P_recebera])
                elif parc in ata:
                    data_recebera = (
                        table.iloc[line][self.column_D_recebera])
                elif fat in ata:
                    data_recebera = (
                        table.iloc[line][self.column_FAT_recebera])
                data_situacao = table.iloc[line][column_situacao_parc]
                # list_situacao_to_comission = ['NORMAL', 'PAGA']
                list_situacao = self.list_situacao_to_comission
                if data_situacao not in list_situacao:
                    data_recebera = 'NAO'
                    '''devido a emissão deste recibos poderem ser feito em
                     momentos futuros e pagamento da coluna "Situação"
                    não esta na list_situacao_to_comission temos que ver se
                    e entrega para ão gera diferente dos recibos emitidos
                    no momento certo'''
                    if entrega in ata or cad_adm in ata:
                        data_recebera = (
                            table.iloc[line][self.column_1P_recebera])
                # list_recebera_to_comission = ['SIM']
                list_recebera = self.list_recebera_to_comission
                if data_recebera in list_recebera:
                    calculate_commission = True
                else:
                    calculate_commission = False
                if calculate_commission:
                    value = table.iloc[line][self.column_credito]
                    value = str(value)
                    value = value.replace('.', '')
                    value = value.replace(',', '.')
                    value = float(value)
                    comissao = value * data_percentual
                    sum_comissao += comissao
                else:
                    comissao = 0
                comissao = locale.format_string(
                    "%.2f", comissao, grouping=True)
                table.loc[line, self.column_comissao] = comissao
            if (sums_compliance / sums) >= 0.5:
                sum_comissao_compliance = sum_comissao
                sum_all_comissao += sum_comissao
            else:
                sum_comissao_compliance = 0
            sum_all_comissao_gerente += sum_comissao
            percentage_compliance = str(
                round(((sums_compliance / sums) * 100), 1)
            ) + '%'
            self.list_table_column_comissao.append([
                table,
                ata,
                sums,
                sums_compliance,
                sum_comissao,
                sum_comissao_compliance,
                percentage_compliance,
                vendedor,
                cargo,
                list_administradora_qtdcotas_parc
            ])
        self.list_unique_information.append(sum_all_comissao)
        self.list_unique_information.append(sum_all_comissao_gerente)
        # for (table,
        #      ata,
        #      sums,
        #      sums_compliance,
        #      sum_comissao,
        #      sum_comissao_compliance,
        #      percentage_compliance,
        #      vendedor,
        #      cargo,
        #      list_administradora_qtdcotas_parc
        #      ) in self.list_table_column_comissao:
        #     print(f'ATA -> {ata}')
        #     print(f'soma do credito -> {sums}')
        #     print(f'soma do comissao -> {sum_comissao}')
        #     print(f'Vendedor -> {vendedor}')
        #     print(f'cargo -> {cargo}')
        #     print(f'percentage_compliance -> {percentage_compliance}')
        #     text = 'list_administradora_qtdcotas_parc ->'
        #     print(f'{text} {list_administradora_qtdcotas_parc}')
        #     print(f'table: {table}')
        #     print('')
        #     print('')

    def edit_table(self):
        self.list_table_edit = []
        table_full: pd.DataFrame = pd.DataFrame()
        for (table,
             ata,
             sums,
             sums_compliance,
             sum_comissao,
             sum_comissao_compliance,
             percentage_compliance,
             vendedor,
             cargo,
             list_administradora_qtdcotas_parc
             ) in self.list_table_column_comissao:
            # excluir comissão zerada
            table = table[table[self.column_comissao] != '0,00'].copy()
            table.reset_index(drop=True, inplace=True)
            # colocar coluna Parcela
            text = ata
            text = text.replace('ATA', '').replace('º Parc', 'ª')
            text = text.replace('Entrega', '1ª').replace('Cad Adm', '1ª')
            table[self.list_columns_new[0]] = text
            table[self.list_columns_new[1]] = percentage_compliance
            # adicionar coluna comissão
            text = text.replace('ª', '')
            if table_full.empty:
                table_full = table
            else:
                table_full = pd.concat([table_full, table], ignore_index=True)
            # excluir linhas comissão zerada
            table_full.reset_index(drop=True, inplace=True)
            table = table[self.list_columns_end]
            self.list_table_edit.append([
                table,
                ata,
                sums,
                sums_compliance,
                sum_comissao,
                sum_comissao_compliance,
                percentage_compliance,
                vendedor,
                cargo,
                list_administradora_qtdcotas_parc
            ])
        table_full = table_full[self.list_columns_end]
        self.list_unique_information.append(table_full)
    # table_full.to_csv(self.arqTableTeste1, index=False, header=True, sep=';')
    # limitas as colunas da tabela que serão impressa no pdf
    # def table_columns_end(self):
    #     self.list_table_column_define = []
    #     for (
    #         table,
    #         ata,
    #         sums,
    #         sums_compliance,
    #         sum_comissao,
    #         sum_comissao_compliance,
    #         percentage_compliance,
    #         vendedor,
    #         cargo,
    #         list_administradora_qtdcotas_parc
    #     ) in self.list_table_column_comissao:
    #         list_columns_end_ATA = self.list_columns_end
    #         new_table = table[list_columns_end_ATA]
    #         self.list_table_column_define.append([
    #             new_table,
    #             ata,
    #             sums,
    #             sums_compliance,
    #             sum_comissao,
    #             sum_comissao_compliance,
    #             percentage_compliance,
    #             vendedor,
    #             cargo,
    #             list_administradora_qtdcotas_parc
    #         ])

    def table_convert_pdf(self):
        # Configurar a localização para o Brasil
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        size_font = 8
        size_font2 = 7
        size_line = 6
        space_paragraph = 2
        begin = True
        ata2 = self.list_unique_information[0]
        sum_all_comissao = self.list_unique_information[1]
        sum_all_comissao_gerente = self.list_unique_information[2]
        table_full = self.list_unique_information[3]
        list_ata_sum_comissao_credito = []
        # Cria uma instância da classe PDF
        pdf = PDF()
        pdf.title = 'RECIBO DE PAGAMENTO'
        pdf.text_size_head = 12
        pdf.text_size_footer = 10
        pdf.text_size_table = 6
        pdf.cell_height = 4
        pdf.space_columns = 4
        pdf.add_page()
        pdf.add_image('select.jpg', 172, 10, 28, 9)
        if self.list_table_edit == []:
            print("Lista vazia")
            return '0', 'zerado'
        if self.profession == 'Gerente':
            comissao = sum_all_comissao_gerente
        else:
            comissao = sum_all_comissao
        if comissao == 0:
            print("Comissão zerada")
            return '0', 'zerado'
        for (
            table,
            ata,
            sums,
            sums_compliance,
            sum_comissao,
            sum_comissao_compliance,
            percentage_compliance,
            vendedor,
            cargo,
            list_administradora_qtdcotas_parc
        ) in self.list_table_edit:
            if begin is True:
                pdf.set_font('Arial', '', size_font)
                comissao = locale.currency(
                    comissao,  # type: ignore
                    grouping=True
                )
                # sum_all_comissao_gerente = locale.currency(
                #     sum_all_comissao_gerente,  # type: ignore
                #     grouping=True
                # )
                # Guarda a posição inicial do texto
                text = 'FUNCIONÁRIO:'
                pdf.add_underlined_text(text, size_font, size_line)
                text = f'{vendedor}'
                text2 = f'ATA: {ata2}'
                pdf.add_content_in_columns(
                    [text, text2],
                    2,
                    size_font,
                    size_line
                )
                text = f'{cargo}'
                # if self.profession == 'Gerente':
                #     text2 = f'Total a receber:  R$ {
                #   sum_all_comissao_gerente}'
                # else:
                #     text2 = f'Total a receber:  R$ {sum_all_comissao}'
                pdf.add_content_in_columns(
                    [text, comissao],
                    2,
                    size_font,
                    size_line
                )
                pdf.ln(space_paragraph * 2)
                begin = False

            # Adiciona texto ao PDF
            pdf.set_font('Arial', '', size_font2)
            sums = locale.currency(sums, grouping=True)
            sums_compliance = locale.currency(sums_compliance, grouping=True)
            sum_comissao = locale.currency(sum_comissao, grouping=True)
            sum_comissao_compliance = locale.currency(
                sum_comissao_compliance, grouping=True)
            commission = False
            for (
                administradora_qtdcotas_parc
            ) in list_administradora_qtdcotas_parc:
                # administradora = administradora_qtdcotas_parc[0]
                # column_qtd_cotas_inicial = administradora_qtdcotas_parc[1]
                data_qtd_cotas_inicial = administradora_qtdcotas_parc[2]
                # column_qtd_cotas_final = administradora_qtdcotas_parc[3]
                data_qtd_cotas_final = administradora_qtdcotas_parc[4]
                # column_parc = administradora_qtdcotas_parc[5]
                data_parc = administradora_qtdcotas_parc[6]
                if data_parc != 0:
                    commission = True
                data_qtd_cotas_inicial = locale.currency(
                    data_qtd_cotas_inicial, grouping=True)
                data_qtd_cotas_final = locale.currency(
                    data_qtd_cotas_final, grouping=True)
            if commission and not (table.empty):
                list_ata_sum_comissao_credito.append(
                    [ata,
                     sums,
                     sums_compliance,
                     sum_comissao,
                     sum_comissao_compliance,
                     percentage_compliance]
                )
                if self.model == '1':
                    text = ata
                    text = text.replace('ATA', '')
                    text = text.replace('º Parc', 'ª Parcela')
                    text = text.replace('Entrega', '1ª Parcela')
                    text = text.replace('Cad Adm', '1ª Parcela')
                    pdf.add_underlined_text(text, size_font, size_line)
                    pdf.add_table(table)
                    pdf.ln(space_paragraph)
                    pdf.multi_cell(0, size_line, '')
        if self.model == '2':
            pdf.add_table(table_full)
            pdf.ln(space_paragraph)
            pdf.multi_cell(0, size_line, '')
        text = 'Resumo'
        pdf.add_underlined_text(text, size_font, size_line)

        list_ata = []
        list_sum_comissao = []
        # list_sum_credito = []
        list_sums_compliance = []
        list_sum_comissao_compliance = []
        list_percentage_compliance = []
        for (
            ata,
            sums,
            sums_compliance,
            sum_comissao,
            sum_comissao_compliance,
            percentage_compliance
        ) in list_ata_sum_comissao_credito:
            text = ata
            text = text.replace('ATA', '').replace('º Parc', 'ª Parcela')
            text = text.replace('Entrega', '1ª Parcela')
            text = text.replace('Cad Adm', '1ª Parcela')
            list_ata.append(text)
            # list_sum_credito.append(sums)
            list_sums_compliance.append(sums_compliance)
            list_sum_comissao.append(sum_comissao)
            list_sum_comissao_compliance.append(sum_comissao_compliance)
            list_percentage_compliance.append(percentage_compliance)
        if self.profession == 'Vendedor':
            data = {
                'TOTAL': list_ata,
                # 'CRÉDITO': list_sum_credito,
                'CRÉDITO': list_sums_compliance,
                'COMISSÃO': list_sum_comissao,
                'ADIMPLÊNCIA': list_percentage_compliance,
                'COMISSÃO ADIMPLENTE': list_sum_comissao_compliance,
            }
        else:
            data = {
                'TOTAL': list_ata,
                # 'CRÉDITO': list_sum_credito,
                'CRÉDITO': list_sums_compliance,
                'COMISSÃO': list_sum_comissao,
            }
        df = pd.DataFrame(data)
        pdf.add_table(df)
        pdf.ln(space_paragraph)
        text = ''
        text2 = ''
        # if self.profession == 'Gerente':
        #     text = f'TOTAL COMISSÃO: R$ {sum_all_comissao_gerente}'
        # else:
        #     text = f'TOTAL COMISSÃO: R$ {sum_all_comissao}'
        pdf.add_text_to_end_of_line(comissao, size_font, size_line)
        pdf.ln(space_paragraph)
        pdf.ln(space_paragraph)
        pdf.ln(space_paragraph)
        pdf.ln(space_paragraph)
        text = ' '
        pdf.add_underlined_text(text, size_font, size_line)
        text = '                      ASSINATURA'
        text2 = 'FORTALEZA, ____/____/____ '
        pdf.add_content_in_columns([text, text2], 2, size_font, size_line)
        # Salva o PDF
        folder_documnts = os.path.expanduser("~/Documents")
        new_folder = os.path.join(folder_documnts, "RECIBO")
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        name_ata = self.data_ata_single
        name_ata = name_ata.replace('/', ' ')
        if self.word == '_Gerente':
            text_profession = 'Supervisor'
        else:
            text_profession = ''
        name_file = f'RP {text_profession} {name_ata} {vendedor}.pdf'
        path_file = os.path.join(new_folder, name_file)
        pdf.output(path_file)
        return comissao, vendedor


if __name__ == '__main__':
    generat_payroll = Generat_payroll()
    is_gerente = True
    # is_gerente = False
    model = '1'
    model = '2'
    seller_single_unit = ''
    # seller_single_unit = 'MARIA ILLYEDJA RODRIGUES DE SOUZA'
    # seller_single_unit = 'PARCEIRINHO EQUIPE - VALMON'
    # seller_single_unit = 'DENISE VITOR COSTA'
    # 'ANTONIO HELIO DE SOUSA TORRES',
    column_vendedor = 'Vendedor'
    column_gerente = 'Gerente'
    column_cargo = 'Cargo'
    column_administradora = 'Administradora'
    column_tabela = 'Tabela'
    column_dt_pag_por = 'Dt pag. por'
    column_1p_referencia = '1P referencia'
    column_1P_recebera = '1P recebera'
    column_D_referencia = 'D+ referencia'
    column_D_recebera = 'D+ recebera'
    column_FAT_referencia = 'FAT referencia'
    column_FAT_recebera = 'FAT recebera'
    column_credito = 'Crédito'
    column_comissao = 'Comissão'
    column_situacao = 'Situação'
    column_ata_cad_Adm = 'ATA Cad Adm'
    column_ata_entrega = 'ATA Entrega'
    column_sma_ent = 'Sma Ent'
    column_sma_cad_adm = 'Sma Cad Adm'
    column_cliente = 'Cliente'
    column_n_contrato = 'Nº Contrato'
    column_grupo = 'Grupo'
    column_cota = 'Cota'
    column_data_entrega = 'Data de Entrega'
    column_cad_adm = 'Data Cad. Adm'
    column_new_parcela = 'Parcela'
    column_new_adimplencia = 'Adimplência'
    column_new_porcentagem_comissão = '%'
    column_ata_entrega_qtd_cotas = 'ATA Entrega qtd cotas'
    column_ata_entrega_qtd_cotas_ger = 'ATA Entrega qtd cotas Ger'
    column_ata_cad_adm_qtd_cotas = 'ATA Cad Adm qtd cotas'
    column_ata_cad_adm_qtd_cotas_ger = 'ATA Cad Adm qtd cotas Ger'
    # definição de variavel
    if is_gerente:
        profession = column_gerente
        word = '_Gerente'
    else:
        profession = column_vendedor
        word = ''
    data_ata_single = 'MAIO/2024'
    table_full = pd.read_csv(
        "tables\\tableMerge.csv",
        sep=';',
        encoding='utf-8',
        dtype=str
    )
    generat_payroll.table_full = table_full
    generat_payroll.num_columns = ['ATA ', 'º Parc']
    num_atas_parc = generat_payroll.number  # num col -> ATA {N} º Parc
    list_columns_full_ata = [column_ata_entrega, column_ata_cad_Adm]
    list_columns_full_weekly = [column_sma_ent, column_sma_cad_adm]
    list_columns_new = [
        column_new_parcela,
        column_new_adimplencia,
        column_new_porcentagem_comissão
    ]
    list_columns_end = [
        column_new_parcela,
        column_administradora,
        column_n_contrato,
        column_data_entrega,
        column_cliente,
        column_credito,
        column_new_porcentagem_comissão,
        column_comissao,
        column_new_adimplencia,
        # column_cad_adm,
        # column_grupo,
        # column_cota,
    ]

    list_columns_ata_ent = [
        column_ata_entrega_qtd_cotas,
        column_ata_entrega_qtd_cotas_ger
    ]
    list_columns_ata_cad = [
        column_ata_cad_adm_qtd_cotas,
        column_ata_cad_adm_qtd_cotas_ger
    ]
    # Preencher o restante das colunas sequenciais
    for i in range(2, num_atas_parc + 1):
        list_columns_full_ata.append(f'ATA {i}º Parc')
        list_columns_full_weekly.append(f'Sma {i}º Parc')
    list_seller_single_all = []

    # é por ata ou por semana ata?
    # ira selecionar tabela que tenha data_ata_single e o
    # profesion(Vendedor ou Gerete)
    for column in list_columns_full_ata:
        table_full_ata_def = (
            table_full.loc[table_full[column] == data_ata_single]
        )
        list_unique = table_full_ata_def[profession].unique()
        if len(list_unique) > 0:
            list_seller_single_all.extend(list_unique)

    list_seller_single = []
    for seller in list_seller_single_all:
        if seller not in list_seller_single:
            list_seller_single.append(seller)
    list_seller_single.sort()

    comissao_anterior1 = 0
    vendedor_anterior1 = ''
    comissao_anterior2 = 0
    vendedor_anterior2 = ''
    comissao_anterior3 = 0
    vendedor_anterior3 = ''
    for seller_single in list_seller_single:
        if seller_single_unit:
            if seller_single_unit not in seller_single:
                continue
        print('\n \n', seller_single)
        generat_payroll = Generat_payroll()
        pathTables = Path(__file__).parent.parent / 'tables'
        name_arq = 'table_teste.csv'
        # arqTableTeste = pathTables / name_arq
        table_full = pd.read_csv(
            "tables\\tableMerge.csv",
            sep=';',
            encoding='utf-8',
            dtype=str
        )

        # column_situacao_d = 'º Parc'

        data_date_pay = 'DIA DA SEMANA'
        column_cadastro = 'CADASTRO'

        list_situacao_to_comission = ['NORMAL', 'PAGA']
        list_recebera_to_comission = ['SIM']
        list_condition_ata = ['Entrega', 'Cad Adm', 'Parc', 'FAT']
        list_cargo_not_calc_commis = ['ESTAGIÁRIO', 'ZERADO']

        # Definir o número de grupos e de parcelas

        generat_payroll.table_full = table_full

        generat_payroll.num_columns = ['ATA ', 'º Parc']
        num_atas_parc = generat_payroll.number  # num col -> ATA {N} º Parc
        generat_payroll.num_columns = ['', ' Qtd. Cotas Inicial']
        num_regras = generat_payroll.number  # num col -> {N} Qtd. Cotas Inicia
        generat_payroll.num_columns = [str(num_regras) + ' Parc ', '']
        num_parcelas = generat_payroll.number  # num col  -> Parc {N}

        generat_payroll.word = word
        list_columns_full_ata = [column_ata_entrega, column_ata_cad_Adm]
        list_columns_full_weekly = [column_sma_ent, column_sma_cad_adm]
        # Preencher a lista sequencialmente
        for i in range(2, num_atas_parc + 1):
            list_columns_full_ata.append(f'ATA {i}º Parc')
            list_columns_full_weekly.append(f'Sma {i}º Parc')
        list_qtd_cotas_parc = []
        list_qtd_cotas_inicial = []
        list_qtd_cotas_final = []
        dic_qtd_cotas_parc = {}
        for i in range(1, num_regras + 1):
            list_qtd_cotas_parc.append(f'{i} Qtd. Cotas Inicial{word}')
            list_qtd_cotas_inicial.append(f'{i} Qtd. Cotas Inicial{word}')
            list_qtd_cotas_parc.append(f'{i} Qtd. Cotas Final{word}')
            list_qtd_cotas_final.append(f'{i} Qtd. Cotas Final{word}')
            list = []
            for j in range(1, num_parcelas + 1):
                list_qtd_cotas_parc.append(f'{i} Parc {j}{word}')
                list.append(f'{i} Parc {j}{word}')
            chave = f'{i} Qtd. Cotas Inicial{word}'
            valor = [f'{i} Qtd. Cotas Final{word}'] + list
            dic_qtd_cotas_parc[chave] = valor

        # Preencher o dicionário sequencialmente
        # for i in range(1, num_grupos + 1):
        #     chave_inicial = f'{i} Qtd. Cotas Inicial'
        #     valores = (
        #         [f'{i} Qtd. Cotas Final'] +
        #         [f'{i} Parc {j}' for j in range(1, num_parcelas + 1)]
        #     )
        #     dic_qtd_cotas_parc[chave_inicial] = valores

        # list_qtd_cotas_parc = [
        #     '1 Qtd. Cotas Inicial', '1 Qtd. Cotas Final',
        #     '1 Parc 1', '1 Parc 2', '1 Parc 3', '1 Parc 4', '1 Parc 5',
        #     '1 Parc 6', '1 Parc 7', '1 Parc 8', '1 Parc 9', '1 Parc 10',
        #     '2 Qtd. Cotas Inicial', '2 Qtd. Cotas Final',
        #     '2 Parc 1', '2 Parc 2', '2 Parc 3', '2 Parc 4', '2 Parc 5',
        #     '2 Parc 6', '2 Parc 7', '2 Parc 8', '2 Parc 9', '2 Parc 10',
        #     '3 Qtd. Cotas Inicial', '3 Qtd. Cotas Final',
        #     '3 Parc 1', '3 Parc 2', '3 Parc 3', '3 Parc 4', '3 Parc 5',
        #     '3 Parc 6', '3 Parc 7', '3 Parc 8', '3 Parc 9', '3 Parc 10',
        #     '4 Qtd. Cotas Inicial', '4 Qtd. Cotas Final',
        #     '4 Parc 1', '4 Parc 2', '4 Parc 3', '4 Parc 4', '4 Parc 5',
        #     '4 Parc 6', '4 Parc 7', '4 Parc 8', '4 Parc 9', '4 Parc 10',
        #     '5 Qtd. Cotas Inicial', '5 Qtd. Cotas Final',
        #     '5 Parc 1', '5 Parc 2', '5 Parc 3', '5 Parc 4', '5 Parc 5',
        #     '5 Parc 6', '5 Parc 7', '5 Parc 8', '5 Parc 9', '5 Parc 10',
        # ]

        # dic_qtd_cotas_parc = {
        #     '1 Qtd. Cotas Inicial': [
        #         '1 Qtd. Cotas Final',
        #         '1 Parc 1', '1 Parc 2', '1 Parc 3', '1 Parc 4', '1 Parc 5',
        #         '1 Parc 6', '1 Parc 7', '1 Parc 8', '1 Parc 9', '1 Parc 10'
        #     ],
        #     '2 Qtd. Cotas Inicial': [
        #         '2 Qtd. Cotas Final',
        #         '2 Parc 1', '2 Parc 2', '2 Parc 3', '2 Parc 4', '2 Parc 5',
        #         '2 Parc 6', '2 Parc 7', '2 Parc 8', '2 Parc 9', '2 Parc 10'
        #     ],
        #     '3 Qtd. Cotas Inicial': [
        #         '3 Qtd. Cotas Final',
        #         '3 Parc 1', '3 Parc 2', '3 Parc 3', '3 Parc 4', '3 Parc 5',
        #         '3 Parc 6', '3 Parc 7', '3 Parc 8', '3 Parc 9', '3 Parc 10'
        #     ],
        #     '4 Qtd. Cotas Inicial': [
        #         '4 Qtd. Cotas Final',
        #         '4 Parc 1', '4 Parc 2', '4 Parc 3', '4 Parc 4', '4 Parc 5',
        #         '4 Parc 6', '4 Parc 7', '4 Parc 8', '4 Parc 9', '4 Parc 10'
        #     ],
        #     '5 Qtd. Cotas Inicial': [
        #         '5 Qtd. Cotas Final',
        #         '5 Parc 1', '5 Parc 2', '5 Parc 3', '5 Parc 4', '5 Parc 5',
        #         '5 Parc 6', '5 Parc 7', '5 Parc 8', '5 Parc 9', '5 Parc 10'
        #     ],
        #     '6 Qtd. Cotas Inicial': [
        #         '6 Qtd. Cotas Final',
        #         '6 Parc 1', '6 Parc 2', '6 Parc 3', '6 Parc 4', '6 Parc 5',
        #         '6 Parc 6', '6 Parc 7', '6 Parc 8', '6 Parc 9', '6 Parc 10'
        #     ]
        # }

        dic_months = {
            'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4, 'MAIO': 5,
            'JUNHO': 6, 'JULHO': 7, 'AGOSTO': 8, 'SETEMBRO': 9, 'OUTUBRO': 10,
            'NOVEMBRO': 11, 'DEZEMBRO': 12
        }

        # variaveis criada atravez de outras

        list_columns_full_ata_entrega = [
            item for item in list_columns_full_ata if item != column_ata_cad_Adm]  # noqa
        list_columns_full_ata_cadastro = [
            item for item in list_columns_full_ata if item != column_ata_entrega]  # noqa

        name_columns_full = table_full.columns.tolist()

        table_full_ata = table_full[
            table_full[column_dt_pag_por] != data_date_pay]
        table_full_weekly = table_full[
            table_full[column_dt_pag_por] == data_date_pay]
        table_seller_single = table_full[
            table_full[profession] == seller_single]
        generat_payroll.table_seller_single = table_seller_single

        quantity_line_full = table_full.shape[0]
        quantity_line_ata = table_full_ata.shape[0]
        quantity_line_weekly = table_full_weekly.shape[0]

        # exportar variaveis
        generat_payroll.data_ata_single = data_ata_single
        generat_payroll.seller_single = seller_single
        # generat_payroll.arqTableTeste = arqTableTeste
        generat_payroll.model = model

        generat_payroll.column_credito = column_credito
        generat_payroll.column_administradora = column_administradora
        generat_payroll.column_tabela = column_tabela
        generat_payroll.profession = profession
        generat_payroll.column_cargo = column_cargo
        generat_payroll.column_dt_pag_por = column_dt_pag_por
        generat_payroll.column_1p_referencia = column_1p_referencia
        generat_payroll.column_1P_recebera = column_1P_recebera
        generat_payroll.column_D_referencia = column_D_referencia
        generat_payroll.column_D_recebera = column_D_recebera
        generat_payroll.column_FAT_referencia = column_FAT_referencia
        generat_payroll.column_FAT_recebera = column_FAT_recebera
        generat_payroll.column_comissao = column_comissao
        generat_payroll.column_situacao = column_situacao
        generat_payroll.column_ata_entrega = column_ata_entrega
        generat_payroll.column_ata_cad_Adm = column_ata_cad_Adm
        # generat_payroll.column_situacao_d = column_situacao_d

        generat_payroll.data_date_pay = data_date_pay
        generat_payroll.column_cadastro = column_cadastro

        generat_payroll.list_situacao_to_comission = list_situacao_to_comission
        generat_payroll.list_recebera_to_comission = list_recebera_to_comission
        generat_payroll.list_condition_ata = list_condition_ata
        generat_payroll.list_cargo_not_calc_commis = list_cargo_not_calc_commis
        generat_payroll.list_columns_new = list_columns_new
        generat_payroll.list_columns_end = list_columns_end
        generat_payroll.list_columns_ata_ent = list_columns_ata_ent
        generat_payroll.list_columns_ata_cad = list_columns_ata_cad

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

        # fim da exportacao variavel
        list_columns_str_to_float = (
            list_qtd_cotas_inicial + list_qtd_cotas_final
        )
        list_columns_str_to_float.append(column_credito)
        generat_payroll.list_columns_str_to_float = list_columns_str_to_float
        generat_payroll.convert_str_float = table_full
        # generat_payroll.table_full = generat_payroll.convert_str_float
        generat_payroll.columns_to_list_full_seller()
        generat_payroll.columns_ata_full_seller_single()
        generat_payroll.tables_columns_ata_seller_single()
        generat_payroll.tables_concat_seller_single()
        generat_payroll.is_to_stop_program()
        stop_program = generat_payroll.stop_program
        if stop_program:
            continue
        generat_payroll.create_dictionary_datas()
        generat_payroll.table_list_administradora_add_line()
        generat_payroll.table_list_administradora_line_add_sum()
        generat_payroll.table_list_administradora_sum_add_qtdcotasinicial()
        generat_payroll.table_list_administradora_sum_add_full()
        generat_payroll.add_column_comissao()
        # generat_payroll.table_columns_end()
        generat_payroll.edit_table()
        comissao, vendedor = generat_payroll.table_convert_pdf()
        comissao = comissao.replace('R$', '').replace(' ', '')
        comissao = comissao.replace('.', '').replace(',', '.')
        comissao = float(comissao)
        if comissao >= comissao_anterior1:
            comissao_anterior3 = comissao_anterior2
            vendedor_anterior3 = vendedor_anterior2
            comissao_anterior2 = comissao_anterior1
            vendedor_anterior2 = vendedor_anterior1
            comissao_anterior1 = comissao
            vendedor_anterior1 = vendedor
        elif comissao >= comissao_anterior2:
            comissao_anterior3 = comissao_anterior2
            vendedor_anterior3 = vendedor_anterior2
            comissao_anterior2 = comissao
            vendedor_anterior2 = vendedor
        elif comissao >= comissao_anterior3:
            comissao_anterior3 = comissao
            vendedor_anterior3 = vendedor
    text = f'1º maior comissão: {vendedor_anterior1}, '
    text += f' sua comissão é: {comissao_anterior1} \n'
    text += f'2º maior comissão: {vendedor_anterior2}, '
    text += f' sua comissão é: {comissao_anterior2} \n'
    text += f'3º maior comissão: {vendedor_anterior3}, '
    text += f' sua comissão é: {comissao_anterior3}'
    # print(text)
