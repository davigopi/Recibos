# flake8: noqa
# pyright: # type: ignore

import pandas as pd
import locale
import os
import sys
from pathlib import Path
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
        self.father = kwargs.get('father')

        self.model = model

        self.stop_program = False

        self.word_profissao = ''
        self.column_profissao = ''
        self.column_Cargo = column_Cargo
        self.column_Data_Pag_Por = column_Data_Pag_Por
        self.column_1_Parcela_Referencia = column_1_Parcela_Referencia
        self.column_1_Parcela_Recebera = column_1_Parcela_Recebera
        self.column_Demais_Recebera = column_Demais_Recebera
        self.column_FAT_Recebera = column_FAT_Recebera
        self.column_Credito = column_Credito
        self.column_Comissao = column_Comissao
        self.column_Situacao = column_Situacao
        self.column_ATA_Entrega = column_ATA_Entrega
        self.column_ATA_Cad_Adm = column_ATA_Cad_Adm
        self.column_Sma_Entrega = column_Sma_Entrega
        self.column_Sma_Cad_Adm = column_Sma_Cad_Adm
        self.column_ata_sma = ''
        self.date_ata_single = ''
        self.date_sma_single = ''
        self.seller_single = ''
        self.word_DIA_DA_SEMANA = word_DIA_DA_SEMANA
        self.word_CADASTRO = word_CADASTRO
        # self.word = ''
        self.list_columns_Total = ''

        self.data_single = ''

        self.word_Supervisor = word_Supervisor
        self.word_Gerencia = word_Gerencia

        # self.quantity_line_full = 0
        # self.quantity_line_ata = 0
        # self.quantity_line_weekly = 0
        self.number_in_column = number_in_column

        self.list_situacao_to_comission = list_situacao_to_comission
        self.list_recebera_to_comission = list_recebera_to_comission
        self.list_condition_ata = list_condition_ata
        self.list_cargo_not_calc_commis = list_cargo_not_calc_commis
        self.list_columns_end = list_columns_end

        self.column_Porcentagem = column_Porcentagem
        self.column_Parcela = column_Parcela
        self.column_Adimplencia = column_Adimplencia

        self.list_columns_ATA_Mes = []

        self.list_columns_full_ata_entrega_pag = list_columns_full_ata_entrega_pag
        self.list_columns_full_ata_cadastro_pag = list_columns_full_ata_cadastro_pag
        self.list_columns_full_sma_entrega_pag = list_columns_full_sma_entrega_pag
        self.list_columns_full_sma_cadastro_pag = list_columns_full_sma_cadastro_pag
        self.list_columns_full_ata_entrega_venc = list_columns_full_ata_entrega_venc
        self.list_columns_full_ata_cadastro_venc = list_columns_full_ata_cadastro_venc
        self.list_columns_full_sma_entrega_venc = list_columns_full_sma_entrega_venc
        self.list_columns_full_sma_cadastro_venc = list_columns_full_sma_cadastro_venc
        self.list_cols_full_ata_sing_pag = list_cols_full_ata_sing_pag
        self.list_cols_full_ata_sing_venc = list_cols_full_ata_sing_venc

        self.list_name_columns_Pagar_Comissao_N_Parc = list_name_columns_Pagar_Comissao_N_Parc

        self.list_ata = []

        self.list_tables_ata = []
        self.list_tables_ata_sums = []

        self.list_table_column_comissao = []
        self.list_table_edit = []
        self.list_unique_information = []

        self.table: pd.DataFrame = pd.DataFrame()
        self.table_full: pd.DataFrame = pd.DataFrame()
        self.table_single_merge: pd.DataFrame = pd.DataFrame()
        self.table_seller_single: pd.DataFrame = pd.DataFrame()

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
        for table_pag, table_venc, ata in self.list_tables_ata:
            if not table_pag.empty:
                self.table_single_merge = pd.concat([self.table_single_merge, table_pag])  # noqa

    # 1º criar lista de variaveis
    def generate_variable_for_all(self):
        # as colunas da tabela ficara no arqvuio pdf
        self.table_full = pd.read_csv(arqtableMerge, sep=';', encoding='utf-8', dtype=str)
        self.find_number_in_column = list_words_ATA_Venc_º_Parc
        # Preencher o restante das colunas sequenciais
        for i in range(2, self.number_in_column + 1):
            n_Parc = str(i) + word_º_Parc
            self.list_columns_full_sma_cadastro_pag.append(word_Sma_ + word_Pag_ + n_Parc)  # noqa
            self.list_columns_full_sma_cadastro_venc.append(word_Sma_ + word_Venc_ + n_Parc)  # noqa

            self.list_columns_full_ata_cadastro_pag.append(word_ATA_ + word_Pag_ + n_Parc)  # noqa
            self.list_columns_full_ata_cadastro_venc.append(word_ATA_ + word_Venc_ + n_Parc)  # noqa

            self.list_columns_full_sma_entrega_pag.append(word_Sma_ + word_Pag_ + n_Parc)  # noqa
            self.list_columns_full_sma_entrega_venc.append(word_Sma_ + word_Venc_ + n_Parc)  # noqa

            self.list_columns_full_ata_entrega_pag.append(word_ATA_ + word_Pag_ + n_Parc)  # noqa
            self.list_columns_full_ata_entrega_venc.append(word_ATA_ + word_Venc_ + n_Parc)  # noqa

            self.list_name_columns_Pagar_Comissao_N_Parc.append(word_Pagar_Comissao_ + n_Parc)  # noqa

    # 2º define se vendedor/parceiro a primeira é pela ata entrea/cadastro
    def columns_ata_full_seller_single(self):
        # 1ª inf da coluna '1P referencia' -> ENTREGA ou CADASRO
        p1_referencia = str(self.table_seller_single.iloc[0][self.column_1_Parcela_Referencia])
        # 1ª inf da coluna 'Dt pag. por' -> ATA ou DIA DA SEMANA
        dt_pag_por = str(self.table_seller_single.iloc[0][self.column_Data_Pag_Por])

        #   'DIA DA SEMANA'
        if self.word_DIA_DA_SEMANA == dt_pag_por:
            #                  Xº/MES/ANO
            self.data_single = self.date_sma_single
        else:
            #                  MES/ANO
            self.data_single = self.date_ata_single
        if self.word_CADASTRO in p1_referencia and self.word_DIA_DA_SEMANA == dt_pag_por:
            self.column_ata_sma = self.column_Sma_Cad_Adm
            #            '[Sma Cad Adm', 'Sma 2º Parc', ..., 'Sma 6º Parc']
            self.list_cols_full_ata_sing_pag = self.list_columns_full_sma_cadastro_pag
            self.list_cols_full_ata_sing_venc = self.list_columns_full_sma_cadastro_venc
            list_columns_ATA_Mes = list_columns_Mes_Cad_Adm_Qtd_Cotas
            # list_columns_Total = list_columns_Total_Sma_Cad_Adm
        elif self.word_CADASTRO in p1_referencia and self.word_DIA_DA_SEMANA != dt_pag_por:
            self.column_ata_sma = self.column_ATA_Cad_Adm
            # ['ATA Cad Adm', 'ATA 2º Parc', 'ATA 3º P ..., 'ATA 6º Parc']
            self.list_cols_full_ata_sing_pag = self.list_columns_full_ata_cadastro_pag
            self.list_cols_full_ata_sing_venc = self.list_columns_full_ata_cadastro_venc
            list_columns_ATA_Mes = list_columns_ATA_Cad_Adm_Qtd_Cotas
            # list_columns_Total = list_columns_Total_ATA_Cad_Adm
        elif self.word_CADASTRO not in p1_referencia and self.word_DIA_DA_SEMANA == dt_pag_por:
            self.column_ata_sma = self.column_Sma_Entrega
            # '[Sma Ent', 'Sma 2º Parc', ..., 'Sma 6º Parc']
            self.list_cols_full_ata_sing_pag = self.list_columns_full_sma_entrega_pag
            self.list_cols_full_ata_sing_venc = self.list_columns_full_sma_entrega_venc
            list_columns_ATA_Mes = list_columns_Mes_Entrega_Qtd_Cotas
            # list_columns_Total = list_columns_Total_Sma_Entrega
        elif self.word_CADASTRO not in p1_referencia and self.word_DIA_DA_SEMANA != dt_pag_por:
            self.column_ata_sma = self.column_ATA_Entrega
            # ['ATA Entrega', 'ATA 2º Parc', ..., 'ATA 6º Parc']
            self.list_cols_full_ata_sing_pag = self.list_columns_full_ata_entrega_pag
            self.list_cols_full_ata_sing_venc = self.list_columns_full_ata_entrega_venc
            list_columns_ATA_Mes = list_columns_ATA_Entrega_Qtd_Cotas
            # list_columns_Total = list_columns_Total_ATA_Entrega
        if self.word_profissao == word_Gerencia:
            # ATA XX qtd cotas Ger Ger
            self.list_columns_ATA_Mes = list_columns_ATA_Mes[2]
            # 'Total XX Ger Ger'
            self.list_columns_Total = list_columns_Total[2]
        elif self.word_profissao == word_Supervisor:
            # ATA XX qtd cotas Ger
            self.list_columns_ATA_Mes = list_columns_ATA_Mes[1]
            # 'Total XX Ger'
            self.list_columns_Total = list_columns_Total[1]
        else:
            # ATA XX qtd cotas
            self.list_columns_ATA_Mes = list_columns_ATA_Mes[0]
            # 'Total XX'
            self.list_columns_Total = list_columns_Total[0]

    # 3º Criar uma lista tabelas aparti do dado ATA ou SMA
    def tables_columns_ata_seller_single(self):
        self.list_tables_ata = []
        # ['ATA Entrega', 'ATA 2º Parc', ..., 'ATA 6º Parc']
        for key, column_ata in enumerate(self.list_cols_full_ata_sing_pag):
            # MES/ANO ou Xº/MES/ANO
            table_pag = self.table_seller_single[self.table_seller_single[column_ata] == self.data_single].copy()  # noqa
            table_pag.reset_index(drop=True, inplace=True)
            # #                ATA Entrega, Sma Ent, ATA cad Adm, Sma Cad Adm
            # if column_ata == self.column_ata_sma:
            #     column_ata_venc = column_ata
            # else:
            #     column_ata_venc = column_ata + ' Venc'
            column_ata_venc = self.list_cols_full_ata_sing_venc[key]
            table_venc = self.table_seller_single[self.table_seller_single[column_ata_venc] == self.data_single].copy()  # noqa
            table_venc.reset_index(drop=True, inplace=True)
            # table não é fazia?
            if not table_pag.empty:
                self.list_tables_ata.append([table_pag, table_venc, column_ata])
        # informações unicas para o pdf      MES/ANO
        self.list_unique_information.append(self.data_single)
        # for table_pag, table_venc, column_ata in self.list_tables_ata:
        #     if not table_pag.empty:
        #         print(f'ATA => {column_ata}')
        #         print(table_pag)
        #         print(table_venc)
        #         print('')
        #         print('')

    # 4º situações para sair e ir para o próximo vendedor

    def is_to_stop_program(self):
        self.tables_concat_seller_single()
        self.stop_program = False
        # se junção de tabela estiver vazio sair
        if self.table_single_merge.empty:
            self.stop_program = True
            return
        cargo = self.table_single_merge.iloc[0][self.column_Cargo]
        # se for o cargo especifico sair
        #                            ['ESTAGIÁRIO', 'ZERADO']
        for cargo_not_calc_commis in self.list_cargo_not_calc_commis:
            if cargo_not_calc_commis in cargo:
                self.stop_program = True

    # 5º Ira criar a soma de todos as vendas aparti da ATA especifica ira detarminar os 50%
    def table_list_administradora_line_add_sum(self):
        # OBS: infelizmente o comando self.sums =
        # table[self.column_Credito].sum(), nao funciona
        self.list_tables_ata_sums = []
        for (table_pag, table_venc, ata) in self.list_tables_ata:
            sums_compliance = 0
            value = 0
            dividend = 'venc'  # pag
            sums_all = 0
            divisor = 'venc'  # pag
            if self.word_profissao == word_Parceiro:
                dividend = 'pag'
                divisor = 'pag'

            if divisor == 'venc':
                table_choose = table_venc
            elif divisor == 'pag':
                table_choose = table_pag
            quantity_line_table = table_choose.shape[0]
            for line in range(quantity_line_table):
                value = table_choose.iloc[line][self.column_Credito]
                value = self.convert_str_float(value)
                sums_all += value

            # quantity_line_table = table_pag.shape[0]
            # for line in range(quantity_line_table):
            #     value = table_pag.iloc[line][self.column_Credito]
            #     value = self.convert_str_float(value)
            #     sums_all += value

            if dividend == 'venc':
                table_choose = table_venc
            elif dividend == 'pag':
                table_choose = table_pag

            # é primeira parcela? ATA ou Sma Entrega ou ATA ou Sma Cad Adm
            if ata in self.column_ata_sma:
                sums_compliance = sums_all
            elif dividend == 'venc':
                column = ata
                column = column.replace(word_ATA_, '').replace(word_Sma_, '')
                column = column.replace(word_Pag_, '').replace(word_Venc_, '')
                column_situacao = 'Situação ' + column
                quantity_line_table = table_choose.shape[0]
                for line in range(quantity_line_table):
                    situacao = table_choose.iloc[line][column_situacao]
                    #             'NORMAL', 'PAGA'
                    if situacao in self.list_situacao_to_comission:
                        value = table_choose.iloc[line][self.column_Credito]
                        value = self.convert_str_float(value)
                        sums_compliance += value
            # elif dividend == 'pag':
            #     quantity_line_table = table_pag.shape[0]
            #     for line in range(quantity_line_table):
            #         value = table_pag.iloc[line][self.column_Credito]
            #         value = self.convert_str_float(value)
            #         sums_compliance += value

            self.list_tables_ata_sums.append([
                table_pag,
                table_venc,
                ata,
                sums_all,
                sums_compliance
            ])
        # for (table,
        #      ata,
        #      sums,
        #      sums_compliance,
        #      list_admnimistradora_line
        #      ) in self.list_tables_ata_sums:
        #     print('table_list_administradora_line_add_sum')
        #     print(f'ata -> {ata}')
        #     print(f'sums -> {sums}')
        #     print(f'Soma do confirmados -> {sums_compliance}')
        #     print(f'list_admnimistradora_line ->{list_admnimistradora_line}')
        #     print(f'table {table}')
        #     print('')
        #     print('')

    # 6º adiciona sum_comissao, sum_comissao_compliance, percentage_compliance,
    # vendedor, cargo
    def add_column_Comissao(self):
        sum_all_comissao = 0
        sum_all_comissao_gerente = 0
        percentage_compliance = ''
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        for (
            table_pag,
            table_venc,
            ata,
            sums_all,
            sums_compliance
        ) in self.list_tables_ata_sums:
            # nova tabela que esta sendo criada para o pdf
            table_pag[self.column_Porcentagem] = '0'
            vendedor = table_pag.iloc[0][self.column_profissao]
            cargo = table_pag.iloc[0][self.column_Cargo]
            sum_comissao = 0
            sum_comissao_compliance = 0
            text = ata
            text = rename_ata(text, 'mod1')
            #                       'Situação'
            column_situacao_parc = self.column_Situacao
            if text != '1':
                column_situacao_parc += ' ' + text + 'º Parc'
            if self.word_profissao == word_Supervisor:
                text += ' ' + self.word_Supervisor
            elif self.word_profissao == word_Gerencia:
                text += ' ' + self.word_Gerencia
            quantity_line_table = table_pag.shape[0]
            for line in range(quantity_line_table):
                text2 = table_pag.iloc[line][self.list_columns_ATA_Mes]
                # cliente = table_pag.iloc[line]['Cliente']
                # if cliente == 'LIZANDRA MAXIMO DE OLIVEIRA':
                #     pass
                # se for igua a 0 não atigiu o minimo nao existe comissão
                minimum = True
                if text2 != '0':
                    name_column = text2 + ' Parc ' + text
                    data_percentual = table_pag.iloc[line][name_column]
                    if pd.isnull(data_percentual):
                        data_percentual = 0
                else:
                    data_percentual = 0
                    if ata == self.column_ata_sma:
                        minimum = False
                try:
                    data_percentual = float(data_percentual)
                except ValueError:
                    data_percentual = convert_str_float(data_percentual)
                    data_percentual = float(data_percentual)
                text_perc = str(data_percentual) + ' %'
                table_pag.loc[line, self.column_Porcentagem] = text_perc
                # data_percentual = data_percentual / 100
                if minimum:
                    data_percentual = data_percentual / 100
                else:
                    data_percentual = 0.0000001
                # [word_Entrega, 'Cad Adm', word_Parc, 'FAT']
                entrega = self.list_condition_ata[0]
                cad_adm = self.list_condition_ata[1]
                parc = self.list_condition_ata[2]
                fat = self.list_condition_ata[3]
                if entrega in ata or cad_adm in ata:
                    data_recebera = (
                        table_pag.iloc[line][self.column_1_Parcela_Recebera])
                elif parc in ata:
                    data_recebera = (
                        table_pag.iloc[line][self.column_Demais_Recebera])
                elif fat in ata:
                    data_recebera = (
                        table_pag.iloc[line][self.column_FAT_Recebera])
                data_situacao = table_pag.iloc[line][column_situacao_parc]
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
                            table_pag.iloc[line][self.column_1_Parcela_Recebera])
                # list_recebera_to_comission = ['SIM']
                list_recebera = self.list_recebera_to_comission
                if data_recebera in list_recebera:
                    calculate_commission = True
                else:
                    calculate_commission = False
                if calculate_commission:
                    value = table_pag.iloc[line][self.column_Credito]
                    value = self.convert_str_float(value)
                    comissao = value * data_percentual
                    sum_comissao += comissao
                else:
                    comissao = 0
                comissao = locale.format_string(
                    "%.2f", comissao, grouping=True)
                table_pag.loc[line, self.column_Comissao] = comissao
            if sums_all != 0:
                if (sums_compliance / sums_all) >= 0.5:
                    sum_comissao_compliance = sum_comissao
                    sum_all_comissao += sum_comissao
                sum_all_comissao_gerente += sum_comissao
                percentage_compliance = str(
                    round(((sums_compliance / sums_all) * 100), 1)
                ) + '%'
            self.list_table_column_comissao.append([
                table_pag,
                table_venc,
                ata,
                sums_all,
                sums_compliance,
                sum_comissao,
                sum_comissao_compliance,
                percentage_compliance,
                vendedor,
                cargo
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
        #     print(f'sums_compliance ->{sums_compliance}')
        #     print(f'sum_comissao_compliance -> {sum_comissao_compliance}')
        #     print(f'table: {table}')
        #     print('')
        #     print('')

    # 7º deixar apenas valores validos nas tabelas, ou seja,
    # valores que forma pagos e estao ativos
    def edit_table(self):
        self.list_table_edit = []
        table_full: pd.DataFrame = pd.DataFrame()
        for (table_pag,
             table_venc,
             ata,
             sums_all,
             sums_compliance,
             sum_comissao,
             sum_comissao_compliance,
             percentage_compliance,
             vendedor,
             cargo
             ) in self.list_table_column_comissao:
            # excluir comissão zerada
            table_pag = table_pag[table_pag[self.column_Comissao] != '0,00'].copy()
            table_pag.reset_index(drop=True, inplace=True)
            # colocar coluna Parcela
            text = ata
            text = rename_ata(text, 'mod2')
            # text = text.replace('ATA', '').replace('Sma', '').replace('º Parc', 'ª')
            # text = text.replace(word_Entrega, '1ª').replace('Cad Adm', '1ª')
            table_pag[self.column_Parcela] = text
            table_pag[self.column_Adimplencia] = percentage_compliance
            # adicionar coluna comissão
            text = text.replace('ª', '')
            if table_full.empty:
                table_full = table_pag
            else:
                table_full = pd.concat([table_full, table_pag], ignore_index=True)
            # excluir linhas comissão zerada
            table_full.reset_index(drop=True, inplace=True)
            table_pag = table_pag[self.list_columns_end]
            self.list_table_edit.append([
                table_pag,
                table_venc,
                ata,
                sums_all,
                sums_compliance,
                sum_comissao,
                sum_comissao_compliance,
                percentage_compliance,
                vendedor,
                cargo
            ])
        table_full = table_full[self.list_columns_end]
        self.list_unique_information.append(table_full)
        # for (table_pag,
        #         table_venc,
        #         ata,
        #         sums_all,
        #         sums_compliance,
        #         sum_comissao,
        #         sum_comissao_compliance,
        #         percentage_compliance,
        #         vendedor,
        #         cargo
        #      ) in self.list_table_edit:
        #     print(f'ATA -> {ata}')
        #     print(f'soma do credito -> {sums_all}')
        #     print(f'soma do comissao -> {sum_comissao}')
        #     print(f'Vendedor -> {vendedor}')
        #     print(f'cargo -> {cargo}')
        #     print(f'percentage_compliance -> {percentage_compliance}')
        #     text = 'list_administradora_qtdcotas_parc ->'
        #     print(f'sums_compliance ->{sums_compliance}')
        #     print(f'sum_comissao_compliance -> {sum_comissao_compliance}')
        #     print(f'table: {table_pag}')
        #     print('')
        #     print('')

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
        # ata2 = self.list_unique_information[0]
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
        image_path = resource_path('img/select.jpg')
        pdf.add_image(image_path, 172, 10, 28, 9)
        if self.list_table_edit == []:
            return '0', 'zerado'
        if self.word_profissao == word_Supervisor or self.word_profissao == word_Gerencia:
            comissao = sum_all_comissao_gerente
        else:
            comissao = sum_all_comissao
        if comissao == 0:
            return '0', 'zerado'
        for (
            table_pag,
            table_venc,
            ata,
            sums_all,
            sums_compliance,
            sum_comissao,
            sum_comissao_compliance,
            percentage_compliance,
            vendedor,
            cargo
        ) in self.list_table_edit:
            if begin is True:
                pdf.set_font('Arial', '', size_font)
                comissao = locale.currency(
                    comissao,
                    grouping=True
                )
                # Guarda a posição inicial do texto
                if self.word_profissao == word_Parceiro:
                    text = 'PARCEIRO:'
                    text2 = f'Semana: {self.date_sma_single}'
                else:
                    text = 'FUNCIONÁRIO:'
                    text2 = f'ATA: {self.date_ata_single}'
                text1 = f'{vendedor}'
                text3 = f'{cargo}'
                pdf.add_underlined_text(text, size_font, size_line)
                pdf.add_content_in_columns([text1, text2], 2, size_font, size_line)
                pdf.add_content_in_columns([text3, comissao], 2, size_font, size_line)
                pdf.ln(space_paragraph * 2)
                begin = False
            # Adiciona texto ao PDF
            pdf.set_font('Arial', '', size_font2)
            sums_all = locale.currency(sums_all, grouping=True)
            sums_compliance = locale.currency(sums_compliance, grouping=True)
            sum_comissao = locale.currency(sum_comissao, grouping=True)
            sum_comissao_compliance = locale.currency(
                sum_comissao_compliance, grouping=True)
            if not (table_pag.empty):
                list_ata_sum_comissao_credito.append(
                    [ata,
                     sums_all,
                     sums_compliance,
                     sum_comissao,
                     sum_comissao_compliance,
                     percentage_compliance]
                )
                if self.model == '1':
                    text = ata
                    # text = text.replace('ATA', '')
                    # text = text.replace('º Parc', 'ª Parcela')
                    # text = text.replace(word_Entrega, '1ª Parcela')
                    # text = text.replace('Cad Adm', '1ª Parcela')
                    text = rename_ata(text, 'mod2')
                    pdf.add_underlined_text(text, size_font, size_line)
                    pdf.add_table(table_pag)
                    pdf.ln(space_paragraph)
                    pdf.multi_cell(0, size_line, '')
        if self.model == '2':
            pdf.add_table(table_full)
            pdf.ln(space_paragraph)
            pdf.multi_cell(0, size_line, '')
        # inicio do resumo
        text = 'RESUMO:'
        pdf.add_underlined_text(text, size_font, size_line)
        list_ata = []
        list_sum_comissao = []
        list_sums_compliance = []
        list_sum_comissao_compliance = []
        list_percentage_compliance = []
        for (
            ata,
            sums_all,
            sums_compliance,
            sum_comissao,
            sum_comissao_compliance,
            percentage_compliance
        ) in list_ata_sum_comissao_credito:
            text = ata
            text = rename_ata(text, 'mod2')
            list_ata.append(text)
            list_sums_compliance.append(sums_compliance)
            list_sum_comissao.append(sum_comissao)
            list_sum_comissao_compliance.append(sum_comissao_compliance)
            list_percentage_compliance.append(percentage_compliance)
        if self.word_profissao == word_Vendedor:
            data = {
                'TOTAL': list_ata,
                'CRÉDITO': list_sums_compliance,
                'COMISSÃO': list_sum_comissao,
                'ADIMPLÊNCIA': list_percentage_compliance,
                'COMISSÃO ADIMPLENTE': list_sum_comissao_compliance,
            }
        else:
            data = {
                'TOTAL': list_ata,
                'CRÉDITO': list_sums_compliance,
                'COMISSÃO': list_sum_comissao,
            }
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
        words_sellers = vendedor.lower().split()
        for word_seller in words_sellers:
            if len(word_seller) >= 3:
                word_seller = word_seller.capitalize()
            text_seller += " " + word_seller
        name_file = f'RP {text_word_profissao} {name_ata} {text_seller}.pdf'
        path_file = path_file.path_file_create_user(path_user="Documentos", path_origin="RECIBO", name_file=name_file)  # noqa
        # path_file = os.path.join(new_folder, name_file)
        pdf.output(path_file)
        return comissao, vendedor
