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
from components.creat_table_gerente import Creat_table_gerente
# from PySide6.QtCore import QThread
from typing import Optional
from path_file import Path_file
# from time import ctime
import locale
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
    return table_created


class Main_table:
    def __init__(self, *args, **kwargs) -> None:
        self.father = kwargs.get('father')
        self.tableManip = TableManip()
        # self.table_manip_value = Table_manip_value()
        self.date_weekly = Date_weekly()
        self.fileManip = FileManip()
        self.path_file = Path_file()
        self.creat_table_gerente = Creat_table_gerente()

        self.siteSircon = "https://app.sistemasircon.com.br/login"
        self.user = 'usuario@gmail.com'
        self.password = 'Senha'

        self.month = 1

        self.new_table_Cadastro_Consorciado = False
        self.new_table_Cadastro_Funcionario = False
        self.new_table_Cadastro_Ata = False
        self.new_table_Comissoes_Configuracao = False
        self.new_table_Comissoes_ConfigPagamento = False

        self.mix = False

        self.connected = True

        self.start = True

        self.arqTableCadastroConsorciado = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Cadastro_Consorciado.csv')  # noqa
        self.arqTableCadastroFuncionario = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Cadastro_Funcionario.csv')  # noqa
        self.arqTableCadastroAta = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Cadastro_Ata.csv')  # noqa
        self.arqTableComissoesConfiguracao = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Comissoes_Configuracao.csv')  # noqa
        self.arqTableComissoesConfigPag = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Comissoes_ConfigPagamento.csv')  # noqa
        self.arqTableComissoesConfigPagTratada = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Comissoes_ConfigPagTratada.csv')  # noqa
        self.arqTableComissoesConfigPagDupl = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Comissoes_ConfigPagamento_Dupl.csv')  # noqa
        self.arqTableGerente = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Gerente.csv')  # noqa
        self.arqTableComissoesConfigPagGerente = self.path_file.path_file_create_user('Appdata', 'tables', 'table_Comissoes_ConfigPagamento_gerente.csv')  # noqa
        self.arqtableMerge = self.path_file.path_file_create_user('Appdata', 'tables', 'tableMerge.csv')  # noqa
        self.arqTableDatasSemanais = self.path_file.path_file_create_user('Appdata', 'tables', 'table_datas_semanais.csv')  # noqa
        self.arq_log = self.path_file.path_file_create_user('Appdata', 'log', 'log.txt')  # noqa
        self.arqTableTeste1 = self.path_file.path_file_create_user('Appdata', 'tables', 'table_teste1.csv')  # noqa
        # self.arqTableTeste2 = self.path_file.path_file_create_user('Appdata', 'tables', 'table_teste2.csv')  # noqa
        # self.arqTableTeste3 = self.path_file.path_file_create_user('Appdata', 'tables', 'table_teste3.csv')  # noqa

        self.fileManip.arq_log = self.arq_log

        self.pathDonwload = os.environ['USERPROFILE'] + '\\Downloads'
        self.arqDonwloadSales = self.pathDonwload + '\\consorciados.csv'
        self.arqDonwloadFunction = self.pathDonwload + '\\funcionarios.csv'

        '''Variaveis'''
        self.column_primary_key = 'PK'

        self.column_Vendedor = 'Vendedor'
        self.column_gerente = 'Gerente'
        self.column_Credito = 'Crédito'

        self.column_ATA_Entrega = 'ATA Entrega'
        self.column_Total_ATA_Entrega = 'Total ATA Entrega'

        self.column_qtd_valor_vend = 'Qtd Valor Vend'
        self.column_1p_referencia = '1P referencia'
        self.column_Data_de_Entrega = 'Data de Entrega'
        self.column_Data_Cad_Adm = 'Data Cad. Adm'

        self.keyword_periodo_valor_qtd = 'Qtd. Vendas'
        self.keyword_1p_referencia = 'CADASTRO'

        self.column_Situacao = 'Situação'

        self.column_Ata_Entrega = 'ATA Entrega'
        self.column_Mes_Entrega = 'Mes Entrega'
        self.column_Sma_Entrega = 'Sma Entrega'
        self.column_Ata_Cad_Adm = 'ATA Cad Adm'
        self.column_Mes_Cad_Adm = 'Mes Cad Adm'
        self.column_Sma_Cad_Adm = 'Sma Cad Adm'

        self.column_N_Semana_Mes = 'N Semana Mes'
        self.column_Mes_ano = 'Mes ano'
        self.column_Data_semana = 'Data semana'
        self.column_Dia_semana = 'Dia semana'

        self.column_Periodo_final = 'Periodo_final'
        self.column_Periodo_inicial = 'Periodo_inicial'
        self.column_ATA = 'ATA'

        self.column_Telefone = 'Telefone'
        self.column_Celular = 'Celular'

        self.column_Cliente = 'Cliente'

        self.column_Nome = 'Nome'
        self.column_Cargo = 'Cargo'
        self.column_Administradora = 'Administradora'
        self.column_Tipo_Pagamento = 'Tipo Pagamento'
        self.column_Index = 'Index'

        self.column_periodo_valor_qtd_vendas = '1 Periodo valor qtd vendas'

        self.column_Tabela = 'Tabela'

        self.word_Funcionario = 'Funcionario'
        self.word_Gerente = 'Gerente'
        self.word_Gerente_Geral = 'Gerente Geral'
        self.word_Cliente = 'Cliente'

        self.word_column_total = 'Total'

        self.column_Nome_Funcionario = self.column_Nome + ' ' + self.word_Funcionario

        self.column_Nome_Gerente = self.column_Nome + ' ' + self.word_Gerente
        self.column_Cargo_Gerente = self.column_Cargo + ' ' + self.word_Gerente
        self.column_Administradora_Gerente = self.column_Administradora + ' ' + self.word_Gerente
        self.column_Tabela_Gerente = self.column_Tabela + ' ' + self.word_Gerente

        self.column_periodo_valor_qtd_vendas_Gerente = self.column_periodo_valor_qtd_vendas + ' ' + self.word_Gerente

        self.column_periodo_valor_qtd_vendas_Gerente_Geral = self.column_periodo_valor_qtd_vendas + ' ' + self.word_Gerente_Geral
        self.column_cargo_gerente_geral = self.column_Cargo + ' ' + self.word_Gerente_Geral

        self.word_Data = 'Data '
        self.word_Venc = 'Venc. '
        self.word_Pag = 'Pag. '
        self.word_º_Parc = 'º Parc'
        self.word_ATA = 'ATA '
        self.word_Sma = 'Sma '
        self.word_Mes = 'Mes '
        self.word_Situacao = 'Situação '
        self.word_Num = 'Num. '
        self.word_1_Porc = '1º % '
        self.word_2_Porc = '2º % '
        self.word_3_Porc = '3º % '

        # self.list_columns_total_vendidos = [
        #     self.column_total_vendidos]

        self.list_columns_ata_mes_sma = [
            self.column_Ata_Entrega, self.column_Mes_Entrega, self.column_Sma_Entrega,
            self.column_Ata_Cad_Adm, self.column_Mes_Cad_Adm, self.column_Sma_Cad_Adm
        ]

        '''#################### TAGS #######################################'''
        self.tag_option = 'option'
        self.tag_select = 'select'
        self.tag_outerHTML = 'outerHTML'
        self.tag_value = 'value'
        self.tag_selected = '/option[@selected="selected"]'
        # self.tag_table = 'table'
        self.tag_row = 'tr'
        self.tag_data = 'td'
        # self.tag_cab = 'th'
        '''#################### XPATHS #####################################'''
        self.listXpathLog = [
            '//*[@id="form:txtUsuarioSircon"]',  # campo usuario
            '//*[@id="form:txtSenhaSircon"]',  # campo senha
            '//*[@id="form:btLogar"]'  # botao confirmar
        ]
        # linha coluna calendario
        self.line_ = 1
        self.column_ = 0
        self.xp0_ = '//*[@id="menucadastro"]/a'  # menu cadastro
        self.xp1_ = '//*[@id="menucadastro"]/ul/li[5]'  # menu consorciado
        # cp entrega venda inici
        self.xp2_ = '//*[@id="pnlBloco"]/div[6]/div/div[3]/div'
        # bt seta para esquerda
        self.xp3_ = '//*[@id="ui-datepicker-div"]/div[1]/a[1]'
        self.text = '//*[@id="ui-datepicker-div"]/table/tbody'
        self.xp4_ = f'{self.text}/tr[{self.line_}]/td[{self.column_}]'
        # bt fechar calend
        self.xp5_ = '//*[@id="ui-datepicker-div"]/div[3]/button[2]'
        # cp entrega venda final
        self.xp6_ = '//*[@id="pnlBloco"]/div[6]/div/div[4]/div'
        self.xp7_ = '//*[@id="btnConsultar"]'  # botao consultar
        self.xp8_ = '//*[@id="btnGerarXls"]'  # botao de download
        self.listXpathSales = [
            self.xp0_, self.xp1_, self.xp2_, self.xp3_, self.xp4_, self.xp5_,
            self.xp6_, self.xp3_, self.xp4_, self.xp5_, self.xp7_, self.xp8_]
        self.listXpathComissoesConfiguracao = [
            '//*[@id="menufinan"]',  # comissões
            '//*[@id="menufinan"]/ul/li[2]'  # Config
        ]
        self.xpathTipoComissao = [
            '//*[@id="frm:tpComissao"]',
            '//*[@id="frm:tpComissao"]/option[2]'  # Pagamento
        ]
        self.xpathAdministradora = '//*[@id="frm:cbAdministradora"]'
        self.xpathTabelaRecebimento = '//*[@id="frm:cbTabelaRecebimento"]'
        self.xpathCargo = '//*[@id="frm:cbCargo"]'
        self.listCampoCotaPeriodoParcela = []
        for num in range(30):  # quantidade de campos comissões configuracao
            self.listCampoCotaPeriodoParcela.append([
                f'//*[@id="frm:pnlEsacalas"]/div[{str(num + 1)}]',  # cp 0 a 2
                [f'frm:j_idt124:{num}:j_idt194',
                    f'frm:j_idt124:{num}:j_idt188'],  # qtd cotas inicial
                [f'frm:j_idt124:{num}:j_idt196',
                    f'frm:j_idt124:{num}:j_idt190'],  # qtd cotas final
                f'//*[@id="frm:j_idt124:{num}:j_idt182_input"]',  # dt vd inic
                f'//*[@id="frm:j_idt124:{num}:j_idt184_input"]',  # dt vd fim
                f'//*[@id="frm:j_idt124:{num}:j_idt149"]',  # parcela 1
                f'//*[@id="frm:j_idt124:{num}:j_idt156"]',  # parcela 2
                f'//*[@id="frm:j_idt124:{num}:j_idt158"]',  # parcela 3
                f'//*[@id="frm:j_idt124:{num}:j_idt160"]',  # parcela 4
                f'//*[@id="frm:j_idt124:{num}:j_idt162"]',  # parcela 5
                f'//*[@id="frm:j_idt124:{num}:j_idt164"]',  # parcela 6
                f'//*[@id="frm:j_idt124:{num}:j_idt166"]',  # parcela 7
                f'//*[@id="frm:j_idt124:{num}:j_idt168"]',  # parcela 8
                f'//*[@id="frm:j_idt124:{num}:j_idt170"]',  # parcela 9
                f'//*[@id="frm:j_idt124:{num}:j_idt172"]',  # parcela 10
                f'//*[@id="frm:j_idt124:{num}:j_idt174"]',  # parcela 11
                f'//*[@id="frm:j_idt124:{num}:j_idt176"]'  # parcela 12
            ])

        self.listXpathFunction = [
            '//*[@id="menucadastro"]/a',  # menu cadastro
            '//*[@id="menucadastro"]/ul/li[7]',  # menu funcionario
            '//*[@id="btnConsultar"]',  # botao consultar
            '//*[@id="btnGerarXls"]'  # botao consultar
        ]

        self.listXpathComissoesConfPagamento = [
            '//*[@id="menufinan"]',  # comissões
            '//*[@id="menufinan"]/ul/li[3]/a'  # ConfigPagamento
        ]
        self.xpathTipoComissaoPagamento = [
            '//*[@id="frm:cbTpConfig"]',
            '//*[@id="frm:cbTpConfig"]/option[1]'  # Pagamento
        ]
        self.listXpathCargAdminsPag = [
            '//*[@id="frm:cbCargo"]',
            '//*[@id="frm:cbAdministradora"]',
            '//*[@id="frm:cbTpRecebimento"]'
        ]
        self.listXpathDtPagamentoParcelas = [
            '//*[@id="frm:pnlBloco"]',  # xpath Father
            '//*[@id="frm:cbFormaReceb"]',  # data pagamento por
            ['//*[@id="frm:cb1"]',
             '//*[@id="frm:cb2"]',
             '//*[@id="frm:cb3"]'],  # dias
            '//*[@id="frm:recPriParc"]',  # 1º parcela recebera
            '//*[@id="frm:cb4"]',  # 1º parcela referencia
            '//*[@id="frm:cbRefApuracaoPrimParc"]',  # periodo inicial tipo
            ['//*[@id="frm:cbP1"]',
             '//*[@id="frm:cbP2"]',
             '//*[@id="frm:cbP3"]',
             '//*[@id="frm:cbP4"]',
             '//*[@id="frm:cbP28"]',
             '//*[@id="frm:cbP29"]',
             '//*[@id="frm:cbP39"]'],   # periodo inicial quando
            '//*[@id="frm:cbRefApuracaoFimPrimParc"]',  # periodo final tipo
            ['//*[@id="frm:cbP5"]',
             '//*[@id="frm:cbP6"]',
             '//*[@id="frm:cbP7"]',
             '//*[@id="frm:cbP8"]',
             '//*[@id="frm:cbP30"]',
             '//*[@id="frm:cbP40"]',
             '//*[@id="frm:j_idt193"]'],  # periodo final quando
            '//*[@id="frm:recConfimac"]',  # Demais parcela recebera
            '//*[@id="frm:cbP10"]',  # Demais parcela referencia
            '//*[@id="frm:cbRefApuracaoConfirmacoes"]',  # periodo inicial tipo
            ['//*[@id="frm:cbP11"]',
             '//*[@id="frm:cbP12"]',
             '//*[@id="frm:cbP13"]',
             '//*[@id="frm:cbP14"]',
             '//*[@id="frm:cbP31"]',
             '//*[@id="frm:cbP38"]',
             '//*[@id="frm:cbP41"]'],   # periodo inicial quando
            '//*[@id="frm:cbRefApuracaoFimConfirmacoes"]',  # periodo fim tipo
            ['//*[@id="frm:cbP15"]',
             '//*[@id="frm:cbP16"]',
             '//*[@id="frm:cbP17"]',
             '//*[@id="frm:cbP18"]',
             '//*[@id="frm:cbP32"]',
             '//*[@id="frm:cbP37"]',
             '//*[@id="frm:cbP42"]'],  # periodo final quando
            '//*[@id="frm:recFat"]',  # Faturamento recebera
            '//*[@id="frm:cbP19"]',  # Faturamento referencia
            '//*[@id="frm:cbRefApuracaoFaturamento"]',  # periodo inicial tipo
            ['//*[@id="frm:cbP20"]',
             '//*[@id="frm:cbP21"]',
             '//*[@id="frm:cbP22"]',
             '//*[@id="frm:cbP23"]',
             '//*[@id="frm:cbP33"]',
             '//*[@id="frm:cbP36"]',
             '//*[@id="frm:cbP43"]'],   # periodo inicial quando
            '//*[@id="frm:cbRefApuracaoFimFaturamento"]',  # periodo final tipo
            ['//*[@id="frm:cbP24"]',
             '//*[@id="frm:cbP25"]',
             '//*[@id="frm:cbP26"]',
             '//*[@id="frm:cbP27"]',
             '//*[@id="frm:cbP34"]',
             '//*[@id="frm:cbP35"]',
             '//*[@id="frm:cbP44"]'],  # periodo final quando
        ]

        self.listXpathMinutes = [
            '//*[@id="menucadastro"]/a',  # menu cadastro
            '//*[@id="menucadastro"]/ul/li[2]/a',  # menu Ata
            '//*[@id="frm:cbAno"]',  # Ano
            '//*[@id="frm:pnlLista"]',   # informacao OBS: alterado ordem.
            '//*[@id="frm:cbAdministradora"]',  # administradora
        ]

        self.headerDtPagamentoParcelas = [
            self.column_Cargo,
            self.column_Administradora,
            self.column_Tipo_Pagamento,
            'Dt pag. por',
            'dia pag.',
            '1P recebera',
            '1P referencia',
            '1P periodo inicial',
            '1P dt inicial',
            '1P periodo final',
            '1P dt final',
            'D+ recebera',
            'D+ referencia',
            'D+ periodo inicial',
            'D+ dt inicial',
            'D+ periodo final',
            'D+ dt final',
            'FAT recebera',
            'FAT referencia',
            'FAT periodo inicial',
            'FAT dt inicial',
            'FAT periodo final',
            'FAT dt final',
            self.column_Index]

        self.list_columns_pag = [[self.column_Situacao,
                                  self.column_Data_de_Entrega,
                                  self.column_Ata_Entrega,
                                  self.column_Sma_Entrega,
                                  self.column_Mes_Entrega],
                                 [self.column_Situacao,
                                  self.column_Data_Cad_Adm,
                                  self.column_Ata_Cad_Adm,
                                  self.column_Sma_Cad_Adm,
                                  self.column_Mes_Cad_Adm]]

        self.list_columns_venc = []

        self.list_list_columns_order = [[
            self.column_Situacao,
            self.column_Data_de_Entrega,
            self.column_Data_Cad_Adm,
            self.column_Ata_Entrega,
            self.column_Ata_Cad_Adm,
            self.column_Sma_Entrega,
            self.column_Sma_Cad_Adm,
            self.column_Mes_Entrega,
            self.column_Mes_Cad_Adm]]

        self.list_list_columns_situacao_num_ATA = []

        self.list_list_columns_percentage = []

        # self.columns_data_venc = ['Data Venc. ', 'º Parc']
        # self.columns_data_pag = ['Data Pag. ', 'º Parc']
        # self.columns_ata = ['ATA ', 'º Parc']
        # self.columns_sma = ['Sma ', 'º Parc']
        # self.columns_mes = ['Mes ', 'º Parc']
        # self.columns_ata_venc = ['ATA ', 'º Parc Venc']
        # self.columns_sma_venc = ['Sma ', 'º Parc Venc']
        # self.columns_mes_venc = ['Mes ', 'º Parc Venc']
        # self.columns_situacao = ['Situação ', 'º Parc']

        self.listColumnsStart = [
            self.column_Cliente,
            self.column_Administradora,
            self.column_Cargo,
            self.column_Cargo_Gerente,
            self.column_cargo_gerente_geral,
            self.column_Vendedor,
            self.column_gerente,
            self.column_Credito,
            'Valor Parc. Inicial',
            'Data Pag. 1º Parc',
            'Dt pag. por',
            'dia pag.',
            '1P recebera',
            'D+ recebera',
            'FAT recebera',
            '1P referencia',
            'D+ referencia']

        self.driver: Optional[webdriver.Chrome] = None
        self.connect = Connect()
        self.table_Cadastro_Consorciado: pd.DataFrame = pd.DataFrame()
        self.table_Cadastro_Funcionario: pd.DataFrame = pd.DataFrame()
        self.table_Cadastro_Ata: pd.DataFrame = pd.DataFrame()
        self.table_Comissoes_Configuracao: pd.DataFrame = pd.DataFrame()
        self.table_Comissoes_ConfigPagamento: pd.DataFrame = pd.DataFrame()
        self.table_Gerente: pd.DataFrame = pd.DataFrame()
        self.table_date_weekly: pd.DataFrame = pd.DataFrame()
        self.table_Cadastro_funcionario_gerente: pd.DataFrame = pd.DataFrame()
        self.table_Comissoes_Configuracao_gerente: pd.DataFrame = (
            pd.DataFrame())
        self.table_full: pd.DataFrame = pd.DataFrame()
        self.table_duplicate: pd.DataFrame = pd.DataFrame()

    # ################### ABRIR SITES ########################################

    def date_file(self):
        text_te = 'Datas das tabelas de: \n'
        date_table_Cadastro_Consorciado = datetime.fromtimestamp(os.path.getmtime(self.arqTableCadastroConsorciado)).strftime('%c')  # noqa
        text_te += f'Cadastro de consorciado: {date_table_Cadastro_Consorciado} \n'
        date_table_Cadastro_Funcionario = datetime.fromtimestamp(os.path.getmtime(self.arqTableCadastroFuncionario)).strftime('%c')  # noqa
        text_te += f'Cadastro de funcionario: {date_table_Cadastro_Funcionario} \n'
        date_table_Cadastro_Ata = datetime.fromtimestamp(os.path.getmtime(self.arqTableCadastroAta)).strftime('%c')  # noqa
        text_te += f'Cadastro de ATAs: {date_table_Cadastro_Ata} \n'
        date_table_Comissoes_Configuracao = datetime.fromtimestamp(os.path.getmtime(self.arqTableComissoesConfiguracao)).strftime('%c')  # noqa
        text_te += f'Comissões configuração: {date_table_Comissoes_Configuracao} \n'
        date_table_Comissoes_ConfigPagamento = datetime.fromtimestamp(os.path.getmtime(self.arqTableComissoesConfigPag)).strftime('%c')  # noqa
        text_te += f'Comissões configuração de pagamento: {date_table_Comissoes_ConfigPagamento} \n'
        return (text_te)
        # self.father.prog1(text_te)

    def openSite(self):
        ''' defined '''
        text_te = f'Abrindo site: {self.siteSircon}'
        self.father.prog1(text_te)
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.connect = Connect(driver=self.driver)
        xpathManip = XpathManip(driver=self.driver)
        self.connect.arq_log = self.arq_log
        self.driver.get(self.siteSircon)
        # logar
        self.connect.user = self.user
        self.connect.password = self.password
        count = 0
        while True:
            self.connect.logarSircon = self.listXpathLog
            xpathManip.locate = self.listXpathComissoesConfiguracao[0]
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

    def log_start_end(self):
        self.new_table_Cadastro_Consorciado = False
        self.new_table_Cadastro_Funcionario = False
        self.new_table_Cadastro_Ata = False
        self.new_table_Comissoes_Configuracao = False
        self.new_table_Comissoes_ConfigPagamento = False

        self.mix = False
        if self.start:
            text = '\n' + 'Inicio: '
            self.start = False
        else:
            text = 'Fim:    '
        text += str(datetime.now())
        self.fileManip.writeLog = text

    def limited_search_administradoras(self):
        self.connect.valueExistAdministradora = self.table_Cadastro_Consorciado

    def limited_search_cargos(self):
        self.connect.valueExistCargos = self.table_Cadastro_Funcionario

    def mesclar_tables(self):
        text = 'Unir todas Tabelas: '
        if self.mix is False:
            text += 'Não'
            self.table_full = load_table(self.arqtableMerge)
        else:
            text += 'Sim'
        self.father.prog1(text)

    def create_table_Cadastro_Consorciado(self):
        '''table_Cadastro_Consorciado'''
        text_lc = 'cadastro de consorciado'
        if self.new_table_Cadastro_Consorciado:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            self.connected = self.openSite()
            if self.connected is False:
                return
            self.connect.file = self.arqDonwloadSales
            self.connect.month = self.month
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.connect.sales = self.listXpathSales
            self.connect.create_primary_key = self.column_primary_key
            self.table_Cadastro_Consorciado = self.connect.dfNew
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.table_Cadastro_Consorciado = create_table(
                self.table_Cadastro_Consorciado,
                self.arqTableCadastroConsorciado)
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Cadastro_Consorciado = load_table(
                self.arqTableCadastroConsorciado)
        # self.father.prog1(f'Arqvuivos:  {self.arqTableCadastroConsorciado}')

    def create_table_Cadastro_Funcionario(self):
        '''table_Cadastro_Funcionario '''
        text_lc = 'cadastro de funcionário'
        if self.new_table_Cadastro_Funcionario:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            self.connected = self.openSite()
            if self.connected is False:
                return
            self.connect.file = self.arqDonwloadFunction
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.connect.function = self.listXpathFunction
            self.table_Cadastro_Funcionario = self.connect.dfNew
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.table_Cadastro_Funcionario = create_table(
                self.table_Cadastro_Funcionario,
                self.arqTableCadastroFuncionario)
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Cadastro_Funcionario = load_table(self.arqTableCadastroFuncionario)
        # self.father.prog1(f'Arqvuivos:  {self.arqTableCadastroFuncionario}')

    def create_table_Cadastro_Ata(self):
        '''#################### LIMITAR PESQUISAS ##########################'''
        text_lc = 'cadastro de ATA'
        if self.new_table_Cadastro_Ata is True:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            self.connected = self.openSite()
            if self.connected is False:
                return
            self.connect.month = self.month + 12
            self.connect.tagSon = self.tag_data
            self.connect.tagFather = self.tag_row
            self.connect.tagGet = self.tag_outerHTML
            self.connect.tagReturnValue
            self.limited_search_administradoras()
            self.limited_search_cargos()
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.connect.minutes = self.listXpathMinutes
            self.table_Cadastro_Ata = self.connect.table
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.tableManip.table = self.table_Cadastro_Ata
            list_columns_rename = [
                [1, 'Mes'],
                [2, self.column_Periodo_inicial],
                [3, self.column_Periodo_final]]
            for column_rename in list_columns_rename:
                self.tableManip.rename_name_column_indix = column_rename
            self.tableManip.add_column_clone_two_columns = [self.column_ATA, 'Mes', 'Ano']
            self.table_Cadastro_Ata = self.tableManip.table
            self.table_Cadastro_Ata = create_table(self.table_Cadastro_Ata, self.arqTableCadastroAta)  # noqa
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Cadastro_Ata = load_table(self.arqTableCadastroAta)

    def create_table_Comissoes_Configuracao(self):
        '''table_Comissoes_Configuracao'''
        text_lc = 'comissões configuração'
        if self.new_table_Comissoes_Configuracao:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            self.connected = self.openSite()
            if self.connected is False:
                return
            self.connect.pressListXpath = self.listXpathComissoesConfiguracao
            self.connect.pressListXpath = self.xpathTipoComissao
            self.connect.tagSon = self.tag_option
            self.connect.tagFather = self.tag_select
            self.connect.tagGet = self.tag_outerHTML
            self.connect.tagReturnValue
            # criar lista de administradoras
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.limited_search_administradoras()
            self.connect.pressXpathResultListValue = self.xpathAdministradora
            # criar lista de administradoras + tabela de recebiemnto
            self.connect.pressListValueXpathResultListValue = self.xpathTabelaRecebimento
            # criar lista de administradoras + tabela de recebiemnto + cargos
            self.limited_search_cargos()
            self.connect.pressListValueXpathResultListValueDouble = self.xpathCargo
            # alterar a tagets
            self.connect.tagGet = self.tag_value
            self.connect.tagReturnValue
            # lista administradoras, tabela de recebiemnto, cargos, valores
            self.connect.pressListValueResultListValueTriple = self.listCampoCotaPeriodoParcela
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
            create_table(table, self.arqTableTeste1)
            self.table_Comissoes_Configuracao = self.connect.renameColumn
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.table_Comissoes_Configuracao = create_table(self.table_Comissoes_Configuracao, self.arqTableComissoesConfiguracao)  # noqa
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Comissoes_Configuracao = load_table(self.arqTableComissoesConfiguracao)

    def create_table_Comissoes_ConfigPagamento(self):
        '''table_Comissoes_ConfigPagamento'''
        text_lc = 'comissões configuração de pagamento'
        if self.new_table_Comissoes_ConfigPagamento:
            text_te = 'Início da criação da tabela de ' + text_lc + ':'
            self.father.prog1(text_te)
            self.connected = self.openSite()
            if self.connected is False:
                return
            self.connect.tagSon = self.tag_option
            self.connect.tagFather = self.tag_select
            self.connect.tagGet = self.tag_outerHTML
            self.connect.tagSelected = self.tag_selected
            self.connect.tagReturnValue
            # caminho no site para entra local especifico pelo xpath
            self.connect.pressListXpath = self.listXpathComissoesConfPagamento
            self.connect.pressListXpath = self.xpathTipoComissaoPagamento
            # list os valores existentes no campos cargos, administradora, tipoPagamento
            self.limited_search_administradoras()
            self.limited_search_cargos()
            text_te = 'Obtendo informações da tabela de ' + text_lc + '.'
            self.father.prog1(text_te)
            self.connect.pressListXpathReturnListValue = self.listXpathCargAdminsPag
            self.connect.pressListValueReturnListValue = self.listXpathDtPagamentoParcelas
            self.connect.organizeListLine = self.headerDtPagamentoParcelas
            # listFull = self.connect.organizeListLine
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.table_Comissoes_ConfigPagamento = self.connect.listLineToTable
            self.table_Comissoes_ConfigPagamento = create_table(
                self.table_Comissoes_ConfigPagamento,
                self.arqTableComissoesConfigPag)
        else:
            text_te = 'Ler a tabela de ' + text_lc + ' dos arquivos já salvos.'
            self.father.prog1(text_te)
            self.table_Comissoes_ConfigPagamento = load_table(self.arqTableComissoesConfigPag)

    def create_table_gerente(self):
        if self.mix is False:
            return
        text_lc = 'comissões Gerente'
        text_te = 'Início da criação da tabela de ' + text_lc + ':'
        self.father.prog1(text_te)
        self.table_Gerente = self.creat_table_gerente.table_salve
        self.table_Gerente = create_table(self.table_Gerente, self.arqTableGerente)
        # self.table_Gerente = self.creat_table_gerente.table

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
        self.date_weekly.create_table_weekMonth_week_date = [self.column_N_Semana_Mes,
                                                             self.column_Data_semana,
                                                             self.column_Dia_semana,
                                                             self.column_Mes_ano]
        self.table_date_weekly = self.date_weekly.return_table

    def merge_table_Cadastro_Ata_table_date_weekly(self):
        if self.mix is False:
            return
        self.tableManip.column_Data_semana = self.column_Data_semana
        self.tableManip.column_Periodo_final = self.column_Periodo_final
        self.tableManip.column_Periodo_inicial = self.column_Periodo_inicial
        self.tableManip.column_ATA = self.column_ATA
        self.tableManip.table = self.table_date_weekly
        self.tableManip.merge_table_ata_table_weekly = self.table_Cadastro_Ata
        self.table_date_weekly = self.tableManip.table

        self.table_date_weekly = create_table(self.table_date_weekly, self.arqTableDatasSemanais)

    def table_manip_funcionario(self):
        ''' manipular table_Cadastro_Funcionario, para alterar os Nomes
        duplicados com os Cargos, que gera comissão duplicada, pois o mesmo
        tem dois ou mais cargos'''
        text_te = 'Manipular a tabela de cadastro de funcionários para '
        text_te += 'duplicação de cargos.'
        self.father.prog1(text_te)
        if self.table_Cadastro_Funcionario.empty or self.connected is False or self.mix is False:
            return
        self.tableManip.table = self.table_Cadastro_Funcionario
        self.tableManip.row_duplicate_column = [self.column_Nome]
        self.tableManip.list_columns_one_two = [self.column_Nome, self.column_Cargo]
        self.tableManip.edit_data_column_2 = [self.column_Nome, self.column_Cargo]
        self.table_Cadastro_Funcionario = self.tableManip.table
        self.table_Cadastro_funcionario_gerente = self.table_Cadastro_Funcionario

        self.tableManip.table = self.table_Cadastro_Funcionario
        self.tableManip.word = self.word_Funcionario
        self.tableManip.rename_list_name_column = self.table_Cadastro_Funcionario.columns
        self.table_Cadastro_Funcionario = self.tableManip.table

    def table_manip_cadastro_consorciado(self):
        ''' manipular table_Cadastro_Consorciado, para altera coluna Vendedor
        e igualar aos alterados no table_Cadastro_Funcionario'''
        text_te = 'Manipular a tabela de cadastro de consorciado para alterar '
        text_te += 'coluna igual a funcionário.'
        self.father.prog1(text_te)
        if self.table_Cadastro_Consorciado.empty or self.connected is False or self.mix is False:
            return
        self.tableManip.table = self.table_Cadastro_Consorciado

        name_column = self.column_Telefone + ' ' + self.word_Cliente
        self.tableManip.rename_name_column = [self.column_Telefone, name_column]
        name_column = self.column_Celular + ' ' + self.word_Cliente
        self.tableManip.rename_name_column = [self.column_Celular, name_column]

        self.tableManip.data_duplicate_change = self.column_Vendedor
        self.table_Cadastro_Consorciado = self.tableManip.table

    def table_manip_comissoes_configuracao(self):
        ''' manipular table_Comissoes_Configuracao remover as duplicação nas
        colunas self.column_Administradora e self.column_Cargo '''
        text_te = 'Manipular a tabela de comissões configuração de pagamento '
        text_te += 'para remover duplicação colunas admin. cargo.'
        self.father.prog1(text_te)
        if self.table_Comissoes_Configuracao.empty or self.connected is False or self.mix is False:
            return
        cols_comConf_rept = [self.column_Administradora, self.column_Cargo,
                             'Tabela de recebimento']
        self.tableManip.table = self.table_Comissoes_Configuracao
        self.tableManip.row_duplicate_column = cols_comConf_rept
        self.tableManip.list_columns_one_two_three = cols_comConf_rept
        self.tableManip.edit_data_column_3 = cols_comConf_rept
        self.table_Comissoes_Configuracao = self.tableManip.table
        self.table_Comissoes_Configuracao.rename(
            columns={'Tabela de recebimento': self.column_Tabela}, inplace=True)

    def table_manip_Cadastro_funcionario_gerente(self):
        text_te = 'Manipular a tabela de cadastro de funcionario'
        text_te += 'para adicionar colunas para cargo supervisor(gerente).'
        self.father.prog1(text_te)
        if self.table_Cadastro_funcionario_gerente.empty or self.connected is False or self.mix is False:
            return
        self.tableManip = TableManip()
        # names_columns = self.table_Cadastro_funcionario_gerente.columns
        self.tableManip.table = self.table_Cadastro_funcionario_gerente
        self.tableManip.word = self.word_Gerente
        self.tableManip.rename_list_name_column = self.table_Cadastro_funcionario_gerente.columns
        # for name_column in names_columns:
        #     name_column_gerente = name_column + '_Gerente'
        #     self.tableManip.rename_name_column = [name_column, name_column_gerente]
        self.table_Cadastro_funcionario_gerente = self.tableManip.table

    def table_manip_comissoes_configuracao_gerente(self):
        text_te = 'Manipular a tabela de comissões configuração para  '
        text_te += 'adicionar colunas do cargo supervisor(gerente).'
        self.father.prog1(text_te)
        if self.table_Comissoes_Configuracao.empty or self.connected is False or self.mix is False:
            return
        self.table_Comissoes_Configuracao_gerente = self.table_Comissoes_Configuracao
        self.tableManip = TableManip()

        self.tableManip.table = self.table_Comissoes_Configuracao_gerente
        self.tableManip.word = self.word_Gerente
        self.tableManip.rename_list_name_column = self.table_Comissoes_Configuracao_gerente.columns
        self.table_Comissoes_Configuracao_gerente = self.tableManip.table

        self.table_Comissoes_Configuracao_gerente = create_table(
            self.table_Comissoes_Configuracao_gerente,
            self.arqTableComissoesConfigPagGerente)

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
        if self.connected is False:
            self.mix = False
            text_cd = 'Não'
        text_te = 'Foi solicitado fazer a mesclagem entre tabelas: '
        text_te += text_cd
        self.father.prog1(text_te)

    def merge_consorciado_funcionario(self):
        # self.prog1('Mesclar tabela consorciado com funcionário')
        text_te = 'Mesclar a tebela de cadastro de consorciado com a '
        text_te += 'tabela de cadastro de funcionário.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_Cadastro_Consorciado.empty or (self.table_Cadastro_Funcionario.empty):  # noqa
            # print(self.mix is False, self.table_Cadastro_Consorciado.empty, self.table_Cadastro_Funcionario.empty)  # noqa
            # self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_Cadastro_Consorciado,
            self.table_Cadastro_Funcionario,
            left_on=self.column_Vendedor,
            right_on=self.column_Nome_Funcionario,
            how='left'
        )

    def merge_consorciado_funcionario_gerente(self):
        text_te = 'Mesclar a tebela já unida anteriomente coma a '
        text_te += 'tabela de cadastro de funcionário de gerente.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty or (self.table_Cadastro_funcionario_gerente.empty):  # noqa
            # self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Cadastro_funcionario_gerente,
            left_on=self.column_gerente,
            right_on=self.column_Nome_Gerente,
            how='left'
        )

    def merge_full_comissoes_configuracao(self):
        text_te = 'Mesclar a tebela já unida anteriomente coma a '
        text_te += 'tabela de cadastro de funcionário.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty or (self.table_Comissoes_Configuracao.empty):
            # self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Comissoes_Configuracao,
            on=[self.column_Administradora, self.column_Cargo, self.column_Tabela],
            how='left')

    def merge_full_comissoes_configuracao_gerente(self):
        text_te = 'Mesclar a tebela já unida anteriomente coma a '
        text_te += 'tabela de comissões configuração de gerente.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty or self.table_Comissoes_Configuracao_gerente.empty:  # noqa
            # self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Comissoes_Configuracao_gerente,
            left_on=[
                self.column_Administradora,
                self.column_Cargo_Gerente,
                self.column_Tabela],
            right_on=[
                self.column_Administradora_Gerente,
                self.column_Cargo_Gerente,
                self.column_Tabela_Gerente],
            how='left')

    def merge_full_comissoes_configuracao_gerente_geral(self):
        text_te = 'Mesclar a tebela já unida anteriomente coma a '
        text_te += 'tabela de cadastro de funcionário de gerente geral.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty or (self.table_Gerente.empty):
            # self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Gerente,
            on=[self.column_Administradora, self.column_Cargo_Gerente],
            how='left')

    def create_columns_ata(self):
        # descori a quantidade de num_atas_parc
        text_te = 'A partir da tabela mesclada criar os nomes das colunas.'
        self.father.prog1(text_te)
        # if self.mix is False:
        #     return
        # num_atas_parc = 10000
        # for i in range(2, num_atas_parc + 1):
        i = 1
        while True:
            i += 1
            n_parc = str(i) + self.word_º_Parc
            name_column_situacao = self.word_Situacao + n_parc
            if name_column_situacao not in self.table_full.columns:
                break

            name_column_data_pag = self.word_Data + self.word_Pag + n_parc
            name_column_ata_pag = self.word_ATA + self.word_Pag + n_parc
            name_column_sma_pag = self.word_Sma + self.word_Pag + n_parc
            name_column_mes_pag = self.word_Mes + self.word_Pag + n_parc

            name_column_data_venc = self.word_Data + self.word_Venc + n_parc
            name_column_ata_venc = self.word_ATA + self.word_Venc + n_parc
            name_column_sma_venc = self.word_Sma + self.word_Venc + n_parc
            name_column_mes_venc = self.word_Mes + self.word_Venc + n_parc

            mane_column_situacao_ata = self.word_Situacao + self.word_ATA + n_parc

            name_column_num_ata = self.word_Num + self.word_ATA + n_parc

            name_column_1_porc_ata = self.word_1_Porc + self.word_ATA + n_parc
            name_column_2_porc_ata = self.word_2_Porc + self.word_ATA + n_parc
            name_column_3_porc_ata = self.word_3_Porc + self.word_ATA + n_parc

            self.list_columns_pag.append([
                name_column_situacao,
                name_column_data_pag,
                name_column_ata_pag,
                name_column_sma_pag,
                name_column_mes_pag
            ])
            self.list_columns_venc.append([
                name_column_situacao,
                name_column_data_venc,
                name_column_ata_venc,
                name_column_sma_venc,
                name_column_mes_venc
            ])
            self.list_list_columns_order.append([
                name_column_situacao,
                name_column_data_pag,
                name_column_data_venc,
                mane_column_situacao_ata,
                name_column_ata_pag,
                name_column_ata_venc,
                name_column_num_ata,
                name_column_1_porc_ata,
                name_column_2_porc_ata,
                name_column_3_porc_ata,
                name_column_sma_pag,
                name_column_sma_venc,
                name_column_mes_pag,
                name_column_mes_venc
            ])
            self.list_list_columns_situacao_num_ATA.append([
                name_column_situacao,
                name_column_data_pag,
                name_column_data_venc,
                name_column_ata_pag,
                name_column_ata_venc,
                mane_column_situacao_ata,
                name_column_num_ata
            ])
            self.list_list_columns_percentage.append([
                name_column_1_porc_ata,
                name_column_2_porc_ata,
                name_column_3_porc_ata,
                name_column_num_ata
            ])

    def merge_full_ata_weekly_month(self):
        text_te = 'Mesclar a tebela já unida coma a '
        text_te += 'tabela de ATAs apenas semanais(Sma).'
        self.father.prog1(text_te)
        '''# mesclar table_full com table_weekly'''
        if self.mix is False or self.table_full.empty or (self.table_date_weekly.empty):
            # self.table_full = load_table(self.arqtableMerge)
            return
        self.tableManip.table = self.table_date_weekly.copy()
        # deixar apenas as duas colunas 'N Semanda Mes e Data semana'
        self.tableManip.del_column = self.column_Dia_semana
        self.tableManip.del_column = self.column_Mes_ano
        self.tableManip.del_column = self.column_ATA
        table_weekly = self.tableManip.table

        self.tableManip.table = self.table_date_weekly.copy()
        # deixar apenas as duas colunas 'Mes ano e Data semana'
        self.tableManip.del_column = self.column_Dia_semana
        self.tableManip.del_column = self.column_N_Semana_Mes
        self.tableManip.del_column = self.column_ATA
        table_month = self.tableManip.table

        self.tableManip.table = self.table_date_weekly.copy()
        # deixar apenas as duas colunas 'Mes ano e Data semana'
        self.tableManip.del_column = self.column_Dia_semana
        self.tableManip.del_column = self.column_N_Semana_Mes
        self.tableManip.del_column = self.column_Mes_ano
        table_ata = self.tableManip.table

        # list_table_date = [table_weekly, table_month]
        # list_column_rename = [self.column_N_Semana_Mes, self.column_Mes_ano]
        list_list_full = [self.list_columns_pag, self.list_columns_venc]

        for list_full in list_list_full:
            for columns_all in list_full:
                #                      ['Data Pag. Xº Parc']
                name_column_data_full = columns_all[1]
                for name_column in columns_all:
                    if name_column == columns_all[0] or name_column == columns_all[1]:
                        continue
                    if name_column == columns_all[2]:
                        name_column_renomear = self.column_ATA
                        table_date = table_ata
                    elif name_column == columns_all[3]:
                        name_column_renomear = self.column_N_Semana_Mes
                        table_date = table_weekly
                    elif name_column == columns_all[4]:
                        name_column_renomear = self.column_Mes_ano
                        table_date = table_month
                    # num_name_column_sma_full = 3
                    # print('######################################')
                    # print(f'columns_all: {columns_all}')
                    # columnsList = self.table_full.columns.to_list()
                    # print(columnsList)
                    self.table_full = pd.merge(
                        self.table_full,
                        table_date,
                        left_on=name_column_data_full,
                        right_on=self.column_Data_semana,
                        how='left'
                    )
                    #   Renomear coluna
                    #                    ['Sma Xº Parc']
                    # name_column_sma_full = columns_all[num_name_column_sma_full]
                    self.tableManip.table = self.table_full
                    self.tableManip.rename_name_column = [name_column_renomear, name_column]
                    self.tableManip.del_column = self.column_Data_semana
                    self.table_full = self.tableManip.table
                    # num_name_column_sma_full += 1

    def merge_full_configPagamento(self):
        text_te = 'Combinar a tabela unificada com a '
        text_te += 'tabela de Configuração de Pagamento. '
        self.father.prog1(text_te)
        ''' manipular table ATA  e colocar na table_full'''
        if self.mix is False or self.table_full.empty:
            # self.table_full = load_table(self.arqtableMerge)
            return

        self.tableManip.column_Cargo = self.column_Cargo
        self.tableManip.column_Administradora = self.column_Administradora
        self.tableManip.column_Tipo_Pagamento = self.column_Tipo_Pagamento
        self.tableManip.column_Index = self.column_Index

        self.tableManip.table = self.table_full
        # mescla os valores da tablea ConfigPagamento com table_full
        self.tableManip.add_columns_full = self.table_Comissoes_ConfigPagamento
        self.table_full = self.tableManip.table

    def column_add(self):
        text_te = 'Incorporar as colunas de totais e cota correspondentes à '
        text_te += 'tabela agregada.'
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            # self.table_full = load_table(self.arqtableMerge)
            return
        # Variaveis
        self.tableManip.column_vendedor = self.column_Vendedor
        self.tableManip.column_gerente = self.column_gerente
        self.tableManip.column_cargo_gerente_geral = self.column_cargo_gerente_geral
        self.tableManip.column_credito = self.column_Credito
        self.tableManip.column_periodo_valor_qtd_vendas = self.column_periodo_valor_qtd_vendas
        self.tableManip.column_periodo_valor_qtd_vendas_Gerente = self.column_periodo_valor_qtd_vendas_Gerente
        self.tableManip.column_periodo_valor_qtd_vendas_Gerente_Geral = self.column_periodo_valor_qtd_vendas_Gerente_Geral
        self.tableManip.column_qtd_valor_vend = self.column_qtd_valor_vend
        self.tableManip.column_1p_referencia = self.column_1p_referencia
        self.tableManip.column_data_entrega = self.column_Data_de_Entrega
        self.tableManip.column_data_cad_adm = self.column_Data_Cad_Adm
        # self.tebleManip.column_ata_entrega = self.column_ATA_Entrega

        self.tableManip.keyword_periodo_valor_qtd = self.keyword_periodo_valor_qtd
        self.tableManip.keyword_1p_referencia = self.keyword_1p_referencia

        self.tableManip.list_columns_ata_mes_sma = self.list_columns_ata_mes_sma

        self.tableManip.table = self.table_full
        # programa:
        self.tableManip.alter_value_line_total_sum = self.word_column_total
        # retorno
        self.table_full = self.tableManip.table
        self.list_list_column_orden_total = self.tableManip.list_list_column_orden_total

    def order_column(self):
        ''' Ordenar colunas da tabela para a forma que quiser'''
        text_te = 'Ordenar as colunas, colocando as mais importantes no início '
        self.father.prog1(text_te)
        if self.mix is False or self.table_full.empty:
            # self.table_full = load_table(self.arqtableMerge)
            return
        for list_columns_ata in self.list_list_columns_order:
            for columns_ata in list_columns_ata:
                # remover coluna Mes Xº Parc
                # if 'Mes ' in column_ata and 'º Parc' in column_ata:
                if columns_ata not in self.listColumnsStart:
                    self.listColumnsStart.append(columns_ata)
        columnsList = self.table_full.columns.to_list()
        columnsListNew = []
        for key, columnList in enumerate(columnsList):
            if key == 0:
                for listColumnStart in self.listColumnsStart:
                    columnsListNew.append(listColumnStart)
            if columnList in self.listColumnsStart:
                continue
            columnsListNew.append(columnList)
        self.table_full = self.table_full[columnsListNew]

    def save_full(self):
        text_te = 'Salvar uma tabela previamente consolidada e tratada.'
        self.father.prog1(text_te)
        if self.mix is False:
            return
        # salvar a tabela
        if self.table_full.empty:
            return
        self.table_full = create_table(self.table_full, self.arqtableMerge)

    def test_full_double(self):
        text_te = 'Realizar um teste de integridade entre a tabela '
        text_te += 'consolidada e a tabela de cadastro de consorciado para '
        text_te += 'identificar discrepâncias nas vendas. '
        text_te += 'Registrar os resultados no arquivo de log (log.txt).'
        self.father.prog1(text_te)
        ''' teste para sabEr a diferença e mostra que é diferente.
        pois se existir diferença ele ira salvar no log'''
        if self.table_full.empty or self.table_Cadastro_Consorciado.empty or self.connected is False or self.mix is False:  # noqa
            return
        text = 'OK'
        num_line = len(self.table_full)
        nDiferente = 0
        for line_1 in range(num_line):
            line_2 = line_1 - nDiferente
            clit_1 = self.table_full.at[line_1, self.column_Cliente]
            clit_2 = self.table_Cadastro_Consorciado.at[line_2, self.column_Cliente]
            if clit_1 != clit_2:
                vend_1 = self.table_full.at[line_1, self.column_Vendedor]
                vend_2 = self.table_Cadastro_Consorciado.at[line_2, self.column_Vendedor]
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
        if self.table_Comissoes_ConfigPagamento.empty or self.connected is False or self.mix is False:  # noqa
            return
        self.tableManip.table = self.table_Comissoes_ConfigPagamento
        colummns = [
            self.column_Cargo,
            self.column_Administradora,
            self.column_Tipo_Pagamento,
            'Dt pag. por',
            'dia pag.',
            '1P recebera',
            'D+ recebera',
            'FAT recebera',
            self.column_Index]
        self.tableManip.edit_data_column_all = colummns
        # table = self.tableManip.table
        # self.tableManip.table = table
        columns = [self.column_Cargo, self.column_Administradora, self.column_Tipo_Pagamento]
        self.tableManip.row_duplicate_column = columns
        self.table_duplicate = self.tableManip.table_duplicate
        if self.table_duplicate.empty:
            text = 'OK: tabela_Comissões_ConfigPagamento não tem duplicância.'
        else:
            text = 'ERRO: tabela_Comissões_ConfigPagamento '
            text += 'Existe arquivos duplicados que podem gera vendas '
            text += 'duplicadas. Tem que ser analizada as colunas: '
            text += 'Cargo, Administradora, Tipo Pagamento'
            self.fileManip.writeLog = text
            self.table_duplicate = create_table(self.table_duplicate, self.arqTableComissoesConfigPagDupl)  # noqa
        # tratar tabela para não existir duplicancia

    def test_table_Cadastro_Funcionario(self):
        text_te = 'Realizar um teste na tabela de cadastro de funcionários '
        text_te += 'para identificar casos de homônimos com funções distintas. '
        text_te += 'Registrar os resultados no arquivo de log (log.txt).'
        self.father.prog1(text_te)
        if self.table_Cadastro_Funcionario.empty or self.connected is False or self.mix is False:
            return
        list_funcionario_double = self.table_Cadastro_Funcionario[self.column_Nome_Funcionario].tolist(
        )
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

    def test_primary_key(self):
        text_te = 'Realizar uma verificação de integridade na tabela '
        text_te += 'consolidada para evitar a duplicação de chaves primárias. '
        text_te += 'Registrar os resultados no arquivo de log (log.txt).'
        self.father.prog1(text_te)
        if (self.table_full.empty or self.connected is False or self.mix is False):
            return
        list_primary_key = self.table_full[self.column_primary_key].tolist()
        text = 'OK: tabelaMergem full não exite chave primaria duplicada. '
        while list_primary_key != []:
            primary_key = list_primary_key.pop()
            if primary_key in list_primary_key:
                text = 'ERRO: table_merge '
                text += f'Foi repetido o primary key ({primary_key}).\n'
                text += 'Isso siguinifica que tem vendas duplicados, '
                text += 'devido a mesclagem entre as tabelas. '
                self.fileManip.writeLog = text

    def ata_atrasada_adiantada_igual(self):
        self.tableManip.table = self.table_full
        self.tableManip.add_value_situacao_num_ATA = self.list_list_columns_situacao_num_ATA
        self.table_full = self.tableManip.table

    def calc_percentual(self):
        self.tableManip.table = self.table_full
        self.tableManip.column_vendedor = self.column_Vendedor
        self.tableManip.column_ata_entrega = self.column_ATA_Entrega
        self.tableManip.column_total_ata_entrega = self.column_Total_ATA_Entrega
        self.tableManip.column_credito = self.column_Credito
        self.tableManip.add_value_porcentagem = self.list_list_columns_percentage
        self.table_full = self.tableManip.table
        # ordenar

        # colunas total
        self.tableManip.list_columns_ata_mes_sma = self.list_columns_ata_mes_sma
        self.tableManip.keyword_periodo_valor_qtd = self.keyword_periodo_valor_qtd
        self.tableManip.columns_total = self.word_column_total
        list_list_column_orden_total = self.tableManip.list_list_column_orden_total
        for list_column_orden_total in list_list_column_orden_total:
            for column_orden_total in list_column_orden_total:
                self.listColumnsStart.append(column_orden_total)

        for list_columns_ata in self.list_list_columns_order:
            for columns_ata in list_columns_ata:
                # remover coluna Mes Xº Parc
                # if 'Mes ' in column_ata and 'º Parc' in column_ata:
                if columns_ata not in self.listColumnsStart:
                    self.listColumnsStart.append(columns_ata)

        columnsList = self.table_full.columns.to_list()
        columnsListNew = []
        for key, columnList in enumerate(columnsList):
            if key == 0:
                for listColumnStart in self.listColumnsStart:
                    columnsListNew.append(listColumnStart)
            if columnList in self.listColumnsStart:
                continue
            columnsListNew.append(columnList)
        self.table_full = self.table_full[columnsListNew]
        # salvar
        self.table_full = create_table(self.table_full, self.arqTableTeste1)
        # print(self.table_full)
