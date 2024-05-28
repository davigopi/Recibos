import os
from pathlib import Path
# from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# import datetime
# from datetime import date
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from typing import Union
from components.connect import Connect
from components.fileManip import FileManip
from components.tableManip import TableManip
from components.xpathManip import XpathManip
from components.table_manip_value import Table_manip_value
from components.date_weekly import Date_weekly
# from time import sleep

tableManip = TableManip()
table_manip_value = Table_manip_value()
date_weekly = Date_weekly()


siteSircon = "https://app.sistemasircon.com.br/login"
user = 'davigopi@gmail.com'
password = '36vad28'
month = 12

new_table_Cadastro_Consorciado = True
new_table_Cadastro_Funcionario = True
new_table_Cadastro_Ata = True
new_table_Comissoes_Configuracao = True
new_table_Comissoes_ConfigPagamento = True


# new_table_Cadastro_Consorciado = False
# new_table_Cadastro_Funcionario = False
# new_table_Cadastro_Ata = False
# new_table_Comissoes_Configuracao = False
# new_table_Comissoes_ConfigPagamento = False


path_source = Path(__file__).parent
path_tables = path_source / 'tables'
name_arq = 'table_Cadastro_Consorciado.csv'
arqTableCadastroConsorciado = path_tables / name_arq
name_arq = 'table_Cadastro_Funcionario.csv'
arqTableCadastroFuncionario = path_tables / name_arq
name_arq = 'table_Cadastro_Ata.csv'
arqTableCadastroAta = path_tables / name_arq
name_arq = 'table_Comissoes_Configuracao.csv'
arqTableComissoesConfiguracao = path_tables / name_arq
name_arq = 'table_Comissoes_ConfigPagamento.csv'
arqTableComissoesConfigPag = path_tables / name_arq
name_arq = 'table_Comissoes_ConfigPagTratada.csv'
arqTableComissoesConfigPagTratada = path_tables / name_arq
name_arq = 'table_Comissoes_ConfigPagamento_Dupl.csv'
arqTableComissoesConfigPagDupl = path_tables / name_arq
name_arq = 'table_datas_semanais.csv'
arqTableDatasSemanais = path_tables / name_arq
name_arq = 'table_teste.csv'
arqTableTeste = path_tables / name_arq
name_arq = 'log.txt'
arq_log = path_source / name_arq

pathDonwload = os.environ['USERPROFILE'] + '\\Downloads'
arqDonwloadSales = pathDonwload + '\\consorciados.csv'
arqDonwloadFunction = pathDonwload + '\\funcionarios.csv'

