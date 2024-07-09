# from dbm import _Database
import os
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from components.connect import Connect
from components.fileManip import FileManip
from components.tableManip import TableManip
from components.xpathManip import XpathManip
from components.table_manip_value import Table_manip_value
from components.date_weekly import Date_weekly
# from PySide6.QtCore import QThread
from typing import Optional


def load_table(path):
    table_loaded = pd.read_csv(path, sep=';', encoding='utf-8', dtype=str)
    # remover espaços inicio fim
    table_loaded.columns = (table_loaded.columns.str.strip())
    return table_loaded


def create_table(table_created, path):
    table_created.columns = (table_created.columns.str.strip())
    table_created.to_csv(path, sep=';', index=False, header=True)
    return table_created


class Main_table:
    def __init__(self, *args, **kwargs) -> None:
        self.tableManip = TableManip()
        self.table_manip_value = Table_manip_value()
        self.date_weekly = Date_weekly()
        self.fileManip = FileManip()

        self.siteSircon = "https://app.sistemasircon.com.br/login"
        self.user = 'usuario@gmail.com'
        self.password = 'Senha'
        self.month = 1

        # variavel para log

        # self.new_table_Cadastro_Consorciado = True
        # self.new_table_Cadastro_Funcionario = True
        # self.new_table_Cadastro_Ata = True
        # self.new_table_Comissoes_Configuracao = True
        # self.new_table_Comissoes_ConfigPagamento = True

        self.new_table_Cadastro_Consorciado = False
        self.new_table_Cadastro_Funcionario = False
        self.new_table_Cadastro_Ata = False
        self.new_table_Comissoes_Configuracao = False
        self.new_table_Comissoes_ConfigPagamento = False

        self.mix = False
        self.mix = True

        self.connected = True

        self.start = True

        self.path_source = Path(__file__).parent
        self.path_tables = self.path_source / 'tables'
        self.name_arq = 'table_Cadastro_Consorciado.csv'
        self.arqTableCadastroConsorciado = self.path_tables / self.name_arq
        self.name_arq = 'table_Cadastro_Funcionario.csv'
        self.arqTableCadastroFuncionario = self.path_tables / self.name_arq
        self.name_arq = 'table_Cadastro_Ata.csv'
        self.arqTableCadastroAta = self.path_tables / self.name_arq
        self.name_arq = 'table_Comissoes_Configuracao.csv'
        self.arqTableComissoesConfiguracao = self.path_tables / self.name_arq
        self.name_arq = 'table_Comissoes_ConfigPagamento.csv'
        self.arqTableComissoesConfigPag = self.path_tables / self.name_arq
        self.name_arq = 'table_Comissoes_ConfigPagTratada.csv'
        self.arqTableComissoesConfigPagTratada = (
            self.path_tables / self.name_arq)
        self.name_arq = 'table_Comissoes_ConfigPagamento_Dupl.csv'
        self.arqTableComissoesConfigPagDupl = self.path_tables / self.name_arq

        self.name_arq = 'tableMerge.csv'
        self.arqtableMerge = self.path_tables / self.name_arq

        self.name_arq = 'table_datas_semanais.csv'
        self.arqTableDatasSemanais = self.path_tables / self.name_arq
        self.name_arq = 'table_teste1.csv'

        self.name_arq = 'log.txt'
        self.arq_log = self.path_source / self.name_arq
        self.fileManip.arq_log = self.arq_log

        self.arqTableTeste1 = self.path_tables / self.name_arq
        self.name_arq = 'table_teste2.csv'
        self.arqTableTeste2 = self.path_tables / self.name_arq
        self.name_arq = 'table_teste3.csv'
        self.arqTableTeste3 = self.path_tables / self.name_arq
        # table_full.to_csv(
        # self.arqTableTeste1, index=False, header=True, sep=';')
        # table_full.to_csv(
        # self.arqTableTeste2, index=False, header=True, sep=';')
        # table_full.to_csv(
        # self.arqTableTeste3, index=False, header=True, sep=';')

        self.pathDonwload = os.environ['USERPROFILE'] + '\\Downloads'
        self.arqDonwloadSales = self.pathDonwload + '\\consorciados.csv'
        self.arqDonwloadFunction = self.pathDonwload + '\\funcionarios.csv'

        '''Variaveis'''
        self.column_primary_key = 'PK'
        self.column_total_vendidos = 'Total'
        self.column_vendedor = 'Vendedor'
        self.column_gerente = 'Gerente'
        self.column_credito = 'Crédito'
        self.column_ata_entrega = 'ATA Entrega'
        self.column_sma_ent = 'Sma Ent'
        self.column_ata_cad_adm = 'ATA Cad Adm'
        self.column_sma_cad_adm = 'Sma Cad Adm'

        self.list_columns_total_vendidos = [
            self.column_total_vendidos, self.column_vendedor,
            self.column_gerente, self.column_credito,
            self.column_ata_entrega, self.column_sma_ent,
            self.column_ata_cad_adm, self.column_sma_cad_adm]

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
            'Cargo', 'Administradora', 'Tipo Pagamento', 'Dt pag. por',
            'dia pag.', '1P recebera', '1P referencia', '1P periodo inicial',
            '1P dt inicial', '1P periodo final', '1P dt final', 'D+ recebera',
            'D+ referencia', 'D+ perido inicial', 'D+ dt inicial',
            'D+ periodo final', 'D+ dt final',
            'FAT recebera', 'FAT referencia', 'FAT perido inicial',
            'FAT dt inicial', 'FAT periodo final', 'FAT dt final', 'Index'
        ]

        self.list_columns_ATA = [
            ['Situação', 'Data de Entrega', 'ATA Entrega', 'Sma Ent'],
            ['Situação', 'Data Cad. Adm', 'ATA Cad Adm', 'Sma Cad Adm']
        ]

        self.columns_data_venc = ['Data Venc. ', 'º Parc']
        self.columns_ata = ['ATA ', 'º Parc']
        self.columns_sma = ['Sma ', 'º Parc']
        self.columns_situacao = ['Situação ', 'º Parc']

        self.listColumnsStart = [
            'Administradora', 'Cargo', 'Cargo_Gerente', 'Vendedor',
            'Gerente', 'Cliente', 'Crédito', 'Valor Parc. Inicial',
            'Data Pag. 1º Parc', 'Dt pag. por', 'dia pag.',
            '1P recebera', 'D+ recebera', 'FAT recebera',
            '1P referencia', 'D+ referencia'
        ]

        self.driver: Optional[webdriver.Chrome] = None
        self.connect = Connect()
        self.table_Cadastro_Consorciado: pd.DataFrame = pd.DataFrame()
        self.table_Cadastro_Funcionario: pd.DataFrame = pd.DataFrame()
        self.table_Cadastro_Ata: pd.DataFrame = pd.DataFrame()
        self.table_Comissoes_Configuracao: pd.DataFrame = pd.DataFrame()
        self.table_Comissoes_ConfigPagamento: pd.DataFrame = pd.DataFrame()
        self.table_date_weekly: pd.DataFrame = pd.DataFrame()
        self.table_Cadastro_funcionario_gerente: pd.DataFrame = pd.DataFrame()
        self.table_Comissoes_Configuracao_gerente: pd.DataFrame = (
            pd.DataFrame())
        self.table_full: pd.DataFrame = pd.DataFrame()
        self.table_duplicate: pd.DataFrame = pd.DataFrame()

    # ################### ABRIR SITES ########################################

    def openSite(self):
        ''' defined '''
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
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
                print('FALSE => CONNECT FALSO | Usuário e/ou senha errado')
                self.new_table_Cadastro_Consorciado = False
                self.new_table_Cadastro_Funcionario = False
                self.new_table_Cadastro_Ata = False
                self.new_table_Comissoes_Configuracao = False
                self.new_table_Comissoes_ConfigPagamento = False
                return False

    def log_start_end(self):
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

    def create_table_Cadastro_Consorciado(self):
        '''table_Cadastro_Consorciado'''
        if self.new_table_Cadastro_Consorciado:
            self.connected = self.openSite()
            if self.connected is False:
                return
            self.connect.file = self.arqDonwloadSales  # type: ignore
            self.connect.month = self.month
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
            self.table_Cadastro_Consorciado = load_table(
                self.arqTableCadastroConsorciado)

    def create_table_Cadastro_Funcionario(self):
        '''table_Cadastro_Funcionario '''
        if self.new_table_Cadastro_Funcionario:
            self.connected = self.openSite()
            if self.connected is False:
                return
            self.connect.file = self.arqDonwloadFunction  # type: ignore
            self.connect.function = self.listXpathFunction
            self.table_Cadastro_Funcionario = self.connect.dfNew
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.table_Cadastro_Funcionario = create_table(
                self.table_Cadastro_Funcionario,
                self.arqTableCadastroFuncionario)
        else:
            self.table_Cadastro_Funcionario = load_table(
                self.arqTableCadastroFuncionario)

    def create_table_Cadastro_Ata(self):
        '''#################### LIMITAR PESQUISAS ##########################'''
        if self.new_table_Cadastro_Ata is True:
            self.connected = self.openSite()
            if self.connected is False:
                return
            self.connect.month = self.month
            self.connect.tagSon = self.tag_data
            self.connect.tagFather = self.tag_row
            self.connect.tagGet = self.tag_outerHTML
            self.connect.tagReturnValue
            self.limited_search_administradoras()
            self.limited_search_cargos()
            self.connect.minutes = self.listXpathMinutes
            self.table_Cadastro_Ata = self.connect.table
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.tableManip.table = self.table_Cadastro_Ata  # type: ignore
            list_columns_rename = [[1, 'Mes'],
                                   [2, 'Periodo_inicial'],
                                   [3, 'Periodo_final']]
            for column_rename in list_columns_rename:
                self.tableManip.rename_name_column_indix = column_rename
            self.tableManip.add_column_clone_two_columns = [
                'ATA', 'Mes', 'Ano']
            self.table_Cadastro_Ata = self.tableManip.table
            self.table_Cadastro_Ata = create_table(
                self.table_Cadastro_Ata,
                self.arqTableCadastroAta)
        else:
            self.table_Cadastro_Ata = load_table(self.arqTableCadastroAta)

    def create_table_Comissoes_Configuracao(self):
        '''table_Comissoes_Configuracao'''
        if self.new_table_Comissoes_Configuracao:
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
            self.limited_search_administradoras()
            self.connect.pressXpathResultListValue = self.xpathAdministradora
            # criar lista de administradoras + tabela de recebiemnto
            self.connect.pressListValueXpathResultListValue = (
                self.xpathTabelaRecebimento)
            # criar lista de administradoras + tabela de recebiemnto + cargos
            self.limited_search_cargos()
            self.connect.pressListValueXpathResultListValueDouble = (
                self.xpathCargo)
            # alterar a tagets
            self.connect.tagGet = self.tag_value
            self.connect.tagReturnValue
            # lista administradoras, tabela de recebiemnto, cargos, valores
            self.connect.pressListValueResultListValueTriple = (
                self.listCampoCotaPeriodoParcela)
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
            self.connect.listColunmToTable
            self.table_Comissoes_Configuracao = self.connect.renameColumn
            if self.driver:
                self.driver.quit()
                self.driver = None
            self.table_Comissoes_Configuracao = create_table(
                self.table_Comissoes_Configuracao,
                self.arqTableComissoesConfiguracao)
        else:
            self.table_Comissoes_Configuracao = load_table(
                self.arqTableComissoesConfiguracao)

    def create_table_Comissoes_ConfigPagamento(self):
        '''table_Comissoes_ConfigPagamento'''
        if self.new_table_Comissoes_ConfigPagamento:
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
            # list os valores existentes no campos cargos, administradora,
            # tipoPagamento
            self.limited_search_administradoras()
            self.limited_search_cargos()
            self.connect.pressListXpathReturnListValue = (
                self.listXpathCargAdminsPag)
            self.connect.pressListValueReturnListValue = (
                self.listXpathDtPagamentoParcelas)
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
            self.table_Comissoes_ConfigPagamento = load_table(
                self.arqTableComissoesConfigPag)

    # def limited_search_chosse(self):
    #     valueAdministradora = ['DISAL']
    #     valueChooseCargo = [
    #         'CONSULTOR CLT - A PARTIR JAN-2018',
    #         'CONSULTOR DE PARCEIRO'
    #     ]
    #     self.connect.valueAdministradora = valueAdministradora
    #     self.connect.cargo = valueChooseCargo

    # def limited_search_delete_word(self):
    #     valueChooseTabelarecebimento = ['FERIAS']
    #     self.connect.listExistTabelarecebimento = (
    #       valueChooseTabelarecebimento)

    def date_weekly_new(self):
        '''tabela numero da semana no mes'''
        if self.connected is False:
            print(f'False => date_weekly_new')
            return
        self.date_weekly.year_weeklys = 24
        self.date_weekly.create_weekYear_week_date = None
        self.date_weekly.edit_weekYear_week_date_separate_week = None
        self.date_weekly.edit_weekYear_week_date_separate_weekMonth = None
        self.date_weekly.edit_weekMonth_week_date = None
        self.date_weekly.create_table_weekMonth_week_date = ['N Semana Mes',
                                                             'Data semana',
                                                             'Dia semana']
        self.table_date_weekly = self.date_weekly.return_table
        self.table_date_weekly = create_table(
            self.table_date_weekly,
            self.arqTableDatasSemanais)

    def table_manip_funcionario(self):
        ''' manipular table_Cadastro_Funcionario, para alterar os Nomes
        duplicados com os Cargos, que gera comissão duplicada, pois o mesmo
        tem dois ou mais cargos'''
        if self.table_Cadastro_Funcionario.empty or self.connected is False:
            print(f'False => table_manip_funcionario')
            return
        self.table_manip_value.table = self.table_Cadastro_Funcionario
        self.table_manip_value.row_duplicate_column = ['Nome']
        self.table_manip_value.list_columns_one_two = ['Nome', 'Cargo']
        self.table_manip_value.edit_data_column_2 = ['Nome', 'Cargo']
        self.table_Cadastro_Funcionario = self.table_manip_value.table
        self.table_Cadastro_funcionario_gerente = (
            self.table_Cadastro_Funcionario)
        self.tableManip.table = self.table_Cadastro_Funcionario
        self.tableManip.rename_name_column = ['Cargo', 'Cargo_funcionario']
        self.table_Cadastro_Funcionario = self.tableManip.table

    def table_manip_cadastro_consorciado(self):
        ''' manipular table_Cadastro_Consorciado, para altera coluna Vendedor
        e igualar aos alterados no table_Cadastro_Funcionario'''
        if self.table_Cadastro_Consorciado.empty or (
                self.connected is False):
            print(f'False => table_manip_cadastro_consorciado')
            return
        self.table_manip_value.table = self.table_Cadastro_Consorciado
        self.table_manip_value.data_duplicate_change = 'Vendedor'
        self.table_Cadastro_Consorciado = self.table_manip_value.table

    def table_manip_comissoes_configuracao(self):
        ''' manipular table_Comissoes_Configuracao remover as duplicação nas
        colunas 'Administradora' e 'Cargo' '''
        if self.table_Comissoes_Configuracao.empty or (
                self.connected is False):
            print(f'False => table_manip_comissoes_configuracao')
            return
        cols_comConf_rept = ['Administradora', 'Cargo',
                             'Tabela de recebimento']
        self.table_manip_value.table = self.table_Comissoes_Configuracao
        self.table_manip_value.row_duplicate_column = cols_comConf_rept
        self.table_manip_value.list_columns_one_two_three = cols_comConf_rept
        self.table_manip_value.edit_data_column_3 = cols_comConf_rept
        self.table_Comissoes_Configuracao = self.table_manip_value.table
        self.table_Comissoes_Configuracao.rename(
            columns={'Tabela de recebimento': 'Tabela'}, inplace=True)

    def table_manip_Cadastro_funcionario_gerente(self):
        if self.table_Cadastro_funcionario_gerente.empty or (
                self.connected is False):
            print(f'False => table_manip_Cadastro_funcionario_gerente')
            return
        self.tableManip = TableManip()
        names_columns = self.table_Cadastro_funcionario_gerente.columns
        self.tableManip.table = self.table_Cadastro_funcionario_gerente
        for name_column in names_columns:
            name_column_gerente = name_column + '_Gerente'
            self.tableManip.rename_name_column = [
                name_column, name_column_gerente]
        self.table_Cadastro_funcionario_gerente = self.tableManip.table

    def table_manip_comissoes_configuracao_gerente(self):
        if self.table_Comissoes_Configuracao.empty or (
                self.connected is False):
            print(f'False => table_manip_comissoes_configuracao_gerente')
            return
        self.table_Comissoes_Configuracao_gerente = (
            self.table_Comissoes_Configuracao)
        self.tableManip = TableManip()
        names_columns = self.table_Comissoes_Configuracao_gerente.columns
        self.tableManip.table = self.table_Comissoes_Configuracao_gerente
        for name_column in names_columns:
            name_column_gerente = name_column + '_Gerente'
            self.tableManip.rename_name_column = [name_column,
                                                  name_column_gerente]
        self.table_Comissoes_Configuracao_gerente = self.tableManip.table

    def merge_star(self):
        if (
            self.new_table_Cadastro_Consorciado
            or self.new_table_Cadastro_Funcionario
            or self.new_table_Cadastro_Ata
            or self.new_table_Comissoes_Configuracao
            or self.new_table_Comissoes_ConfigPagamento
        ):
            print(f'True => merge_star')
            self.mix = True
        if self.connected is False:
            print(f'False => merge_star')
            self.mix = False

    def merge_consorciado_funcionario(self):
        if self.mix is False or self.table_Cadastro_Consorciado.empty or (
           self.table_Cadastro_Funcionario.empty
           ):
            print(self.mix is False,
                  self.table_Cadastro_Consorciado.empty,
                  self.table_Cadastro_Funcionario.empty)
            print(f'False => merge_consorciado_funcionario')
            self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_Cadastro_Consorciado,
            self.table_Cadastro_Funcionario,
            left_on='Vendedor',
            right_on='Nome',
            how='left'
        )

    def merge_consorciado_funcionario_gerente(self):
        if self.mix is False or self.table_full.empty or (
           self.table_Cadastro_funcionario_gerente.empty
           ):
            print(f'False => merge_consorciado_funcionario_gerente')
            self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Cadastro_funcionario_gerente,
            left_on='Gerente',
            right_on='Nome_Gerente',
            how='left'
        )

    def merge_full_comissoes_configuracao(self):
        if self.mix is False or self.table_full.empty or (
           self.table_Comissoes_Configuracao.empty
           ):
            print(f'False => merge_full_comissoes_configuracao')
            self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Comissoes_Configuracao,
            on=['Administradora', 'Cargo', 'Tabela'],
            how='left')

    def merge_full_comissoes_configuracao_gerente(self):
        if self.mix is False or self.table_full.empty or (
            self.table_Comissoes_Configuracao_gerente.empty
        ):
            print(f'False => merge_full_comissoes_configuracao_gerente')
            self.table_full = load_table(self.arqtableMerge)
            return
        self.table_full = pd.merge(
            self.table_full,
            self.table_Comissoes_Configuracao_gerente,
            left_on=['Administradora', 'Cargo_Gerente', 'Tabela'],
            right_on=['Administradora_Gerente', 'Cargo_Gerente',
                      'Tabela_Gerente'],
            how='left')

    def create_columns_ata(self):
        # descori a quantidade de num_atas_parc
        if self.mix is False:
            print(f'False => create_columns_ata')
            self.table_full = load_table(self.arqtableMerge)
            return
        num_atas_parc = 10000
        for i in range(2, num_atas_parc + 1):
            name_column_data_venc = (
                self.columns_data_venc[0] + str(i) + (
                    self.columns_data_venc[1])
            )
            if name_column_data_venc in self.table_full.columns:
                name_column_ata = (
                    self.columns_ata[0] + str(i) + self.columns_ata[1])
                name_column_sma = (
                    self.columns_sma[0] + str(i) + self.columns_sma[1])
                name_column_situacao = (
                    self.columns_situacao[0] + str(i) + (
                        self.columns_situacao[1])
                )
                self.list_columns_ATA.append(
                    [name_column_situacao,
                        name_column_data_venc,
                        name_column_ata,
                        name_column_sma,
                     ]
                )
            else:
                break

    def merge_full_weekly(self):
        '''# mesclar table_full com table_date_weekly_changed'''
        if self.mix is False or self.table_full.empty or (
            self.table_date_weekly.empty
        ):
            print(f'False => merge_full_weekly')
            self.table_full = load_table(self.arqtableMerge)
            return
        self.tableManip.table = self.table_date_weekly
        self.tableManip.del_column = 'Dia semana'
        table_date_weekly_changed = self.tableManip.table
        for columns_date in self.list_columns_ATA:
            name_column_data_venc = columns_date[1]
            name_column_sma = columns_date[3]
            self.table_full = pd.merge(
                self.table_full,
                table_date_weekly_changed,
                left_on=name_column_data_venc,
                right_on='Data semana',
                how='left'
            )
            self.tableManip.table = self.table_full
            self.tableManip.rename_name_column = [
                'N Semana Mes', name_column_sma]
            self.tableManip.del_column = 'Data semana'
            self.table_full = self.tableManip.table

    def merge_full_ata(self):
        ''' manipular table ATA  e colocar na table_full'''
        if self.mix is False or self.table_full.empty:
            print(f'False => merge_full_ata')
            self.table_full = load_table(self.arqtableMerge)
            return
        self.table_manip_value.table_2 = self.table_Cadastro_Ata
        for date_ATA in self.list_columns_ATA:
            name_column_data_venc = date_ATA[1]
            name_column_ata = date_ATA[2]
            self.tableManip.table = self.table_full
            self.tableManip.add_value_fixed_column = [name_column_ata]
            self.table_full = self.tableManip.table
            self.table_manip_value.table = self.table_full
            self.table_manip_value.edit_data_column_ATA = [
                name_column_data_venc,
                name_column_ata,
                'Periodo_inicial',
                'Periodo_final',
                'ATA']
            self.table_full = self.table_manip_value.table
        self.table_manip_value.table_2 = (
            self.table_Comissoes_ConfigPagamento)
        self.table_manip_value.add_columns_full = [
            'Cargo',
            'Administradora',
            'Tipo Pagamento',
            'Index']
        self.table_full = self.table_manip_value.table

    def column_add(self):
        if self.mix is False or self.table_full.empty:
            print(f'False => column_add')
            self.table_full = load_table(self.arqtableMerge)
            return
        self.tableManip.table = self.table_full
        self.tableManip.alter_value_line_total_sum = (
            self.list_columns_total_vendidos)
        self.table_full = self.tableManip.table

    def order_column(self):
        ''' Ordenar colunas da tabela para a forma que quiser'''
        if self.mix is False or self.table_full.empty:
            print(f'False => order_column')
            self.table_full = load_table(self.arqtableMerge)
            return
        for columns_ata in self.list_columns_ATA:
            for column_ata in columns_ata:
                if column_ata not in self.listColumnsStart:
                    self.listColumnsStart.append(column_ata)
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
        # salvar a tabela
        if self.table_full.empty:
            print(f'False => save_full')
            return
        self.table_full = create_table(self.table_full, self.arqtableMerge)

    def test_full_double(self):
        ''' teste para sabEr a diferença e mostra que é diferente.
        pois se existir diferença ele ira salvar no log'''
        if self.table_full.empty or self.table_Cadastro_Consorciado.empty or (
            self.connected is False or self.mix is False
        ):
            print(f'False => test_full_double')
            return
        text = 'OK'
        num_line = len(self.table_full)
        nDiferente = 0
        for line_1 in range(num_line):
            line_2 = line_1 - nDiferente
            clit_1 = self.table_full.at[line_1, 'Cliente']
            clit_2 = self.table_Cadastro_Consorciado.at[line_2, 'Cliente']
            if clit_1 != clit_2:
                vend_1 = self.table_full.at[line_1, 'Vendedor']
                vend_2 = self.table_Cadastro_Consorciado.at[line_2, 'Vendedor']
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
        print(text)
        self.fileManip.writeLog = text

    def test_table_Comissoes_ConfigPagamento(self):
        ''' manipular table_comissoes_configuPagamento'''
        if self.table_Comissoes_ConfigPagamento.empty or (
                self.connected is False or self.mix is False):
            print(f'False => test_table_Comissoes_ConfigPagamento')
            return
        self.table_manip_value.table = self.table_Comissoes_ConfigPagamento
        colummns = [
            'Cargo', 'Administradora', 'Tipo Pagamento', 'Dt pag. por',
            'dia pag.', '1P recebera', 'D+ recebera', 'FAT recebera', 'Index']
        self.table_manip_value.edit_data_column_all = colummns
        table = self.table_manip_value.table
        self.table_manip_value.table = table
        columns = ['Cargo', 'Administradora', 'Tipo Pagamento']
        self.table_manip_value.row_duplicate_column = columns
        self.table_duplicate = self.table_manip_value.table_duplicate
        if self.table_duplicate.empty:
            text = 'OK: tabela_Comissões_ConfigPagamento não tem duplicância.'
        else:
            text = 'ERRO: tabela_Comissões_ConfigPagamento '
            text += 'Existe arquivos duplicados que podem gera vendas '
            text += 'duplicadas. Tem que ser analizada as colunas: '
            text += 'Cargo, Administradora, Tipo Pagamento'
            self.fileManip.writeLog = text
            self.table_duplicate = create_table(
                self.table_duplicate,
                self.arqTableComissoesConfigPagDupl)
        print(text)
        # tratar tabela para não existir duplicancia
        # table_Comissoes_ConfigPagTratada = self.table_manip_value.table
        # table_Comissoes_ConfigPagTratada.to_csv(
        #     self.arqTableComissoesConfigPagTratada,
        #     index=False, header=True, sep=';')

    def test_table_Cadastro_Funcionario(self):
        if (self.table_Cadastro_Funcionario.empty or self.connected is False
                or self.mix is False):
            print(f'False => test_table_Cadastro_Funcionario')
            return
        list_funcionario_double = (
            self.table_Cadastro_Funcionario['Nome'].tolist())
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
        if (self.table_full.empty or self.connected is False
                or self.mix is False):
            print(f'False => test_primary_key')
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
        print(text)


if __name__ == '__main__':
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    main = Main_table()
    main.log_start_end()
    main.create_table_Cadastro_Consorciado()
    main.create_table_Cadastro_Funcionario()
    main.create_table_Cadastro_Ata()
    main.create_table_Comissoes_Configuracao()
    main.create_table_Comissoes_ConfigPagamento()
    main.date_weekly_new()
    main.table_manip_funcionario()
    main.table_manip_cadastro_consorciado()
    main.table_manip_comissoes_configuracao()
    main.test_table_Comissoes_ConfigPagamento()
    main.table_manip_Cadastro_funcionario_gerente()
    main.test_table_Cadastro_Funcionario()
    main.table_manip_comissoes_configuracao_gerente()
    main.merge_star()
    main.merge_consorciado_funcionario()
    main.merge_consorciado_funcionario_gerente()
    main.merge_full_comissoes_configuracao()
    main.merge_full_comissoes_configuracao_gerente()
    main.create_columns_ata()
    main.merge_full_weekly()
    main.merge_full_ata()
    main.column_add()
    main.order_column()
    main.save_full()
    main.test_full_double()
    main.test_primary_key()
    main.log_start_end()
