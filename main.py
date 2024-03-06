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
arqTableSales = pathTables/'table_Cadastro_Consorciado.csv'
arqTableSalesSetup = pathTables/'table_Comissoes_ConfigPagamento.csv'
arqTableFunction = pathTables/'table_Cadastro_Funcionario.csv'
pathDonwload = os.environ['USERPROFILE'] + '\\Downloads'
arqDonwloadSales = pathDonwload + '\\consorciados.csv'
arqDonwloadFunction = pathDonwload + '\\funcionarios.csv'

# security = [user, password]

'''#################### LIMITAR PESQUISAS ##################################'''
limitSearchChosse = False
valueChooseAdministradora = ['DISAL']
valueChooseCargo = ['CONSULTOR CLT - A PARTIR JAN-2018', 'CONSULTOR DE PARCEIRO']
limitSearchSystem = True
limitSearchDeleteWord = True
valueChooseTabelarecebimento = ['FERIAS']
'''#################### TAGS ###############################################'''
tagSon = 'option'
tagFather = 'select'
tagGet = 'outerHTML'
tagGetEnd = 'value'
tagSelected = '/option[@selected="selected"]'
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
        f'//*[@id="frm:pnlEsacalas"]/div[{str(num+1)}]',  # campo 0 a 2 Father
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
listDtPagamentoParcelas = [
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

'''#################### ABRIR SITES ########################################'''
openSite = True
sales = False
functionSetup = False
salesSetup = False
salesSetupPay = True

if openSite is False:
    sales = False
    salesSetup = False
    salesSetupPay = False
    functionSetup = False


######################### defined ################################
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

if sales:
    connect.files = arqDonwloadSales
    connect.months = month
    connect.sales = listXpathSales
    table_Cadastro_Consorciado = connect.sales
    table_Cadastro_Consorciado.to_csv(
        "tables\\table_Cadastro_Consorciado.csv",
        index=False, 
        header=True, 
        sep=';'
        )
else: 
    # ler as tabelas que para nao precisar executar novamente
    table_Cadastro_Consorciado = pd.read_csv(arqTableSales, sep=';', 
                                             encoding='utf-8', 
                                             dtype=str)

if functionSetup:
    connect.files = arqDonwloadFunction
    connect.function = listXpathFunction
    table_Cadastro_Funcionario = connect.function
    table_Cadastro_Funcionario.to_csv(
        "tables\\table_Cadastro_Funcionario.csv",
        index=False, 
        header=True, 
        sep=';'
        )  # type: ignore
else:
    table_Cadastro_Funcionario = pd.read_csv(arqTableFunction, sep=';', 
                                             encoding='utf-8', 
                                             dtype=str)


# para limitar pesquisa escolhida pelo usuario
if limitSearchChosse is True:
    connect.valueChooseAdministradoras = valueChooseAdministradora
    connect.valueChooseCargos = valueChooseCargo
if limitSearchSystem is True:
    connect.valueExistAdministradoras = table_Cadastro_Consorciado
    connect.valueExistCargos = table_Cadastro_Funcionario
if limitSearchDeleteWord is True:
    connect.valueExistTabelarecebimento = valueChooseTabelarecebimento

if salesSetup:
    connect.pressListXpath = listXpathComissoesConfiguracao
    connect.pressListXpath = xpathTipoComissao
    connect.tagSons = tagSon
    connect.tagFathers = tagFather
    connect.tagGets = tagGet
    connect.tagReturnValue
    # criar lista de administradoras
    connect.pressXpathResultListValue = xpathAdministradora
    # criar lista de administradoras + tabela de recebiemnto 
    connect.pressListValueXpathResultListValue = xpathTabelaRecebimento
    # criar lista de administradoras + tabela de recebiemnto + cargos
    connect.pressListValueXpathResultListValueDouble = xpathCargo
    # alterar a tagets
    connect.tagGets = tagGetEnd
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
    table_Comissoes_ConfigPagamento = connect.listToTable
    table_Comissoes_ConfigPagamento = connect.renameColumn
    table_Comissoes_ConfigPagamento.to_csv(
        "tables\\table_Comissoes_ConfigPagamento.csv",
        index=False, 
        header=True, 
        sep=';'
        )  # type: ignore
    # table.to_csv("table2.csv", index=False, header=True)
else:
    table_Comissoes_ConfigPagamento = pd.read_csv(arqTableSalesSetup, sep=';', 
                                                  encoding='utf-8', 
                                                  dtype=str)

print('###########salesSetupPay#############')

if salesSetupPay:
    connect.tagSons = tagSon
    connect.tagFathers = tagFather
    connect.tagGets = tagGet
    connect.tagSelecteds = tagSelected
    connect.tagReturnValue
    # caminho no site para entra local especifico pelo xpath
    connect.pressListXpath = listXpathComissoesConfPagamento
    connect.pressListXpath = xpathTipoComissaoPagamento
    # list os valores existentes no campos cargos, administradora,tipoPagamento
    connect.pressListXpathReturnListValue = listXpathCargAdminsPag
    # listCargo = connect.pressListXpathReturnListValue  # precisa do tagGet
    # connect.tagGets = tagGetEnd
    # connect.tagReturnValue
    connect.pressListValueReturnListValue = listDtPagamentoParcelas
    listFull = connect.pressListValueReturnListValue
    for cargoOutros in listFull:
        cargo = cargoOutros[0]
        for administradoraOutros in cargoOutros[1]:
            administradora = administradoraOutros[0]
            for tipopagamentoOutros in administradoraOutros[1]:
                tipopagamento = tipopagamentoOutros[0]
                print('###################')
                print(f'cargo: {cargo}')
                print(f'administradora: {administradora}')
                print(f'tipo de pagamento: {tipopagamento}')
                print(f'Informações: {tipopagamentoOutros[1]}')

# print(table_Cadastro_Consorciado)
# print(table_Comissoes_ConfigPagamento)
# print(table_Cadastro_Funcionario)
# print(listAdministradora)
# print(nLine)

sleep(3000)

# editar tabela tara nao dar conflito com mesmo nome 
nLine = table_Comissoes_ConfigPagamento[table_Comissoes_ConfigPagamento.columns[0]].count()
for i in range(nLine):
    if 'FERIAS' in table_Comissoes_ConfigPagamento.at[i, 'Tabela de recebimento']: 
        table_Comissoes_ConfigPagamento.at[i, 'Administradora'] += ' FERIAS'
        # print(table_Comissoes_ConfigPagamento.at[i, 'Administradora'])

# print(table_Comissoes_ConfigPagamento) 
#     inf = inf.replace('" ', '')
#     inf = inf.replace(' "', '')
#     inf = inf.replace('"', '')
#     if inf != table_Cadastro_Consorciado.at[i, 'Vendedor']:
#         pass
#     print(inf) 
#     table_Cadastro_Consorciado.at[i, 'Vendedor'] = inf

# columnsList = table_Comissoes_ConfigPagamento.columns.to_list()
# print(columnsList)

# mesclar tabela
df = pd.merge(table_Cadastro_Consorciado, table_Cadastro_Funcionario, 
              left_on='Vendedor', right_on='Nome', how='left')


# ordenar calunas da tabela para a forma que quiser
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

# mesclar tabela 
df = pd.merge(df, table_Comissoes_ConfigPagamento, on=['Administradora', 'Cargo'], how='left')

# salvar a tabela
df.to_csv(
    "tables\\tableMerge.csv",
    index=False, 
    header=True, 
    sep=';'
    )  # type: ignore
# print(df)

# teste para saebr a diferença e mostra que é diferente
nDiferente = 0
for i in range(nLine):
    i2 = i - nDiferente
    if df.at[i, 'Vendedor'] != table_Cadastro_Consorciado.at[i2, 'Vendedor']:
        print(i, '    ', df.at[i, 'Vendedor'], "      ", table_Cadastro_Consorciado.at[i, 'Vendedor'])
        print()
        nDiferente += 1
        # break
        

sleep(1)
