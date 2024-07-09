from datetime import datetime
import pandas as pd
from pathlib import Path
from components.generat_payroll import Generat_payroll


class Main_gerar:
    def __init__(self, *args, **kwargs) -> None:
        self.generat_payroll = Generat_payroll()
        self.path_source = Path(__file__).parent
        self.path_tables = self.path_source / 'tables'
        self.name_arq = 'tableMerge.csv'
        self.arqtableMerge = self.path_tables / self.name_arq

        self.is_gerente = True
        self.model = '1'
        self.model = '2'
        self.seller_single_unit = ''
        # self.seller_single_unit = 'MARIA ILLYEDJA RODRIGUES DE SOUZA'
        # self.seller_single_unit = 'PARCEIRINHO EQUIPE - VALMON'
        # self.seller_single_unit = 'DENISE VITOR COSTA'
        # 'ANTONIO HELIO DE SOUSA TORRES',
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
        self.column_ata_cad_Adm = 'ATA Cad Adm'
        self.column_ata_entrega = 'ATA Entrega'
        self.column_sma_ent = 'Sma Ent'
        self.column_sma_cad_adm = 'Sma Cad Adm'
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
        self.data_date_pay = 'DIA DA SEMANA'
        self.column_cadastro = 'CADASTRO'
        # definição de variavel

        self.data_ata_single = 'MAIO/2024'
        self.data_ata = datetime.now()
        self.is_vendedores = False
        self.is_supervirores = False

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
        self.data_ata_single = data_ata = month_written + '/' + year
        print(data_ata)

    def generate_is_vendedores(self):
        if self.error:
            return
        print(f'self.is_vendedores: {self.is_vendedores}')
        if self.is_vendedores:
            self.is_gerente = False
            self.generate_employee()

    def generate_is_supervisores(self):
        if self.error:
            return
        print(f'self.is_supervirores: {self.is_supervirores}')
        if self.is_supervirores:
            self.is_gerente = True
            self.generate_employee()

    def generate_employee(self):
        if self.error:
            return
        if self.is_gerente:
            self.profession = self.column_gerente
            self.word = '_Gerente'
        else:
            self.profession = self.column_vendedor
            self.word = ''

        self.list_columns_full_ata = [
            self.column_ata_entrega,
            self.column_ata_cad_Adm
        ]
        self.list_columns_full_weekly = [
            self.column_sma_ent,
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

        self.table_full = pd.read_csv(self.arqtableMerge, sep=';',
                                      encoding='utf-8', dtype=str)

        self.generat_payroll.table_full = self.table_full
        self.generat_payroll.num_columns = ['ATA ', 'º Parc']
        self.num_atas_parc = self.generat_payroll.number  # ncol->ATA{N}ºParc

        # Preencher o restante das colunas sequenciais
        for i in range(2, self.num_atas_parc + 1):
            self.list_columns_full_ata.append(f'ATA {i}º Parc')
            self.list_columns_full_weekly.append(f'Sma {i}º Parc')
        self.list_seller_single_all = []

        # é por ata ou por semana ata?
        # ira selecionar tabela que tenha data_ata_single e o
        # profesion(Vendedor ou Gerete)
        for column in self.list_columns_full_ata:
            self.table_full_ata_def = (
                self.table_full.loc[self.table_full[column] == self.data_ata_single]  # noqa
            )
            self.list_unique = self.table_full_ata_def[self.profession].unique()  # noqa
            if len(self.list_unique) > 0:
                self.list_seller_single_all.extend(self.list_unique)

        self.list_seller_single = []
        for seller in self.list_seller_single_all:
            if seller not in self.list_seller_single:
                self.list_seller_single.append(seller)
        self.list_seller_single.sort()

        for self.seller_single in self.list_seller_single:
            if self.seller_single_unit:
                if self.seller_single_unit not in self.seller_single:
                    continue
            print('\n \n', self.seller_single)
            self.generat_payroll = Generat_payroll()
            self.pathTables = Path(__file__).parent.parent / 'tables'
            # name_arq = 'table_teste.csv'
            # arqTableTeste = pathTables / name_arq
            self.table_full = pd.read_csv(self.arqtableMerge, sep=';',
                                          encoding='utf-8', dtype=str)
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
            self.list_columns_full_ata = [self.column_ata_entrega, self.column_ata_cad_Adm]  # noqa
            self.list_columns_full_weekly = [self.column_sma_ent, self.column_sma_cad_adm]  # noqa
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

            self.list_columns_full_ata_entrega = [
                item for item in self.list_columns_full_ata if item != self.column_ata_cad_Adm]  # noqa
            self.list_columns_full_ata_cadastro = [
                item for item in self.list_columns_full_ata if item != self.column_ata_entrega]  # noqa

            self.name_columns_full = self.table_full.columns.tolist()

            self.table_full_ata = self.table_full[
                self.table_full[self.column_dt_pag_por] != self.data_date_pay]
            self.table_full_weekly = self.table_full[
                self.table_full[self.column_dt_pag_por] == self.data_date_pay]
            self.table_seller_single = self.table_full[
                self.table_full[self.profession] == self.seller_single]
            self.generat_payroll.table_seller_single = self.table_seller_single

            self.quantity_line_full = self.table_full.shape[0]
            self.quantity_line_ata = self.table_full_ata.shape[0]
            self.quantity_line_weekly = self.table_full_weekly.shape[0]

            # exportar variaveis
            self.generat_payroll.data_ata_single = self.data_ata_single
            self.generat_payroll.seller_single = self.seller_single
            # self.generat_payroll.arqTableTeste = self.arqTableTeste
            self.generat_payroll.model = self.model

            self.generat_payroll.column_credito = self.column_credito
            self.generat_payroll.column_administradora = self.column_administradora  # noqa
            self.generat_payroll.column_tabela = self.column_tabela
            self.generat_payroll.profession = self.profession
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
            self.generat_payroll.column_ata_cad_Adm = self.column_ata_cad_Adm
            # self.generat_payroll.column_situacao_d = self.column_situacao_d

            self.generat_payroll.data_date_pay = self.data_date_pay
            self.generat_payroll.column_cadastro = self.column_cadastro

            self.generat_payroll.list_situacao_to_comission = self.list_situacao_to_comission  # noqa
            self.generat_payroll.list_recebera_to_comission = self.list_recebera_to_comission  # noqa
            self.generat_payroll.list_condition_ata = self.list_condition_ata
            self.generat_payroll.list_cargo_not_calc_commis = self.list_cargo_not_calc_commis  # noqa
            self.generat_payroll.list_columns_new = self.list_columns_new
            self.generat_payroll.list_columns_end = self.list_columns_end
            self.generat_payroll.list_columns_ata_ent = self.list_columns_ata_ent  # noqa
            self.generat_payroll.list_columns_ata_cad = self.list_columns_ata_cad  # noqa

            self.generat_payroll.list_qtd_cotas_inicial = self.list_qtd_cotas_inicial  # noqa
            self.generat_payroll.list_qtd_cotas_final = self.list_qtd_cotas_final  # noqa
            self.generat_payroll.list_columns_full_ata = self.list_columns_full_ata  # noqa
            self.generat_payroll.list_columns_full_weekly = self.list_columns_full_weekly  # noqa
            self.generat_payroll.list_columns_full_ata_entrega = self.list_columns_full_ata_entrega  # noqa
            self.generat_payroll.list_columns_full_ata_cadastro = self.list_columns_full_ata_cadastro  # noqa
            self.generat_payroll.list_qtd_cotas_parc = self.list_qtd_cotas_parc
            self.generat_payroll.name_columns_full = self.name_columns_full

            self.generat_payroll.quantity_line_full = self.quantity_line_full
            self.generat_payroll.quantity_line_ata = self.quantity_line_ata
            self.generat_payroll.quantity_line_weekly = self.quantity_line_weekly  # noqa

            self.generat_payroll.dic_qtd_cotas_parc = self.dic_qtd_cotas_parc
            self.generat_payroll.dic_months = self.dic_months

            self.generat_payroll.table_full_ata = self.table_full_ata
            self.generat_payroll.table_full_weekly = self.table_full_weekly

            # fim da exportacao variavel
            self.list_columns_str_to_float = (
                self.list_qtd_cotas_inicial + self.list_qtd_cotas_final
            )
            self.list_columns_str_to_float.append(self.column_credito)
            self.generat_payroll.list_columns_str_to_float = self.list_columns_str_to_float  # noqa
            self.generat_payroll.convert_str_float = self.table_full
            # self.generat_payroll.table_full = (
            # self.generat_payroll.convert_str_float)
            self.generat_payroll.columns_to_list_full_seller()
            self.generat_payroll.columns_ata_full_seller_single()
            self.generat_payroll.tables_columns_ata_seller_single()
            self.generat_payroll.tables_concat_seller_single()
            self.generat_payroll.is_to_stop_program()
            self.stop_program = self.generat_payroll.stop_program
            if self.stop_program:
                continue
            self.generat_payroll.create_dictionary_datas()
            self.generat_payroll.table_list_administradora_add_line()
            self.generat_payroll.table_list_administradora_line_add_sum()
            self.generat_payroll.table_list_administradora_sum_add_qtdcotasinicial()  # noqa
            self.generat_payroll.table_list_administradora_sum_add_full()
            self.generat_payroll.add_column_comissao()
            # self.generat_payroll.table_columns_end()
            self.generat_payroll.edit_table()
            self.comissao, self.vendedor = self.generat_payroll.table_convert_pdf()  # noqa
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
        # print(text)


if __name__ == '__main__':
    main_gerar = Main_gerar()
    main_gerar.generate_employee()
