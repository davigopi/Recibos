# from numpy import append
import pandas as pd
import locale
import os
# import numpy as np
from pathlib import Path
from fileManip import PDF
from fileManip import FileManip


class Generat_payroll:
    def __init__(self, *args, **kwargs) -> None:
        self.arqTableTeste = Path()

        self.profession = ''
        self.column_cargo = ''
        self.column_administradora = ''
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
        # self.column_situacao_d = ''
        self.data_ata_single = ''
        self.seller_single = ''
        self.data_date_pay = ''
        self.solumn_cadastro = ''
        self.word = ''

        self.quantity_line_full = 0
        self.quantity_line_ata = 0
        self.quantity_line_weekly = 0
        # quantity_line_table = 0
        self.sum_credito = 0
        self.number = 0

        self.list_situacao_to_comission = []
        self.list_recebera_to_comission = []
        self.list_condition_ata = []
        self.list_columns_end = []

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
        self.list_columns_full_ata_single = []
        self.table_single_ata = []
        self.list_single_administradora = []
        self.list_administradora_line = []
        self.list_administradora_line_sum = []
        self.list_administradora_sum_qtdcotasinicial = []
        self.list_administradora_sum_qtdcotasinicial_parc = []
        self.list_table_column_comissao = []
        self.list_table_column_define = []
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

    # converter em float as columns string

    # @property
    # def num_regras(self):
    #     return self.number

    # @num_regras.setter
    # def num_regras(self, text):
    #     for num in range(1, 100):
    #         column = str(num) + text
    #         if column not in self.table_full.columns:
    #             self.number = num - 1
    #             break

    @property
    def num_columns(self):
        return self.number

    @num_columns.setter
    def num_columns(self, text):
        for num in range(2, 100):
            column = text[0] + str(num) + text[1]
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

    # ira criar duas lista de todos os vendedores clt e parceiros
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

    # define se vendedor/parceiro a primeira é pela ata entrea/cadastro
    def columns_ata_full_seller_single(self):
        p1_referencia = (
            self.table_seller_single.iloc[1][self.column_1p_referencia]
        )
        if self.solumn_cadastro in p1_referencia:
            list = self.list_columns_full_ata_cadastro
        else:
            list = self.list_columns_full_ata_entrega
        self.list_columns_full_ata_single = list
        # print(self.list_columns_full_ata_single)

    # Criar uma lista tabelas aparti do dado ata e colunas definidas
    def tables_columns_ata_seller_single(self):
        for ata in self.list_columns_full_ata_single:
            table = self.table_seller_single[
                self.table_seller_single[ata] == self.data_ata_single
            ].copy()
            table.reset_index(drop=True, inplace=True)
            self.table_single_ata.append([table, ata])
        self.list_unique_information.append(self.data_ata_single)
        # for table, ata in self.table_single_ata:
        #     print(table)
        #     print('############ata#################')
        #     print(ata)
        #     print('===============================================')
        # print(self.list_unique_information)

    # ira mesclar todas as tabelas que tiver valor
    def tables_concat_seller_single(self):
        for table, ata in self.table_single_ata:
            if not table.empty:
                self.table_single_merge = pd.concat(
                    [self.table_single_merge, table]
                )
        # print(self.table_single_merge)

    # pegar informações de valores da administradoras
    def create_dictionary_datas(self):
        self.list_single_administradora = self.table_single_merge[
            self.column_administradora].unique()
        for administradora in self.list_single_administradora:
            for line in range(self.quantity_line_full):
                data_administradora = self.table_single_merge.iloc[
                    line][self.column_administradora]
                if data_administradora == administradora:
                    self.dic_administradoras[administradora] = {}
                    for qtd_cotas in self.list_qtd_cotas_parc:
                        # try:
                        data = self.table_single_merge.iloc[
                            line][qtd_cotas]
                        # except KeyError:
                        #     continue
                        if not pd.isna(data):
                            self.dic_administradoras[
                                administradora][qtd_cotas] = data
                    break

        # for key, dic in self.dic_administradoras.items():
        #     print(key)
        #     for key2, value in dic.items():
        #         print(f'{key2} => {value}')
        # print(self.list_single_administradora)

    def table_list_administradora_add_line(self):
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
        # for table, ata, list_admnimistradora_line in self.list_administradora_line:
        #     print('###############################')
        #     print(table)
        #     print(f'ata -> {ata}')
        #     print(list_admnimistradora_line)
        #     print('')

    def table_list_administradora_line_add_sum(self):
        for (
            table,
            ata,
            list_admnimistradora_line
        ) in self.list_administradora_line:
            quantity_line_table = table.shape[0]
            sums = 0
            for line in range(quantity_line_table):
                value = table.iloc[line][self.column_credito]
                value = str(value)
                value = value.replace('.', '')
                value = value.replace(',', '.')
                value = float(value)
                sums += value
            self.list_administradora_line_sum.append([
                table,
                ata,
                sums,
                list_admnimistradora_line,
            ])
            # self.sum_credito = table[self.column_credito].sum() #nao funciona
        # for table, ata, sums, list_admnimistradora_line in self.list_administradora_line_sum:
        #     print('######################')
        #     print(table)
        #     print(ata)
        #     print(sums)
        #     print(list_admnimistradora_line)

    def table_list_administradora_sum_add_qtdcotasinicial(self):
        for (
            table,
            ata,
            sums,
            list_admnimistradora_line
        ) in self.list_administradora_line_sum:
            list_administradora_qtdcotas = []
            for administradora_line in list_admnimistradora_line:
                data_administradora = administradora_line[0]
                line = administradora_line[1]
                for column_qtd_cota_inicial in reversed(
                        self.list_qtd_cotas_inicial):
                    try:
                        value = table.iloc[line][column_qtd_cota_inicial]
                        value = str(value)
                        value = value.replace('.', '')
                        value = value.replace(',', '.')
                        value = float(value)
                    except KeyError:
                        # print(column_qtd_cota_inicial)
                        continue
                    if sums >= value:
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
                list_administradora_qtdcotas
            ])
        # for table, ata, sums, list_admnimistradora_line in self.list_administradora_sum_qtdcotasinicial:
        #     print('################################')
        #     print(table)
        #     print(ata)
        #     print(sums)
        #     print(list_admnimistradora_line)

    def table_list_administradora_sum_add_full(self):
        for (
            table,
            ata,
            sum_credito,
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
                # print(list_column_parc)
                for key2, column_parc in enumerate(list_column_parc):
                    if key2 == 0:  # tira a primeira coluna qtdcotafinal
                        continue
                    # if '_Gerente' in column_parc:
                    #     # new_column_parc = column_parc
                    #     new_column_parc = column_parc.replace('_Gerente', '')
                    #     if number_ata in new_column_parc[-2:]:
                    #         break
                    # else:
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
            # print(f'ATA {ata}    administradoras: {list_administradora_qtdcotas_parc}')
            self.list_administradora_sum_qtdcotasinicial_parc.append([
                table,
                ata,
                sum_credito,
                list_administradora_qtdcotas_parc
            ])

    def add_column_comissao(self):
        sum_all_comissao = 0
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        for (
            table,
            ata,
            sum_credito,
            list_administradora_qtdcotas_parc
        ) in self.list_administradora_sum_qtdcotasinicial_parc:
            vendedor = table.iloc[0][self.profession]
            cargo = table.iloc[0][self.column_cargo]
            quantity_line_table = table.shape[0]
            sum_comissao = 0
            column_situacao_parc = self.column_situacao
            # ira pegar a coluna especifica da situação
            if (self.list_condition_ata[0] not in ata and
                    self.list_condition_ata[1] not in ata):
                text = ata.replace('ATA', '')
                column_situacao_parc += text
                # print(f' ATA => {ata}')
                # print(column_situacao_parc)
                # print(list_administradora_qtdcotas_parc)
            if list_administradora_qtdcotas_parc != []:
                for (
                    administradora_qtdcotas_parc
                ) in list_administradora_qtdcotas_parc:
                    administradora = administradora_qtdcotas_parc[0]
                    data_parc = administradora_qtdcotas_parc[6]
                    for line in range(quantity_line_table):
                        cliente = table.iloc[line]['Cliente']
                        if cliente == 'WILLIAN DE PAIVA DE SOUSA':
                            pass
                        data_situacao = table.iloc[line][column_situacao_parc]
                        calculate_commission = True
                        comissao = 0
                        list = self.list_situacao_to_comission
                        entrega = self.list_condition_ata[0]
                        cad_adm = self.list_condition_ata[1]
                        parc = self.list_condition_ata[2]
                        fat = self.list_condition_ata[3]
                        if (entrega in ata or cad_adm in ata):
                            ata_start = True
                        else:
                            ata_start = False
                        if data_situacao not in list and ata_start is False:
                            calculate_commission = False
                        elif entrega in ata:
                            data_1P_recebera = (
                                table.iloc[line][self.column_1P_recebera])
                            list = self.list_recebera_to_comission
                            if data_1P_recebera not in list:
                                calculate_commission = False
                        elif cad_adm in ata:
                            data_1P_recebera = (
                                table.iloc[line][self.column_1P_recebera])
                            list = self.list_recebera_to_comission
                            if data_1P_recebera not in list:
                                calculate_commission = False
                        elif parc in ata:
                            data_D_recebera = (
                                table.iloc[line][self.column_D_recebera])
                            list = self.list_recebera_to_comission
                            if data_D_recebera not in list:
                                calculate_commission = False
                        elif fat in ata:
                            data_FAT_recebera = (
                                table.iloc[line][self.column_FAT_recebera])
                            list = self.list_recebera_to_comission
                            if data_FAT_recebera not in list:
                                calculate_commission = False
                        else:
                            text = f'A condição da ata: {ata} não prevista'
                            print(text)
                            FileManip().writeLog = text
                        if calculate_commission:
                            data_admin = table.iloc[
                                line][self.column_administradora]
                            if administradora == data_admin:
                                value = table.iloc[line][self.column_credito]
                                value = str(value)
                                value = value.replace('.', '')
                                value = value.replace(',', '.')
                                value = float(value)
                                data_parc = float(data_parc)
                                comissao = value * data_parc / 100
                                sum_comissao += comissao
                        data_admin = table.iloc[line][self.column_administradora]
                        # print(f'{administradora} == {data_admin}')
                        if administradora == data_admin:
                            comissao = locale.format_string(
                                "%.2f", comissao, grouping=True)
                            table.loc[line, 'column_temp'] = comissao
                table.insert(0, self.column_comissao, table['column_temp'])
                del table['column_temp']
                sum_all_comissao += sum_comissao
                self.list_table_column_comissao.append([
                    table,
                    ata,
                    sum_credito,
                    sum_comissao,
                    vendedor,
                    cargo,
                    list_administradora_qtdcotas_parc
                ])
        self.list_unique_information.append(sum_all_comissao)
        # for table, ata, sum_credito, sum_comissao, vendedor, cargo, list_administradora_qtdcotas_parc in self.list_table_column_comissao:
        #     text = '################################### \n'
        #     text += f' {table} \n \n ATA: {ata}      '
        #     text += f'soma do credito {sum_credito}     '
        #     text += f' soma do comissao  {sum_comissao} \n '
        #     text += f'Vendedor: {vendedor}       cargo:{cargo} \n'
        #     text += f'Lista: {list_administradora_qtdcotas_parc}'
        #     print(text)

    def table_columns_end(self):
        for (
            table,
            ata,
            sum_credito,
            sum_comissao,
            vendedor,
            cargo,
            list_administradora_qtdcotas_parc
        ) in self.list_table_column_comissao:
            # text = ata.replace('ATA', '')
            # if 'Entrega' in text:
            #     column_date = 'Data de' + text
            #     column_situacao = 'Situação'
            # else:
            #     column_date = 'Data Pag.' + text
            #     column_situacao = 'Situação' + text
            list_columns_end_ATA = self.list_columns_end
            # list_columns_end_ATA.append(column_date)
            # list_columns_end_ATA.insert(1, column_situacao)
            new_table = table[list_columns_end_ATA]
            # list_columns_end_ATA.pop()
            # del list_columns_end_ATA[1]
            self.list_table_column_define.append([
                new_table,
                ata,
                sum_credito,
                sum_comissao,
                vendedor,
                cargo,
                list_administradora_qtdcotas_parc
            ])

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
        for (
            table,
            ata,
            sum_credito,
            sum_comissao,
            vendedor,
            cargo,
            list_administradora_qtdcotas_parc
        ) in self.list_table_column_define:
            if begin is True:
                pdf.set_font('Arial', '', size_font)
                sum_all_comissao = locale.currency(
                    sum_all_comissao,  # type: ignore
                    grouping=True
                )
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
                # pdf.multi_cell(0, size_line, text)
                text = f'{cargo}'
                text2 = f'Total a receber:  R$ {sum_all_comissao}'
                # pdf.multi_cell(0, size_line, text)
                # text += f'na ATA de {ata2}, '
                # Adiciona text2 e text3 em colunas
                pdf.add_content_in_columns(
                    [text, text2],
                    2,
                    size_font,
                    size_line
                )
                # text += f'e sua comissão foi de .'
                # pdf.multi_cell(0, size_line, text)
                pdf.ln(space_paragraph * 2)
                begin = False

            # Adiciona texto ao PDF
            pdf.set_font('Arial', '', size_font2)
            sum_comissao = locale.currency(sum_comissao, grouping=True)
            sum_credito = locale.currency(sum_credito, grouping=True)
            # text = ''
            # text += f'            A comissão de R$ {sum_comissao} '
            # text += f'referente a  {ata} foi calculada sobre um '
            # text += f'total de vendas de R$ {sum_credito}. '
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
                # text += f'Na administradora {administradora}, a escala '
                # text += 'da comissão para o total de vendas inicia em '
                # text += f'R$ {data_qtd_cotas_inicial} '
                # text += f'e termina em R$ {data_qtd_cotas_final}, '
                # text += f'com um percentual de comissão de {data_parc} %. '
            if commission:
                # pdf.multi_cell(0, size_line, text)
                # pdf.ln(space_paragraph)
                pdf.add_table(table)
                pdf.ln(space_paragraph)
                pdf.multi_cell(0, size_line, '')
                list_ata_sum_comissao_credito.append(
                    [ata, sum_comissao, sum_credito]
                )

        text = ''
        text2 = ''
        list_ata = []
        list_sum_comissao = []
        list_sum_credito = []
        for ata, sum_comissao, sum_credito in list_ata_sum_comissao_credito:
            list_ata.append(ata)
            list_sum_comissao.append(sum_comissao)
            list_sum_credito.append(sum_credito)
            # text += f'{ata}: R$ {sum_comissao}              '
            # text2 += f'{ata}: R$ {sum_credito}     '
            # print(ata, sum_comissao, sum_credito)
        # text3 = 'TOTAL COMISSAO POR PARCELA'
        # pdf.add_underlined_text(text3, size_font, size_line)
        # pdf.multi_cell(0, size_line, text)
        # text4 = 'TOTAL CRÉDITO'
        # pdf.add_underlined_text(text4, size_font, size_line)
        # pdf.multi_cell(0, size_line, text2)
        data = {
            ' ': list_ata,
            'TOTAL CRÉDITO': list_sum_credito,
            'TOTAL COMISSÃO POR PARCELA': list_sum_comissao
        }
        df = pd.DataFrame(data)
        pdf.add_table(df)
        pdf.ln(space_paragraph)
        text = f'TOTAL COMISSÃO: R$ {sum_all_comissao}'
        pdf.add_text_to_end_of_line(text, size_font, size_line)
        pdf.ln(space_paragraph)
        pdf.ln(space_paragraph)
        pdf.ln(space_paragraph)
        pdf.ln(space_paragraph)
        text = ' '
        pdf.add_underlined_text(text, size_font, size_line)
        text = '                      ASSINATURA'
        text2 = 'FORTALEZA, ____/____/____ '
        pdf.add_content_in_columns([text, text2], 2, size_font, size_line)

        # print(text, text2)
        # print(ata2, sum_all_comissao)
        # Salva o PDF
        folder_documnts = os.path.expanduser("~/Documents")
        new_folder = os.path.join(folder_documnts, "RECIBO")
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        name_file = f'Recibo de pagamento {vendedor}.pdf'
        path_file = os.path.join(new_folder, name_file)
        pdf.output(path_file)

    def prints(self):
        # print(self.list_seller_weekly)
        # print(self.list_weekly)
        # print(self.list_columns_full_ata_single)
        # print(self.table_single_ata)
        # print(self.table_single_merge)
        # print(self.list_single_administradora)
        # dic_administradoras_json = json.dumps(
        #     self.dic_administradoras, indent=4)
        # print(dic_administradoras_json)

        begin = True
        for (
            table,
            ata,
            sum_credito,
            sum_comissao,
            vendedor,
            cargo,
            list_administradora_qtdcotas_parc
        ) in self.list_table_column_define:
            if begin is True:
                ata2 = self.list_unique_information[0]
                sum_all_comissao = self.list_unique_information[1]
                sum_all_comissao = locale.currency(
                    sum_all_comissao,
                    grouping=True
                )
                text = ''
                text += f'            O/A Funcionário/a {vendedor}, '
                text += f'na ATA de {ata2}, '
                text += f'ocupa o cargo de {cargo}, '
                text += f'e sua comissão foi de R$ {sum_all_comissao}.'
                print(text)
                begin = False
            sum_comissao = locale.currency(sum_comissao, grouping=True)
            sum_credito = locale.currency(sum_credito, grouping=True)
            text = ''
            text += f'            A comissão de R$ {sum_comissao} '
            text += f'referente a  {ata} foi calculada sobre um '
            text += f'total de vendas de R$ {sum_credito}. '
            commission = False
            for (
                administradora_qtdcotas_parc
            ) in list_administradora_qtdcotas_parc:
                administradora = administradora_qtdcotas_parc[0]
                # column_qtd_cotas_inicial = administradora_qtdcotas_parc[1]
                data_qtd_cotas_inicial = administradora_qtdcotas_parc[2]
                # column_qtd_cotas_final = administradora_qtdcotas_parc[3]
                data_qtd_cotas_final = administradora_qtdcotas_parc[4]
                # column_parc = administradora_qtdcotas_parc[5]
                data_parc = administradora_qtdcotas_parc[6]
                if data_parc != 0:
                    commission = True
                    print(data_parc, type(data_parc))
                data_qtd_cotas_inicial = locale.currency(
                    data_qtd_cotas_inicial, grouping=True)
                data_qtd_cotas_final = locale.currency(
                    data_qtd_cotas_final, grouping=True)
                text += f'Na administradora {administradora}, a escala '
                text += 'da comissão para o total de vendas inicia em '
                text += f'R$ {data_qtd_cotas_inicial} '
                text += f'e termina em R$ {data_qtd_cotas_final}, '
                text += f'com um percentual de comissão de {data_parc} %. '
            if commission:
                print(text)
                print(table)
                print('')


if __name__ == '__main__':
    data_ata_single = 'MAIO/2024'
    is_manager = False
    # is_manager = True
    # seller_single = 'MARIA ILLYEDJA RODRIGUES DE SOUZA '
    # seller_single = 'BRUNA ALINE DE AZEVEDO (ENIO)'
    # seller_single = 'DENISE VITOR COSTA'
    # from generat_payroll import Generat_payroll
    generat_payroll = Generat_payroll()

    pathTables = Path(__file__).parent.parent / 'tables'
    name_arq = 'table_teste.csv'
    arqTableTeste = pathTables / name_arq

    table_full = pd.read_csv(
        "tables\\tableMerge.csv",
        sep=';',
        encoding='utf-8',
        dtype=str
    )

    column_vendedor = 'Vendedor'
    column_gerente = 'Gerente'
    column_cargo = 'Cargo'
    column_administradora = 'Administradora'
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
    column_cliente = 'Cliente'
    column_n_contrato = 'Nº Contrato'
    column_grupo = 'Grupo'
    column_cota = 'Cota'
    column_data_entrega = 'Data de Entrega'
    column_cad_adm = 'Data Cad. Adm'
    # column_situacao_d = 'º Parc'

    data_date_pay = 'DIA DA SEMANA'
    solumn_cadastro = 'CADASTRO'

    list_situacao_to_comission = ['NORMAL', 'PAGA']
    list_recebera_to_comission = ['SIM']
    list_condition_ata = ['Entrega', 'Cad Adm', 'Parc', 'FAT']

    # Definir o número de grupos e de parcelas

    # list_qtd_cotas_inicial = [
    #     '1 Qtd. Cotas Inicial', '2 Qtd. Cotas Inicial', '3 Qtd. Cotas Inicial',
    #     '4 Qtd. Cotas Inicial', '5 Qtd. Cotas Inicial',
    # ]
    # list_qtd_cotas_final = [
    #     '1 Qtd. Cotas Final', '2 Qtd. Cotas Final', '3 Qtd. Cotas Final',
    #     '4 Qtd. Cotas Final', '5 Qtd. Cotas Final',
    # ]

    # list_columns_full_ata = [
    #     'ATA Entrega', 'ATA Cad Adm', 'ATA 2º Parc', 'ATA 3º Parc',
    #     'ATA 4º Parc', 'ATA 5º Parc', 'ATA 6º Parc'
    # ]
    # list_columns_full_weekly = [
    #     'Sma Ent', 'Sma Cad Adm', 'Sma 2º Parc', 'Sma 3º Parc',
    #     'Sma 4º Parc', 'Sma 5º Parc', 'Sma 6º Parc'
    # ]
    # if is_manager:
    #     profession = column_gerente
    #     # list_full = [list_qtd_cotas_inicial, list_qtd_cotas_final]
    #     # for list_column in list_full:
    #     #     list = []
    #     #     for i in range(len(list_column)):
    #     #         list_column[i] = list_column[i] + '_Gerente'
    #     #     list_column = list
    #     # print(list_qtd_cotas_inicial)
    #     # print(list_qtd_cotas_final)
    # else:
    #     profession = column_vendedor
    generat_payroll.table_full = table_full

    generat_payroll.num_columns = ['ATA ', 'º Parc']
    num_atas_parc = generat_payroll.number
    generat_payroll.num_columns = ['', ' Qtd. Cotas Inicial']
    num_regras = generat_payroll.number
    generat_payroll.num_columns = [str(num_regras) + ' Parc ', '']
    num_parcelas = generat_payroll.number
    if is_manager:
        profession = column_gerente
        word = '_Gerente'
    else:
        profession = column_vendedor
        word = ''
    generat_payroll.word = word
    list_columns_full_ata = ['ATA Entrega', 'ATA Cad Adm']
    list_columns_full_weekly = ['Sma Ent', 'Sma Cad Adm']
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
        item for item in list_columns_full_ata if item != column_ata_cad_Adm]
    list_columns_full_ata_cadastro = [
        item for item in list_columns_full_ata if item != column_ata_entrega]

    list_columns_end = [
        column_data_entrega,
        column_cad_adm,
        column_n_contrato,
        column_grupo,
        column_cota,
        column_administradora,
        column_cliente,
        column_credito,
        column_comissao
    ]

    name_columns_full = table_full.columns.tolist()

    list_seller_single_all = []
    for column in list_columns_full_ata:
        table_full_ata_def = table_full.loc[table_full[column] == data_ata_single]
        list_unique = table_full_ata_def[column_vendedor].unique()
        if len(list_unique) > 0:
            list_seller_single_all.extend(list_unique)

    list_seller_single = []
    for seller in list_seller_single_all:
        if seller not in list_seller_single:
            list_seller_single.append(seller)
    list_seller_single.sort()

    for seller_single in list_seller_single:

        table_full_ata = table_full[table_full[column_dt_pag_por] != data_date_pay]
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
        generat_payroll.arqTableTeste = arqTableTeste

        generat_payroll.column_credito = column_credito
        generat_payroll.column_administradora = column_administradora
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
        generat_payroll.list_columns_end = list_columns_end
        # generat_payroll.column_situacao_d = column_situacao_d

        generat_payroll.data_date_pay = data_date_pay
        generat_payroll.solumn_cadastro = solumn_cadastro

        generat_payroll.list_situacao_to_comission = list_situacao_to_comission
        generat_payroll.list_recebera_to_comission = list_recebera_to_comission
        generat_payroll.list_condition_ata = list_condition_ata

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
        list_columns_str_to_float = (list_qtd_cotas_inicial + list_qtd_cotas_final)
        list_columns_str_to_float.append(column_credito)
        generat_payroll.list_columns_str_to_float = list_columns_str_to_float
        generat_payroll.convert_str_float = table_full

        print(seller_single)

        # generat_payroll.table_full = generat_payroll.convert_str_float
        generat_payroll.columns_to_list_full_seller()
        generat_payroll.columns_ata_full_seller_single()
        generat_payroll.tables_columns_ata_seller_single()
        generat_payroll.tables_concat_seller_single()
        generat_payroll.create_dictionary_datas()
        generat_payroll.table_list_administradora_add_line()
        generat_payroll.table_list_administradora_line_add_sum()
        generat_payroll.table_list_administradora_sum_add_qtdcotasinicial()
        generat_payroll.table_list_administradora_sum_add_full()
        generat_payroll.add_column_comissao()
        generat_payroll.table_columns_end()
        generat_payroll.table_convert_pdf()
        # generat_payroll.prints()
