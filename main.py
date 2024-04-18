import os
from pathlib import Path
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from typing import Union
from components.connect import Connect
from components.tableManip import TableManip
from components.xpathManip import XpathManip
from components.table_manip_value import Table_manip_value
from components.date_weekly import Date_weekly

tableManip = TableManip()
table_manip_value = Table_manip_value()
date_weekly = Date_weekly()


siteSircon = "https://app.sistemasircon.com.br/login"
user = 'davigopi@gmail.com'
password = '36vad28'
month = 24
pathTables = Path(__file__).parent / 'tables'
arqTableCadastroConsorciado = pathTables / 'table_Cadastro_Consorciado.csv'
arqTableCadastroFuncionario = pathTables / 'table_Cadastro_Funcionario.csv'
arqTableCadastroAta = pathTables / 'table_Cadastro_Ata.csv'
arqTableComissoesConfiguracao = pathTables / 'table_Comissoes_Configuracao.csv'
arqTableComissoesConfigPag = pathTables / 'table_Comissoes_ConfigPagamento.csv'
arqTableComissoesConfigPagDupl = pathTables / 'table_Comissoes_ConfigPagamento_Dupl.csv'
arqTableDatasSemanais = pathTables / 'table_datas_semanais.csv'
arqTableTeste = pathTables / 'table_teste.csv'
arqInformacao = pathTables / 'informacao.txt'

pathDonwload = os.environ['USERPROFILE'] + '\\Downloads'
arqDonwloadSales = pathDonwload + '\\consorciados.csv'
arqDonwloadFunction = pathDonwload + '\\funcionarios.csv'

# security = [user, password]

'''#################### LIMITAR PESQUISAS ##################################'''
limitSearchChosse = False
valueChooseAdministradora = ['DISAL']
valueChooseCargo = [
    'CONSULTOR CLT - A PARTIR JAN-2018',
    'CONSULTOR DE PARCEIRO'
]
limitSearchSystem = True
limitSearchDeleteWord = True
valueChooseTabelarecebimento = ['FERIAS']
'''#################### TAGS ###############################################'''
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
openSite = True
new_table_Cadastro_Consorciado = True
new_table_Cadastro_Funcionario = True
new_table_Comissoes_Configuracao = True
new_table_Comissoes_ConfigPagamento = True
new_table_Cadastro_Ata = True
# openSite = False
new_table_Cadastro_Consorciado = False
new_table_Cadastro_Funcionario = False
new_table_Cadastro_Ata = False
new_table_Comissoes_Configuracao = False
# new_table_Comissoes_ConfigPagamento = False


''' defined '''
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
connect = Connect(driver=driver)
xpathManip = XpathManip(driver=driver)
if openSite:
    driver.get(siteSircon)
    # logar
    connect.users = user
    connect.passwords = password
    while True:
        connect.logarSircon = listXpathLog
        xpathManip.locate = listXpathComissoesConfiguracao[0]
        xpathOk = xpathManip.locate
        if xpathOk is True:
            break
else:
    driver.quit()

'''table_Cadastro_Consorciado'''
if new_table_Cadastro_Consorciado:
    connect.files = arqDonwloadSales
    connect.months = month
    connect.sales = listXpathSales
    table_Cadastro_Consorciado = connect.sales
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
    connect.files = arqDonwloadFunction
    connect.function = listXpathFunction
    table_Cadastro_Funcionario = connect.function
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


'''Limitar pesquisa escolhida pelo usuario'''
if limitSearchChosse is True:
    connect.valueChooseAdministradoras = valueChooseAdministradora
    connect.valueChooseCargos = valueChooseCargo
if limitSearchSystem is True:
    connect.valueExistAdministradoras = table_Cadastro_Consorciado
    connect.valueExistCargos = table_Cadastro_Funcionario
if limitSearchDeleteWord is True:
    connect.valueExistTabelarecebimento = valueChooseTabelarecebimento

