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
        # variaveis alteradas:
        self.is_vendedores = False
        self.is_supervisores = False
        self.is_gerentes = True
        self.is_parceiros = False
        self.seller_single_unit = ''
        self.date_ata_single = date_ata_single
        self.data_semana = datetime.now()
        self.date_sma_single = date_sma_single
        self.data_ata = datetime.now()
        # variaveis
        self.column_profissao = column_profissao
        # para calcular maiores comissões
        self.comissao_anterior1 = comissao_anterior1
        self.vendedor_anterior1 = vendedor_anterior1
        self.comissao_anterior2 = comissao_anterior2
        self.vendedor_anterior2 = vendedor_anterior2
        self.comissao_anterior3 = comissao_anterior3
        self.vendedor_anterior3 = vendedor_anterior3
        self.error = error
        self.start = start

        self.list_columns_ATA_EntregaCad_Adm = list_columns_ATA_EntregaCad_Adm
        self.list_columns_Sma_EntregaCad_Adm = list_columns_Sma_EntregaCad_Adm

    def generate_list_seller(self):
        try:
            self.table_full = pd.read_csv(arqTableMergeOrder, sep=';', encoding='utf-8', dtype=str)
        except pd.errors.EmptyDataError:
            return []
        list_seller_vendedores = list(self.table_full[column_Vendedor].unique())
        list_seller_supervisores = list(self.table_full[column_Supervisor].unique())
        list_seller = list_seller_vendedores + list_seller_supervisores
        list_seller = [item for item in list_seller if item and item.strip()]
        list_seller.sort()
        return list_seller

    def generate_date_ata(self):
        if self.error:
            return
        month = self.data_ata.strftime('%m')
        year = self.data_ata.strftime('%Y')
        # ATA
        month = int(month)
        month_written = inverted_dic_months.get(month, None)
        if month_written is None:
            self.error = True
            return
        self.date_ata_single = month_written + '/' + year
        # semana
        table_datas_semanais = load_table(arqTableDatasSemanais)
        data = self.data_semana.strftime('%d/%m/%Y')
        quantity_line = table_datas_semanais.shape[0]
        for line in range(quantity_line):
            data_table = table_datas_semanais.iloc[line][column_Data_Semana]
            if data_table == data:
                self.date_sma_single = table_datas_semanais.iloc[line][column_N_Semana_Mes]
                break
        self.father.prog2(word_ATA_ + f'mensal:   {self.date_ata_single}')
        self.father.prog2(word_ATA_ + f'semanal:  {self.date_sma_single}')

    def generate_is_vendedores(self):
        if self.error:
            return
        if self.is_vendedores:
            self.word_profissao = word_Vendedor
            self.word_Valor_Qtd_Vendas_Inicial_profissao = ''
            self.column_profissao = column_Vendedor
            self.father.prog2('Gerar recibos dos vendores:')
            self.generate_employee()

    def generate_is_supervisores(self):
        if self.error:
            return
        if self.is_supervisores:
            self.word_profissao = word_Supervisor
            self.word_Valor_Qtd_Vendas_Inicial_profissao = word_Supervisor
            self.column_profissao = column_Supervisor
            self.father.prog2('Gerar recibos dos supervisores:')
            self.generate_employee()

    def generate_is_gerentes(self):
        if self.error:
            return
        if self.is_gerentes:
            self.word_profissao = word_Gerencia
            self.word_Valor_Qtd_Vendas_Inicial_profissao = word_Gerencia
            self.column_profissao = column_Cargo_Gerencia
            self.father.prog2('Gerar recibos dos gerentes:')
            self.generate_employee()

    def generate_is_parceiros(self):
        if self.error:
            return
        if self.is_parceiros:
            self.word_profissao = word_Parceiro
            self.word_Valor_Qtd_Vendas_Inicial_profissao = ''
            self.column_profissao = column_Vendedor
            self.father.prog2('Gerar recibos dos parceiros:')
            self.generate_employee()

    def create_list_all_sellers(self):
        list_seller_single_all = []
        # é por ata ou por semana ata?
        if self.word_profissao == word_Parceiro:
            data_ata = self.date_sma_single
            list_columns_ATASma_EntregaCad_Adm = self.list_columns_Sma_EntregaCad_Adm
            # self.table_full = self.table_full.loc[(self.table_full[column_Data_Pag_Por] == word_DIA_DA_SEMANA)]  # noqa
        else:  # profesion(Vendedor, supervisor, Gerete, Gerente_Geral)
            data_ata = self.date_ata_single  # ATA -> MES/ANO
            # ATA Entreta, ATA Cad Adm ..
            list_columns_ATASma_EntregaCad_Adm = self.list_columns_ATA_EntregaCad_Adm

        # ira selecionar tabela que tenha column_ATASma_EntregaCad_Adm na ata selecionada
        for column_ATASma_EntregaCad_Adm in list_columns_ATASma_EntregaCad_Adm:
            table_full_def = self.table_full.loc[self.table_full[column_ATASma_EntregaCad_Adm] == data_ata]
            list_unique = table_full_def[self.column_profissao].unique()
            if len(list_unique) > 0:
                list_seller_single_all.extend(list_unique)

        list_seller_single = []
        for seller in list_seller_single_all:
            if seller not in list_seller_single:
                if not pd.isna(seller):
                    list_seller_single.append(seller)
        list_seller_single.sort()
        return list_seller_single

    def format_name_profissional(self):
        text_seller = ''
        words_sellers = self.seller_single.lower().split()
        for word_seller in words_sellers:
            if len(word_seller) >= 3:
                word_seller = word_seller.capitalize()
            text_seller += " " + word_seller
        return text_seller

    # def generate_variable_for_specific(self):
    #     column_profisinal = word__Valor_Qtd_Vendas_Inicial + self.word_Valor_Qtd_Vendas_Inicial_profissao
    #     self.generat_payroll.find_number_in_column = ['', column_profisinal]
    #     num_regras = self.generat_payroll.number  # ncol->{N}Qtd.CotIn
    #     self.generat_payroll.find_number_in_column = [str(num_regras) + word__Parc_, '']
    #     num_parcelas = self.generat_payroll.number  # ncol->Parc {N}
    #     print('===============')
    #     print(num_regras)
    #     print(num_parcelas)
    #     print('===============')

    def commission_bigger(self, comissao, vendedor):
        # apenas para saber qual as 3 maiores  comissões é a maior
        comissao = comissao.replace('R$', '').replace(' ', '')
        comissao = comissao.replace('.', '').replace(',', '.')
        comissao = float(comissao)
        if comissao >= self.comissao_anterior1:
            self.comissao_anterior3 = self.comissao_anterior2
            self.vendedor_anterior3 = self.vendedor_anterior2
            self.comissao_anterior2 = self.comissao_anterior1
            self.vendedor_anterior2 = self.vendedor_anterior1
            self.comissao_anterior1 = comissao
            self.vendedor_anterior1 = vendedor
        elif comissao >= self.comissao_anterior2:
            self.comissao_anterior3 = self.comissao_anterior2
            self.vendedor_anterior3 = self.vendedor_anterior2
            self.comissao_anterior2 = comissao
            self.vendedor_anterior2 = vendedor
        elif comissao >= self.comissao_anterior3:
            self.comissao_anterior3 = comissao
            self.vendedor_anterior3 = vendedor

    def print_commission_bigger(self):
        self.text = f'1º maior comissão: {self.vendedor_anterior1}, '
        self.text += f' sua comissão é: {self.comissao_anterior1} \n'
        self.text += f'2º maior comissão: {self.vendedor_anterior2}, '
        self.text += f' sua comissão é: {self.comissao_anterior2} \n'
        self.text += f'3º maior comissão: {self.vendedor_anterior3}, '
        self.text += f' sua comissão é: {self.comissao_anterior3}'

    def generate_employee(self):
        if self.error:
            return
        # self.generate_variable_for_specific()
        if self.start:
            self.table_full = pd.read_csv(arqTableMergeOrder, sep=';', encoding='utf-8', dtype=str)
            self.generat_payroll.generate_columns_for_all()
            self.generat_payroll.date_sma_single = self.date_sma_single
            self.generat_payroll.date_ata_single = self.date_ata_single
            self.start = False

        self.generat_payroll.word_profissao = self.word_profissao
        self.generat_payroll.column_profissao = self.column_profissao
        list_seller_single = self.create_list_all_sellers()
        self.seller_single_unit = 'LUCIANE MARIA MATOS PIMENTEL'
        for self.seller_single in list_seller_single:
            # Foi escolhido um vededor?
            if self.seller_single_unit:
                # só passa se for o vendedor escolhido
                if self.seller_single_unit not in self.seller_single:
                    continue
            self.generat_payroll.seller_single = self.seller_single
            # Saber se o vendedor parceiro é data smana
            sair = self.generat_payroll.columns_ata_full_seller_single()
            if sair:
                continue
            self.generat_payroll.tables_columns_ata_seller_single()

            # saber se é para para o programa
            text_seller = self.format_name_profissional()
            stop_program = self.generat_payroll.is_to_stop_program()
            if stop_program:
                text = text_seller + ' -> Não existe venda ou cargo não gera comissão.'
                self.father.prog2(text)
                continue
            # self.generat_payroll.create_dictionary_datas()
            # self.generat_payroll.table_list_administradora_add_line()

            # self.generat_payroll.table_list_administradora_line_add_sum()

            # self.generat_payroll.table_list_administradora_sum_add_qtdcotasinicial()
            # self.generat_payroll.table_list_administradora_sum_add_full()
            self.generat_payroll.add_column_Comissao()
            # self.generat_payroll.table_columns_end()
            # self.generat_payroll.edit_table()

            comissao = self.generat_payroll.table_convert_pdf()
            if comissao == '0':
                text = text_seller + ' -> Comissão zerada.'
                self.father.prog2(text)
            else:
                text = text_seller + ' -> OK.'
                self.father.prog2(text)

            self.commission_bigger(comissao, self.seller_single)

        self.print_commission_bigger()
