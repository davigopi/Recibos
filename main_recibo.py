# flake8: noqa
# pyright: # type: ignore

from datetime import datetime
import pandas as pd
# from pathlib import Path
from components.generat_payroll import Generat_payroll
# import main_window
from path_file import Path_file
from components.variables import *


def load_table(path):
    table_loaded = pd.read_csv(path, sep=';', encoding='utf-8', dtype=str)
    # remover espaços inicio fim
    table_loaded.columns = (table_loaded.columns.str.strip())
    return table_loaded


class Main_recibo:
    def __init__(self, *args, **kwargs) -> None:
        self.father = kwargs.get('father')
        self.generat_payroll = Generat_payroll(father=self.father)
        self.path_file = Path_file()
        self.arqtableMerge = self.path_file.path_file_create_user('Appdata', 'tables', 'tableMerge.csv')  # noqa
        self.arqtableDatasSemanais = self.path_file.path_file_create_user('Appdata', 'tables', 'table_datas_semanais.csv')  # noqa
        self.model = '1'
        self.model = '2'
        # variaveis alteradas:
        self.is_vendedores = False
        self.is_supervisores = False
        self.is_gerentes = True
        self.is_parceiros = False
        self.seller_single_unit = ''
        self.date_ata_single = 'MAIO/2024'
        self.data_semana = datetime.now()

        self.date_sma_single = '1ª/MAIO/2024'

        self.data_ata = datetime.now()

        # self.prof_vendedores = 'Vendedor'
        # self.prof_supervisores = word_Supervisor
        # self.prof_gerentes = word_Supervisor
        # self.prof_parceiros = word_Parceiro
        # self.word = ''
        self.column_profissao = ''
        self.column_Vendedor = column_Vendedor
        self.column_Supervisor = column_Supervisor
        self.column_Cargo_Gerencia = column_Cargo_Gerencia
        self.column_Data_Pag_Por = column_Data_Pag_Por

        self.column_Ata_Cad_Adm = column_Ata_Cad_Adm
        self.column_ATA_Entrega = column_ATA_Entrega
        self.column_Sma_Cad_Adm = column_Sma_Cad_Adm
        self.column_Sma_Entrega = column_Sma_Entrega

        self.word_DIA_DA_SEMANA = word_DIA_DA_SEMANA
        self.column_N_Semana_Mes = column_N_Semana_Mes
        self.column_Data_Semana = column_Data_Semana

        self.column_Data_Pag_Por = column_Data_Pag_Por
        self.word_DIA_DA_SEMANA = word_DIA_DA_SEMANA
        self.word__Qtd_Cotas_Inicial = word__Qtd_Cotas_Inicial
        self.word__Parc_ = word__Parc_

        self.list_situacao_to_comission = list_situacao_to_comission
        self.list_recebera_to_comission = list_recebera_to_comission
        self.list_condition_ata = list_condition_ata
        self.list_cargo_not_calc_commis = list_cargo_not_calc_commis

        self.word_Vendedor = word_Vendedor
        self.word_Supervisor = word_Supervisor
        self.word_Parceiro = word_Parceiro
        self.word_ATA_ = word_ATA_
        self.word_º_Parc = word_º_Parc
        # definição de variavel

        # Inverte o dicionário
        self.inverted_dic_months = inverted_dic_months
        # para calcular maiores comissões
        self.comissao_anterior1 = comissao_anterior1
        self.vendedor_anterior1 = vendedor_anterior1
        self.comissao_anterior2 = comissao_anterior2
        self.vendedor_anterior2 = vendedor_anterior2
        self.comissao_anterior3 = comissao_anterior3
        self.vendedor_anterior3 = vendedor_anterior3
        self.error = error

    def generate_date_ata(self):
        if self.error:
            return
        month = self.data_ata.strftime('%m')
        year = self.data_ata.strftime('%Y')
        # ATA
        month = int(month)
        month_written = self.inverted_dic_months.get(month, None)
        if month_written is None:
            self.error = True
            return
        self.date_ata_single = month_written + '/' + year
        # semana
        table_datas_semanais = load_table(self.arqtableDatasSemanais)
        data = self.data_semana.strftime('%d/%m/%Y')
        quantity_line = table_datas_semanais.shape[0]
        for line in range(quantity_line):
            data_table = table_datas_semanais.iloc[line][self.column_Data_Semana]
            if data_table == data:
                self.date_sma_single = table_datas_semanais.iloc[line][self.column_N_Semana_Mes]
                break
        self.father.prog2(self.word_ATA_ + f'mensal:   {self.date_ata_single}')
        self.father.prog2(self.word_ATA_ + f'semanal:  {self.date_sma_single}')

    def generate_is_vendedores(self):
        if self.error:
            return
        if self.is_vendedores:
            # self.word = ''
            self.profession = self.word_Vendedor
            self.column_profissao = self.column_Vendedor
            self.father.prog2('Gerar recibos dos vendores:')
            self.generate_employee()

    def generate_is_supervisores(self):
        if self.error:
            return
        if self.is_supervisores:
            # self.word = '_Gerente'
            self.profession = word_Supervisor
            self.column_profissao = self.column_Supervisor
            self.father.prog2('Gerar recibos dos supervisores:')
            self.generate_employee()

    def generate_is_gerentes(self):
        if self.error:
            return
        if self.is_gerentes:
            # self.word = '_Gerente_Geral'
            self.profession = word_Supervisor
            self.column_profissao = self.column_Cargo_Gerencia
            self.father.prog2('Gerar recibos dos gerentes:')
            self.generate_employee()

    def generate_is_parceiros(self):
        if self.error:
            return
        if self.is_parceiros:
            # self.word = ''
            self.profession = word_Parceiro
            self.column_profissao = self.column_Vendedor
            self.father.prog2('Gerar recibos dos parceiros:')
            self.generate_employee()

    def generate_list_seller(self):
        try:
            self.table_full = pd.read_csv(self.arqtableMerge, sep=';', encoding='utf-8', dtype=str)
        except pd.errors.EmptyDataError:
            return []
        list_seller_vendedores = list(self.table_full[self.column_Vendedor].unique())
        list_seller_supervisores = list(self.table_full[self.column_Supervisor].unique())
        list_seller = list_seller_vendedores + list_seller_supervisores
        list_seller = [item for item in list_seller if item and item.strip()]
        list_seller.sort()
        return list_seller

    def generate_employee(self):
        if self.error:
            return
        self.list_columns_full_ata = [
            self.column_ATA_Entrega,
            self.column_Ata_Cad_Adm
        ]
        self.list_columns_full_weekly = [
            self.column_Sma_Entrega,
            self.column_Sma_Cad_Adm
        ]

        # as colunas da tabela ficara no arqvuio pdf

        try:
            self.table_full = pd.read_csv(self.arqtableMerge, sep=';', encoding='utf-8', dtype=str)
        except pd.errors.EmptyDataError:
            return
        self.generat_payroll.table_full = self.table_full
        self.generat_payroll.num_columns = [self.word_ATA_, self.word_ATA_]
        self.num_atas_parc = self.generat_payroll.number  # ncol->ATA{N}ºParc

        # Preencher o restante das colunas sequenciais
        for i in range(2, self.num_atas_parc + 1):
            self.list_columns_full_ata.append(self.word_ATA_ + f'{i}' + self.word_ATA_)
            self.list_columns_full_weekly.append(f'Sma {i}' + self.word_ATA_)

        list_seller_single_all = []
        # é por ata ou por semana ata?
        if self.profession == word_Parceiro:
            data_ata = self.date_sma_single
            self.table_full = self.table_full.loc[
                (self.table_full[self.column_Data_Pag_Por] == self.word_DIA_DA_SEMANA)
            ]
            list_columns_full = self.list_columns_full_weekly
        else:  # profesion(Vendedor, supervisor, Gerete, Gerente_Geral)
            # MES / ANO
            data_ata = self.date_ata_single
            #                   ATA Entreta, ATA Cad Adm
            list_columns_full = self.list_columns_full_ata

        # ira selecionar tabela que tenha date_ata_single e o
        for column in list_columns_full:
            table_full_def = self.table_full.loc[self.table_full[column] == data_ata]
            list_unique = table_full_def[self.column_profissao].unique()
            if len(list_unique) > 0:
                list_seller_single_all.extend(list_unique)

        list_seller_single = []
        for seller in list_seller_single_all:
            if seller not in list_seller_single:
                if not pd.isna(seller):
                    list_seller_single.append(seller)
        list_seller_single.sort()
        for self.seller_single in list_seller_single:
            # Foi escolhido um vededor?
            if self.seller_single_unit:
                if self.seller_single_unit not in self.seller_single:
                    continue
            self.generat_payroll = Generat_payroll(father=self.father)
            text_seller = ''
            words_sellers = self.seller_single.lower().split()
            for word_seller in words_sellers:
                if len(word_seller) >= 3:
                    word_seller = word_seller.capitalize()
                text_seller += " " + word_seller

            # self.pathTables = Path(__file__).parent.parent / 'tables'
            # name_arq = 'table_teste.csv'
            # arqTableTeste = pathTables / name_arq
            self.table_full = pd.read_csv(self.arqtableMerge, sep=';', encoding='utf-8', dtype=str)

            # Definir o número de grupos e de parcelas
            self.generat_payroll.table_full = self.table_full
            self.generat_payroll.num_columns = [self.word_ATA_, self.word_ATA_]
            self.num_atas_parc = self.generat_payroll.number  # ncol->ATA{N}ºPa
            self.generat_payroll.num_columns = ['', self.word__Qtd_Cotas_Inicial]
            self.num_regras = self.generat_payroll.number  # ncol->{N}Qtd.CotIn
            self.generat_payroll.num_columns = [str(self.num_regras) + self.word__Parc_, '']
            self.num_parcelas = self.generat_payroll.number  # ncol->Parc {N}
            # self.generat_payroll.word = self.word
            self.list_columns_full_ata = [self.column_ATA_Entrega, self.column_Ata_Cad_Adm]
            self.list_columns_full_weekly = [self.column_Sma_Entrega, self.column_Sma_Cad_Adm]
            # Preencher a lista sequencialmente
            for i in range(2, self.num_atas_parc + 1):
                self.list_columns_full_ata.append(self.word_ATA_ + f'{i}' + self.word_ATA_)
                self.list_columns_full_weekly.append(f'Sma {i}' + self.word_ATA_)
            # self.list_qtd_cotas_parc = []
            # self.list_qtd_cotas_inicial = []
            # self.list_qtd_cotas_final = []
            # self.dic_qtd_cotas_parc = {}
            # for i in range(1, self.num_regras + 1):
                # self.list_qtd_cotas_parc.append(f'{i} Qtd. Cotas Inicial{self.profession}')
                # self.list_qtd_cotas_inicial.append(f'{i} Qtd. Cotas Inicial{self.profession}')
                # self.list_qtd_cotas_parc.append(f'{i} Qtd. Cotas Final{self.profession}')
                # self.list_qtd_cotas_final.append(f'{i} Qtd. Cotas Final{self.profession}')
                # self.list = []
                # for j in range(1, self.num_parcelas + 1):
                # self.list_qtd_cotas_parc.append(f'{i} Parc {j}{self.profession}')
                # self.list.append(f'{i} Parc {j}{self.profession}')
                # self.chave = f'{i} Qtd. Cotas Inicial{self.profession}'
                # self.valor = [f'{i} Qtd. Cotas Final{self.profession}'] + self.list
                # self.dic_qtd_cotas_parc[self.chave] = self.valor

            # variaveis criada atravez de outras

            # self.column_Ata_Cad_Adm = 'ATA Cad Adm'
            # self.column_ATA_Entrega = 'ATA Entrega'
            # self.column_Sma_Entrega = 'Sma Entrega'
            # self.column_Sma_Cad_Adm = 'Sma Cad Adm'

            self.list_columns_full_ata_entrega = [
                item for item in self.list_columns_full_ata if item != self.column_Ata_Cad_Adm]
            self.list_columns_full_ata_cadastro = [
                item for item in self.list_columns_full_ata if item != self.column_ATA_Entrega]
            self.list_columns_full_sma_entrega = [
                item for item in self.list_columns_full_weekly if item != self.column_Sma_Cad_Adm]
            self.list_columns_full_sma_cadastro = [
                item for item in self.list_columns_full_weekly if item != self.column_Sma_Entrega]

            self.name_columns_full = self.table_full.columns.tolist()

            self.table_full_ata = self.table_full[
                self.table_full[self.column_Data_Pag_Por] != self.word_DIA_DA_SEMANA]
            self.table_full_weekly = self.table_full[
                self.table_full[self.column_Data_Pag_Por] == self.word_DIA_DA_SEMANA]
            self.table_seller_single = self.table_full[
                self.table_full[self.column_profissao] == self.seller_single]
            self.generat_payroll.table_seller_single = self.table_seller_single

            self.quantity_line_full = self.table_full.shape[0]
            self.quantity_line_ata = self.table_full_ata.shape[0]
            self.quantity_line_weekly = self.table_full_weekly.shape[0]

            # exportar variaveis
            self.generat_payroll.date_ata_single = self.date_ata_single
            self.generat_payroll.date_sma_single = self.date_sma_single
            self.generat_payroll.seller_single = self.seller_single
            # self.generat_payroll.arqTableTeste = self.arqTableTeste
            self.generat_payroll.model = self.model
            self.generat_payroll.profession = self.profession
            self.generat_payroll.column_profissao = self.column_profissao

            self.generat_payroll.list_situacao_to_comission = self.list_situacao_to_comission
            self.generat_payroll.list_recebera_to_comission = self.list_recebera_to_comission
            self.generat_payroll.list_condition_ata = self.list_condition_ata
            self.generat_payroll.list_cargo_not_calc_commis = self.list_cargo_not_calc_commis

            # self.generat_payroll.list_qtd_cotas_inicial = self.list_qtd_cotas_inicial
            # self.generat_payroll.list_qtd_cotas_final = self.list_qtd_cotas_final
            self.generat_payroll.list_columns_full_ata = self.list_columns_full_ata
            self.generat_payroll.list_columns_full_weekly = self.list_columns_full_weekly
            self.generat_payroll.list_columns_full_ata_entrega = self.list_columns_full_ata_entrega
            self.generat_payroll.list_columns_full_ata_cadastro = self.list_columns_full_ata_cadastro
            self.generat_payroll.list_columns_full_sma_entrega = self.list_columns_full_sma_entrega
            self.generat_payroll.list_columns_full_sma_cadastro = self.list_columns_full_sma_cadastro
            # self.generat_payroll.list_qtd_cotas_parc = self.list_qtd_cotas_parc
            self.generat_payroll.name_columns_full = self.name_columns_full

            self.generat_payroll.quantity_line_full = self.quantity_line_full
            self.generat_payroll.quantity_line_ata = self.quantity_line_ata
            self.generat_payroll.quantity_line_weekly = self.quantity_line_weekly

            # self.generat_payroll.dic_qtd_cotas_parc = self.dic_qtd_cotas_parc

            self.generat_payroll.table_full_ata = self.table_full_ata
            self.generat_payroll.table_full_weekly = self.table_full_weekly

            self.generat_payroll.columns_ata_full_seller_single()
            self.generat_payroll.tables_columns_ata_seller_single()
            self.generat_payroll.tables_concat_seller_single()
            self.generat_payroll.is_to_stop_program()
            self.stop_program = self.generat_payroll.stop_program
            if self.stop_program:
                text = text_seller + ' -> Cargo não gera comissão.'
                self.father.prog2(text)
                continue
            # self.generat_payroll.create_dictionary_datas()
            # self.generat_payroll.table_list_administradora_add_line()
            self.generat_payroll.table_list_administradora_line_add_sum()
            # self.generat_payroll.table_list_administradora_sum_add_qtdcotasinicial()
            # self.generat_payroll.table_list_administradora_sum_add_full()
            self.generat_payroll.add_column_Comissao()
            # self.generat_payroll.table_columns_end()
            self.generat_payroll.edit_table()
            self.comissao, self.vendedor = self.generat_payroll.table_convert_pdf()
            if self.comissao == '0':
                text = text_seller + ' -> Comissão zerada.'
                self.father.prog2(text)
            else:
                text = text_seller + ' -> OK.'
                self.father.prog2(text)
            self.comissao = self.comissao.replace('R$', '').replace(' ', '')
            self.comissao = self.comissao.replace('.', '').replace(',', '.')

            self.comissao = float(self.comissao)
            if self.comissao >= self.comissao_anterior1:
                self.comissao_anterior3 = self.comissao_anterior2
                self.vendedor_anterior3 = self.vendedor_anterior2
                self.comissao_anterior2 = self.comissao_anterior1
                self.vendedor_anterior2 = self.vendedor_anterior1
                self.comissao_anterior1 = self.comissao
                self.vendedor_anterior1 = self.vendedor
            elif self.comissao >= self.comissao_anterior2:
                self.comissao_anterior3 = self.comissao_anterior2
                self.vendedor_anterior3 = self.vendedor_anterior2
                self.comissao_anterior2 = self.comissao
                self.vendedor_anterior2 = self.vendedor
            elif self.comissao >= self.comissao_anterior3:
                self.comissao_anterior3 = self.comissao
                self.vendedor_anterior3 = self.vendedor
        self.text = f'1º maior comissão: {self.vendedor_anterior1}, '
        self.text += f' sua comissão é: {self.comissao_anterior1} \n'
        self.text += f'2º maior comissão: {self.vendedor_anterior2}, '
        self.text += f' sua comissão é: {self.comissao_anterior2} \n'
        self.text += f'3º maior comissão: {self.vendedor_anterior3}, '
        self.text += f' sua comissão é: {self.comissao_anterior3}'
