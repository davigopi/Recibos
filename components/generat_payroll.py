# flake8: noqa
# pyright: # type: ignore

import pandas as pd
import locale
import os
import sys
from pathlib import Path
# from components import renomear
from components.renomear import Renomear
from components.fileManip import PDF
from components.variables import *

try:
    from path_file import Path_file
except ImportError:
    parent_dir = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(parent_dir))
    try:
        from path_file import Path_file
    except ImportError:
        raise ImportError("Não foi possível importar 'Path_fiel'")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # type: ignore[attr-defined]
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def create_table(table_created, path):
    table_created.columns = (table_created.columns.str.strip())
    table_created.to_csv(path, sep=';', index=False, header=True)
    return table_created


# entrada texto da ATA saida apenas o número ATA
def rename_ata(text, model):
    text = text.replace(word_ATA_, '')
    text = text.replace(word_Sma_, '')
    text = text.replace(word_Parc, '')
    text = text.replace(word_Pag_, '')
    text = text.replace(word_Venc_, '')
    if model == 'mod1':
        text = text.replace('º', '')
        text = text.replace(word_Entrega, '1')
        text = text.replace(word_Cad_Adm, '1')
    elif model == 'mod2':
        text = text.replace('º', 'ª')
        text = text.replace(word_Entrega, '1ª')
        text = text.replace(word_Cad_Adm, '1ª')
    text = text.replace(' ', '')
    return text


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


