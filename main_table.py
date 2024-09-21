# flake8: noqa
# pyright: # type: ignore

import os
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from components.connect import Connect
from components.fileManip import FileManip
from components.tableManip import TableManip
from components.xpathManip import XpathManip
# from components.table_manip_value import Table_manip_value
from components.date_weekly import Date_weekly
from components.creat_table_gerencia import Creat_table_gerencia
# from PySide6.QtCore import QThread
from typing import Optional
from path_file import Path_file
# from time import ctime
import locale
from components.variables import *
import sys
# Definir a localidade para Português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


def load_table(path):
    try:
        table_loaded = pd.read_csv(path, sep=';', encoding='utf-8', dtype=str)
        # remover espaços inicio fim
        table_loaded.columns = (table_loaded.columns.str.strip())
    except pd.errors.EmptyDataError:
        table_loaded: pd.DataFrame = pd.DataFrame()
    return table_loaded


def create_table(table_created, path):
    table_created.columns = (table_created.columns.str.strip())
    table_created.to_csv(path, sep=';', index=False, header=True, decimal=',')
    # return table_created


class Main_table:
    def __init__(self, *args, **kwargs) -> None:
        # Variaveis
        self.father = kwargs.get('father')
        self.fileManip = FileManip()
        self.connect = Connect()
        self.tableManip = TableManip()
        self.path_file = Path_file()
        self.creat_table_gerencia = Creat_table_gerencia()
        self.date_weekly = Date_weekly()
        # Variaveis alternadas
        self.user = user
        self.password = password
        self.month = month
        self.new_table_Cadastro_Consorciado = new_table_Cadastro_Consorciado
        self.new_table_Cadastro_Funcionario = new_table_Cadastro_Funcionario
        self.new_table_Cadastro_Ata = new_table_Cadastro_Ata
        self.new_table_Comissoes_Configuracao = new_table_Comissoes_Configuracao
        self.new_table_Comissoes_ConfigPagamento = new_table_Comissoes_ConfigPagamento
        self.mix = mix

        self.list_list_columns_pag = list_list_columns_pag
        self.list_list_columns_venc = list_list_columns_venc
        self.list_list_columns_situacao_num_ATA = list_list_columns_situacao_num_ATA
        self.list_list_columns_num_ATA_atrasado = list_list_columns_num_ATA_atrasado
        self.list_list_columns_percentage = list_list_columns_percentage
        self.list_list_columns_ata_pag_atrasado_n_ata = list_list_columns_ata_pag_atrasado_n_ata
        self.list_list_columns_comissao_atrasada = list_list_columns_comissao_atrasada
        self.list_list_columns_order = list_list_columns_order
        self.list_columns_start = list_columns_start.copy()
        self.salve_first = salve_first
        self.start = start

        self.driver: Optional[webdriver.Chrome] = None
        self.table_Cadastro_Consorciado = table_Cadastro_Consorciado
        self.table_Cadastro_Funcionario = table_Cadastro_Funcionario
        self.table_Cadastro_Ata = table_Cadastro_Ata
        self.table_Comissoes_Configuracao = table_Comissoes_Configuracao
        self.table_Comissoes_ConfigPagamento = table_Comissoes_ConfigPagamento
        self.table_Gerencia = table_Gerencia
        self.table_date_weekly = table_date_weekly
        self.table_Cadastro_funcionario_supervisor = table_Cadastro_funcionario_supervisor
        self.table_Comissoes_Configuracao_supervisor = table_Comissoes_Configuracao_supervisor
        self.table_full = table_full
        self.table_duplicate = table_duplicate
        self.list_list_column_orden_total = list_list_column_orden_total

    def openSite(self):
        ''' defined '''
        text_te = f'Abrindo site: {siteSircon}'
        self.father.prog1(text_te)
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.connect = Connect(driver=self.driver)
        self.connect.month = self.month
        self.connect.user = self.user
        self.connect.password = self.password
        xpathManip = XpathManip(driver=self.driver)
        self.driver.get(siteSircon)
        # logar
        count = 0
        while True:
            self.connect.logarSircon = listXpathLog
            xpathManip.locate = listXpathComissoesConfiguracao[0]
            xpathOk = xpathManip.locate
            if xpathOk is True:
                return True
            count += 1
            if count >= 3:
                self.new_table_Cadastro_Consorciado = False
                self.new_table_Cadastro_Funcionario = False
                self.new_table_Cadastro_Ata = False
                self.new_table_Comissoes_Configuracao = False
                self.new_table_Comissoes_ConfigPagamento = False
                return False

    def mesclar_tables(self):
        text = 'Unir todas Tabelas: '
        if self.mix is False:
            text += 'Não'
            self.table_full = load_table(self.arqtableMerge)
        else:
            text += 'Sim'
        self.father.prog1(text)

    def create_list_columns_total(self):
        self.tableManip.create_columns_total()
        self.list_list_column_orden_total = self.tableManip.list_list_column_orden_total

    def limited_search_administradoras(self):
        self.connect.valueExistAdministradora = self.table_Cadastro_Consorciado

    def limited_search_cargos(self):
        self.connect.valueExistCargos = self.table_Cadastro_Funcionario

    def log_start_end(self):
        if self.start:
            # self.new_table_Cadastro_Consorciado = False
            # self.new_table_Cadastro_Funcionario = False
            # self.new_table_Cadastro_Ata = False
            # self.new_table_Comissoes_Configuracao = False
            # self.new_table_Comissoes_ConfigPagamento = False
            # self.mix = False
            self.mesclar_tables()
            self.create_list_columns_total()
            # self.tableManip.printVariaveis()
            text = '\n' + 'Inicio: '
            self.start = False

        else:
            text = 'Fim:    '
        text += str(datetime.now())
        self.fileManip.writeLog = text

    def create_table_Cadastro_Consorciado(self):
        '''table_Cadastro_Consorciado'''
        text_lc = 'cadastro de consorciado'
        if self.new_table_Cadastro_Consorciado:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            connected = self.openSite()
            if connected is False:
                return
            self.connect.file = arqDonwloadSales
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.connect.sales = listXpathSales
            self.connect.create_primary_key = column_primary_key
            self.table_Cadastro_Consorciado = self.connect.dfNew
            if self.driver:
                self.driver.quit()
                self.driver = None
            create_table(self.table_Cadastro_Consorciado, arqTableCadastroConsorciado)
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Cadastro_Consorciado = load_table(arqTableCadastroConsorciado)

    def create_table_Cadastro_Funcionario(self):
        '''table_Cadastro_Funcionario '''
        text_lc = 'cadastro de funcionário'
        if self.new_table_Cadastro_Funcionario:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            connected = self.openSite()
            if connected is False:
                return
            self.connect.file = arqDonwloadFunction
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.connect.function = listXpathFunction
            self.table_Cadastro_Funcionario = self.connect.dfNew
            if self.driver:
                self.driver.quit()
                self.driver = None
            create_table(self.table_Cadastro_Funcionario, arqTableCadastroFuncionario)
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Cadastro_Funcionario = load_table(arqTableCadastroFuncionario)

    def create_table_Cadastro_Ata(self):
        '''#################### LIMITAR PESQUISAS ##########################'''
        text_lc = 'cadastro de ATA'
        if self.new_table_Cadastro_Ata is True:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            connected = self.openSite()
            if connected is False:
                return
            self.connect.month = self.month + 12
            self.connect.tagSon = tag_data
            self.connect.tagFather = tag_row
            self.connect.tagGet = tag_outerHTML
            self.connect.tagReturnValue
            self.limited_search_administradoras()
            self.limited_search_cargos()
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.connect.minutes = listXpathMinutes
            self.table_Cadastro_Ata = self.connect.table
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.tableManip.table = self.table_Cadastro_Ata
            list_columns_rename = [
                [1, word_Mes_],
                [2, column_Periodo_inicial],
                [3, column_Periodo_final]]
            for column_rename in list_columns_rename:
                self.tableManip.rename_name_column_indix = column_rename
            self.tableManip.add_column_clone_two_columns = [
                column_ATA, word_Mes_, word_Ano]
            self.table_Cadastro_Ata = self.tableManip.table
            create_table(self.table_Cadastro_Ata, arqTableCadastroAta)  # noqa
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Cadastro_Ata = load_table(arqTableCadastroAta)

    def create_table_Comissoes_Configuracao(self):
        '''table_Comissoes_Configuracao'''
        text_lc = 'comissões configuração'
        if self.new_table_Comissoes_Configuracao:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            connected = self.openSite()
            if connected is False:
                return
            self.connect.pressListXpath = listXpathComissoesConfiguracao
            self.connect.pressListXpath = xpathTipoComissao
            self.connect.tagSon = tag_option
            self.connect.tagFather = tag_select
            self.connect.tagGet = tag_outerHTML
            self.connect.tagReturnValue
            # criar lista de administradoras
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.limited_search_administradoras()
            self.connect.pressXpathResultListValue = xpathAdministradora
            # criar lista de administradoras + tabela de recebiemnto
            self.connect.pressListValueXpathResultListValue = xpathTabelaRecebimento
            # criar lista de administradoras + tabela de recebiemnto + cargos
            self.limited_search_cargos()
            self.connect.pressListValueXpathResultListValueDouble = xpathCargo
            # alterar a tagets
            self.connect.tagGet = tag_value
            self.connect.tagReturnValue
            # lista administradoras, tabela de recebiemnto, cargos, valores
            self.connect.pressListValueResultListValueTriple = listCampoCotaPeriodoParcela
            # adicionar 'None' para todos terem o mesmo quantidade de elementos
            # e tambem o ultimo elemento adiciona uma coluna 'None'
            self.connect.addNone
            # adiciona o index
            self.connect.addIndex
            # substitu o ultimo elemento 'None' por 'endValue'
            self.connect.addEnd
            # substitu  da ulitmo coluna da 'endValue' por 'endValueLast'
            self.connect.lineToColumn
            # substitu todos no 'None' por ''
            self.connect.noneToEmpty
            # excluir se tudo for ''
            self.connect.killAllEmpty
            table = self.connect.listColunmToTable

            self.table_Comissoes_Configuracao = self.connect.renameColumn
            if self.driver:
                self.driver.quit()
                self.driver = None
            create_table(self.table_Comissoes_Configuracao, arqTableComissoesConfiguracao)  # noqa
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Comissoes_Configuracao = load_table(arqTableComissoesConfiguracao)

    def create_table_Comissoes_ConfigPagamento(self):
        '''table_Comissoes_ConfigPagamento'''
        text_lc = 'comissões configuração de pagamento'
        if self.new_table_Comissoes_ConfigPagamento:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            connected = self.openSite()
            if connected is False:
                return
            self.connect.tagSon = tag_option
            self.connect.tagFather = tag_select
            self.connect.tagGet = tag_outerHTML
            self.connect.tagSelected = tag_selected
            self.connect.tagReturnValue
            # caminho no site para entra local especifico pelo xpath
            self.connect.pressListXpath = listXpathComissoesConfPagamento
            self.connect.pressListXpath = xpathTipoComissaoPagamento
            # list os valores existentes no campos cargos, administradora, tipoPagamento
            self.limited_search_administradoras()
            self.limited_search_cargos()
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.connect.pressListXpathReturnListValue = listXpathCargAdminsPag
            self.connect.pressListValueReturnListValue = listXpathDtPagamentoParcelas
            self.connect.organizeListLine = headerDtPagamentoParcelas
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.table_Comissoes_ConfigPagamento = self.connect.listLineToTable
            create_table(self.table_Comissoes_ConfigPagamento, arqTableComissoesConfigPag)
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Comissoes_ConfigPagamento = load_table(arqTableComissoesConfigPag)

    def create_table_gerencia(self):
        if self.mix is False:
            return
        text_lc = 'comissões Gerente'
        text_te = 'Início da criação da tabela de ' + text_lc + ':'
        self.father.prog1(text_te)

        self.creat_table_gerencia.start_creat()
        self.table_Gerencia = self.creat_table_gerencia.table
        create_table(self.table_Gerencia, arqTableGerencia)

    def create_date_weekly_new(self):
        '''tabela numero da semana no mes'''
        text_te = 'Início da criação da tabela de Atas semanais exclusivamente'
        text_te += ' com base nas datas.'
        self.father.prog1(text_te)
        if self.mix is False:
            return
        self.date_weekly.year_weeklys = self.month + 12
        self.date_weekly.create_weekYear_week_date = None
        self.date_weekly.edit_weekYear_week_date_separate_week = None
        self.date_weekly.edit_weekYear_week_date_separate_weekMonth = None
        self.date_weekly.edit_weekMonth_week_date = None
        self.date_weekly.create_table_weekMonth_week_date = list_columns_date_weekly_new

        self.table_date_weekly = self.date_weekly.return_table

    def merge_table_Cadastro_Ata_table_date_weekly(self):
        if self.mix is False:
            return
        self.tableManip.table = self.table_date_weekly
        self.tableManip.merge_table_ata_table_weekly = self.table_Cadastro_Ata
        self.table_date_weekly = self.tableManip.table
        create_table(self.table_date_weekly, arqTableDatasSemanais)

    def table_manip_funcionario(self):
        ''' manipular table_Cadastro_Funcionario, para alterar os Nomes
        duplicados com os Cargos, que gera comissão duplicada, pois o mesmo
        tem dois ou mais cargos'''
        text_te = 'Manipular a tabela de cadastro de funcionários para '
        text_te += 'duplicação de cargos.'
        self.father.prog1(text_te)
        if self.table_Cadastro_Funcionario.empty or connected is False or self.mix is False:
            return
        self.tableManip.table = self.table_Cadastro_Funcionario
        self.tableManip.row_duplicate_column = [column_Nome]
        self.tableManip.list_columns_one_two = [column_Nome, column_Cargo]
        self.tableManip.edit_data_column_2 = [column_Nome, column_Cargo]
        self.table_Cadastro_Funcionario = self.tableManip.table
        self.table_Cadastro_funcionario_supervisor = self.table_Cadastro_Funcionario.copy()

        self.tableManip.table = self.table_Cadastro_Funcionario
        self.tableManip.rename_list_name_column(self.table_Cadastro_Funcionario.columns, word_Vendedor)  # noqa
        self.table_Cadastro_Funcionario = self.tableManip.table

    def table_manip_cadastro_consorciado(self):
        ''' manipular table_Cadastro_Consorciado, para altera coluna Vendedor
        e igualar aos alterados no table_Cadastro_Funcionario'''
        text_te = 'Manipular a tabela de cadastro de consorciado para alterar '
        text_te += 'coluna igual a funcionário.'
        self.father.prog1(text_te)
        if self.table_Cadastro_Consorciado.empty or connected is False or self.mix is False:
            return
        self.tableManip.table = self.table_Cadastro_Consorciado

        # renomear colunas
        for column in list_columns_cliente:
            new_column = column + ' ' + word_Cliente
            self.tableManip.rename_name_column = [column, new_column]
        self.tableManip.rename_name_column = [column_Gerente, column_Supervisor]

        self.tableManip.data_duplicate_change = column_Vendedor
        self.table_Cadastro_Consorciado = self.tableManip.table

    def table_manip_comissoes_configuracao(self):
        ''' manipular table_Comissoes_Configuracao remover as duplicação nas
        colunas self.column_Administradora e self.column_Cargo '''
        text_te = 'Manipular a tabela de comissões configuração de pagamento '
        text_te += 'para remover duplicação colunas admin. cargo.'
        self.father.prog1(text_te)
        if self.table_Comissoes_Configuracao.empty or connected is False or self.mix is False:
            return
        cols_comConf_rept = [column_Administradora, column_Cargo, column_Tabela_de_recebimento]  # noqa
        self.tableManip.table = self.table_Comissoes_Configuracao
        self.tableManip.row_duplicate_column = cols_comConf_rept
        self.tableManip.list_columns_one_two_three = cols_comConf_rept
        self.tableManip.edit_data_column_3 = cols_comConf_rept
        self.tableManip.del_column = column_Index
        self.table_Comissoes_Configuracao = self.tableManip.table
        self.table_Comissoes_Configuracao.rename(
            columns={column_Tabela_de_recebimento: column_Tabela}, inplace=True)

    def table_manip_Cadastro_funcionario_supervisor(self):
        text_te = 'Manipular a tabela de cadastro de funcionario'
        text_te += 'para adicionar colunas para cargo supervisor(gerente).'
        self.father.prog1(text_te)
        if self.table_Cadastro_funcionario_supervisor.empty or connected is False or self.mix is False:
            return
        self.tableManip.table = self.table_Cadastro_funcionario_supervisor
        self.tableManip.rename_list_name_column(self.table_Cadastro_funcionario_supervisor.columns, word_Supervisor)  # noqa
        self.table_Cadastro_funcionario_supervisor = self.tableManip.table

    def table_manip_comissoes_configuracao_supervisor(self):
        text_te = 'Manipular a tabela de comissões configuração para  '
        text_te += 'adicionar colunas do cargo supervisor(gerente).'
        self.father.prog1(text_te)
        if self.table_Comissoes_Configuracao.empty or connected is False or self.mix is False:
            return
        self.table_Comissoes_Configuracao_supervisor = self.table_Comissoes_Configuracao
        self.tableManip.table = self.table_Comissoes_Configuracao_supervisor
        self.tableManip.rename_list_name_column(self.table_Comissoes_Configuracao_supervisor.columns, word_Supervisor)  # noqa
        self.table_Comissoes_Configuracao_supervisor = self.tableManip.table
        create_table(self.table_Comissoes_Configuracao_supervisor, arqTableComissoesConfigPagSupervisor)  # noqa

    def merge_star(self):
        text_cd = 'Sim'
        if (
            self.new_table_Cadastro_Consorciado
            or self.new_table_Cadastro_Funcionario
            or self.new_table_Cadastro_Ata
            or self.new_table_Comissoes_Configuracao
            or self.new_table_Comissoes_ConfigPagamento
        ):
            self.mix = True
        if connected is False:
            self.mix = False
            text_cd = 'Não'
        text_te = 'Foi solicitado fazer a mesclagem entre tabelas: '
        text_te += text_cd
        self.father.prog1(text_te)

    def merge_consorciado_funcionario(self):
        text_te = 'Mesclar a tebela de cadastro de consorciado com a '
        text_te += 'tabela de cadastro de funcionário.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_Cadastro_Consorciado.empty or (self.table_Cadastro_Funcionario.empty):  # noqa
            return
        self.table_full = pd.merge(
            self.table_Cadastro_Consorciado,
            self.table_Cadastro_Funcionario,
            left_on=column_Vendedor,
            right_on=column_Nome_Vendedor,
            how='left'
        )

    def merge_consorciado_funcionario_supervisor(self):
        text_te = 'Mesclar a tebela já unida anteriomente coma a '
        text_te += 'tabela de cadastro de funcionário de gerente.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty or (self.table_Cadastro_funcionario_supervisor.empty):  # noqa
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Cadastro_funcionario_supervisor,
            left_on=column_Supervisor,
            right_on=column_Nome_Supervisor,
            how='left'
        )

    def merge_full_comissoes_configuracao(self):
        text_te = 'Mesclar a tebela já unida anteriomente coma a '
        text_te += 'tabela de cadastro de funcionário.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty or (self.table_Comissoes_Configuracao.empty):
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Comissoes_Configuracao,
            on=[column_Administradora, column_Cargo, column_Tabela],
            how='left')

    def merge_full_comissoes_configuracao_Supervisor(self):
        text_te = 'Mesclar a tebela já unida anteriomente coma a '
        text_te += 'tabela de comissões configuração de gerente.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty or self.table_Comissoes_Configuracao_supervisor.empty:  # noqa
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Comissoes_Configuracao_supervisor,
            left_on=[column_Administradora, column_Cargo_Supervisor, column_Tabela],
            right_on=[column_Administradora_Supervisor, column_Cargo_Supervisor, column_Tabela_Supervisor],  # noqa
            how='left')

    def merge_full_comissoes_configuracao_gerencia(self):
        text_te = 'Mesclar a tebela já unida anteriomente coma a '
        text_te += 'tabela de cadastro de funcionário de gerente geral.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty or (self.table_Gerencia.empty):
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Gerencia,
            on=[column_Administradora, column_Cargo_Supervisor],
            how='left')

    def create_columns_ata(self):
        # descori a quantidade de num_atas_parc
        text_te = 'A partir da tabela mesclada criar os nomes das colunas.'
        self.father.prog1(text_te)
        i = 1
        while True:
            i += 1
            n_parc = str(i) + word_º_Parc
            column_situacao = word_Situacao_ + n_parc
            if column_situacao not in self.table_full.columns:
                break

            column_data_pag = word_Data_ + word_Pag_ + n_parc
            column_ata_pag = word_ATA_ + word_Pag_ + n_parc
            column_sma_pag = word_Sma_ + word_Pag_ + n_parc
            column_mes_pag = word_Mes_ + word_Pag_ + n_parc
            column_data_venc = word_Data_ + word_Venc_ + n_parc
            column_ata_venc = word_ATA_ + word_Venc_ + n_parc
            column_sma_venc = word_Sma_ + word_Venc_ + n_parc
            column_mes_venc = word_Mes_ + word_Venc_ + n_parc
            column_situacao_ata = word_Situacao_ + word_ATA_ + n_parc
            column_num_ata_nparc = word_Num_ + word_ATA_ + n_parc
            column_1_porc_ata = word_1_Porc_ + word_ATA_ + n_parc
            column_2_porc_ata = word_2_Porc_ + word_ATA_ + n_parc
            column_3_porc_ata = word_3_Porc_ + word_ATA_ + n_parc
            column_num_ata_nparc_atrasado = word_Num_ + word_ATA_ + n_parc + word__Atrasado
            column_ata_pag_atrasado_1_ata = column_ata_pag + word__Atrasado_1_ATA
            column_ata_pag_atrasado_2_atas = column_ata_pag + word__Atrasado_2_ATAs
            column_comissao_atrasada = word_Pagar_Comissao_ + n_parc

            self.list_list_columns_pag.append([
                column_situacao,
                column_data_pag,
                column_ata_pag,
                column_sma_pag,
                column_mes_pag
            ])
            self.list_list_columns_venc.append([
                column_situacao,
                column_data_venc,
                column_ata_venc,
                column_sma_venc,
                column_mes_venc
            ])
            self.list_list_columns_situacao_num_ATA.append([
                column_situacao,
                column_data_pag,
                column_data_venc,
                column_ata_pag,
                column_ata_venc,
                column_situacao_ata,
                column_num_ata_nparc
            ])
            self.list_list_columns_num_ATA_atrasado.append([
                column_num_ata_nparc,
                column_num_ata_nparc_atrasado
            ])
            self.list_list_columns_percentage.append([
                column_1_porc_ata,
                column_2_porc_ata,
                column_3_porc_ata,
                column_num_ata_nparc
            ])
            self.list_list_columns_ata_pag_atrasado_n_ata.append([
                column_ata_venc,
                column_ata_pag_atrasado_1_ata,
                column_ata_pag_atrasado_2_atas
            ])
            self.list_list_columns_comissao_atrasada.append([
                column_comissao_atrasada,
                column_1_porc_ata,
                column_2_porc_ata,
                column_3_porc_ata
            ])
            self.list_list_columns_order.append([
                column_situacao,
                column_situacao_ata,
                column_data_pag,
                column_data_venc,
                column_num_ata_nparc,
                column_num_ata_nparc_atrasado,
                column_comissao_atrasada,
                column_ata_pag,
                column_1_porc_ata,
                column_ata_venc,
                column_2_porc_ata,
                column_ata_pag_atrasado_1_ata,
                column_3_porc_ata,
                column_ata_pag_atrasado_2_atas,
                column_mes_pag,
                column_mes_venc,
                column_sma_pag,
                column_sma_venc
            ])

    def merge_full_ata_weekly_month(self):
        text_te = 'Mesclar a tebela já unida coma a '
        text_te += 'tabela de ATAs apenas semanais(Sma).'
        self.father.prog1(text_te)
        '''# mesclar table_full com table_weekly'''
        if self.mix is False or self.table_full.empty or (self.table_date_weekly.empty):
            return
        self.tableManip.table = self.table_date_weekly.copy()
        # deixar apenas as duas colunas 'N Semanda Mes e Data semana'
        self.tableManip.del_column = column_Dia_semana
        self.tableManip.del_column = column_Mes_ano
        self.tableManip.del_column = column_ATA
        table_weekly = self.tableManip.table

        self.tableManip.table = self.table_date_weekly.copy()
        # deixar apenas as duas colunas 'Mes ano e Data semana'
        self.tableManip.del_column = column_Dia_semana
        self.tableManip.del_column = column_N_Semana_Mes
        self.tableManip.del_column = column_ATA
        table_month = self.tableManip.table

        self.tableManip.table = self.table_date_weekly.copy()
        # deixar apenas as duas colunas 'Mes ano e Data semana'
        self.tableManip.del_column = column_Dia_semana
        self.tableManip.del_column = column_N_Semana_Mes
        self.tableManip.del_column = column_Mes_ano
        table_ata = self.tableManip.table
        list_list_full = [self.list_list_columns_pag, self.list_list_columns_venc]

        for list_full in list_list_full:
            for columns_all in list_full:
                #           Data Pag. Xº Parc     ou     Data venc. Xº Parc
                column_data_full = columns_all[1]
                for name_column in columns_all:
                    if name_column == columns_all[0] or name_column == columns_all[1]:
                        continue
                    if name_column == columns_all[2]:
                        column_renomear = column_ATA
                        table_date = table_ata
                    elif name_column == columns_all[3]:
                        column_renomear = column_N_Semana_Mes
                        table_date = table_weekly
                    elif name_column == columns_all[4]:
                        column_renomear = column_Mes_ano
                        table_date = table_month
                    self.table_full = pd.merge(
                        self.table_full,
                        table_date,
                        left_on=column_data_full,
                        right_on=column_Data_Semana,
                        how='left'
                    )
                    #   Renomear coluna   column_ATA  column_N_Semana_Mes  column_Mes_ano
                    self.tableManip.table = self.table_full
                    self.tableManip.rename_name_column = [column_renomear, name_column]
                    self.tableManip.del_column = column_Data_Semana
                    self.table_full = self.tableManip.table

    def merge_full_configPagamento(self):
        text_te = 'Combinar a tabela unificada com a '
        text_te += 'tabela de Configuração de Pagamento. '
        self.father.prog1(text_te)
        ''' manipular table ATA  e colocar na table_full'''
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        # mescla os valores da tablea ConfigPagamento com table_full
        self.tableManip.add_columns_full = self.table_Comissoes_ConfigPagamento
        self.tableManip.del_column = column_Index
        self.table_full = self.tableManip.table

    def column_add(self):
        text_te = 'Adicionar as colunas de totais e cota correspondentes à '
        text_te += 'tabela agregada.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        # programa:
        self.tableManip.alter_value_line_total_sum()
        self.table_full = self.tableManip.table

    def create_column_pk_vend_ata_entrega(self):
        text_te = 'Criar coluna com chaves primaira que identifique '
        text_te += 'o vendedor e a ATA únicas.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_pk_vend_ata_entrega()
        self.table_full = self.tableManip.table

    def create_columns_ata_atrasada_adiantada_igual(self):
        text_te = 'Criar coluna de numero e situação de quantidade '
        text_te += 'de ata atrasada ou adiantada ou no prazo'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_situacao_num_ATA = self.list_list_columns_situacao_num_ATA
        self.table_full = self.tableManip.table

    def create_columns_ata_atrasadas(self):
        text_te = 'Criar coluna ATAs atrasadas '
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_num_ATA_atrasada = self.list_list_columns_num_ATA_atrasado
        self.table_full = self.tableManip.table

    def create_columns_calc_percentual(self):
        text_te = 'Criar coluna porcentagem da ATA 1º, 2º e 3º '
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_porcentagem = self.list_list_columns_percentage
        self.table_full = self.tableManip.table

    def create_columns_ata_pag_atrasado_n_ata(self):
        text_te = 'Criar coluna ATA pagamento atrasados '
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_ata_pag_atrasados = self.list_list_columns_ata_pag_atrasado_n_ata
        self.table_full = self.tableManip.table

    def create_columns_comissao_atrasada(self):
        text_te = 'Criar coluna ATA pagamento atrasados '
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_pagar_comissao = self.list_list_columns_comissao_atrasada
        self.table_full = self.tableManip.table

    def create_list_order_columns(self):
        list_columns_full = self.table_full.columns.to_list()
        list_columns_cliente = []
        list_columns_Cad_Adm = []
        list_columns_Mes = []
        list_columns_Sma = []
        list_columns_1Parcela_Demais_FAT = []
        for column_full in list_columns_full:
            if column_full in list_columns_start:
                continue
            elif word_Cliente in column_full:
                list_columns_cliente.append(column_full)
            elif word_Cad_Adm in column_full:
                list_columns_Cad_Adm.append(column_full)
            elif word_Mes in column_full:
                list_columns_Mes.append(column_full)
            elif word_Sma_ in column_full:
                list_columns_Sma.append(column_full)
            elif word_1_Parcela in column_full or word_Demais in column_full or word_FAT in column_full:
                list_columns_1Parcela_Demais_FAT.append(column_full)

        for columns_Cliente in list_columns_cliente:
            if columns_Cliente in self.list_columns_start:
                self.list_columns_start.remove(columns_Cliente)
            self.list_columns_start.append(columns_Cliente)

        for columns_Cad_Adm in list_columns_Cad_Adm:
            if columns_Cad_Adm in self.list_columns_start:
                self.list_columns_start.remove(columns_Cad_Adm)
            self.list_columns_start.append(columns_Cad_Adm)

        for columns_Mes in list_columns_Mes:
            if columns_Mes in self.list_columns_start:
                self.list_columns_start.remove(columns_Mes)
            self.list_columns_start.append(columns_Mes)

        for columns_Sma in list_columns_Sma:
            if columns_Sma in self.list_columns_start:
                self.list_columns_start.remove(columns_Sma)
            self.list_columns_start.append(columns_Sma)

        for columns_1Parcela_Demais_FAT in list_columns_1Parcela_Demais_FAT:
            if columns_1Parcela_Demais_FAT in self.list_columns_start:
                self.list_columns_start.remove(columns_1Parcela_Demais_FAT)
            self.list_columns_start.append(columns_1Parcela_Demais_FAT)

    def order_column(self):
        ''' Ordenar colunas da tabela para a forma que quiser'''
        text_te = 'Ordenar as colunas, colocando as mais importantes no início '
        self.father.prog1(text_te)
        for list_columns_ata in self.list_list_columns_order:
            for columns_ata in list_columns_ata:
                # remover coluna Mes Xº Parc
                if columns_ata not in self.list_columns_start:
                    self.list_columns_start.append(columns_ata)

        for list_column_orden_total in self.list_list_column_orden_total:
            for column_orden_total in list_column_orden_total:
                self.list_columns_start.append(column_orden_total)

        self.create_list_order_columns()
        list_columns_full = self.table_full.columns.to_list()
        list_columns_full_new = []
        for key, columnList in enumerate(list_columns_full):
            if key == 0:
                for listColumnStart in self.list_columns_start:
                    list_columns_full_new.append(listColumnStart)
            if columnList in self.list_columns_start:
                continue
            list_columns_full_new.append(columnList)
        self.table_full = self.table_full[list_columns_full_new]

    def save_full(self):
        text_te = 'Salvar uma tabela previamente consolidada e tratada.'
        self.father.prog1(text_te)
        if self.table_full.empty:
            return
        if self.salve_first:
            if self.mix:
                create_table(self.table_full, arqtableMerge)
            self.salve_first = False
        else:
            create_table(self.table_full, arqtableMergeOrder)

    def save_full_teste(self, n):
        text_te = 'Salvar uma tabela em testes'
        self.father.prog1(text_te)
        if n == 3:
            create_table(self.table_full, arqTableTeste3)
        elif n == 2:
            create_table(self.table_full, arqTableTeste2)
        else:
            create_table(self.table_full, arqTableTeste1)

    def test_full_double(self):
        text_te = 'Realizar um teste de integridade entre a tabela '
        text_te += 'consolidada e a tabela de cadastro de consorciado para '
        text_te += 'identificar discrepâncias nas vendas. '
        text_te += 'Registrar os resultados no arquivo de log (log.txt).'
        self.father.prog1(text_te)
        ''' teste para sabEr a diferença e mostra que é diferente.
        pois se existir diferença ele ira salvar no log'''
        if self.table_full.empty or self.table_Cadastro_Consorciado.empty or connected is False or self.mix is False:  # noqa
            return
        text = 'OK'
        num_line = len(self.table_full)
        nDiferente = 0
        for line_1 in range(num_line):
            line_2 = line_1 - nDiferente
            clit_1 = self.table_full.at[line_1, column_Cliente]
            clit_2 = self.table_Cadastro_Consorciado.at[line_2, column_Cliente]
            if clit_1 != clit_2:
                vend_1 = self.table_full.at[line_1, column_Vendedor]
                vend_2 = self.table_Cadastro_Consorciado.at[line_2, column_Vendedor]
                if text == 'OK':
                    text = ''
                text += f' linha:   ({line_1 + 2})  | ({line_2 + 2}).\n'
                text += f'Cliente:  ({clit_1})  | ({clit_2}) \n'
                text += f'Vendedor: ({vend_1})  | ({vend_2})\n'

                nDiferente += 1
        if text == 'OK':
            text += ': tabelaMergem full não existe duplicidades'
        else:
            text2 = f'ERRO: Foram encontraos {nDiferente} linhas difrerenças.'
            text2 += '\n table_merge | table_cadastro_consorciado'
            text2 += '\n' + text
            text = text2
        self.fileManip.writeLog = text

    def test_table_Comissoes_ConfigPagamento(self):
        ''' manipular table_comissoes_configuPagamento'''
        text_te = 'Realizar um teste na tabela de comissões para verificar '
        text_te += 'a configuração de pagamentos duplicados, que possam '
        text_te += 'resultar em vendas adicionais. '
        text_te += 'Registrar os resultados no arquivo de log (log.txt).'
        self.father.prog1(text_te)
        if self.table_Comissoes_ConfigPagamento.empty or connected is False or self.mix is False:  # noqa
            return
        self.tableManip.table = self.table_Comissoes_ConfigPagamento
        self.tableManip.edit_data_column_all = list_columns_test_table_configPag_1
        self.tableManip.row_duplicate_column = list_columns_test_table_configPag_2
        self.table_duplicate = self.tableManip.table_duplicate
        if self.table_duplicate.empty:
            text = 'OK: tabela_Comissões_ConfigPagamento não tem duplicância.'
        else:
            text = 'ERRO: tabela_Comissões_ConfigPagamento '
            text += 'Existe arquivos duplicados que podem gera vendas '
            text += 'duplicadas. Tem que ser analizada as colunas: '
            text += 'Cargo, Administradora, Tipo Pagamento'
            self.fileManip.writeLog = text
            create_table(self.table_duplicate, arqTesteDuplTableComissoesConfigPag)  # noqa
        # tratar tabela para não existir duplicancia

    def test_table_Cadastro_Funcionario(self):
        text_te = 'Realizar um teste na tabela de cadastro de funcionários '
        text_te += 'para identificar casos de homônimos com funções distintas. '
        text_te += 'Registrar os resultados no arquivo de log (log.txt).'
        self.father.prog1(text_te)
        if self.table_Cadastro_Funcionario.empty or connected is False or self.mix is False:
            return
        list_funcionario_double = self.table_Cadastro_Funcionario[column_Nome_Vendedor].tolist()  # noqa
        text = 'OK: tabela_Cadastro_Funcionario não existe duplicidades '
        text += 'nas funções'
        while True:
            n_element = len(list_funcionario_double)
            if n_element <= 1:
                break
            funcionario_double = list_funcionario_double.pop()
            if funcionario_double in list_funcionario_double:
                text = 'ERRO: tabela_Cadastro_Funcionario tem funcionario com '
                text += f'mesmo nome: ({funcionario_double}) com duas funções '
                text += 'diferentes.'
                self.fileManip.writeLog = text
                print(text)

    def test_primary_key(self):
        text_te = 'Realizar uma verificação de integridade na tabela '
        text_te += 'consolidada para evitar a duplicação de chaves primárias. '
        text_te += 'Registrar os resultados no arquivo de log (log.txt).'
        self.father.prog1(text_te)
        if (self.table_full.empty or connected is False or self.mix is False):
            return
        list_primary_key = self.table_full[column_primary_key].tolist()
        text = 'OK: tabelaMergem full não exite chave primaria duplicada. '
        while list_primary_key != []:
            primary_key = list_primary_key.pop()
            if primary_key in list_primary_key:
                text = 'ERRO: table_merge '
                text += f'Foi repetido o primary key ({primary_key}).\n'
                text += 'Isso siguinifica que tem vendas duplicados, '
                text += 'devido a mesclagem entre as tabelas. '
                self.fileManip.writeLog = text
                print(F'ALERTE main_table: {text}')
