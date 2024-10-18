# flake8: noqa
# pyright: # type: ignore

import pandas as pd
import locale
import os
import sys
from pathlib import Path
# from components import renomear
from components import renomear
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

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # type: ignore[attr-defined]
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def create_table(table_created, path):
    if table_created.empty:
        return table_created
    table_created.columns = (table_created.columns.str.strip())
    table_created.to_csv(path, sep=';', index=False, header=True)
    return table_created

# entrada texto da ATA saida apenas o número ATA


class Generat_payroll:
    def __init__(self, *args, **kwargs) -> None:
        self.path_file = Path_file()
        self.renomear = Renomear()
        self.father = kwargs.get('father')
        self.list_keys = list_keys
        self.list_key_single = list_key_single
        self.word_profissao = word_profissao
        self.column_profissao = column_profissao
        self.word_Valor_Qtd_Vendas_Inicial_profissao = word_Valor_Qtd_Vendas_Inicial_profissao
        self.column_Cargo = column_Cargo
        self.column_Data_Pag_Por = column_Data_Pag_Por
        self.column_1_Parcela_Referencia = column_1_Parcela_Referencia
        self.column_Credito = column_Credito
        self.column_Situacao = column_Situacao
        self.column_ATA_Entrega = column_ATA_Entrega
        self.column_ATA_Cad_Adm = column_ATA_Cad_Adm
        self.column_Sma_Entrega = column_Sma_Entrega
        self.column_Sma_Cad_Adm = column_Sma_Cad_Adm
        # self.column_ATASma_EntregaCada_Adm = column_ATASma_EntregaCada_Adm
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

        self.sum_comissao = sum_comissao
        self.sum_comissao_adimplencia = sum_comissao_adimplencia
        self.sum_all_comissao = sum_all_comissao
        self.sum_all_comissao_gerente = sum_all_comissao_gerente
        self.sum_credito = sum_credito

        self.adimplencias = adimplencias
        self.list_line_delete = list_line_delete

        self.column_Escala_ATAMes_EntregaCad_Adm = column_Escala_ATAMes_EntregaCad_Adm

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
        self.list_columns_Situacao_n_Parc = list_columns_Situacao_n_Parc
        self.list_columns_Pag_Comissao_n_Parc = list_columns_Pag_Comissao_n_Parc
        self.list_columns_ATA_n_Parc_1_Atrasada = list_columns_ATA_n_Parc_1_Atrasada
        self.list_columns_ATA_n_Parc_2_Atrasada = list_columns_ATA_n_Parc_2_Atrasada

        self.list_columns_porc_ATA_Venc_n_Parc = list_columns_porc_ATA_Venc_n_Parc
        self.list_columns_porc_ATA_Venc_n_Parc_1_ATA_Atrasada = list_columns_porc_ATA_Venc_n_Parc_1_ATA_Atrasada
        self.list_columns_porc_ATA_Venc_n_Parc_2_ATA_Atrasada = list_columns_porc_ATA_Venc_n_Parc_2_ATA_Atrasada

        # self.list_ata = list_ata
        # self.list_sum_credito = list_sum_credito
        # self.list_sum_comissao = list_sum_comissao
        # self.list_adimplencias = list_adimplencias
        # self.list_sum_comissao_adimplencia = list_sum_comissao_adimplencia

        self.disc_temp = disc_temp
        self.disc_all = disc_all
        self.disc_atrasado = disc_atrasado

        self.list_tables_venc = list_tables_venc
        self.list_tables_ata_sums = []

        self.list_table_edit_all = list_table_edit_all
        self.list_table_edit_atrasada = list_table_edit_atrasada
        self.list_unique_information = list_unique_information

        self.table: pd.DataFrame = pd.DataFrame()
        self.table_full: pd.DataFrame = pd.DataFrame()
        self.table_all: pd.DataFrame = pd.DataFrame()
        self.table_atrasado: pd.DataFrame = pd.DataFrame()
        self.table_all_temp: pd.DataFrame = pd.DataFrame()
        self.table_seller_single: pd.DataFrame = pd.DataFrame()
        self.table_empty: pd.DataFrame = pd.DataFrame()
        # self.table_venc: pd.DataFrame = pd.DataFrame()
        # self.table_venc_atrasada: pd.DataFrame = pd.DataFrame()

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

    def print_list_list(self, list_list):
        for i1, list in enumerate(list_list):
            for i2, var in enumerate(list):
                print(f'arq: {i1}    arq2: {i2}')
                print(var)
                print('#############################')

    # 2º 1
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

    # 2º 2
    def set_value_cargo(self):
        if self.word_profissao == word_Gerencia:
            column_Cargo_professional = column_Cargo_Gerencia
        elif self.word_profissao == word_Supervisor:
            column_Cargo_professional = column_Cargo_Supervisor
        else:
            column_Cargo_professional = column_Cargo
        self.cargo = self.table_seller_single.iloc[0][column_Cargo_professional]

    # 2º 3
    def set_list_columns(self):
        p1_referencia = str(self.table_seller_single.iloc[0][self.column_1_Parcela_Referencia])
        data_pag_por = str(self.table_seller_single.iloc[0][self.column_Data_Pag_Por])
        if self.word_CADASTRO in p1_referencia and self.word_DIA_DA_SEMANA == data_pag_por:
            # self.column_ATASma_EntregaCada_Adm = self.column_Sma_Cad_Adm
            self.list_columns_ATASma_Pag_n_Parc = self.list_columns_Sma_Cad_AdmPag_n_Parc
            self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_Sma_Cad_AdmVenc_n_Parc
            list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_Mes_Cad_Adm
        elif self.word_CADASTRO in p1_referencia and self.word_DIA_DA_SEMANA != data_pag_por:
            # self.column_ATASma_EntregaCada_Adm = self.column_ATA_Cad_Adm
            self.list_columns_ATASma_Pag_n_Parc = self.list_columns_ATA_Cad_AdmPag_n_Parc
            self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_ATA_Cad_AdmVenc_n_Parc
            list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATA_Cad_Adm
        elif self.word_CADASTRO not in p1_referencia and self.word_DIA_DA_SEMANA == data_pag_por:
            # self.column_ATASma_EntregaCada_Adm = self.column_Sma_Entrega
            self.list_columns_ATASma_Pag_n_Parc = self.list_columns_Sma_EntregaPag_n_Parc
            self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_Sma_EntregaVenc_n_Parc
            list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_Mes_Entrega
        elif self.word_CADASTRO not in p1_referencia and self.word_DIA_DA_SEMANA != data_pag_por:
            # self.column_ATASma_EntregaCada_Adm = self.column_ATA_Entrega
            self.list_columns_ATASma_Pag_n_Parc = self.list_columns_ATA_EntregaPag_n_Parc
            self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_ATA_EntregaVenc_n_Parc
            list_columns_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATA_Entrega
        if self.word_profissao == word_Gerencia:
            self.column_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATAMes_EntregaCad_Adm[2]  # noqa
        elif self.word_profissao == word_Supervisor:
            self.column_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATAMes_EntregaCad_Adm[1]  # noqa
        else:
            self.column_Escala_ATAMes_EntregaCad_Adm = list_columns_Escala_ATAMes_EntregaCad_Adm[0]  # noqa

    # 4º 1 / 5º 12 /  6º 12
    def concat_tables(self, table_):
        if table_ is None:
            return
        if table_.empty:
            return
        if self.table_all_temp.empty:
            self.table_all_temp = table_
        else:
            self.table_all_temp = pd.concat([self.table_all_temp, table_], ignore_index=True)  # noqa
        # excluir linhas comissão zerada
        self.table_all_temp.reset_index(drop=True, inplace=True)

    # 5º 1 /  6º 3
    def find_num_column_ATASma_Pag_n_Parc(self, column_):
        # text = column_ATASma_EntregaCad_AdmVenc_n_Parc
        self.renomear.inf = column_
        num = self.renomear.n_ata('mod1')
        #                       'Situação'
        # column_situacao_parc = self.column_Situacao
        if self.word_profissao == word_Supervisor:
            num += ' ' + self.word_Supervisor
        elif self.word_profissao == word_Gerencia:
            num += ' ' + self.word_Gerencia
        return num

    # 5º 2  / 6º 4
    def creat_column_porc_ATA_Entrega(self, table_):
        table_[column_porc_ATA_Entrega] = porcentagem_Entrega
        return table_

    # 5º 3 / 6º 5
    def create_columns_sit_pag(self, table_, column_Situacao_n_Parc, key):
        table_[column_Situacoes] = ''
        quantity_line_table = table_.shape[0]
        for line in range(quantity_line_table):
            if key == 0:
                table_.loc[line, column_Situacoes] = word_PAGA
            else:
                self.renomear.inf = table_.iloc[line][column_Situacao_n_Parc]
                table_.loc[line, column_Situacoes] = self.renomear.situacao_pag()
        return table_

    # 5º 4 / 6º 6
    def create_columns_porc_num(self, table_, num, key):  # noqa
        table_[column_porc] = '0'
        quantity_line_table = table_.shape[0]
        for line in range(quantity_line_table):
            n_escala = table_.iloc[line][self.column_Escala_ATAMes_EntregaCad_Adm]  # noqa
            # se for igua a 0 não atigiu o minimo nao existe comissão
            minimum = True
            if n_escala != '0':
                column_Escala_Parc_num = n_escala + word__Parc_ + str(num) + self.word_Valor_Qtd_Vendas_Inicial_profissao  # noqa
                percentual = table_.iloc[line][column_Escala_Parc_num]
                if pd.isnull(percentual):
                    percentual = 0
            else:
                percentual = 0
                # if column_ATASma_EntregaCad_AdmVenc_n_Parc == self.column_ATASma_EntregaCada_Adm:
                if key == 0:
                    minimum = False
            try:
                percentual = float(percentual)
            except ValueError:
                self.renomear.inf = percentual
                percentual = float(self.renomear.valor())
            text_perc = str(percentual) + word__porc
            table_.loc[line, column_porc] = text_perc

            if minimum:
                num_percentual = percentual / 100
            else:
                num_percentual = 0.0000001
            num_percentual = locale.format_string("%.5f", num_percentual, grouping=True)  # noqa
            table_.loc[line, column_porc_Num] = num_percentual
        return table_

    # 5º 5 / 6º 7
    def create_colunm_comissao(self, table_, key, column_ATASma_EntregaCad_AdmVenc_n_Parc):  # noqa
        quantity_line_table = table_.shape[0]
        for line in range(quantity_line_table):
            if word_Entrega in column_ATASma_EntregaCad_AdmVenc_n_Parc or word_Cad_Adm in column_ATASma_EntregaCad_AdmVenc_n_Parc:
                data_recebera = (table_.iloc[line][column_1_Parcela_Recebera])  # noqa
            elif word_Parc in column_ATASma_EntregaCad_AdmVenc_n_Parc:
                data_recebera = (table_.iloc[line][column_Demais_Recebera])  # noqa
            elif word_FAT in column_ATASma_EntregaCad_AdmVenc_n_Parc:
                data_recebera = (table_.iloc[line][column_FAT_Recebera])  # noqa
            data_situacao = table_.iloc[line][column_Situacoes]
            if data_situacao not in list_situacao_to_comission:
                data_recebera = 'NAO'
                # A venda de entrada não importa a situação, OBS: a situação nã só representa a entrada # noqa
                if key == 0:
                    data_recebera = (table_.iloc[line][column_1_Parcela_Recebera])  # noqa
            if data_recebera in list_recebera_to_comission:
                self.renomear.inf = table_.iloc[line][self.column_Credito]
                value = round(float(self.renomear.valor()), 2)
                self.renomear.inf = table_.loc[line, column_porc_Num]
                percentual = float(self.renomear.valor())
                comissao = value * percentual
            else:
                comissao = 0
            comissao = locale.format_string("%.2f", comissao, grouping=True)
            table_.loc[line, column_Comissao] = comissao
        return table_

    # 5º 7 / 6º 9
    def create_column_parc(self, table_, num):
        table_[column_Parc] = str(num) + 'ª'
        return table_

    # 5º 10  / 6º 11
    def delete_lines_comissao_zero(self, table_):
        self.list_line_delete = []
        quantity_line_table = table_.shape[0]
        for line in range(quantity_line_table):
            self.renomear.inf = table_.iloc[line][column_Comissao]
            comissao = float(self.renomear.valor())
            if comissao == 0:
                self.renomear.inf = table_.iloc[line][column_porc_Num]
                porc_n = float(self.renomear.valor())
                if porc_n == 0:
                    if line not in self.list_line_delete:
                        self.list_line_delete.append(line)
        table_ = table_.drop(self.list_line_delete)
        table_.reset_index(drop=True, inplace=True)
        return table_

    # 5º 12  / 6º 12
    def set_sum_comissoes(self, table_):
        self.sum_comissao = 0
        self.sum_comissao_adimplencia = 0
        self.sum_credito = 0
        self.renomear.inf = self.sum_all_comissao
        self.sum_all_comissao = float(self.renomear.valor())
        quantity_line_table = table_.shape[0]
        for line in range(quantity_line_table):
            self.renomear.inf = table_.iloc[line][column_Comissao]
            self.sum_comissao += float(self.renomear.valor())
            self.renomear.inf = table_.iloc[line][column_Comissao_50_porc]
            self.sum_comissao_adimplencia += float(self.renomear.valor())
            self.renomear.inf = table_.iloc[line][column_Credito]
            self.sum_credito += float(self.renomear.valor())
        if self.word_profissao == word_Vendedor:
            self.sum_all_comissao += self.sum_comissao_adimplencia
        else:
            self.sum_all_comissao += self.sum_comissao
        # self.sum_all_comissao_gerente += self.sum_comissao
        self.sum_comissao = locale.currency(self.sum_comissao, grouping=True)
        self.sum_comissao_adimplencia = locale.currency(self.sum_comissao_adimplencia, grouping=True)  # noqa

    # 5º 14 / 6º 14
    def set_list_sum_comissão(self, list_):
        list_ata = []
        list_sum_credito = []
        list_sum_comissao = []
        list_adimplencias = []
        list_sum_comissao_adimplencia = []
        for (
            table_,
            column_ATASma_EntregaCad_AdmVenc_n_Parc,
            sum_comissao,
            sum_comissao_adimplencia,
            sum_credito,
            adimplencias
        ) in list_:
            if table_.empty:
                continue
            if sum_credito == 0:
                continue
            self.renomear.inf = column_ATASma_EntregaCad_AdmVenc_n_Parc
            list_ata.append(self.renomear.n_ata('mod2'))
            list_sum_credito.append(sum_credito)
            list_sum_comissao.append(sum_comissao)
            list_adimplencias.append(adimplencias)
            list_sum_comissao_adimplencia.append(sum_comissao_adimplencia)
        self.disc_temp = {
            word_TOTAL: list_ata,
            word_CREDITO: list_sum_credito,
            word_COMISSAO: list_sum_comissao,
        }
        if self.word_profissao == word_Vendedor:
            self.disc_temp[word_ADIMPLENCIA] = list_adimplencias
            self.disc_temp[word_COMISSAO_ADIMPLENTE] = list_sum_comissao_adimplencia

    # 5º 6
    def create_column_comissao_50_porc(self, table_venc, column_porc_ATA_Pag_n_Parc):
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            self.renomear.inf = table_venc.iloc[line][column_porc_ATA_Pag_n_Parc]
            porc_ATA_Pag_n_Parc = float(self.renomear.valor())
            if porc_ATA_Pag_n_Parc >= 50:
                table_venc.loc[line, column_Comissao_50_porc] = table_venc.iloc[line][column_Comissao]  # noqa
            else:
                table_venc.loc[line, column_Comissao_50_porc] = '0'
        return table_venc

    # 5º 8
    def create_column_ata_venc_n_parc(self, table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc):
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            table_venc.loc[line, column_ATA_Venc_n_Parc] = str(table_venc.iloc[line][column_ATASma_EntregaCad_AdmVenc_n_Parc])  # noqa
        return table_venc

    # 5º 9
    def delete_lines_different_ATA_Venc_n_Parc(self, table_venc):
        self.list_line_delete = []
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            ATA_Venc_n_Parc = table_venc.loc[line, column_ATA_Venc_n_Parc]
            if ATA_Venc_n_Parc != self.date_ata_single:
                self.list_line_delete.append(line)
        table_venc = table_venc.drop(self.list_line_delete)
        table_venc.reset_index(drop=True, inplace=True)
        return table_venc

    # 5º 11
    def create_column_adimplencia(self, table_venc, key):
        self.adimplencias = ''
        list_adimplencias_all = []
        # column_porc_ATA_Pag_n_Parc = word_porc_ + word_ATA_ + word_Pag_ + num + word_º_Parc
        column_porc_ATA_Pag_n_Parc = self.list_columns_porc_ATA_Venc_n_Parc[key]
        # column_ATA_Pag_n_Parc = self.list_columns_ATA_Pag_n_Parc[key]
        quantity_line_table = table_venc.shape[0]
        for line in range(quantity_line_table):
            print('############ alterar por aqui ####################')
            porc_ATA_Pag_n_Parc = table_venc.iloc[line][column_porc_ATA_Pag_n_Parc]
            valor = str(porc_ATA_Pag_n_Parc) + word__porc
            table_venc.loc[line, column_Adimplencia] = valor
            list_adimplencias_all.append(valor)
        list_adimplencias_sem_repetidos = list(dict.fromkeys(list_adimplencias_all))
        for adimplencia in list_adimplencias_sem_repetidos:
            self.adimplencias += adimplencia + '   '
        return table_venc

    # 6º 1
    def delete_lines_pag_comissao_n_parc(self, column_Pag_Comissao_n_Parc):
        table_atrasada = self.table_seller_single.copy()
        table_atrasada.reset_index(drop=True, inplace=True)
        list_line_delete = []
        quantity_line_table = table_atrasada.shape[0]
        for line in range(quantity_line_table):
            column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada = table_atrasada.iloc[line][column_Pag_Comissao_n_Parc]  # noqa
            if str(column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada).lower() == 'nan' or column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada is None:  # noqa
                if line not in list_line_delete:
                    list_line_delete.append(line)
            elif word_ATA_Atrasada not in column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada:
                if line not in list_line_delete:
                    list_line_delete.append(line)
        table_atrasada = table_atrasada.drop(list_line_delete)
        table_atrasada.reset_index(drop=True, inplace=True)
        return table_atrasada

    # 6º 2
    def delete_lines_pag_porc_n_parc_n_ata_atrasada(self, table_atrasada, column_Pag_Comissao_n_Parc):  # noqa
        list_line_delete = []
        quantity_line_table = table_atrasada.shape[0]
        for line in range(quantity_line_table):
            column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada = table_atrasada.iloc[line][column_Pag_Comissao_n_Parc]  # noqa
            column_ATA_Venc_n_Parc_n_ATA_Atrasada = column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada.replace(word_porc_, '').replace(word_Pag, word_Venc)  # noqa
            porc_n_parc_n_ata_atrasada = table_atrasada.iloc[line][
                column_ATA_Venc_n_Parc_n_ATA_Atrasada]
            if porc_n_parc_n_ata_atrasada != self.date_atasma_single:
                if line not in list_line_delete:
                    list_line_delete.append(line)
        table_atrasada = table_atrasada.drop(list_line_delete)
        table_atrasada.reset_index(drop=True, inplace=True)
        return table_atrasada

    # 6º 8
    def create_column_comissao_50_porc_atrasada(self, table_atrasada, column_Pag_Comissao_n_Parc):
        quantity_line_table = table_atrasada.shape[0]
        for line in range(quantity_line_table):
            column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada = table_atrasada.iloc[line][column_Pag_Comissao_n_Parc]  # noqa
            self.renomear.inf = table_atrasada.iloc[line][column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada]  # noqa
            porc_ATA_Pag_n_Parc = float(self.renomear.valor())
            if porc_ATA_Pag_n_Parc >= 50:
                table_atrasada.loc[line, column_Comissao_50_porc] = table_atrasada.iloc[line][column_Comissao]  # noqa
            else:
                table_atrasada.loc[line, column_Comissao_50_porc] = 0
        return table_atrasada

    # 6º 9
    def create_column_ata_venc_n_parc_atrasada(self, table_atrasada, column_Pag_Comissao_n_Parc):  # noqa
        quantity_line_table = table_atrasada.shape[0]
        for line in range(quantity_line_table):
            column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada = table_atrasada.iloc[line][column_Pag_Comissao_n_Parc]  # noqa
            column_ATA_Venc_n_Parc_n_ATA_Atrasada = column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada.replace(word_porc_, '').replace(word_Pag, word_Venc)  # noqa
            table_atrasada.loc[line, column_ATA_Venc_n_Parc] = table_atrasada.iloc[line][column_ATA_Venc_n_Parc_n_ATA_Atrasada]  # noqa
        return table_atrasada

    # 6º 10
    def create_column_adimplencia_atrasada(self, table_atrasada, column_Pag_Comissao_n_Parc, num):
        self.adimplencias = ''
        list_adimplencias_all = []
        # column_porc_ATA_Pag_n_Parc = word_porc_ + word_ATA_ + word_Pag_ + num + word_º_Parc
        # column_porc_ATA_Pag_n_Parc = self.list_columns_porc_ATA_Venc_n_Parc[key]
        quantity_line_table = table_atrasada.shape[0]
        for line in range(quantity_line_table):
            column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada = table_atrasada.iloc[line][column_Pag_Comissao_n_Parc]  # noqa
            print(f'antes: {column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada}')
            if column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada == '':
                column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada = word_porc_ + word_ATA + num + 'º ' + word_Parc
                print(f'depois: {column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada}')
            porc_ATA_Pag_n_Parc = table_atrasada.iloc[line][column_porc_ATA__Pag_n_Parc_n_ATA_Atrasada]  # noqa
            valor = str(porc_ATA_Pag_n_Parc) + word__porc
            table_atrasada.loc[line, column_Adimplencia] = valor
            list_adimplencias_all.append(valor)
        list_adimplencias_sem_repetidos = list(dict.fromkeys(list_adimplencias_all))
        for adimplencia in list_adimplencias_sem_repetidos:
            self.adimplencias += adimplencia + '   '
        return table_atrasada

    # 7º 1

    def comissao_be_doing(self):
        if self.list_table_edit_all == []:
            return True
        # if self.word_profissao == word_Supervisor or self.word_profissao == word_Gerencia:
        #     comissao = self.sum_all_comissao_gerente
        # else:
        #     comissao = self.sum_all_comissao
        if self.sum_all_comissao == 0:
            return True
        return False

    # 7º 2
    def creat_name_ata(self):
        name_ata = self.date_ata_single
        if self.word_profissao == word_Parceiro:
            name_ata = self.date_sma_single
        name_ata = name_ata.replace('/', ' ').lower().capitalize()
        return name_ata

    # 7º 3
    def creat_text_seller(self):
        text_seller = ''
        words_sellers = self.seller_single.lower().split()
        for word_seller in words_sellers:
            if len(word_seller) >= 3:
                word_seller = word_seller.capitalize()
            text_seller += " " + word_seller
        return text_seller

    # 1º criar lista de variaveis
    def generate_columns_for_all(self):
        # as colunas da tabela ficara no arqvuio pdf
        self.table_full = pd.read_csv(arqTableMergeOrder, sep=';', encoding='utf-8', dtype=str)
        self.find_number_in_column = list_words_ATA_Venc_º_Parc
        self.list_keys = []
        key = 0
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

            self.list_columns_ATA_n_Parc_1_Atrasada.append(word_Num_ + word_ATA_ + n_Parc + ' 1' + word__Atrasada)  # noqa
            self.list_columns_ATA_n_Parc_2_Atrasada.append(word_Num_ + word_ATA_ + n_Parc + ' 2' + word__Atrasada)  # noqa

            self.list_columns_porc_ATA_Venc_n_Parc.append(word_porc_ + word_ATA_ + word_Venc_ + n_Parc)  # noqa
            self.list_columns_porc_ATA_Venc_n_Parc_1_ATA_Atrasada.append(word_porc_ + word_ATA_ + word_Venc_ + n_Parc + ' 1 ' + word_ATA + word__Atrasada)  # noqa
            self.list_columns_porc_ATA_Venc_n_Parc_2_ATA_Atrasada.append(word_porc_ + word_ATA_ + word_Venc_ + n_Parc + ' 2 ' + word_ATA + word__Atrasada)  # noqa

            self.list_columns_Situacao_n_Parc.append(word_Situacao_ + n_Parc)

            self.list_columns_Pag_Comissao_n_Parc.append(word_Pag_Comissao_ + n_Parc)

            self.list_keys.append(key)
            key += 1

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
    def create_list_tables_venc(self):
        self.list_tables_venc = []
        self.list_key_single = self.list_keys.copy()
        for key in self.list_keys:
            column_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc[key]  # noqa
            table_temp = self.table_seller_single[self.table_seller_single[column_ATASma_EntregaCad_AdmVenc_n_Parc] == self.date_atasma_single].copy()  # noqa
            pk_Vend_ATA_Entrega = table_temp[column_PK_Vend_ATA_Entrega].unique()
            table_venc = self.table_seller_single[self.table_seller_single[column_PK_Vend_ATA_Entrega].isin(pk_Vend_ATA_Entrega)].copy()  # noqa
            table_venc.reset_index(drop=True, inplace=True)
            # table não é fazia?
            if not table_venc.empty:
                self.list_tables_venc.append(table_venc)
            else:
                self.list_tables_venc.append(self.table_empty)
                self.list_key_single.remove(key)
        # self.print_list_list(self.list_tables_venc)

    # 4º situações para sair e ir para o próximo vendedor
    def is_to_stop_program(self):
        self.table_all_temp = pd.DataFrame()
        for key in self.list_key_single:
            tables_venc = self.list_tables_venc[key]
            self.concat_tables(tables_venc)
        # se junção de tabela estiver vazio sair
        if self.table_all_temp.empty:
            return True
        # se for o cargo: ['ESTAGIÁRIO', 'ZERADO'] sair
        for cargo_not_calc_commis in self.list_cargo_not_calc_commis:
            if cargo_not_calc_commis in self.cargo:
                return True
        return False

   # 5º table_venc
    def add_column_Comissao(self):
        self.table_all_temp = pd.DataFrame()
        self.disc_temp = {}
        self.list_table_edit_all = []
        self.sum_all_comissao = 0
        # self.sum_all_comissao_gerente = 0
        for key in self.list_key_single:
            table_venc = self.list_tables_venc[key]
            column_Situacao_n_Parc = self.list_columns_Situacao_n_Parc[key]
            column_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_ATASma_EntregaCad_AdmVenc_n_Parc[key]  # noqa
            column_porc_ATA_Pag_n_Parc = self.list_columns_porc_ATA_Venc_n_Parc[key]
            num = self.find_num_column_ATASma_Pag_n_Parc(column_ATASma_EntregaCad_AdmVenc_n_Parc)
            table_venc = self.creat_column_porc_ATA_Entrega(table_venc)
            if table_venc.empty:
                continue
            table_venc = self.create_columns_sit_pag(table_venc, column_Situacao_n_Parc, key)
            table_venc = self.create_columns_porc_num(table_venc, num, key)
            table_venc = self.create_colunm_comissao(table_venc, key, column_ATASma_EntregaCad_AdmVenc_n_Parc)  # noqa
            table_venc = self.create_column_comissao_50_porc(table_venc, column_porc_ATA_Pag_n_Parc)
            table_venc = self.create_column_parc(table_venc, num)
            table_venc = self.create_column_ata_venc_n_parc(table_venc, column_ATASma_EntregaCad_AdmVenc_n_Parc)  # noqa
            table_venc = self.create_column_adimplencia(table_venc, key)
            table_venc = self.delete_lines_different_ATA_Venc_n_Parc(table_venc)
            table_venc = self.delete_lines_comissao_zero(table_venc)
            self.set_sum_comissoes(table_venc)
            self.concat_tables(table_venc)
            self.list_table_edit_all.append([
                table_venc,
                column_ATASma_EntregaCad_AdmVenc_n_Parc,
                self.sum_comissao,
                self.sum_comissao_adimplencia,
                self.sum_credito,
                self.adimplencias
            ])
        self.set_list_sum_comissão(self.list_table_edit_all)
        self.disc_all = self.disc_temp.copy()
        self.table_all = self.table_all_temp.copy()
        create_table(self.table_all, arqTableTeste1)
        if not self.table_all.empty:
            self.table_all = self.table_all[list_columns_end_pdf]
        # self.print_list_list(self.list_table_edit_all)

    # 6º table_atrasada
    def create_table_atrasada(self):
        self.table_all_temp = pd.DataFrame()
        self.disc_temp = {}
        self.list_table_edit_atrasada = []
        for key in self.list_key_single:
            column_Pag_Comissao_n_Parc = self.list_columns_Pag_Comissao_n_Parc[key]
            column_ATASma_EntregaCad_AdmVenc_n_Parc = self.list_columns_ATA_EntregaVenc_n_Parc[key]  # noqa
            column_Situacao_n_Parc = self.list_columns_Situacao_n_Parc[key]
            if key == 0:  # ATA de entrega
                continue
            table_atrasada = self.delete_lines_pag_comissao_n_parc(column_Pag_Comissao_n_Parc)
            if table_atrasada.empty:
                continue
            table_atrasada = self.delete_lines_pag_porc_n_parc_n_ata_atrasada(table_atrasada, column_Pag_Comissao_n_Parc)  # noqa
            num = self.find_num_column_ATASma_Pag_n_Parc(column_Pag_Comissao_n_Parc)
            table_atrasada = self.creat_column_porc_ATA_Entrega(table_atrasada)
            table_atrasada = self.create_columns_sit_pag(table_atrasada, column_Situacao_n_Parc, key)  # noqa
            table_atrasada = self.create_columns_porc_num(table_atrasada, num, key)
            table_atrasada = self.create_colunm_comissao(table_atrasada, key, column_ATASma_EntregaCad_AdmVenc_n_Parc)  # noqa
            table_atrasada = self.create_column_comissao_50_porc_atrasada(table_atrasada, column_Pag_Comissao_n_Parc)  # noqa
            table_atrasada = self.create_column_parc(table_atrasada, num)
            table_atrasada = self.create_column_ata_venc_n_parc_atrasada(table_atrasada, column_Pag_Comissao_n_Parc)  # noqa
            table_atrasada = self.create_column_adimplencia_atrasada(table_atrasada, column_Pag_Comissao_n_Parc, num)  # noqa
            table_atrasada = self.delete_lines_comissao_zero(table_atrasada)
            self.set_sum_comissoes(table_atrasada)
            self.concat_tables(table_atrasada)
            self.list_table_edit_atrasada.append([
                table_atrasada,
                column_ATASma_EntregaCad_AdmVenc_n_Parc,
                self.sum_comissao,
                self.sum_comissao_adimplencia,
                self.sum_credito,
                self.adimplencias
            ])

        self.set_list_sum_comissão(self.list_table_edit_atrasada)
        self.disc_atrasado = self.disc_temp.copy()
        self.table_atrasado = self.table_all_temp.copy()
        create_table(self.table_atrasado, arqTableTeste2)
        if not self.table_atrasado.empty:
            self.table_atrasado = self.table_atrasado[list_columns_end_pdf]
            print(f'self.seller_single; {self.seller_single}')

    # 7º montar e gerar o pdf
    def table_convert_pdf(self):
        condition = self.comissao_be_doing()
        if condition:
            return '0'
        path_file = Path_file()
        pdf = PDF()
        pdf.title = word_RECIBO_DE_PAGAMENTO
        pdf.text_size_head = text_size_head
        pdf.text_size_footer = text_size_footer
        pdf.text_size_table = text_size_table
        pdf.cell_height = cell_height
        pdf.space_columns = space_columns
        pdf.add_page()
        image_path = resource_path(img_select)
        pdf.add_image(image_path, 172, 10, 28, 9)
        pdf.set_font('Arial', '', size_font)
        if self.word_profissao == word_Parceiro:
            text = word_PARCEIRO
            text2 = f'Semana: {self.date_sma_single}'
        else:
            text = word_FUNCIONARIO
            text2 = f'ATA: {self.date_ata_single}'
        pdf.add_underlined_text(text, size_font, size_line)
        pdf.add_content_in_columns([self.seller_single, text2], 2, size_font, size_line)
        self.sum_all_comissao = locale.currency(self.sum_all_comissao, grouping=True)
        pdf.add_content_in_columns([self.cargo, self.sum_all_comissao], 2, size_font, size_line)
        pdf.ln(space_paragraph * 2)
        pdf.set_font('Arial', '', size_font2)
        # sums_all = locale.currency(sums_all, grouping=True)
        # sum_credito = locale.currency(sum_credito, grouping=True)
        pdf.add_table(self.table_all)
        if not self.table_atrasado.empty:
            pdf.ln(space_paragraph * 2)
            pdf.add_underlined_text(word_PAGAMENTOS_ATRASADOS, size_font, size_line)
            pdf.set_font('Arial', '', size_font2)
            pdf.add_table(self.table_atrasado)
        pdf.ln(space_paragraph)
        pdf.multi_cell(0, size_line, '')
        # Resumo
        pdf.add_underlined_text(word_RESUMO, size_font, size_line)
        df = pd.DataFrame(self.disc_all)
        pdf.add_table(df)
        if not self.table_atrasado.empty:
            pdf.ln(space_paragraph * 2)
            pdf.add_underlined_text(word_RESUMO_PAGAMENTOS_ATRASADOS, size_font, size_line)
            pdf.set_font('Arial', '', size_font2)
            df = pd.DataFrame(self.disc_atrasado)
            pdf.add_table(df)
        pdf.ln(space_paragraph)
        text = ''
        text2 = ''
        pdf.add_text_to_end_of_line(self.sum_all_comissao, size_font, size_line)
        pdf.ln(space_paragraph * 4)
        text = ' '
        pdf.add_underlined_text(text, size_font, size_line)
        text = '                      ASSINATURA'
        text2 = 'FORTALEZA, ____/____/____ '
        pdf.add_content_in_columns([text, text2], 2, size_font, size_line)
        # Salvar
        atrasado_text = ''
        if not self.table_atrasado.empty:
            atrasado_text = word_cifrao
        name_ata = self.creat_name_ata()
        text_seller = self.creat_text_seller()
        name_file = f'RP {self.word_profissao} {name_ata} {text_seller}{atrasado_text}.pdf'
        arqRecibos = path_file.path_file_create_user(path_user="Documentos", path_origin="RECIBO", name_file=name_file)  # noqa
        # path_file = os.path.join(new_folder, name_file)
        pdf.output(arqRecibos)
        return self.sum_all_comissao