'''#################### TAGS ##############################################'''
tag_option = 'option'
tag_select = 'select'
tag_outerHTML = 'outerHTML'
tag_value = 'value'
tag_selected = '/option[@selected="selected"]'
tag_table = 'table'
tag_row = 'tr'
tag_data = 'td'
tag_cab = 'th'
'''#################### XPATHS #############################################'''
listXpathLog = [
    '//*[@id="form:txtUsuarioSircon"]',  # campo usuario
    '//*[@id="form:txtSenhaSircon"]',  # campo senha
    '//*[@id="form:btLogar"]'  # botao confirmar
]
# linha coluna calendario
line = 1
column = 0
xp0 = '//*[@id="menucadastro"]/a'  # menu cadastro
xp1 = '//*[@id="menucadastro"]/ul/li[5]'  # menu consorciado
xp2 = '//*[@id="pnlBloco"]/div[6]/div/div[3]/div'  # campo entrega venda inicio
xp3 = '//*[@id="ui-datepicker-div"]/div[1]/a[1]'  # botao seta para esquerda
xp4 = f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{line}]/td[{column}]'
xp5 = '//*[@id="ui-datepicker-div"]/div[3]/button[2]'  # botao fechar calend
xp6 = '//*[@id="pnlBloco"]/div[6]/div/div[4]/div'  # campo entrega venda final
xp7 = '//*[@id="btnConsultar"]'  # botao consultar
xp8 = '//*[@id="btnGerarXls"]'  # botao de download
listXpathSales = [xp0, xp1, xp2, xp3, xp4, xp5, xp6, xp3, xp4, xp5, xp7, xp8]
listXpathComissoesConfiguracao = [
    '//*[@id="menufinan"]',  # comissões
    '//*[@id="menufinan"]/ul/li[2]'  # Config
]
xpathTipoComissao = [
    '//*[@id="frm:tpComissao"]',
    '//*[@id="frm:tpComissao"]/option[2]'  # Pagamento
]
xpathAdministradora = '//*[@id="frm:cbAdministradora"]'
xpathTabelaRecebimento = '//*[@id="frm:cbTabelaRecebimento"]'
xpathCargo = '//*[@id="frm:cbCargo"]'
listCampoCotaPeriodoParcela = []
for num in range(30):  # quantidade de campos comissões configuracao
    listCampoCotaPeriodoParcela.append([
        f'//*[@id="frm:pnlEsacalas"]/div[{str(num + 1)}]',  # campo 0 a 2Father
        [f'frm:j_idt124:{num}:j_idt194',
            f'frm:j_idt124:{num}:j_idt188'],  # qtd cotas inicial
        [f'frm:j_idt124:{num}:j_idt196',
            f'frm:j_idt124:{num}:j_idt190'],  # qtd cotas final
        f'//*[@id="frm:j_idt124:{num}:j_idt182_input"]',  # data venda inicio
        f'//*[@id="frm:j_idt124:{num}:j_idt184_input"]',  # data venda fim
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
    # listXpathCampoParcela.append([listCampo, listCotaPeriodoParcela])
listXpathFunction = [
    '//*[@id="menucadastro"]/a',  # menu cadastro
    '//*[@id="menucadastro"]/ul/li[7]',  # menu funcionario
    '//*[@id="btnConsultar"]',  # botao consultar
    '//*[@id="btnGerarXls"]'  # botao consultar
]

listXpathComissoesConfPagamento = [
    '//*[@id="menufinan"]',  # comissões
    '//*[@id="menufinan"]/ul/li[3]/a'  # ConfigPagamento
]
xpathTipoComissaoPagamento = [
    '//*[@id="frm:cbTpConfig"]',
    '//*[@id="frm:cbTpConfig"]/option[1]'  # Pagamento
]
listXpathCargAdminsPag = [
    '//*[@id="frm:cbCargo"]',
    '//*[@id="frm:cbAdministradora"]',
    '//*[@id="frm:cbTpRecebimento"]'
]
listXpathDtPagamentoParcelas = [
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
    '//*[@id="frm:cbRefApuracaoFimConfirmacoes"]',  # periodo final tipo
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

listXpathMinutes = [
    '//*[@id="menucadastro"]/a',  # menu cadastro
    '//*[@id="menucadastro"]/ul/li[2]/a',  # menu Ata
    '//*[@id="frm:cbAno"]',  # Ano
    '//*[@id="frm:pnlLista"]',   # informacao OBS: alterado ordem.
    '//*[@id="frm:cbAdministradora"]',  # administradora
]

headerDtPagamentoParcelas = [
    'Cargo', 'Administradora', 'Tipo Pagamento', 'Dt pag. por', 'dia pag.',
    '1P recebera', '1P referencia', '1P periodo inicial', '1P dt inicial',
    '1P periodo final', '1P dt final', 'D+ recebera', 'D+ referencia',
    'D+ perido inicial', 'D+ dt inicial', 'D+ periodo final', 'D+ dt final',
    'FAT recebera', 'FAT referencia', 'FAT perido inicial', 'FAT dt inicial',
    'FAT periodo final', 'FAT dt final', 'Index'
]

'''#################### ABRIR SITES ########################################'''


def log_start_end():
    global start
    fileManip = FileManip()
    if start:
        text = '\n' + 'Inicio: '
        start = False
    else:
        text = 'Fim:    '
    text += str(datetime.now())
    fileManip.arq_log = arq_log
    fileManip.writeLog = text


def limited_search_chosse():
    valueAdministradora = ['DISAL']
    valueChooseCargo = [
        'CONSULTOR CLT - A PARTIR JAN-2018',
        'CONSULTOR DE PARCEIRO'
    ]
    connect.valueAdministradora = valueAdministradora
    connect.cargo = valueChooseCargo


def limited_search_delete_word():
    valueChooseTabelarecebimento = ['FERIAS']
    connect.listExistTabelarecebimento = valueChooseTabelarecebimento


def limited_search_administradoras():
    global table_Cadastro_Consorciado
    connect.valueExistAdministradoras = table_Cadastro_Consorciado


def limited_search_cargos():
    global table_Cadastro_Funcionario
    connect.valueExistCargos = table_Cadastro_Funcionario


def date_weekly_new():
    '''tabela numero da semana no mes'''
    global table_date_weekly
    date_weekly.year_weeklys = 24
    date_weekly.create_weekYear_week_date = None
    date_weekly.edit_weekYear_week_date_separate_week = None
    date_weekly.edit_weekYear_week_date_separate_weekMonth = None
    date_weekly.edit_weekMonth_week_date = None
    date_weekly.create_table_weekMonth_week_date = ['N Semana Mes',
                                                    'Data semana',
                                                    'Dia semana']
    table_date_weekly = date_weekly.return_table
    table_date_weekly.to_csv(arqTableDatasSemanais,
                             index=False, header=True, sep=';')


def table_manip_funcionario():
    ''' manipular table_Cadastro_Funcionario, para alterar os Nomes duplicados
    com os Cargos, que gera comissão duplicada, pois o mesmo tem dois ou mais
    cargos'''
    global table_Cadastro_Funcionario
    global table_Cadastro_funcionario_gerente
    table_manip_value.table = table_Cadastro_Funcionario  # type: ignore
    table_manip_value.row_duplicate_column = ['Nome']
    table_manip_value.list_columns_one_two = ['Nome', 'Cargo']
    table_manip_value.edit_data_column_2 = ['Nome', 'Cargo']
    table_Cadastro_Funcionario = table_manip_value.table
    table_Cadastro_funcionario_gerente = table_Cadastro_Funcionario
    tableManip.table = table_Cadastro_Funcionario
    tableManip.rename_name_column = ['Cargo', 'Cargo_funcionario']
    table_Cadastro_Funcionario = tableManip.table


def table_manip_cadastro_consorciado():
    ''' manipular table_Cadastro_Consorciado, para altera rcoluna Vendedor
    e igualar aos alterados no table_Cadastro_Funcionario'''
    global table_Cadastro_Consorciado
    table_manip_value.table = table_Cadastro_Consorciado  # type: ignore
    table_manip_value.data_duplicate_change = 'Vendedor'
    table_Cadastro_Consorciado = table_manip_value.table


def table_manip_comissoes_configuracao():
    ''' manipular table_Comissoes_Configuracao remover as duplicação nas
    colunas 'Administradora' e 'Cargo' '''
    global table_Comissoes_Configuracao
    table_manip_value.table = table_Comissoes_Configuracao
    table_manip_value.row_duplicate_column = ['Administradora', 'Cargo']
    table_manip_value.list_columns_one_two_three = ['Administradora',
                                                    'Cargo',
                                                    'Tabela de recebimento']
    table_manip_value.edit_data_column_3 = ['Administradora',
                                            'Cargo',
                                            'Tabela de recebimento']
    table_Comissoes_Configuracao = table_manip_value.table


def table_manip_comissao_configPagamento():
    ''' manipular table_comissoes_configuPagamento'''
    global table_Comissoes_ConfigPagamento
    table_manip_value.table = table_Comissoes_ConfigPagamento
    table_manip_value.edit_data_column_all = ['Cargo',
                                              'Administradora',
                                              'Tipo Pagamento',
                                              'Dt pag. por',
                                              'dia pag.',
                                              '1P recebera',
                                              'D+ recebera',
                                              'FAT recebera',
                                              'Index']
    table = table_manip_value.table
    table_manip_value.table = table
    table_manip_value.row_duplicate_column = ['Cargo',
                                              'Administradora',
                                              'Tipo Pagamento']

    table_duplicate = table_manip_value.table_duplicate
    table_Comissoes_ConfigPagTratada = table_manip_value.table
    table_Comissoes_ConfigPagTratada.to_csv(
        arqTableComissoesConfigPagTratada,
        index=False, header=True, sep=';')

    table_duplicate.to_csv(arqTableComissoesConfigPagDupl,  # type: ignore
                           index=False, header=True, sep=';')


def table_manip_Cadastro_funcionario_gerente():
    global table_Cadastro_funcionario_gerente
    tableManip = TableManip()
    names_columns = table_Cadastro_funcionario_gerente.columns  # type: ignore
    tableManip.table = table_Cadastro_funcionario_gerente  # type: ignore
    for name_column in names_columns:
        name_column_gerente = name_column + '_Gerente'
        tableManip.rename_name_column = [name_column, name_column_gerente]
    table_Cadastro_funcionario_gerente = tableManip.table


def table_manip_comissoes_configuracao_gerente():
    global table_Comissoes_Configuracao
    global table_Comissoes_Configuracao_gerente
    table_Comissoes_Configuracao_gerente = table_Comissoes_Configuracao
    tableManip = TableManip()
    names_columns = table_Comissoes_Configuracao_gerente.columns
    tableManip.table = table_Comissoes_Configuracao_gerente
    for name_column in names_columns:
        name_column_gerente = name_column + '_Gerente'
        tableManip.rename_name_column = [name_column, name_column_gerente]
    table_Comissoes_Configuracao_gerente = tableManip.table


def merge_consorciado_funcionario():
    global table_full
    global table_Cadastro_Consorciado
    global table_Cadastro_Funcionario
    table_full = pd.merge(
        table_Cadastro_Consorciado,  # type: ignore
        table_Cadastro_Funcionario,  # type: ignore
        left_on='Vendedor',
        right_on='Nome',
        how='left'
    )


def merge_consorciado_funcionario_gerente():
    global table_full
    global table_Cadastro_funcionario_gerente
    table_full = pd.merge(
        table_full,  # type: ignore
        table_Cadastro_funcionario_gerente,  # type: ignore
        left_on='Gerente',
        right_on='Nome_Gerente',
        how='left'
    )


def merge_full_comissoes_configuracao():
    global table_full
    global table_Comissoes_Configuracao
    table_full = pd.merge(
        table_full,
        table_Comissoes_Configuracao,
        on=['Administradora', 'Cargo'],
        how='left')


def merge_full_comissoes_configuracao_gerente():
    global table_full
    global table_Comissoes_Configuracao_gerente
    table_full = pd.merge(
        table_full,
        table_Comissoes_Configuracao_gerente,
        left_on=['Administradora', 'Cargo_Gerente'],
        right_on=['Administradora_Gerente', 'Cargo_Gerente'],
        how='left')


def merge_full_weekly():
    '''# mesclar table_full com table_date_weekly_changed'''
    global table_date_weekly
    global table_full
    tableManip.table = table_date_weekly
    tableManip.del_column = 'Dia semana'
    table_date_weekly_changed = tableManip.table
    list_columns_date_merge = [['Data de Entrega', 'Sma Ent'],
                               ['Data Cad. Adm', 'Sma Cad Adm'],
                               ['Data Pag. 2º Parc', 'Sma 2º Parc'],
                               ['Data Pag. 3º Parc', 'Sma 3º Parc'],
                               ['Data Pag. 4º Parc', 'Sma 4º Parc'],
                               ['Data Pag. 5º Parc', 'Sma 5º Parc'],
                               ['Data Pag. 6º Parc', 'Sma 6º Parc']]

    for columns_date in list_columns_date_merge:
        column_compare = columns_date[0]
        column_new_merge = columns_date[1]
        table_full = pd.merge(
            table_full,
            table_date_weekly_changed,
            left_on=column_compare,
            right_on='Data semana',
            how='left'
        )
        tableManip.table = table_full
        tableManip.rename_name_column = ['N Semana Mes', column_new_merge]
        tableManip.del_column = 'Data semana'
        table_full = tableManip.table


def merge_full_ata():
    ''' manipular table ATA  e colocar na table_full'''
    global table_full
    global table_Cadastro_Ata
    global table_Comissoes_ConfigPagamento
    table_manip_value.table_2 = table_Cadastro_Ata  # type: ignore
    list_date_ATA = [['Data de Entrega', 'ATA Entrega'],
                     ['Data Cad. Adm', 'ATA Cad Adm'],
                     ['Data Pag. 2º Parc', 'ATA 2º Parc'],
                     ['Data Pag. 3º Parc', 'ATA 3º Parc'],
                     ['Data Pag. 4º Parc', 'ATA 4º Parc'],
                     ['Data Pag. 5º Parc', 'ATA 5º Parc'],
                     ['Data Pag. 6º Parc', 'ATA 6º Parc']]
    for date_ATA in list_date_ATA:
        column_compare = date_ATA[0]
        column_new_edit = date_ATA[1]
        tableManip.table = table_full
        # tableManip.add_column_nan = [column_new_edit]
        tableManip.add_value_fixed_column = [column_new_edit]
        table_full = tableManip.table
        table_manip_value.table = table_full
        table_manip_value.edit_data_column_ATA = [column_compare,
                                                  column_new_edit,
                                                  'Periodo_inicial',
                                                  'Periodo_final',
                                                  'ATA']
        table_full = table_manip_value.table
    table_manip_value.table_2 = table_Comissoes_ConfigPagamento
    table_manip_value.add_columns_full = ['Cargo',
                                          'Administradora',
                                          'Tipo Pagamento',
                                          'Index']
    table_full = table_manip_value.table


def order_column():
    ''' Ordenar colunas da tabela para a forma que quiser'''
    global table_full
    listColumnsStart = [
        'Situação', 'Administradora',
        'Vendedor', 'Cargo',
        'Gerente', 'Cargo_Gerente',
        'Cliente', 'Crédito',
        'Valor Parc. Inicial', 'Data Pag. 1º Parc',
        'Dt pag. por', 'dia pag.',
        '1P recebera', '1P referencia',
        'Data de Entrega', 'Sma Ent', 'ATA Entrega',
        'Data Cad. Adm', 'Sma Cad Adm', 'ATA Cad Adm',
        'D+ recebera', 'D+ referencia',
        'Data Pag. 2º Parc', 'Sma 2º Parc', 'ATA 2º Parc',
        'Data Pag. 3º Parc', 'Sma 3º Parc', 'ATA 3º Parc',
        'Data Pag. 4º Parc', 'Sma 4º Parc', 'ATA 4º Parc',
        'Data Pag. 5º Parc', 'Sma 5º Parc', 'ATA 5º Parc',
        'Data Pag. 6º Parc', 'Sma 6º Parc', 'ATA 6º Parc',
        'FAT recebera',
        'Gerente', 'Cliente',
    ]
    columnsList = table_full.columns.to_list()
    columnsListNew = []
    for key, columnList in enumerate(columnsList):
        if key == 0:
            for listColumnStart in listColumnsStart:
                columnsListNew.append(listColumnStart)
        if columnList in listColumnsStart:
            continue
        columnsListNew.append(columnList)
    table_full = table_full[columnsListNew]


def save_full():
    # salvar a tabela
    table_full.to_csv(
        "tables\\tableMerge.csv",
        index=False,
        header=True,
        sep=';'
    )


def test_full_double():
    ''' teste para sabEr a diferença e mostra que é diferente.
    pois se existir diferença ele ira salvar no log'''
    global table_full
    global table_Cadastro_Consorciado
    fileManip = FileManip()
    fileManip.arq_log = arq_log
    text = 'Na tabela table_merge foi encontrado duplicado:'
    num_line = len(table_full)
    nDiferente = 0
    count = 0
    for i in range(num_line):
        i2 = i - nDiferente
        vend_1 = table_full.at[i, 'Vendedor']
        vend_2 = table_Cadastro_Consorciado.at[i2, 'Vendedor']  # type: ignore
        if vend_1 != vend_2:
            count += 1
            text += str(count) + 'ª divergência'
            text += 'Vendedor: ' + table_full.at[i, 'Vendedor']
            text += 'Cliente: ' + table_full.at[i, 'Cliente']
            fileManip.writeLog = text
            text = ''
            nDiferente += 1
            # break


def test_table_Cadastro_Funcionario_double():
    global table_Cadastro_Funcionario
    list_funcionario_double = (
        table_Cadastro_Funcionario['Nome'].tolist())  # type: ignore
    # print(list_funcionario_double)
    fileManip = FileManip()
    while True:
        n_element = len(list_funcionario_double)
        if n_element <= 1:
            break
        funcionario_double = list_funcionario_double.pop()
        # print(funcionario_double)
        if funcionario_double in list_funcionario_double:
            text = f'O funcionario {funcionario_double} esta duplicado. '
            text += 'Ele tem duas funções'
            fileManip.writeLog = text


def openSite():
    ''' defined '''
    global driver
    global connect
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    connect = Connect(driver=driver)
    xpathManip = XpathManip(driver=driver)
    connect.arq_log = arq_log
    driver.get(siteSircon)
    # logar
    connect.user = user
    connect.password = password
    while True:
        connect.logarSircon = listXpathLog
        xpathManip.locate = listXpathComissoesConfiguracao[0]
        xpathOk = xpathManip.locate
        if xpathOk is True:
            break


start = True
log_start_end()
'''table_Cadastro_Consorciado'''
if new_table_Cadastro_Consorciado:
    openSite()
    connect.file = arqDonwloadSales  # type: ignore
    connect.month = month
    connect.sales = listXpathSales
    table_Cadastro_Consorciado = connect.sales
    driver.quit()
    table_Cadastro_Consorciado.to_csv(  # type: ignore
        arqTableCadastroConsorciado,
        sep=';',
        index=False,
        header=True
    )

else:  # ler as tabelas que para nao precisar executar novamente
    table_Cadastro_Consorciado = pd.read_csv(
        arqTableCadastroConsorciado,
        sep=';',
        encoding='utf-8',
        dtype=str
    )

'''table_Cadastro_Funcionario '''
if new_table_Cadastro_Funcionario:
    openSite()
    connect.file = arqDonwloadFunction  # type: ignore
    connect.function = listXpathFunction
    table_Cadastro_Funcionario = connect.function
    driver.quit()
    table_Cadastro_Funcionario.to_csv(  # type: ignore
        arqTableCadastroFuncionario,
        sep=';',
        index=False,
        header=True,
    )
else:
    table_Cadastro_Funcionario = pd.read_csv(
        arqTableCadastroFuncionario,
        sep=';',
        encoding='utf-8',
        dtype=str
    )

'''#################### LIMITAR PESQUISAS ##################################'''
'''table_Cadastro_Ata'''
if new_table_Cadastro_Ata is True:
    openSite()
    connect.month = month
    connect.tagSon = tag_data
    connect.tagFather = tag_row
    connect.tagGet = tag_outerHTML
    connect.tagReturnValue
    # limited_search()
    limited_search_administradoras()
    limited_search_cargos()
    connect.minutes = listXpathMinutes
    table_Cadastro_Ata = connect.minutes
    driver.quit()
    tableManip.table = table_Cadastro_Ata  # type: ignore
    list_columns_rename = [[1, 'Mes'],
                           [2, 'Periodo_inicial'],
                           [3, 'Periodo_final']]
    for column_rename in list_columns_rename:
        tableManip.rename_name_column_indix = column_rename
    tableManip.add_column_clone_two_columns = ['ATA', 'Mes', 'Ano']
    table_Cadastro_Ata = tableManip.table

    table_Cadastro_Ata.to_csv(  # type: ignore
        arqTableCadastroAta,
        sep=';',
        index=False,
        header=True,
    )
else:
    table_Cadastro_Ata = pd.read_csv(
        arqTableCadastroAta,
        sep=';',
        encoding='utf-8',
        dtype=str
    )


'''table_Comissoes_Configuracao'''
if new_table_Comissoes_Configuracao:
    openSite()
    connect.pressListXpath = listXpathComissoesConfiguracao
    connect.pressListXpath = xpathTipoComissao
    connect.tagSon = tag_option
    connect.tagFather = tag_select
    connect.tagGet = tag_outerHTML
    connect.tagReturnValue
    # criar lista de administradoras
    limited_search_administradoras()
    connect.pressXpathResultListValue = xpathAdministradora
    # criar lista de administradoras + tabela de recebiemnto
    connect.pressListValueXpathResultListValue = xpathTabelaRecebimento
    # criar lista de administradoras + tabela de recebiemnto + cargos
    limited_search_cargos()
    connect.pressListValueXpathResultListValueDouble = xpathCargo
    # alterar a tagets
    connect.tagGet = tag_value
    connect.tagReturnValue
    # criar lista de administradoras + tabela de recebiemnto + cargos + valores
    connect.pressListValueResultListValueTriple = listCampoCotaPeriodoParcela
    # adicionar 'None' para todos terem o mesmo quantidade de elementos
    # e tambem o ultimo elemento adiciona uma coluna 'None'
    connect.addNone
    # adiciona o index
    connect.addIndex
    # substitu o ultimo elemento 'None' por 'endValue'
    connect.addEnd
    # substitu  da ulitmo coluna da 'endValue' por 'endValueLast'
    connect.lineToColumn
    # substitu todos no 'None' por ''
    connect.noneToEmpty
    # excluir se tudo for ''
    connect.killAllEmpty
    # table_Comissoes_Configuracao = connect.listColunmToTable
    connect.listColunmToTable
    table_Comissoes_Configuracao = connect.renameColumn

    driver.quit()
    table_Comissoes_Configuracao.to_csv(
        arqTableComissoesConfiguracao, index=False, header=True, sep=';')
    # table.to_csv("table2.csv", index=False, header=True)
else:
    table_Comissoes_Configuracao = pd.read_csv(
        arqTableComissoesConfiguracao, sep=';', encoding='utf-8', dtype=str)

'''table_Comissoes_ConfigPagamento'''
if new_table_Comissoes_ConfigPagamento:
    openSite()
    connect.tagSon = tag_option
    connect.tagFather = tag_select
    connect.tagGet = tag_outerHTML
    connect.tagSelected = tag_selected
    connect.tagReturnValue
    # caminho no site para entra local especifico pelo xpath
    connect.pressListXpath = listXpathComissoesConfPagamento
    connect.pressListXpath = xpathTipoComissaoPagamento
    # list os valores existentes no campos cargos, administradora,tipoPagamento
    limited_search_administradoras()
    limited_search_cargos()
    connect.pressListXpathReturnListValue = listXpathCargAdminsPag
    # listCargo = connect.pressListXpathReturnListValue  # precisa do tagGet
    # connect.tagGets = tag_value
    # connect.tagReturnValue
    connect.pressListValueReturnListValue = listXpathDtPagamentoParcelas
    # connect.organizeListLine
    connect.organizeListLine = headerDtPagamentoParcelas
    listFull = connect.organizeListLine
    driver.quit()
    table_Comissoes_ConfigPagamento = connect.listLineToTable
    table_Comissoes_ConfigPagamento.to_csv(
        arqTableComissoesConfigPag, index=False, header=True, sep=';'
    )  # type: ignore

else:
    table_Comissoes_ConfigPagamento = pd.read_csv(
        arqTableComissoesConfigPag, sep=';', encoding='utf-8', dtype=str)


date_weekly_new()
table_manip_funcionario()
table_manip_cadastro_consorciado()
table_manip_comissoes_configuracao()
table_manip_comissao_configPagamento()
table_manip_Cadastro_funcionario_gerente()
table_manip_comissoes_configuracao_gerente()
merge_consorciado_funcionario()
merge_consorciado_funcionario_gerente()
merge_full_comissoes_configuracao()
merge_full_comissoes_configuracao_gerente()
merge_full_weekly()
merge_full_ata()
order_column()
save_full()
test_table_Cadastro_Funcionario_double()
test_full_double()
log_start_end()
