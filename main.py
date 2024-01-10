from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from connect import Connect, XpathManip
# from selenium.common.exceptions import TimeoutException
import os
# import ast
from time import sleep

siteSircon = "https://app.sistemasircon.com.br/login"
user = 'davigopi@gmail.com'
password = '36vad28'
security = [user, password]

listXpathLog = ['//*[@id="form:txtUsuarioSircon"]'  # campo usuario
            , '//*[@id="form:txtSenhaSircon"]'  # campo senha
            , '//*[@id="form:btLogar"]'  # botao confirmar
            ]

arqCons = os.environ['USERPROFILE'] + '\Downloads\consorciados.csv'
month = 5
xp0 = '//*[@id="menucadastro"]/a'  # menu cadastro
#xp0 = '//*[@id="menucadastro"]'  # menu cadastro
xp1 = '//*[@id="menucadastro"]/ul/li[5]'  # menu consorciado
xp2 = '//*[@id="pnlBloco"]/div[6]/div/div[3]/div'  # campo entrega venda inicio
xp3 = '//*[@id="ui-datepicker-div"]/div[1]/a[1]'  # botao seta para esquerda
line = 1
column = 0  
xp4 = f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{line}]/td[{column}]'  # linha coluna calendario
xp5 = '//*[@id="ui-datepicker-div"]/div[3]/button[2]'  # botao fechar do calendario
xp6 = '//*[@id="pnlBloco"]/div[6]/div/div[4]/div'  # campo entrega venda final
xp7 = '//*[@id="btnConsultar"]'  # botao consultar
xp8 = '//*[@id="btnGerarXls"]'  # botao de download
listXpath2 = [xp0, xp1, xp2, xp3, xp4, xp5, xp6, xp3, xp4, xp5, xp7, xp8]

tagSon = 'option'
tagFather = 'select'
tagGet = 'outerHTML'
tagGetEnd = 'value'

valueAdministradora = ['DISAL']
valueCargo = ['CONSULTOR CLT - A PARTIR JAN-2018', 'CONSULTOR DE PARCEIRO']

listXpathComissoesConfiguracao = ['//*[@id="menufinan"]'  # comissões
                                , '//*[@id="menufinan"]/ul/li[2]'  # Configuração
                                ]
xpathTipoComissao = ['//*[@id="frm:tpComissao"]'
                    , '//*[@id="frm:tpComissao"]/option[2]'  # Pagamento
                    ]
xpathAdministradora = '//*[@id="frm:cbAdministradora"]'
            # , listAdm  # Disal
xpathTabelaRecebimento = '//*[@id="frm:cbTabelaRecebimento"]'
                        # , '//*[@id="frm:cbTabelaRecebimento"]/option[2]'  # Tabela disal normal
xpathCargo = '//*[@id="frm:cbCargo"]'
            # , '//*[@id="frm:cbCargo"]/option[5]'  # Consultor CLR - a partir jan-2018

listXpathCampoParcela =[]
for num in range(30):  # quantidade de campos comissões configuracao
    listCampo = f'//*[@id="frm:pnlEsacalas"]/div[{str(num+1)}]'  # campo de 0 a 2 

# //*[@id="accordion"]/div/div[1]/h4/a/span/span
# //*[@id="accordion"]/div/div[1]/h4/a/span/span
# //*[@id="accordion"]/div/div[1]/h4/a/span/span
# //*[@id="frm:j_idt124:0:j_idt149"]
# //*[@id="frm:j_idt124:1:j_idt149"]
# //*[@id="frm:j_idt124:0:j_idt182_input"]
# //*[@id="frm:j_idt124:0:j_idt184_input"]
# //*[@id="collapse8443"]/div/div/div/div/div/div[4]/input
# //*[@id="collapse8443"]/div/div/div/div/div/div[5]/input
# //*[@id="collapse8444"]/div/div/div/div/div/div[4]/input
# //*[@id="collapse8444"]/div/div/div/div/div/div[5]/input
# //*[@id="collapse2351"]/div/div/div/div/div/div[4]/input
# //*[@id="frm:j_idt124:1:j_idt182_input"]
# //*[@id="frm:j_idt124:1:j_idt184_input"]
# //*[@id="collapse8444"]/div/div/div/div/div/div[4]/input
# //*[@id="collapse8444"]/div/div/div/div/div/div[5]/input

    listCotaPeriodoParcela = [ 
                f'frm:j_idt124:{num}:j_idt194' # qtd cotas inicial
                , f'frm:j_idt124:{num}:j_idt196'  # qtd cotas final
                , f'//*[@id="frm:j_idt124:{num}:j_idt182_input"]'  # data venda inicio
                , f'//*[@id="frm:j_idt124:{num}:j_idt184_input"]'  # data venda fim
                , f'//*[@id="frm:j_idt124:{num}:j_idt149"]'  # parcela 1
                , f'//*[@id="frm:j_idt124:{num}:j_idt156"]'  # parcela 2
                , f'//*[@id="frm:j_idt124:{num}:j_idt158"]'  # parcela 3
                , f'//*[@id="frm:j_idt124:{num}:j_idt160"]'  # parcela 4
                , f'//*[@id="frm:j_idt124:{num}:j_idt162"]'  # parcela 5
                , f'//*[@id="frm:j_idt124:{num}:j_idt164"]'  # parcela 6
                , f'//*[@id="frm:j_idt124:{num}:j_idt166"]'  # parcela 7
                , f'//*[@id="frm:j_idt124:{num}:j_idt168"]'  # parcela 8
                , f'//*[@id="frm:j_idt124:{num}:j_idt170"]'  # parcela 9
                , f'//*[@id="frm:j_idt124:{num}:j_idt172"]'  # parcela 10
                , f'//*[@id="frm:j_idt124:{num}:j_idt174"]'  # parcela 11
                , f'//*[@id="frm:j_idt124:{num}:j_idt176"]'  # parcela 12
                ]
    listXpathCampoParcela.append([listCampo, listCotaPeriodoParcela])

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(siteSircon)
connect = Connect(driver=driver)
xpathManip = XpathManip(driver=driver)
connect.users = user
connect.passwords = password
while True:
    connect.logarSircon = listXpathLog
    xpathManip.locate = listXpathComissoesConfiguracao[0]
    xpathOk = xpathManip.locate
    if xpathOk is True:
        break
# connect.files = arqCons
# connect.months = month
# connect.dfSircon = listXpath2
# df = connect.dfSircon
# df.to_csv("df.csv", index=False, header=True)

connect.pressListXpath = listXpathComissoesConfiguracao
connect.pressListXpath = xpathTipoComissao
connect.tagSons = tagSon
connect.tagFathers = tagFather
connect.tagGets = tagGet
connect.tagReturnValue
connect.pressXpathReturnListValue = xpathAdministradora
connect.valueAdministradoras = valueAdministradora  # ira limitar a pesquiza
connect.pressListValueXpathReturnListValue = xpathTabelaRecebimento
connect.pressListValueXpathReturnListValueDouble = xpathCargo
connect.valueCargos = valueCargo  # ira limitar a pesquiza
connect.tagGets = tagGetEnd
connect.tagReturnValue
connect.pressListValueReturnListValueTriple = listXpathCampoParcela
connect.removeListInside
connect.addNone
connect.addIndex
connect.addEnd
connect.lineToColumn
connect.noneToEmpty
connect.killAllEmpty
table = connect.listToTable

print(table)
table.to_csv("table.csv", index=False, header=True)

sleep(4)