'''table_Cadastro_Ata'''
if new_table_Cadastro_Ata is True:
    connect.months = month
    connect.tagSons = tag_data
    connect.tagFathers = tag_row
    connect.tagGets = tag_outerHTML
    connect.tagReturnValue
    connect.minutes = listXpathMinutes
    table_Cadastro_Ata = connect.minutes
    tableManip.table = table_Cadastro_Ata  # type: ignore
    tableManip.add_column_clone_two_columns = ['ATA', 'Mês', 'Ano']
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
    connect.pressListXpath = listXpathComissoesConfiguracao
    connect.pressListXpath = xpathTipoComissao
    connect.tagSons = tag_option
    connect.tagFathers = tag_select
    connect.tagGets = tag_outerHTML
    connect.tagReturnValue
    # criar lista de administradoras
    connect.pressXpathResultListValue = xpathAdministradora
    # criar lista de administradoras + tabela de recebiemnto
    connect.pressListValueXpathResultListValue = xpathTabelaRecebimento
    # criar lista de administradoras + tabela de recebiemnto + cargos
    connect.pressListValueXpathResultListValueDouble = xpathCargo
    # alterar a tagets
    connect.tagGets = tag_value
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
    table_Comissoes_Configuracao.to_csv(
        arqTableComissoesConfiguracao, index=False, header=True, sep=';')
    # table.to_csv("table2.csv", index=False, header=True)
else:
    table_Comissoes_Configuracao = pd.read_csv(
        arqTableComissoesConfiguracao, sep=';', encoding='utf-8', dtype=str)

'''table_Comissoes_ConfigPagamento'''
if new_table_Comissoes_ConfigPagamento:
    connect.tagSons = tag_option
    connect.tagFathers = tag_select
    connect.tagGets = tag_outerHTML
    connect.tagSelecteds = tag_selected
    connect.tagReturnValue
    # caminho no site para entra local especifico pelo xpath
    connect.pressListXpath = listXpathComissoesConfPagamento
    connect.pressListXpath = xpathTipoComissaoPagamento
    # list os valores existentes no campos cargos, administradora,tipoPagamento
    connect.pressListXpathReturnListValue = listXpathCargAdminsPag
    # listCargo = connect.pressListXpathReturnListValue  # precisa do tagGet
    # connect.tagGets = tag_value
    # connect.tagReturnValue
    connect.pressListValueReturnListValue = listXpathDtPagamentoParcelas
    # connect.organizeListLine
    connect.organizeListLine = headerDtPagamentoParcelas
    listFull = connect.organizeListLine
    table_Comissoes_ConfigPagamento = connect.listLineToTable
    table_Comissoes_ConfigPagamento.to_csv(
        arqTableComissoesConfigPag, index=False, header=True, sep=';'
    )  # type: ignore

else:
    table_Comissoes_ConfigPagamento = pd.read_csv(
        arqTableComissoesConfigPag, sep=';', encoding='utf-8', dtype=str)


'''tabela numero da semana no mes'''

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

''' termino de carregameno de tabelas '''
# listTable = [table_Cadastro_Consorciado,
#              table_Cadastro_Funcionario,
#              table_Cadastro_Ata,
#              table_Comissoes_Configuracao,
#              table_Comissoes_ConfigPagamento]

# for key, list in enumerate(listTable):
#     print(list)
#     print(key)

# Verificar duplicatas nas colunas de junção

''' manipular table_Cadastro_Funcionario, para alterar os Nomes duplicados com
os Cargos, que gera comissão duplicada, pois o mesmo tem dois ou mais cargos'''
table_manip_value.tables = table_Cadastro_Funcionario
table_manip_value.row_duplicate_column = ['Nome']
table_manip_value.list_columns_one_two = ['Nome', 'Cargo']
table_manip_value.edit_data_column_2 = ['Nome', 'Cargo']
table_Cadastro_Funcionario = table_manip_value.return_table
''' manipular table_Cadastro_Consorciado, para altera rcoluna Vendedor
e igualar aos alterados no table_Cadastro_Funcionario'''
table_manip_value.tables = table_Cadastro_Consorciado
table_manip_value.data_duplicate_change = 'Vendedor'
table_Cadastro_Consorciado = table_manip_value.return_table
''' manipular table_Comissoes_Configuracao remover as duplicação nas colunas
'Administradora' e 'Cargo' '''
table_manip_value.tables = table_Comissoes_Configuracao
table_manip_value.row_duplicate_column = ['Administradora', 'Cargo']
table_manip_value.list_columns_one_two_three = ['Administradora',
                                                'Cargo',
                                                'Tabela de recebimento']
table_manip_value.edit_data_column_3 = ['Administradora',
                                        'Cargo',
                                        'Tabela de recebimento']
