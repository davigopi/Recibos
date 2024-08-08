from datetime import datetime
import pandas as pd
# from pathlib import Path
from components.generat_payroll import Generat_payroll
# import main_window
from path_file import Path_file


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
        self.seller_single_unit = ''
        self.is_vendedores = False
        self.is_supervisores = False
        self.is_gerentes = True
        self.is_parceiros = False
        self.prof_vendedores = 'Vendedor'
        self.prof_supervisores = 'Gerente'
        self.prof_gerentes = 'Gerente_geral'
        self.prof_parceiros = 'Parceiro'
        self.word = ''
        self.column_profissao = ''
        self.column_vendedor = 'Vendedor'
        self.column_gerente = 'Gerente'
        self.column_cargo = 'Cargo'
        self.column_administradora = 'Administradora'
        self.column_tabela = 'Tabela'
        self.column_dt_pag_por = 'Dt pag. por'
        self.column_1p_referencia = '1P referencia'
        self.column_1P_recebera = '1P recebera'
        self.column_D_referencia = 'D+ referencia'
        self.column_D_recebera = 'D+ recebera'
        self.column_FAT_referencia = 'FAT referencia'
        self.column_FAT_recebera = 'FAT recebera'
        self.column_credito = 'Crédito'
        self.column_comissao = 'Comissão'
        self.column_situacao = 'Situação'
        self.column_ata_cad_adm = 'ATA Cad Adm'
        self.column_ata_entrega = 'ATA Entrega'
        self.column_sma_cad_adm = 'Sma Cad Adm'
        self.column_sma_entrega = 'Sma Ent'
        self.column_cliente = 'Cliente'
        self.column_n_contrato = 'Nº Contrato'
        self.column_grupo = 'Grupo'
        self.column_cota = 'Cota'
        self.column_data_entrega = 'Data de Entrega'
        self.column_cad_adm = 'Data Cad. Adm'
        self.column_new_parcela = 'Parcela'
        self.column_new_adimplencia = 'Adimplência'
        self.column_new_porcentagem_comissão = '%'
        self.column_ata_entrega_qtd_cotas = 'ATA Entrega qtd cotas'
        self.column_ata_entrega_qtd_cotas_ger = 'ATA Entrega qtd cotas Ger'
        self.column_ata_cad_adm_qtd_cotas = 'ATA Cad Adm qtd cotas'
        self.column_ata_cad_adm_qtd_cotas_ger = 'ATA Cad Adm qtd cotas Ger'

        self.column_mes_entrega_qtd_cotas = 'Mes Ent qtd cotas'
        self.column_mes_entrega_qtd_cotas_ger = 'Mes Ent qtd cotas Ger'
        self.column_mes_cad_adm_qtd_cotas = 'Mes Cad Adm qtd cotas'
        self.column_mes_cad_adm_qtd_cotas_ger = 'Mes Cad Adm qtd cotas Ger'

        self.data_date_pay = 'DIA DA SEMANA'
        self.data_cadastro = 'CADASTRO'
        self.column_n_semana_mes = 'N Semana Mes'
        self.column_data_semana = 'Data semana'

        self.column_total_sma_cad_adm = 'Total Sma Cad Adm'
        self.column_total_sma_cad_adm_ger = 'Total Sma Cad Adm Ger'
        self.column_total_ata_cad_adm = 'Total ATA Cad Adm'
        self.column_total_ata_cad_adm_ger = 'Total ATA Cad Adm Ger'
        self.column_total_sma_ent = 'Total Sma Ent'
        self.column_total_sma_ent_ger = 'Total Sma Ent Ger'
        self.column_total_ata_entrega = 'Total ATA Entrega'
        self.column_total_ata_entrega_ger = 'Total ATA Entrega Ger'

        # definição de variavel
        self.date_ata_single = 'MAIO/2024'
        self.date_sma_single = '1ª/MAIO/2024'
        self.data_ata = datetime.now()
        self.data_ata_semana = datetime.now()
        self.dic_months = {
            'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4,
            'MAIO': 5, 'JUNHO': 6, 'JULHO': 7, 'AGOSTO': 8, 'SETEMBRO': 9,
            'OUTUBRO': 10, 'NOVEMBRO': 11, 'DEZEMBRO': 12
        }

        # Inverte o dicionário
        self.inverted_dic_months = {v: k for k, v in self.dic_months.items()}
        # para calcular maiores comissões
        self.comissao_anterior1 = 0
        self.vendedor_anterior1 = ''
        self.comissao_anterior2 = 0
        self.vendedor_anterior2 = ''
        self.comissao_anterior3 = 0
        self.vendedor_anterior3 = ''
        self.error = False

    def generate_date_ata(self):
        if self.error:
            return
        month = self.data_ata.strftime('%m')
        year = self.data_ata.strftime('%Y')
        month = int(month)
        month_written = self.inverted_dic_months.get(month, None)
        if month_written is None:
            self.error = True
            return
        self.date_ata_single = month_written + '/' + year

        table_datas_semanais = load_table(self.arqtableDatasSemanais)
        data = self.data_ata.strftime('%d/%m/%Y')
        quantity_line = table_datas_semanais.shape[0]
        for line in range(quantity_line):
            data_table = table_datas_semanais.iloc[line][self.column_data_semana]  # noqa
            if data_table == data:
                self.date_sma_single = table_datas_semanais.iloc[line][self.column_n_semana_mes]  # noqa
                break
        self.father.prog2(f'ATA mensal:   {self.date_ata_single}')  # type: ignore # noqa
        self.father.prog2(f'ATA semanal:  {self.date_sma_single}')  # type: ignore # noqa

    def generate_is_vendedores(self):
        if self.error:
            return
        if self.is_vendedores:
            self.word = ''
            self.profession = self.prof_vendedores
            self.column_profissao = self.column_vendedor
            self.father.prog2('Gerar recibos dos vendores:')  # type: ignore
            self.generate_employee()

    def generate_is_supervisores(self):
        if self.error:
            return
        if self.is_supervisores:
            self.word = '_Gerente'
            self.profession = self.prof_supervisores
            self.column_profissao = self.column_gerente
            self.father.prog2('Gerar recibos dos supervisores:')  # type: ignore # noqa
            self.generate_employee()

    def generate_is_gerentes(self):
        if self.error:
            return
        if self.is_gerentes:
            self.word = '_Gerente'
            self.profession = self.prof_gerentes
            self.column_profissao = self.column_gerente
            self.father.prog2('Gerar recibos dos gerentes:')  # type: ignore
            # self.generate_employee()

    def generate_is_parceiros(self):
        if self.error:
            return
        if self.is_parceiros:
            self.word = ''
            self.profession = self.prof_parceiros
            self.column_profissao = self.column_vendedor
            self.father.prog2('Gerar recibos dos parceiros:')  # type: ignore
            self.generate_employee()

    def generate_list_seller(self):
        try:
            self.table_full = pd.read_csv(self.arqtableMerge, sep=';', encoding='utf-8', dtype=str)  # noqa
        except pd.errors.EmptyDataError:
            return []
        list_seller_vendedores = list(self.table_full['Vendedor'].unique())
        list_seller_supervisores = list(self.table_full['Gerente'].unique())
        list_seller = list_seller_vendedores + list_seller_supervisores
        list_seller = [item for item in list_seller if item and item.strip()]
        list_seller.sort()
        return list_seller

    def generate_employee(self):
        if self.error:
            return
        self.list_columns_full_ata = [
            self.column_ata_entrega,
            self.column_ata_cad_adm
        ]
        self.list_columns_full_weekly = [
            self.column_sma_entrega,
            self.column_sma_cad_adm
        ]
        self.list_columns_new = [
            self.column_new_parcela,
            self.column_new_adimplencia,
            self.column_new_porcentagem_comissão
        ]
        self.list_columns_end = [
            self.column_new_parcela,
            self.column_administradora,
            self.column_n_contrato,
            self.column_data_entrega,
            self.column_cliente,
            self.column_credito,
            self.column_new_porcentagem_comissão,
            self.column_comissao,
            self.column_new_adimplencia,
            # self.column_cad_adm,
            # self.column_grupo,
            # self.column_cota,
        ]
        self.list_columns_ata_ent = [
            self.column_ata_entrega_qtd_cotas,
            self.column_ata_entrega_qtd_cotas_ger
        ]
        self.list_columns_ata_cad = [
            self.column_ata_cad_adm_qtd_cotas,
            self.column_ata_cad_adm_qtd_cotas_ger
        ]

        self.list_columns_mes_ent = [
            self.column_mes_entrega_qtd_cotas,
            self.column_mes_entrega_qtd_cotas_ger
        ]
        self.list_columns_mes_cad = [
            self.column_mes_cad_adm_qtd_cotas,
            self.column_mes_cad_adm_qtd_cotas_ger
        ]

        try:
            self.table_full = pd.read_csv(self.arqtableMerge, sep=';', encoding='utf-8', dtype=str)  # noqa
        except pd.errors.EmptyDataError:
            return
        self.generat_payroll.table_full = self.table_full
        self.generat_payroll.num_columns = ['ATA ', 'º Parc']
        self.num_atas_parc = self.generat_payroll.number  # ncol->ATA{N}ºParc

        # Preencher o restante das colunas sequenciais
        for i in range(2, self.num_atas_parc + 1):
            self.list_columns_full_ata.append(f'ATA {i}º Parc')
            self.list_columns_full_weekly.append(f'Sma {i}º Parc')
        list_seller_single_all = []

        # é por ata ou por semana ata?
        if self.profession == self.prof_parceiros:
            data_ata = self.date_sma_single
            self.table_full = self.table_full.loc[
                (self.table_full['Dt pag. por'] == 'DIA DA SEMANA')
            ]
            list_columns_full = self.list_columns_full_weekly
        else:
            # profesion(Vendedor, supervisor ou  Gerete)
            data_ata = self.date_ata_single
            list_columns_full = self.list_columns_full_ata
        # ira selecionar tabela que tenha date_ata_single e o
        for column in list_columns_full:
            table_full_def = self.table_full.loc[self.table_full[column] == data_ata]  # noqa
            list_unique = table_full_def[self.column_profissao].unique()
            if len(list_unique) > 0:
                list_seller_single_all.extend(list_unique)

        list_seller_single = []
        for seller in list_seller_single_all:
            if seller not in list_seller_single:
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
                # print(len(word_seller))
                if len(word_seller) >= 3:
                    word_seller = word_seller.capitalize()
                text_seller += " " + word_seller

            # self.pathTables = Path(__file__).parent.parent / 'tables'
            # name_arq = 'table_teste.csv'
            # arqTableTeste = pathTables / name_arq
            self.table_full = pd.read_csv(self.arqtableMerge, sep=';', encoding='utf-8', dtype=str)  # noqa
            # column_situacao_d = 'º Parc'
            self.list_situacao_to_comission = ['NORMAL', 'PAGA']
            self.list_recebera_to_comission = ['SIM']
            self.list_condition_ata = ['Entrega', 'Cad Adm', 'Parc', 'FAT']
            self.list_cargo_not_calc_commis = ['ESTAGIÁRIO', 'ZERADO']
            # Definir o número de grupos e de parcelas
            self.generat_payroll.table_full = self.table_full
            self.generat_payroll.num_columns = ['ATA ', 'º Parc']
            self.num_atas_parc = self.generat_payroll.number  # ncol->ATA{N}ºPa
            self.generat_payroll.num_columns = ['', ' Qtd. Cotas Inicial']
            self.num_regras = self.generat_payroll.number  # ncol->{N}Qtd.CotIn
            self.generat_payroll.num_columns = [str(self.num_regras) + ' Parc ', '']  # noqa
            self.num_parcelas = self.generat_payroll.number  # ncol->Parc {N}
            self.generat_payroll.word = self.word
            self.list_columns_full_ata = [self.column_ata_entrega, self.column_ata_cad_adm]  # noqa
            self.list_columns_full_weekly = [self.column_sma_entrega, self.column_sma_cad_adm]  # noqa
            # Preencher a lista sequencialmente
            for i in range(2, self.num_atas_parc + 1):
                self.list_columns_full_ata.append(f'ATA {i}º Parc')
                self.list_columns_full_weekly.append(f'Sma {i}º Parc')
            self.list_qtd_cotas_parc = []
            self.list_qtd_cotas_inicial = []
            self.list_qtd_cotas_final = []
            self.dic_qtd_cotas_parc = {}
            for i in range(1, self.num_regras + 1):
                self.list_qtd_cotas_parc.append(f'{i} Qtd. Cotas Inicial{self.word}')  # noqa
                self.list_qtd_cotas_inicial.append(f'{i} Qtd. Cotas Inicial{self.word}')  # noqa
                self.list_qtd_cotas_parc.append(f'{i} Qtd. Cotas Final{self.word}')  # noqa
                self.list_qtd_cotas_final.append(f'{i} Qtd. Cotas Final{self.word}')  # noqa
                self.list = []
                for j in range(1, self.num_parcelas + 1):
                    self.list_qtd_cotas_parc.append(f'{i} Parc {j}{self.word}')
                    self.list.append(f'{i} Parc {j}{self.word}')
                self.chave = f'{i} Qtd. Cotas Inicial{self.word}'
                self.valor = [f'{i} Qtd. Cotas Final{self.word}'] + self.list
                self.dic_qtd_cotas_parc[self.chave] = self.valor

            # variaveis criada atravez de outras

            # self.column_ata_cad_adm = 'ATA Cad Adm'
            # self.column_ata_entrega = 'ATA Entrega'
            # self.column_sma_entrega = 'Sma Ent'
            # self.column_sma_cad_adm = 'Sma Cad Adm'

            self.list_columns_full_ata_entrega = [
                item for item in self.list_columns_full_ata if item != self.column_ata_cad_adm]  # noqa
            self.list_columns_full_ata_cadastro = [
                item for item in self.list_columns_full_ata if item != self.column_ata_entrega]  # noqa

            self.list_columns_full_sma_entrega = [
                item for item in self.list_columns_full_weekly if item != self.column_sma_cad_adm]  # noqa
            self.list_columns_full_sma_cadastro = [
                item for item in self.list_columns_full_weekly if item != self.column_sma_entrega]  # noqa

            self.name_columns_full = self.table_full.columns.tolist()

            self.table_full_ata = self.table_full[
                self.table_full[self.column_dt_pag_por] != self.data_date_pay]
            self.table_full_weekly = self.table_full[
                self.table_full[self.column_dt_pag_por] == self.data_date_pay]
            self.table_seller_single = self.table_full[
                self.table_full[self.column_profissao] == self.seller_single]
            self.generat_payroll.table_seller_single = self.table_seller_single

            self.quantity_line_full = self.table_full.shape[0]
            self.quantity_line_ata = self.table_full_ata.shape[0]
            self.quantity_line_weekly = self.table_full_weekly.shape[0]

            # exportar variaveis
            self.generat_payroll.date_ata_single = self.date_ata_single
            self.generat_payroll.date_sma_single = self.date_sma_single  # noqa
            self.generat_payroll.seller_single = self.seller_single
            # self.generat_payroll.arqTableTeste = self.arqTableTeste
            self.generat_payroll.model = self.model

            self.generat_payroll.column_credito = self.column_credito
            self.generat_payroll.column_administradora = self.column_administradora  # noqa
            self.generat_payroll.column_tabela = self.column_tabela
            self.generat_payroll.profession = self.profession
            self.generat_payroll.column_profissao = self.column_profissao
            self.generat_payroll.column_cargo = self.column_cargo
            self.generat_payroll.column_dt_pag_por = self.column_dt_pag_por
            self.generat_payroll.column_1p_referencia = self.column_1p_referencia  # noqa
            self.generat_payroll.column_1P_recebera = self.column_1P_recebera
            self.generat_payroll.column_D_referencia = self.column_D_referencia
            self.generat_payroll.column_D_recebera = self.column_D_recebera
            self.generat_payroll.column_FAT_referencia = self.column_FAT_referencia  # noqa
            self.generat_payroll.column_FAT_recebera = self.column_FAT_recebera
            self.generat_payroll.column_comissao = self.column_comissao
            self.generat_payroll.column_situacao = self.column_situacao
            self.generat_payroll.column_ata_entrega = self.column_ata_entrega
            self.generat_payroll.column_sma_entrega = self.column_sma_entrega
            self.generat_payroll.column_ata_cad_adm = self.column_ata_cad_adm
            self.generat_payroll.column_sma_cad_adm = self.column_sma_cad_adm
            self.generat_payroll.column_total_sma_cad_adm = self.column_total_sma_cad_adm  # noqa
            self.generat_payroll.column_total_sma_cad_adm_ger = self.column_total_sma_cad_adm_ger  # noqa
            self.generat_payroll.column_total_ata_cad_adm = self.column_total_ata_cad_adm  # noqa
            self.generat_payroll.column_total_ata_cad_adm_ger = self.column_total_ata_cad_adm_ger  # noqa
            self.generat_payroll.column_total_sma_ent = self.column_total_sma_ent  # noqa
            self.generat_payroll.column_total_sma_ent_ger = self.column_total_sma_ent_ger  # noqa
            self.generat_payroll.column_total_ata_entrega = self.column_total_ata_entrega  # noqa
            self.generat_payroll.column_total_ata_entrega_ger = self.column_total_ata_entrega_ger  # noqa

            # self.generat_payroll.column_situacao_d = self.column_situacao_d

            self.generat_payroll.data_date_pay = self.data_date_pay
            self.generat_payroll.data_cadastro = self.data_cadastro

            self.generat_payroll.list_situacao_to_comission = self.list_situacao_to_comission  # noqa
            self.generat_payroll.list_recebera_to_comission = self.list_recebera_to_comission  # noqa
            self.generat_payroll.list_condition_ata = self.list_condition_ata
            self.generat_payroll.list_cargo_not_calc_commis = self.list_cargo_not_calc_commis  # noqa
            self.generat_payroll.list_columns_new = self.list_columns_new
            self.generat_payroll.list_columns_end = self.list_columns_end
            self.generat_payroll.list_columns_ata_ent = self.list_columns_ata_ent  # noqa
            self.generat_payroll.list_columns_ata_cad = self.list_columns_ata_cad  # noqa

            self.generat_payroll.list_columns_mes_ent = self.list_columns_mes_ent  # noqa
            self.generat_payroll.list_columns_mes_cad = self.list_columns_mes_cad  # noqa

            self.generat_payroll.list_qtd_cotas_inicial = self.list_qtd_cotas_inicial  # noqa
            self.generat_payroll.list_qtd_cotas_final = self.list_qtd_cotas_final  # noqa
            self.generat_payroll.list_columns_full_ata = self.list_columns_full_ata  # noqa
            self.generat_payroll.list_columns_full_weekly = self.list_columns_full_weekly  # noqa
            self.generat_payroll.list_columns_full_ata_entrega = self.list_columns_full_ata_entrega  # noqa
            self.generat_payroll.list_columns_full_ata_cadastro = self.list_columns_full_ata_cadastro  # noqa
            self.generat_payroll.list_columns_full_sma_entrega = self.list_columns_full_sma_entrega  # noqa
            self.generat_payroll.list_columns_full_sma_cadastro = self.list_columns_full_sma_cadastro  # noqa
            self.generat_payroll.list_qtd_cotas_parc = self.list_qtd_cotas_parc
            self.generat_payroll.name_columns_full = self.name_columns_full

            self.generat_payroll.quantity_line_full = self.quantity_line_full
            self.generat_payroll.quantity_line_ata = self.quantity_line_ata
            self.generat_payroll.quantity_line_weekly = self.quantity_line_weekly  # noqa

            self.generat_payroll.dic_qtd_cotas_parc = self.dic_qtd_cotas_parc
            self.generat_payroll.dic_months = self.dic_months

            self.generat_payroll.table_full_ata = self.table_full_ata  # type: ignore # noqa
            self.generat_payroll.table_full_weekly = self.table_full_weekly  # type: ignore # noqa

            # fim da exportacao variavel
            self.list_columns_str_to_float = (
                self.list_qtd_cotas_inicial + self.list_qtd_cotas_final
            )
            self.list_columns_str_to_float.append(self.column_credito)
            self.generat_payroll.list_columns_str_to_float = self.list_columns_str_to_float  # noqa

            # self.generat_payroll.convert_str_float = self.table_full

            # self.generat_payroll.table_full = (
            # self.generat_payroll.convert_str_float)
            self.generat_payroll.columns_to_list_full_seller()
            self.generat_payroll.columns_ata_full_seller_single()
            self.generat_payroll.tables_columns_ata_seller_single()
            self.generat_payroll.tables_concat_seller_single()
            self.generat_payroll.is_to_stop_program()
            self.stop_program = self.generat_payroll.stop_program
            if self.stop_program:
                text = text_seller + ' -> Cargo não gera comissão.'
                self.father.prog2(text)  # type: ignore
                continue
            # self.generat_payroll.create_dictionary_datas()
            # self.generat_payroll.table_list_administradora_add_line()
            self.generat_payroll.table_list_administradora_line_add_sum()
            # self.generat_payroll.table_list_administradora_sum_add_qtdcotasinicial()  # noqa
            # self.generat_payroll.table_list_administradora_sum_add_full()
            self.generat_payroll.add_column_comissao()
            # self.generat_payroll.table_columns_end()
            self.generat_payroll.edit_table()
            self.comissao, self.vendedor = self.generat_payroll.table_convert_pdf()  # noqa
            if self.comissao == '0':
                text = text_seller + ' -> Comissão zerada.'
                self.father.prog2(text)  # type: ignore
            else:
                text = text_seller + ' -> OK.'
                self.father.prog2(text)  # type: ignore
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
