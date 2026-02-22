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
from PySide6.QtWidgets import QApplication
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
        self.list_list_columns_ATA_Venc_n_Parc_n_ATA_Atrasada = list_list_columns_ATA_Venc_n_Parc_n_ATA_Atrasada
        self.list_list_columns_comissao_atrasada = list_list_columns_comissao_atrasada
        self.list_list_columns_PK_Vend_ATA_n_Parc = list_list_columns_PK_Vend_ATA_n_Parc
        self.list_list_order_columns = list_list_order_columns
        self.list_order_columns_start = list_order_columns_start.copy()
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
        self.list_list_order_columns_total = list_list_order_columns_total

    def openSite(self):
        # Finaliza o driver do Selenium
        # try:
        #     self.driver.quit()
        #     print("ChromeDriver finalizado com sucesso.")
        # except Exception as e:
        #     print(f"[ERRO] ao finalizar o driver: {e}")
        # # Encerra a thread com segurança
        # try:
        #     self.thread.quit()
        #     self.thread.wait()
        #     print("Thread encerrada com sucesso.")
        # except Exception as e:
        #     print(f"[ERRO] ao encerrar a thread: {e}")
        ''' defined '''
        text_te = f'Abrindo site: {siteSircon}'
        self.father.prog1(text_te)
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        try:
            chromedriver_path = ChromeDriverManager().install()
            if not chromedriver_path.endswith('chromedriver.exe'):
                chromedriver_path = os.path.join(
                    os.path.dirname(chromedriver_path), 'chromedriver.exe')

            service = Service(chromedriver_path)
            # print(f'chromedriver_path: {chromedriver_path}')
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.maximize_window()
        except Exception as e:
            print(f"Ocorreu um erro ao iniciar o ChromeDriver: {e}")

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
            self.table_full = load_table(arqTableMerge)
        else:
            text += 'Sim'
        self.father.prog1(text)

    def create_list_columns_total(self):
        self.tableManip.create_columns_total()
        self.list_list_order_columns_total = self.tableManip.list_list_order_columns_total

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
                [2, column_Periodo_Inicial],
                [3, column_Periodo_Final]]
            for column_rename in list_columns_rename:
                self.tableManip.rename_name_column_indix = column_rename
            self.tableManip.add_column_clone_two_columns = [column_ATA, word_Mes_, word_Ano]  # noqa
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
        create_table(self.table_date_weekly, arqTableDatasSemanaisInicial)

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
        self.table_Comissoes_Configuracao.rename(columns={column_Tabela_de_recebimento: column_Tabela}, inplace=True)  # noqa

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
            n_Parc = str(i) + word_º_Parc
            column_Situacao_n_Parc = word_Situacao_ + n_Parc
            if column_Situacao_n_Parc not in self.table_full.columns:
                break

            column_Data_Pag_n_Parc = word_Data_ + word_Pag_ + n_Parc
            column_ATA_Pag_n_Parc = word_ATA_ + word_Pag_ + n_Parc
            column_Sma_Pag_n_Parc = word_Sma_ + word_Pag_ + n_Parc
            column_Mes_Pag_n_Parc = word_Mes_ + word_Pag_ + n_Parc
            column_Data_Venc_n_Parc = word_Data_ + word_Venc_ + n_Parc
            column_ATA_Venc_n_Parc = word_ATA_ + word_Venc_ + n_Parc
            column_Sma_Venc_n_Parc = word_Sma_ + word_Venc_ + n_Parc
            column_Mes_Venc_n_Parc = word_Mes_ + word_Venc_ + n_Parc
            column_Situacao_ATA_n_Parc = word_Situacao_ + word_ATA_ + n_Parc
            column_Num_ATA_n_Parc = word_Num_ + word_ATA_ + n_Parc
            column_Num_ATA_n_Parc_Atrasado = word_Num_ + word_ATA_ + n_Parc + word__Atrasada
            column_porc_ATA_Pag = word_porc_ + column_ATA_Pag_n_Parc
            column_porc_ATA_Pag_n_Parc_1_ATA_Atrasada = word_porc_ + column_ATA_Pag_n_Parc + word__1_ATA_Atrasada
            column_porc_ATA_Pag_n_Parc_2_ATA_Atrasada = word_porc_ + column_ATA_Pag_n_Parc + word__2_ATA_Atrasada
            column_ATA_Venc_n_Parc_1_ATA_Atrasada = column_ATA_Venc_n_Parc + word__1_ATA_Atrasada
            column_ATA_Venc_n_Parc_2_ATA_Atrasada = column_ATA_Venc_n_Parc + word__2_ATA_Atrasada
            column_Pag_Comissao_n_Parc = word_Pag_Comissao_ + n_Parc
            column_PK_Vend_ATA_n_Parc = word_PK_ + word_Vend_ + word_ATA_ + n_Parc

            self.list_list_columns_pag.append([
                column_Situacao_n_Parc,
                column_Data_Pag_n_Parc,
                column_ATA_Pag_n_Parc,
                column_Sma_Pag_n_Parc,
                column_Mes_Pag_n_Parc
            ])
            self.list_list_columns_venc.append([
                column_Situacao_n_Parc,
                column_Data_Venc_n_Parc,
                column_ATA_Venc_n_Parc,
                column_Sma_Venc_n_Parc,
                column_Mes_Venc_n_Parc
            ])
            self.list_list_columns_situacao_num_ATA.append([
                column_Situacao_n_Parc,
                column_Data_Pag_n_Parc,
                column_Data_Venc_n_Parc,
                column_ATA_Pag_n_Parc,
                column_ATA_Venc_n_Parc,
                column_Situacao_ATA_n_Parc,
                column_Num_ATA_n_Parc
            ])
            self.list_list_columns_num_ATA_atrasado.append([
                column_Num_ATA_n_Parc,
                column_Num_ATA_n_Parc_Atrasado,
                column_PK_Vend_ATA_n_Parc
            ])
            self.list_list_columns_percentage.append([
                column_porc_ATA_Pag,
                column_porc_ATA_Pag_n_Parc_1_ATA_Atrasada,
                column_porc_ATA_Pag_n_Parc_2_ATA_Atrasada,
                column_Num_ATA_n_Parc,
                column_PK_Vend_ATA_n_Parc
            ])
            self.list_list_columns_ATA_Venc_n_Parc_n_ATA_Atrasada.append([
                column_ATA_Venc_n_Parc,
                column_ATA_Venc_n_Parc_1_ATA_Atrasada,
                column_ATA_Venc_n_Parc_2_ATA_Atrasada
            ])
            self.list_list_columns_comissao_atrasada.append([
                column_Pag_Comissao_n_Parc,
                column_porc_ATA_Pag,
                column_porc_ATA_Pag_n_Parc_1_ATA_Atrasada,
                column_porc_ATA_Pag_n_Parc_2_ATA_Atrasada
            ])
            self.list_list_columns_PK_Vend_ATA_n_Parc.append([
                column_ATA_Venc_n_Parc,
                column_PK_Vend_ATA_n_Parc
            ])
            self.list_list_order_columns.append([
                column_PK_Vend_ATA_n_Parc,
                column_Situacao_n_Parc,
                column_Situacao_ATA_n_Parc,
                column_Data_Pag_n_Parc,
                column_Data_Venc_n_Parc,
                column_Num_ATA_n_Parc,
                column_Num_ATA_n_Parc_Atrasado,
                column_Pag_Comissao_n_Parc,
                column_ATA_Pag_n_Parc,
                column_porc_ATA_Pag,
                column_ATA_Venc_n_Parc,
                column_porc_ATA_Pag_n_Parc_1_ATA_Atrasada,
                column_ATA_Venc_n_Parc_1_ATA_Atrasada,
                column_porc_ATA_Pag_n_Parc_2_ATA_Atrasada,
                column_ATA_Venc_n_Parc_2_ATA_Atrasada,
                column_Mes_Pag_n_Parc,
                column_Mes_Venc_n_Parc,
                column_Sma_Pag_n_Parc,
                column_Sma_Venc_n_Parc
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
        self.tableManip.del_column = column_Dia_Semana
        self.tableManip.del_column = column_Mes_ano
        self.tableManip.del_column = column_ATA
        table_weekly = self.tableManip.table

        self.tableManip.table = self.table_date_weekly.copy()
        # deixar apenas as duas colunas 'Mes ano e Data semana'
        self.tableManip.del_column = column_Dia_Semana
        self.tableManip.del_column = column_N_Semana_Mes
        self.tableManip.del_column = column_ATA
        table_month = self.tableManip.table

        self.tableManip.table = self.table_date_weekly.copy()
        # deixar apenas as duas colunas 'Mes ano e Data semana'
        self.tableManip.del_column = column_Dia_Semana
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

    def create_columns_pk_Vend_ATA_Entrega_n_Parc(self):
        text_te = 'Criar coluna com chaves primaira que identifique '
        text_te += 'o vendedor e a ATA únicas.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.list_list_columns_PK_Vend_ATA_n_Parc = self.list_list_columns_PK_Vend_ATA_n_Parc
        self.tableManip.table = self.table_full
        self.tableManip.add_value_pk_vend_ata_entrega()
        self.table_full = self.tableManip.table

    def error_system(self, text_log):
        self.fileManip.writeLog = text_log
        self.save_full_teste(1)
        QApplication.quit()
        sys.exit()  

    def create_columns_Situacao_ATA_n_Parc(self):
        text_te = 'Criar coluna de numero e situação de quantidade '
        text_te += 'de ata atrasada ou adiantada ou no prazo'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_situacao_num_ATA = self.list_list_columns_situacao_num_ATA
        if self.tableManip.error:
            self.error_system(self.tableManip.log_error)
        self.table_full = self.tableManip.table

    def create_columns_Num_ATA_n_Parc_Atrasada(self):
        text_te = 'Criar coluna ATAs atrasadas '
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_num_ATA_atrasada = self.list_list_columns_num_ATA_atrasado
        self.table_full = self.tableManip.table

    def create_columns_porc_ATA_Pag_n_Parc_n_ATA_Atrasada(self):
        text_te = 'Criar coluna porcentagem da ATA 1º, 2º e 3º '
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_porcentagem = self.list_list_columns_percentage
        self.table_full = self.tableManip.table

    def create_columns_ATA_Venc_n_Parc_n_ATA_Atrasada(self):
        text_te = 'Criar coluna ATA vencimento atrasados '
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            return
        self.tableManip.table = self.table_full
        self.tableManip.add_value_ATA_Venc_n_Parc_n_ATA_Atrasada = self.list_list_columns_ATA_Venc_n_Parc_n_ATA_Atrasada
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
            if column_full in list_order_columns_start:
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

        list_all = list_columns_cliente + list_columns_Cad_Adm + list_columns_Mes + list_columns_Sma + list_columns_1Parcela_Demais_FAT
        return list_all

    def discover_columns_are_not_conlumns_start(self):
        list_columns_full = self.table_full.columns.to_list()
        list_columns_are_not_conlumns_start = []
        for column_full in list_columns_full:
            if column_full not in self.list_order_columns_start:
                list_columns_are_not_conlumns_start.append(column_full)
        return list_columns_are_not_conlumns_start

    def alter_order_columns(self):
        list_columns_end = []
        cout = 0
        for column_start in self.list_order_columns_start:
            cout += 1
            if column_start == column_Periodo_Valor_Qtd_Vendas:
                for column_Valor_Qtd_Vendas in list_order_columns_Valor_Qtd_Vendas_Vendedor:
                    if column_Valor_Qtd_Vendas in list_columns_end:
                        list_columns_end.remove(column_Valor_Qtd_Vendas)
                    list_columns_end.append(column_Valor_Qtd_Vendas)
            elif column_start == column_Periodo_Valor_Qtd_Vendas_Supervisor:
                for column_Valor_Qtd_Vendas in list_order_columns_Valor_Qtd_Vendas_Supervisor:
                    if column_Valor_Qtd_Vendas in list_columns_end:
                        list_columns_end.remove(column_Valor_Qtd_Vendas)
                    list_columns_end.append(column_Valor_Qtd_Vendas)
            elif column_start == column_Periodo_Valor_Qtd_Vendas_Gerencia:
                for column_Valor_Qtd_Vendas in list_order_columns_Valor_Qtd_Vendas_Gerencia:
                    if column_Valor_Qtd_Vendas in list_columns_end:
                        list_columns_end.remove(column_Valor_Qtd_Vendas)
                    list_columns_end.append(column_Valor_Qtd_Vendas)
            list_columns_end.append(column_start)
        return list_columns_end

    def add_order_columns_list_start(self, list_columns):
        for column in list_columns:
            if column in self.list_order_columns_start:
                self.list_order_columns_start.remove(column)
            self.list_order_columns_start.append(column)

    def order_columns(self):
        ''' Ordenar colunas da tabela para a forma que quiser'''
        text_te = 'Ordenar as colunas, colocando as mais importantes no início '
        self.father.prog1(text_te)
        for list_columns_ata in self.list_list_order_columns:
            self.add_order_columns_list_start(list_columns_ata)
        for list_column_orden_total in self.list_list_order_columns_total:
            self.add_order_columns_list_start(list_column_orden_total)
        list_all = self.create_list_order_columns()
        self.add_order_columns_list_start(list_all)
        list_columns_are_not_conlumns_start = self.discover_columns_are_not_conlumns_start()
        self.add_order_columns_list_start(list_columns_are_not_conlumns_start)
        list_columns_end = self.alter_order_columns()
        self.table_full = self.table_full[list_columns_end]

    def save_full(self):
        text_te = 'Salvar uma tabela previamente consolidada e tratada.'
        self.father.prog1(text_te)
        if self.table_full.empty:
            return
        if self.salve_first:
            if self.mix:
                create_table(self.table_full, arqTableMerge)
            self.salve_first = False
        else:
            create_table(self.table_full, arqTableMergeOrder)

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