table_Comissoes_Configuracao = table_manip_value.return_table

'''############## mescla tabelas ###################'''
table_full = pd.merge(
    table_Cadastro_Consorciado,
    table_Cadastro_Funcionario,
    left_on='Vendedor',
    right_on='Nome',
    how='left'
)
table_full = pd.merge(
    table_full,
    table_Comissoes_Configuracao,
    on=['Administradora', 'Cargo'],
    how='left')
# ''' manipular tabela full '''
# table_manip_value.tables = table_full
# table_manip_value.add_column_day_week = ['Data de Entrega',
#                                          'Data Cad. Adm']
''' manipular table_comissoes_configuPagamento'''
table_manip_value.tables = table_Comissoes_ConfigPagamento
# table = table_manip_value.return_table
# print(table)
table_manip_value.edit_data_column_all = ['Cargo',
                                          'Administradora',
                                          'Tipo Pagamento',
                                          'Dt pag. por',
                                          'dia pag.',
                                          '1P recebera',
                                          'D+ recebera',
                                          'FAT recebera',
                                          'Index']
table = table_manip_value.return_table
table_manip_value.tables = table
table_manip_value.row_duplicate_column = ['Cargo',
                                          'Administradora',
                                          'Tipo Pagamento']

table_duplicate = table_manip_value.return_table_duplicate
# print(table_duplicate)
table = table_manip_value.return_table
table.to_csv(arqTableTeste, index=False, header=True, sep=';')  # type: ignore

table_duplicate.to_csv(arqTableComissoesConfigPagDupl,  # type: ignore
                       index=False, header=True, sep=';')

'''# mesclar table_full com table_datas_semanais'''


tableManip.table = table_date_weekly
tableManip.del_column = 'Dia semana'
table_date_weekly_changed = tableManip.table
columns_table_date_weekly_changed = table_date_weekly_changed.columns

table_full = pd.merge(
    table_full,
    table_date_weekly_changed,
    left_on='Data de Entrega',
    right_on='Data semana',
    how='left'
)
tableManip.table = table_full
tableManip.rename_name_column = [
    'N Semana Mes',
    'N Semana Entrega']
table_full = tableManip.table
table_full = pd.merge(
    table_full,
    table_date_weekly_changed,
    left_on='Data Cad. Adm',
    right_on='Data semana',
    how='left'
)
tableManip.table = table_full
tableManip.rename_name_column = [
    'N Semana Mes',
    'N Cad. Adm Entrega']
table_full = tableManip.table

''' manipular table ATA '''

print(table_Cadastro_Ata)


''' Ordenar colunas da tabela para a forma que quiser'''
listColumnsStart = [
    'Situação', 'CPF', 'Vendedor', 'Administradora', 'Cargo', 'Crédito',
    'Data de Entrega', 'N Semana Entrega', 'Data Cad. Adm',
    'N Cad. Adm Entrega', 'Gerente', 'Cliente', 'Valor Parc. Inicial'
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


# salvar a tabela
table_full.to_csv(
    "tables\\tableMerge.csv",
    index=False,
    header=True,
    sep=';'
)


# print(table_Cadastro_Consorciado)
# print(table_full)

# teste para sabEr a diferença e mostra que é diferente
num_line = len(table_full)
nDiferente = 0
count = 0
with open(arqInformacao, 'w') as arquivo:
    arquivo.write('Na tabela table_merge foi encontrado duplicado:  \n \n')
for i in range(num_line):
    i2 = i - nDiferente
    if table_full.at[i, 'Vendedor'] != table_Cadastro_Consorciado.at[
            i2, 'Vendedor']:
        count += 1
        arquivoTxt = str(count) + 'ª divergência \n'
        arquivoTxt += 'Vendedor: ' + table_full.at[i, 'Vendedor'] + '\n'
        arquivoTxt += 'Cliente: ' + table_full.at[i, 'Cliente'] + '\n' + '\n'

        with open(arqInformacao, 'a') as arquivo:
            arquivo.write(arquivoTxt)
        nDiferente += 1
        # break

# # Verificar duplicatas nas colunas de junção
# duplicatas = table_Comissoes_Configuracao.duplicated(
#   subset=['Administradora', 'Cargo'], keep=False)
# duplicatas_rows = table_Comissoes_Configuracao[duplicatas]
# print(duplicatas_rows)

# sleep(1)
