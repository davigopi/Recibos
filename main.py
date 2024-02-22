from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from connect import Connect, XpathManip
from pathlib import Path
# from selenium.common.exceptions import TimeoutException
import os
from time import sleep
# import ast
import pandas as pd

siteSircon = "https://app.sistemasircon.com.br/login"
user = 'davigopi@gmail.com'
password = '36vad28'
month = 6
pathTables = Path(__file__).parent/'tables'
arqTableSales = pathTables/'tableSales.csv'
arqTableSalesSetup = pathTables/'tableSalesSetup.csv'
arqTableFunction = pathTables/'tableFunction.csv'
pathDonwload = os.environ['USERPROFILE'] + '\\Downloads'
arqDonwloadSales = pathDonwload + '\\consorciados.csv'
arqDonwloadFunction = pathDonwload + '\\funcionarios.csv'

# security = [user, password]

'''#################### LIMITAR PESQUISAS ##################################'''
valueAdministradora = ['DISAL']
valueCargo = ['CONSULTOR CLT - A PARTIR JAN-2018', 'CONSULTOR DE PARCEIRO']
'''#################### TAGS ###############################################'''
tagSon = 'option'
tagFather = 'select'
tagGet = 'outerHTML'
tagGetEnd = 'value'
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
        f'//*[@id="frm:pnlEsacalas"]/div[{str(num+1)}]',  # campo de 0 a 2 
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

'''#################### ABRIR SITES ########################################'''
openSite = True
logar = True
sales = True
salesSetup = True
functionSetup = True
if not openSite:
    logar = False
if not logar:
    sales = False
    salesSetup = False
    functionSetup = False

if openSite:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(ChromeDriverManager().install())            
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(siteSircon)
    connect = Connect(driver=driver)
    xpathManip = XpathManip(driver=driver)

if logar:
    connect.users = user
    connect.passwords = password
    while True:
        connect.logarSircon = listXpathLog
        xpathManip.locate = listXpathComissoesConfiguracao[0]
        xpathOk = xpathManip.locate
        if xpathOk is True:
            break

if sales:
    connect.files = arqDonwloadSales
    connect.months = month
    connect.sales = listXpathSales
    tableSales = connect.sales
    tableSales.to_csv(
        "tables\\tableSales.csv",
        index=False, 
        header=True, 
        sep=';'
        )

if salesSetup:
    connect.pressListXpath = listXpathComissoesConfiguracao
    connect.pressListXpath = xpathTipoComissao
    connect.tagSons = tagSon
    connect.tagFathers = tagFather
    connect.tagGets = tagGet
    connect.tagReturnValue
    connect.pressXpathReturnListValue = xpathAdministradora
    # connect.valueAdministradoras = valueAdministradora  # Limitar pesquiza
    connect.pressListValueXpathReturnListValue = xpathTabelaRecebimento
    connect.pressListValueXpathReturnListValueDouble = xpathCargo
    # connect.valueCargos = valueCargo  # Limitar pesquiza
    connect.tagGets = tagGetEnd
    connect.tagReturnValue
    connect.pressListValueReturnListValueTriple = listCampoCotaPeriodoParcela
    connect.addNone
    connect.addIndex
    connect.addEnd
    connect.lineToColumn
    connect.noneToEmpty
    connect.killAllEmpty
    tableSalesSetup = connect.listToTable
    tableSalesSetup = connect.renameColumn
    # print(table)
    tableSalesSetup.to_csv(
        "tables\\tableSalesSetup.csv",
        index=False, 
        header=True, 
        sep=';'
        )  # type: ignore
    # table.to_csv("table2.csv", index=False, header=True)


if functionSetup:
    connect.files = arqDonwloadFunction
    connect.function = listXpathFunction
    tableFunction = connect.function
    tableFunction.to_csv(
        "tables\\tableFunction.csv",
        index=False, 
        header=True, 
        sep=';'
        )  # type: ignore


print('########################')
conf = {}
print(pathTables)
tableSales = pd.read_csv(arqTableSales, sep=';', encoding='utf-8', dtype=str)
tableSalesSetup = pd.read_csv(arqTableSalesSetup, sep=';', encoding='utf-8', 
                              dtype=str)
tableFunction = pd.read_csv(arqTableFunction, sep=';', encoding='utf-8', 
                              dtype=str)
# print(tableSales)
# print(tableSalesSetup)
# print(tableFunction)

nLine = tableSalesSetup[tableSalesSetup.columns[0]].count()
for i in range(nLine):
    if 'FERIAS' in tableSalesSetup.at[i, 'Tabela de recebimento']: 
        tableSalesSetup.at[i, 'Administradora'] += ' FERIAS'
        # print(tableSalesSetup.at[i, 'Administradora'])

# print(tableSalesSetup) 
#     inf = inf.replace('" ', '')
#     inf = inf.replace(' "', '')
#     inf = inf.replace('"', '')
#     if inf != tableSales.at[i, 'Vendedor']:
#         pass
#     print(inf) 
#     tableSales.at[i, 'Vendedor'] = inf
        

# columnsList = tableSalesSetup.columns.to_list()
# print(columnsList)



df = pd.merge(tableSales, tableFunction, 
              left_on='Vendedor', right_on='Nome', how='left')


listColumnsStart = ['Administradora', 'Cargo', 'CPF', 'Vendedor', 'Gerente']
columnsList = df.columns.to_list()
columnsListNew = []
for key, columnList in enumerate(columnsList):
    if key == 0:
        for listColumnStart in listColumnsStart:
            columnsListNew.append(listColumnStart)
    if columnList in listColumnsStart:
        continue
    columnsListNew.append(columnList)
df = df[columnsListNew]

df = pd.merge(df, tableSalesSetup, on=['Administradora', 'Cargo'], how='left')

df.to_csv(
    "tables\\tableMerge.csv",
    index=False, 
    header=True, 
    sep=';'
    )  # type: ignore
# print(df)
nDiferente = 0
for i in range(nLine):
    i2 = i - nDiferente
    if df.at[i, 'Vendedor'] != tableSales.at[i2, 'Vendedor']:
        print(i, '    ', df.at[i, 'Vendedor'], "      ", tableSales.at[i, 'Vendedor'])
        print()
        nDiferente += 1
        # break
        



# sleep(6000)