class Generat_payroll:
    def __init__(self, *args, **kwargs) -> None:
        self.path_file = Path_file()
        self.renomear = Renomear()
        self.father = kwargs.get('father')

        self.model = model

        self.word_profissao = word_profissao
        self.column_profissao = column_profissao
        self.column_Cargo = column_Cargo
        self.column_Data_Pag_Por = column_Data_Pag_Por
        self.column_1_Parcela_Referencia = column_1_Parcela_Referencia
        self.column_1_Parcela_Recebera = column_1_Parcela_Recebera
        self.column_Demais_Recebera = column_Demais_Recebera
        self.column_FAT_Recebera = column_FAT_Recebera
        self.column_Credito = column_Credito
        self.column_Situacao = column_Situacao
        self.column_ATA_Entrega = column_ATA_Entrega
        self.column_ATA_Cad_Adm = column_ATA_Cad_Adm
        self.column_Sma_Entrega = column_Sma_Entrega
        self.column_Sma_Cad_Adm = column_Sma_Cad_Adm
        self.column_ata_sma = ''
        self.date_ata_single = ''
        self.date_sma_single = ''
        self.seller_single = seller_single
        self.word_DIA_DA_SEMANA = word_DIA_DA_SEMANA
        self.word_CADASTRO = word_CADASTRO
        # self.word = ''
        self.list_columns_Total = ''

        self.date_atasma_single = date_atasma_single

        self.word_Supervisor = word_Supervisor
        self.word_Gerencia = word_Gerencia

        # self.quantity_line_full = 0
        # self.quantity_line_ata = 0
        # self.quantity_line_weekly = 0
        self.number_in_column = number_in_column

        self.list_cargo_not_calc_commis = list_cargo_not_calc_commis
        self.list_columns_end = list_columns_end

        self.sum_comissao = sum_comissao
        self.sum_comissao_compliance = sum_comissao_compliance
        self.sum_all_comissao = sum_all_comissao
        self.sum_all_comissao_gerente = sum_all_comissao_gerente
        self.sum_compliance = sum_compliance

        self.adimplencias = adimplencias
        self.list_line_delete = list_line_delete

        self.list_columns_Escala_ATAMes_EntregaCad_Adm = []

        self.list_columns_ATA_EntregaPag_n_Parc = list_columns_ATA_EntregaPag_n_Parc
        self.list_columns_ATA_Cad_AdmPag_n_Parc = list_columns_ATA_Cad_AdmPag_n_Parc
        self.list_columns_Sma_EntregaPag_n_Parc = list_columns_Sma_EntregaPag_n_Parc
        self.list_columns_Sma_Cad_AdmPag_n_Parc = list_columns_Sma_Cad_AdmPag_n_Parc
        self.list_columns_ATA_EntregaVenc_n_Parc = list_columns_ATA_EntregaVenc_n_Parc
        self.list_columns_ATA_Cad_AdmVenc_n_Parc = list_columns_ATA_Cad_AdmVenc_n_Parc
        self.list_columns_Sma_EntregaVenc_n_Parc = list_columns_Sma_EntregaVenc_n_Parc
        self.list_columns_Sma_Cad_AdmVenc_n_Parc = list_columns_Sma_Cad_AdmVenc_n_Parc
        self.list_columns_ATASma_Pag_n_Parc = list_columns_ATASma_Pag_n_Parc
        self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = list_columns_ATASma_EntregaCad_AdmVenc_n_Parc
        self.list_columns_Situacao_n_ATA = list_columns_Situacao_n_ATA
        self.list_columns_Pag_Comissao_n_Parc = list_columns_Pag_Comissao_n_Parc

        self.list_ata = []

        self.list_tables_ata = []
        self.list_tables_ata_sums = []

        self.list_table_edit = []
        self.list_unique_information = list_unique_information

        self.table: pd.DataFrame = pd.DataFrame()
        self.table_full: pd.DataFrame = pd.DataFrame()
        self.table_all: pd.DataFrame = pd.DataFrame()
        self.table_single_merge: pd.DataFrame = pd.DataFrame()
        self.table_seller_single: pd.DataFrame = pd.DataFrame()

        self.cargo = ''

    @property
    def find_number_in_column(self):
        return None

    # recebe uma lista de texto para formar uma palavra que proc nas colunas
    @find_number_in_column.setter
    def find_number_in_column(self, list_text):
        for num in range(2, 100):
            column = list_text[0] + str(num) + list_text[1]
            if column not in self.table_full.columns:
                self.number_in_column = num - 1
                break

    def convert_str_float(self, value):
        value = str(value)
        value = value.replace('.', '')
        value = value.replace(',', '.')
        value = float(value)
        value = round(value, 2)
        return value

    # Mesclar todas as tabelas que tiver valor
    def tables_concat_seller_single(self):
        self.table_single_merge = pd.DataFrame()
        for table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc, column_Situacao_n_ATA in self.list_tables_ata:
            if not table_venc.empty:
                self.table_single_merge = pd.concat([self.table_single_merge, table_venc])  # noqa

    def print_list_list(self, list_list):
        for i1, list in enumerate(list_list):
            for i2, var in enumerate(list):
                print(f'arq: {i1}    arq2: {i2}')
                print(var)
                print('#############################')

    # 1º criar lista de variaveis
    def generate_columns_for_all(self):
        # as colunas da tabela ficara no arqvuio pdf
        self.table_full = pd.read_csv(arqTableMergeOrder, sep=';', encoding='utf-8', dtype=str)
        self.find_number_in_column = list_words_ATA_Venc_º_Parc
        # Preencher o restante das colunas sequenciais
        for i in range(2, self.number_in_column + 1):
            n_Parc = str(i) + word_º_Parc
            self.list_columns_Sma_Cad_AdmPag_n_Parc.append(word_Sma_ + word_Pag_ + n_Parc)  # noqa
            self.list_columns_Sma_Cad_AdmVenc_n_Parc.append(word_Sma_ + word_Venc_ + n_Parc)  # noqa

            self.list_columns_ATA_Cad_AdmPag_n_Parc.append(word_ATA_ + word_Pag_ + n_Parc)  # noqa
            self.list_columns_ATA_Cad_AdmVenc_n_Parc.append(word_ATA_ + word_Venc_ + n_Parc)  # noqa

            self.list_columns_Sma_EntregaPag_n_Parc.append(word_Sma_ + word_Pag_ + n_Parc)  # noqa
            self.list_columns_Sma_EntregaVenc_n_Parc.append(word_Sma_ + word_Venc_ + n_Parc)  # noqa

            self.list_columns_ATA_EntregaPag_n_Parc.append(word_ATA_ + word_Pag_ + n_Parc)  # noqa
            self.list_columns_ATA_EntregaVenc_n_Parc.append(word_ATA_ + word_Venc_ + n_Parc)  # noqa

            self.list_columns_Situacao_n_ATA.append(word_Situacao_ + n_Parc)

            self.list_columns_Pag_Comissao_n_Parc.append(word_Pag_Comissao_ + n_Parc)

    def set_value_cargo(self):
        if self.word_profissao == word_Gerencia:
            column_Cargo_professional = column_Cargo_Gerencia
        elif self.word_profissao == word_Supervisor:
            column_Cargo_professional = column_Cargo_Supervisor
        else:
            column_Cargo_professional = column_Cargo
        self.cargo = self.table_seller_single.iloc[0][column_Cargo_professional]

    def set_value_date_atasma_single(self):
        # 1ª inf da coluna 'Dt pag. por' -> ATA ou DIA DA SEMANA
        data_pag_por = str(self.table_seller_single.iloc[0][self.column_Data_Pag_Por])
        #   'DIA DA SEMANA'
        if self.word_DIA_DA_SEMANA == data_pag_por:
            # irar retornar False os venderes diferente de parceiros
            if self.word_profissao != word_Parceiro:
                return True
            #                  Xº/MES/ANO
            self.date_atasma_single = self.date_sma_single
        else:
            # irar retornar False os venderes iguais aos parceiros
            if self.word_profissao == word_Parceiro:
                return True
            #                  MES/ANO
            self.date_atasma_single = self.date_ata_single
        return False

    def set_list_columns(self):
        # 1ª inf da coluna '1P referencia' -> ENTREGA ou CADASRO
        p1_referencia = str(self.table_seller_single.iloc[0][self.column_1_Parcela_Referencia])
        # 1ª inf da coluna 'Dt pag. por' -> ATA ou DIA DA SEMANA
        data_pag_por = str(self.table_seller_single.iloc[0][self.column_Data_Pag_Por])
        if self.word_CADASTRO in p1_referencia and self.word_DIA_DA_SEMANA == data_pag_por:
            self.column_ata_sma = self.column_Sma_Cad_Adm
            #            '[Sma Cad Adm', 'Sma 2º Parc', ..., 'Sma 6º Parc']
            self.list_columns_ATASma_Pag_n_Parc = self.list_columns_Sma_Cad_AdmPag_n_Parc
            self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_Sma_Cad_AdmVenc_n_Parc
            list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_Mes_Cad_Adm
            # list_columns_Total = list_columns_Total_Sma_Cad_Adm
        elif self.word_CADASTRO in p1_referencia and self.word_DIA_DA_SEMANA != data_pag_por:
            self.column_ata_sma = self.column_ATA_Cad_Adm
            # ['ATA Cad Adm', 'ATA 2º Parc', 'ATA 3º P ..., 'ATA 6º Parc']
            self.list_columns_ATASma_Pag_n_Parc = self.list_columns_ATA_Cad_AdmPag_n_Parc
            self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_ATA_Cad_AdmVenc_n_Parc
            list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATA_Cad_Adm
            # list_columns_Total = list_columns_Total_ATA_Cad_Adm
        elif self.word_CADASTRO not in p1_referencia and self.word_DIA_DA_SEMANA == data_pag_por:
            self.column_ata_sma = self.column_Sma_Entrega
            # '[Sma Ent', 'Sma 2º Parc', ..., 'Sma 6º Parc']
            self.list_columns_ATASma_Pag_n_Parc = self.list_columns_Sma_EntregaPag_n_Parc
            self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_Sma_EntregaVenc_n_Parc
            list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_Mes_Entrega
            # list_columns_Total = list_columns_Total_Sma_Entrega
        elif self.word_CADASTRO not in p1_referencia and self.word_DIA_DA_SEMANA != data_pag_por:
            self.column_ata_sma = self.column_ATA_Entrega
            # ['ATA Entrega', 'ATA 2º Parc', ..., 'ATA 6º Parc']
            self.list_columns_ATASma_Pag_n_Parc = self.list_columns_ATA_EntregaPag_n_Parc
            self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_ATA_EntregaVenc_n_Parc
            list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATA_Entrega
            # list_columns_Total = list_columns_Total_ATA_Entrega
        if self.word_profissao == word_Gerencia:
            # ATA XX qtd cotas Ger Ger
            self.list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATAMes_EntregaCad_Adm[2]  # noqa
            # 'Total XX Ger Ger'
            # self.list_columns_Total = list_columns_Total[2]
        elif self.word_profissao == word_Supervisor:
            # ATA XX qtd cotas Ger
            self.list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATAMes_EntregaCad_Adm[1]  # noqa
            # 'Total XX Ger'
            # self.list_columns_Total = list_columns_Total[1]
        else:
            # ATA XX qtd cotas
            self.list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATAMes_EntregaCad_Adm[0]  # noqa
            # 'Total XX'
            # self.list_columns_Total = list_columns_Total[0]

    # 2º define se vendedor/parceiro a primeira é pela ATA entrea/cadastro
    def columns_ata_full_seller_single(self):
        self.table_full_copy = self.table_full.copy()
        self.table_seller_single = self.table_full_copy[self.table_full_copy[self.column_profissao] == self.seller_single]  # noqa

        sair = self.set_value_date_atasma_single()
        if sair:
            return True
        self.set_value_cargo()
        self.set_list_columns()

        return False

    # 3º Criar uma lista tabelas aparti do dado ATA ou SMA
    def tables_columns_ata_seller_single(self):
        self.list_tables_ata = []
        # ['ATA Entrega', 'ATA 2º Parc', ..., 'ATA 6º Parc']
        # for key, column_ATASma_EntregaCad_AdmVenc_n_Parc in enumerate(self.list_columns_ATASma_Pag_n_Parc):
        # # MES/ANO ou Xº/MES/ANO
        # table_pag = self.table_seller_single[self.table_seller_single[column_ATASma_EntregaCad_AdmVenc_n_Parc] == self.date_atasma_single].copy()  # noqa
        # # valores_unicos = table_temp[column_PK_Vend_ATA_Entrega].unique()
        # # table_pag = self.table_seller_single[self.table_seller_single[column_PK_Vend_ATA_Entrega].isin(valores_unicos)].copy()  # noqa
        # table_pag.reset_index(drop=True, inplace=True)

        # #                ATA Entrega, Sma Ent, ATA cad Adm, Sma Cad Adm
        # if column_ATASma_EntregaCad_AdmVenc_n_Parc == self.column_ata_sma:
        #     column_ata_venc = column_ATASma_EntregaCad_AdmVenc_n_Parc
        # else:
        #     column_ata_venc = column_ATASma_EntregaCad_AdmVenc_n_Parc + ' Venc'
        for key, column_ATASma_EntregaCad_AdmVenc_n_Parc in enumerate(self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc):  # noqa
            # column_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc[key]
            table_temp = self.table_seller_single[self.table_seller_single[column_ATASma_EntregaCad_AdmVenc_n_Parc] == self.date_atasma_single].copy()  # noqa
            valores_unicos = table_temp[column_PK_Vend_ATA_Entrega].unique()
            table_venc = self.table_seller_single[self.table_seller_single[column_PK_Vend_ATA_Entrega].isin(valores_unicos)].copy()  # noqa
            table_venc.reset_index(drop=True, inplace=True)
            column_Situacao_n_ATA = self.list_columns_Situacao_n_ATA[key]
            # table não é fazia?
            if not table_venc.empty:
                self.list_tables_ata.append([table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc, column_Situacao_n_ATA])  # noqa

        # self.print_list_list(self.list_tables_ata)

    # 4º situações para sair e ir para o próximo vendedor
    def is_to_stop_program(self):
        self.tables_concat_seller_single()
        # se junção de tabela estiver vazio sair
        if self.table_single_merge.empty:
            return True
        # se for o cargo: ['ESTAGIÁRIO', 'ZERADO'] sair
        for cargo_not_calc_commis in self.list_cargo_not_calc_commis:
            if cargo_not_calc_commis in self.cargo:
                return True
        return False

    # 5º Ira criar a soma de todos as vendas aparti da ATA especifica ira detarminar os 50%
    # def table_list_administradora_line_add_sum(self):
    #     # OBS: infelizmente o comando self.sums =  table[self.column_Credito].sum(), nao funciona
    #     self.list_tables_ata_sums = []
    #     for  table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc, column_Situacao_n_ATA in self.list_tables_ata:  # noqa
    #         sum_compliance = 0
    #         value = 0
    #         dividend = 'venc'  # pag
    #         sums_all = 0
    #         divisor = 'venc'  # pag
    #         if self.word_profissao == word_Parceiro:
    #             dividend = 'pag'
    #             divisor = 'pag'

    #         if divisor == 'venc':
    #             table_divisor = table_venc
    #         elif divisor == 'pag':
    #             table_divisor = table_pag
    #         if dividend == 'venc':
    #             table_dividend = table_venc
    #         elif dividend == 'pag':
    #             table_dividend = table_pag

    #         dict_divisor_PK_Vend_ATA_Entrega = {}
    #         dict_dividend_PK_Vend_ATA_Entrega = {}
    #         quantity_line_table = table_venc.shape[0]
    #         for line in range(quantity_line_table):
    #             value = table_venc.iloc[line][self.column_Credito]
    #             self.renomear.inf = value
    #             value = float(self.renomear.valor())
    #             PK_Vend_ATA_Entrega = table_venc.iloc[line][column_PK_Vend_ATA_Entrega]
    #             if PK_Vend_ATA_Entrega in dict_divisor_PK_Vend_ATA_Entrega:
    #                 dict_divisor_PK_Vend_ATA_Entrega[PK_Vend_ATA_Entrega] += value
    #             else:
    #                 dict_divisor_PK_Vend_ATA_Entrega[PK_Vend_ATA_Entrega] = value
    #             if column_Situacao_n_ATA == column_Situacao:
    #                 if PK_Vend_ATA_Entrega in dict_dividend_PK_Vend_ATA_Entrega:
    #                     dict_dividend_PK_Vend_ATA_Entrega[PK_Vend_ATA_Entrega] += value
    #                 else:
    #                     dict_dividend_PK_Vend_ATA_Entrega[PK_Vend_ATA_Entrega] = value
    #             else:
    #                 Situacao_n_ATA = table_venc.iloc[line][column_Situacao_n_ATA]
    #                 if Situacao_n_ATA in list_situacao_to_comission:
    #                     if PK_Vend_ATA_Entrega in dict_dividend_PK_Vend_ATA_Entrega:
    #                         dict_dividend_PK_Vend_ATA_Entrega[PK_Vend_ATA_Entrega] += value
    #                     else:
    #                         dict_dividend_PK_Vend_ATA_Entrega[PK_Vend_ATA_Entrega] = value

    #         # print(column_ATASma_EntregaCad_AdmVenc_n_Parc)
    #         # print(column_Situacao_n_ATA)
    #         # print(dict_divisor_PK_Vend_ATA_Entrega)
    #         # print(dict_dividend_PK_Vend_ATA_Entrega)
    #         # for key in dict_divisor_PK_Vend_ATA_Entrega:
    #         #     divisor = dict_divisor_PK_Vend_ATA_Entrega[key]
    #         #     dividend = dict_dividend_PK_Vend_ATA_Entrega[key]
    #         #     print(dividend / divisor)

    #         # value = self.convert_str_float(value)
    #         # sums_all += value

    #         # quantity_line_table = table_divisor.shape[0]
    #         # for line in range(quantity_line_table):
    #         #     value = table_divisor.iloc[line][self.column_Credito]
    #         #     value = self.convert_str_float(value)
    #         #     sums_all += value

    #         # quantity_line_table = table_pag.shape[0]
    #         # for line in range(quantity_line_table):
    #         #     value = table_pag.iloc[line][self.column_Credito]
    #         #     value = self.convert_str_float(value)
    #         #     sums_all += value

    #         # é primeira parcela? ATA ou Sma Entrega ou ATA ou Sma Cad Adm
    #         # if ata in self.column_ata_sma:
    #         #     sum_compliance = sums_all
    #         # elif dividend == 'venc':
    #         #     column = ata
    #         #     column = column.replace(word_ATA_, '').replace(word_Sma_, '')
    #         #     column = column.replace(word_Pag_, '').replace(word_Venc_, '')
    #         #     column_situacao = 'Situação ' + column
    #         #     quantity_line_table = table_dividend.shape[0]
    #         #     for line in range(quantity_line_table):
    #         #         situacao = table_dividend.iloc[line][column_situacao]
    #         #         #             'NORMAL', 'PAGA'
    #         #         if situacao in list_situacao_to_comission:
    #         #             value = table_dividend.iloc[line][self.column_Credito]
    #         #             value = self.convert_str_float(value)
    #         #             sum_compliance += value
    #         # elif dividend == 'pag':
    #         #     quantity_line_table = table_pag.shape[0]
    #         #     for line in range(quantity_line_table):
    #         #         value = table_pag.iloc[line][self.column_Credito]
    #         #         value = self.convert_str_float(value)
    #         #         sum_compliance += value
    #         sums_all = 1
    #         sum_compliance = 1
    #         self.list_tables_ata_sums.append([
    #
    #             table_venc,
    #             column_ATASma_EntregaCad_AdmVenc_n_Parc,
    #             sums_all,
    #             sum_compliance
    #         ])
    #     # self.print_list_list(self.list_tables_ata_sums)

    def find_and_create_percentual_escala(self, table_venc, num, column_ATASma_EntregaCad_AdmVenc_n_Parc):  # noqa
        table_venc[column_porc] = '0'
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            Escala = table_venc.iloc[line][self.list_columns_Escala_ATAMes_EntregaCad_Adm]  # noqa
            # se for igua a 0 não atigiu o minimo nao existe comissão
            minimum = True
            if Escala != '0':
                column_Escala_Parc_num = Escala + word__Parc_ + str(num)
                percentual = table_venc.iloc[line][column_Escala_Parc_num]
                if pd.isnull(percentual):
                    percentual = 0
            else:
                percentual = 0
                if column_ATASma_EntregaCad_AdmVenc_n_Parc == self.column_ata_sma:
                    minimum = False
            try:
                percentual = float(percentual)
            except ValueError:
                percentual = convert_str_float(percentual)
                percentual = float(percentual)
            text_perc = str(percentual) + word__porc
            table_venc.loc[line, column_porc] = text_perc
            if minimum:
                table_venc.loc[line, column_porc_Num] = percentual / 100
            else:
                table_venc.loc[line, column_porc_Num] = 0.0000001
        return table_venc

    def create_comissao_escala(self, table_venc, num, column_ATASma_EntregaCad_AdmVenc_n_Parc, column_Situacao_n_ATA):  # noqa
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            if word_Entrega in column_ATASma_EntregaCad_AdmVenc_n_Parc or word_Cad_Adm in column_ATASma_EntregaCad_AdmVenc_n_Parc:
                data_recebera = (table_venc.iloc[line][self.column_1_Parcela_Recebera])  # noqa
            elif word_Parc in column_ATASma_EntregaCad_AdmVenc_n_Parc:
                data_recebera = (table_venc.iloc[line][self.column_Demais_Recebera])  # noqa
            elif word_FAT in column_ATASma_EntregaCad_AdmVenc_n_Parc:
                data_recebera = (table_venc.iloc[line][self.column_FAT_Recebera])  # noqa

            data_situacao = table_venc.iloc[line][column_Situacao_n_ATA]

            if data_situacao not in list_situacao_to_comission:
                data_recebera = 'NAO'
                ''' Devido à possibilidade de os recibos serem emitidos em momentos futuros e o pagamento da coluna
                'Situação' não estar presente em list_situacao_to_comission, precisamos verificar se é word_Entrega
                para garantir que não seja gerado de forma diferente dos recibos emitidos no momento correto.'''
                if '1' in str(num):
                    data_recebera = (table_venc.iloc[line][self.column_1_Parcela_Recebera])  # noqa
            if data_recebera in list_recebera_to_comission:
                value = table_venc.iloc[line][self.column_Credito]
                value = self.convert_str_float(value)
                percentual = table_venc.loc[line, column_porc_Num]
                comissao = value * percentual
            else:
                comissao = 0
            comissao = locale.format_string("%.2f", comissao, grouping=True)
            table_venc.loc[line, column_Comissao] = comissao

            # table_venc.loc[line, column_ATA_Venc_pag] =

        return table_venc

    def create_comissao_50_porc(self, table_venc, num):
        column_porc_ATA_Pag_n_Parc = word_porc_ + word_ATA_ + word_Pag_ + num + 'º ' + word_Parc
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            if '1' in str(num):
                porc_ATA_Pag_n_Parc = 100
            else:
                self.renomear.inf = table_venc.iloc[line][column_porc_ATA_Pag_n_Parc]
                porc_ATA_Pag_n_Parc = float(self.renomear.valor())
            if porc_ATA_Pag_n_Parc >= 50:
                comissao = table_venc.iloc[line][column_Comissao]
                table_venc.loc[line, column_Comissao_50_porc] = comissao
            else:
                table_venc.loc[line, column_Comissao_50_porc] = 0
        return table_venc

    def set_sum_comissoes(self, table_venc):
        self.sum_comissao = 0
        self.sum_comissao_compliance = 0
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            self.renomear.inf = table_venc.iloc[line][column_Comissao]
            self.sum_comissao += float(self.renomear.valor())
            self.renomear.inf = table_venc.iloc[line][column_Comissao_50_porc]
            self.sum_comissao_compliance += float(self.renomear.valor())
            self.renomear.inf = table_venc.iloc[line][column_Credito]
            self.sum_compliance += float(self.renomear.valor())
        self.sum_all_comissao += self.sum_comissao
        self.sum_all_comissao_gerente += self.sum_comissao

    def find_num_column_ATASma_Pag_n_Parc(self, column_ATASma_EntregaCad_AdmVenc_n_Parc):
        # text = column_ATASma_EntregaCad_AdmVenc_n_Parc
        num = rename_ata(column_ATASma_EntregaCad_AdmVenc_n_Parc, 'mod1')
        #                       'Situação'
        # column_situacao_parc = self.column_Situacao
        if self.word_profissao == word_Supervisor:
            num += ' ' + self.word_Supervisor
        elif self.word_profissao == word_Gerencia:
            num += ' ' + self.word_Gerencia
        return num

    def create_Adimplencia(self, table_venc, num):
        self.adimplencias = ''
        list_adimplencias = []
        column_porc_ATA_Pag_n_Parc = word_porc_ + word_ATA_ + word_Pag_ + num + word_º_Parc
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            if '1' in str(num):
                valor = '100' + word__porc
                table_venc.loc[line, column_Adimplencia] = valor
                list_adimplencias.append(valor)
            else:
                porc_ATA_Pag_n_Parc = table_venc.iloc[line][column_porc_ATA_Pag_n_Parc]
                valor = str(porc_ATA_Pag_n_Parc) + word__porc
                table_venc.loc[line, column_Adimplencia] = valor
                list_adimplencias.append(valor)
        list_adimplencias_sem_repetidos = list(dict.fromkeys(list_adimplencias))
        for adimplencia in list_adimplencias_sem_repetidos:
            if self.adimplencias == '':
                self.adimplencias = adimplencia
            else:
                self.adimplencias += ' ' + adimplencia
        return table_venc

    def create_Parcela(self, table_venc, num):
        table_venc[column_Parcela] = str(num) + 'ª'
        return table_venc

    def create_ATA_Venc_n_Parc(self, table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc):
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            table_venc.loc[line, column_ATA_Venc_n_Parc] = table_venc.iloc[line][column_ATASma_EntregaCad_AdmVenc_n_Parc]  # noqa
        return table_venc

    def concat_tables_all_venc(self, table_venc):
        if self.table_all.empty:
            self.table_all = table_venc
        else:
            self.table_all = pd.concat([self.table_all, table_venc], ignore_index=True)
        # excluir linhas comissão zerada
        self.table_all.reset_index(drop=True, inplace=True)

    def delete_lines_comissao_zero(self, table_venc):
        self.list_line_delete = []
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            self.renomear.inf = table_venc.iloc[line][column_Comissao]
            comissao = float(self.renomear.valor())
            print(f'comissao: {comissao} type: {type(comissao)}')
            if comissao == 0:
                if line not in self.list_line_delete:
                    self.list_line_delete.append(line)
        print('##############################')
        print(f'self.list_line_delete: {self.list_line_delete}.')
        table_venc = table_venc.drop(self.list_line_delete)
        return table_venc

    # 6º adiciona sum_comissao, sum_comissao_compliance
    def add_column_Comissao(self):
        self.list_table_edit = []
        self.sum_all_comissao = 0
        self.sum_all_comissao_gerente = 0
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        for table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc, column_Situacao_n_ATA in self.list_tables_ata:  # noqa
            num = self.find_num_column_ATASma_Pag_n_Parc(column_ATASma_EntregaCad_AdmVenc_n_Parc)
            table_venc = self.find_and_create_percentual_escala(table_venc, num, column_ATASma_EntregaCad_AdmVenc_n_Parc)  # noqa
            table_venc = self.create_comissao_escala(table_venc, num, column_ATASma_EntregaCad_AdmVenc_n_Parc, column_Situacao_n_ATA)  # noqa
            table_venc = self.create_comissao_50_porc(table_venc, num)
            table_venc = self.create_Adimplencia(table_venc, num)
            table_venc = self.create_Parcela(table_venc, num)
            table_venc = self.create_ATA_Venc_n_Parc(table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc)  # noqa
            table_venc = self.delete_lines_comissao_zero(table_venc)

            self.set_sum_comissoes(table_venc)  # noqa

            self.concat_tables_all_venc(table_venc)
            self.list_table_edit.append([
                table_venc,
                column_ATASma_EntregaCad_AdmVenc_n_Parc,
                self.sum_comissao,
                self.sum_comissao_compliance,
                self.sum_compliance,
                self.adimplencias
            ])
        create_table(self.table_all, arqTableTeste1)
        self.table_all = self.table_all[self.list_columns_end]

        # self.print_list_list(self.list_table_edit)

    # # 7º deixar apenas valores validos nas tabelas, ou seja,
    # # valores que forma pagos e estao ativos
    # def edit_table(self):
    #     self.list_table_edit = []
    #     self.table_all: pd.DataFrame = pd.DataFrame()
    #     for table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc, sum_comissao, sum_comissao_compliance in self.list_table_column_comissao:  # noqa
    #         # excluir comissão zerada
    #         # table_venc = table_venc[table_venc[column_Comissao] != '0,00'].copy()
    #         # table_venc.reset_index(drop=True, inplace=True)
    #         # colocar coluna Parcela

    #         self.list_table_edit.append([
    #             table_venc,
    #             column_ATASma_EntregaCad_AdmVenc_n_Parc,
    #             sum_comissao,
    #             sum_comissao_compliance
    #         ])

    #     self.table_all = self.table_all[self.list_columns_end]

    # 8º montar e gerar o pdf

    def table_convert_pdf(self):
        # Configurar a localização para o Brasil
        path_file = Path_file()
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        size_font = 8
        size_font2 = 7
        size_line = 6
        space_paragraph = 2
        begin = True
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
        image_path = resource_path('img/select.jpg')
        pdf.add_image(image_path, 172, 10, 28, 9)
        if self.list_table_edit == []:
            return '0', 'zerado'
        if self.word_profissao == word_Supervisor or self.word_profissao == word_Gerencia:
            comissao = self.sum_all_comissao_gerente
        else:
            comissao = self.sum_all_comissao
        if comissao == 0:
            return '0', 'zerado'
        for (table_venc,
             column_ATASma_EntregaCad_AdmVenc_n_Parc,
             sum_comissao,
             sum_comissao_compliance,
             sum_compliance,
             adimplencias
             ) in self.list_table_edit:
            if begin is True:
                pdf.set_font('Arial', '', size_font)
                comissao = locale.currency(comissao, grouping=True)
                # Guarda a posição inicial do texto
                if self.word_profissao == word_Parceiro:
                    text = 'PARCEIRO:'
                    text2 = f'Semana: {self.date_sma_single}'
                else:
                    text = 'FUNCIONÁRIO:'
                    text2 = f'ATA: {self.date_ata_single}'
                text1 = f'{self.seller_single}'
                text3 = f'{self.cargo}'
                pdf.add_underlined_text(text, size_font, size_line)
                pdf.add_content_in_columns([text1, text2], 2, size_font, size_line)
                pdf.add_content_in_columns([text3, comissao], 2, size_font, size_line)
                pdf.ln(space_paragraph * 2)
                begin = False
            # Adiciona texto ao PDF
            pdf.set_font('Arial', '', size_font2)
            # sums_all = locale.currency(sums_all, grouping=True)
            # sum_compliance = locale.currency(sum_compliance, grouping=True)
            sum_comissao = locale.currency(sum_comissao, grouping=True)
            sum_comissao_compliance = locale.currency(
                sum_comissao_compliance, grouping=True)
            if not (table_venc.empty):
                list_ata_sum_comissao_credito.append(
                    [column_ATASma_EntregaCad_AdmVenc_n_Parc,
                     sum_comissao,
                     sum_comissao_compliance]
                )
                if self.model == '1':
                    text = column_ATASma_EntregaCad_AdmVenc_n_Parc
                    # text = text.replace('ATA', '')
                    # text = text.replace('º Parc', 'ª Parcela')
                    # text = text.replace(word_Entrega, '1ª Parcela')
                    # text = text.replace('Cad Adm', '1ª Parcela')
                    text = rename_ata(text, 'mod2')
                    pdf.add_underlined_text(text, size_font, size_line)
                    pdf.add_table(table_venc)
                    pdf.ln(space_paragraph)
                    pdf.multi_cell(0, size_line, '')
        if self.model == '2':
            pdf.add_table(self.table_all)
            pdf.ln(space_paragraph)
            pdf.multi_cell(0, size_line, '')
        # inicio do resumo
        text = 'RESUMO:'
        pdf.add_underlined_text(text, size_font, size_line)
        list_ata = []
        list_sum_comissao = []
        list_sum_compliance = []
        list_sum_comissao_compliance = []
        list_percentage_compliance = []
        for (
            column_ATASma_EntregaCad_AdmVenc_n_Parc,
            sum_comissao,
            sum_comissao_compliance
        ) in list_ata_sum_comissao_credito:
            text = column_ATASma_EntregaCad_AdmVenc_n_Parc
            text = rename_ata(text, 'mod2')
            list_ata.append(text)
            list_sum_compliance.append(sum_compliance)
            list_sum_comissao.append(sum_comissao)
            list_sum_comissao_compliance.append(sum_comissao_compliance)
            list_percentage_compliance.append(adimplencias)
        if self.word_profissao == word_Vendedor:
            data = {
                'TOTAL': list_ata,
                'CRÉDITO': list_sum_compliance,
                'COMISSÃO': list_sum_comissao,
                'ADIMPLÊNCIA': list_percentage_compliance,
                'COMISSÃO ADIMPLENTE': list_sum_comissao_compliance,
            }
        else:
            data = {
                'TOTAL': list_ata,
                'CRÉDITO': list_sum_compliance,
                'COMISSÃO': list_sum_comissao,
            }
        print(data)
        df = pd.DataFrame(data)
        pdf.add_table(df)
        pdf.ln(space_paragraph)
        text = ''
        text2 = ''
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
        name_ata = self.date_ata_single
        if self.word_profissao == word_Supervisor:
            text_word_profissao = word_Supervisor
        elif self.word_profissao == word_Gerencia:
            text_word_profissao = word_Gerencia
        elif self.word_profissao == word_Parceiro:
            text_word_profissao = word_Parceiro
            name_ata = self.date_sma_single
        else:
            text_word_profissao = word_Vendedor
        name_ata = name_ata.replace('/', ' ').lower().capitalize()
        text_seller = ''
        words_sellers = self.seller_single.lower().split()
        for word_seller in words_sellers:
            if len(word_seller) >= 3:
                word_seller = word_seller.capitalize()
            text_seller += " " + word_seller
        name_file = f'RP {text_word_profissao} {name_ata} {text_seller}.pdf'
        path_file = path_file.path_file_create_user(path_user="Documentos", path_origin="RECIBO", name_file=name_file)  # noqa
        # path_file = os.path.join(new_folder, name_file)
        pdf.output(path_file)
        return comissao
