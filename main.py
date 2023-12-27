from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from connect import Connect
from selenium.common.exceptions import TimeoutException
import os
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
months = 2
xp0 = '//*[@id="menucadastro"]'  # menu cadastro
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

# listAdm =[]
# for key in range(2, 20, 1):
#     listAQdmExistente = f'//*[@id="frm:cbAdministradora"]/option[{key}]'
#     listAdm.append(listAQdmExistente)

tagSon = 'option'
tagFather = 'select'

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
for num in range(30):
    listCampo = f'//*[@id="frm:pnlEsacalas"]/div[{str(num+1)}]'  # campo de 0 a 2 
    listParcela = [f'//*[@id="frm:j_idt124:{num}:j_idt149"]'  # parcela 1
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
    listXpathCampoParcela.append([listCampo, listParcela])

# //*[@id="frm:pnlEsacalas"]/div[1]



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(siteSircon)
connect = Connect(driver=driver)
while True:
    connect.logarSircon(security=security, listXpath=listXpathLog)
    xpathOk = connect.locateXpath(xpath=listXpathComissoesConfiguracao[0]) 
    if xpathOk is True:
        break
while True:
    connect.pressListXpath(listXpath=listXpathComissoesConfiguracao)
    xpathOk = connect.locateXpath(xpath=xpathTipoComissao[0]) 
    if xpathOk is True:
        break
connect.pressListXpath(listXpath=xpathTipoComissao)
listValue = connect.pressXpathReturnListValue(xpath=xpathAdministradora)
listValue = connect.pressListValueXpathReturnListValue(xpath=xpathTabelaRecebimento, listValue=listValue, tagSon=tagSon, tagFather=tagFather)
listValue = connect.pressListValueXpathReturnListValueDouble(xpath=xpathCargo, listValue=listValue, tagSon=tagSon, tagFather=tagFather)
listValue = connect.pressListValueReturnListValueTriple(listXpath=listXpathCampoParcela, listValue=listValue, tagSon=tagSon)
# listValue = connect.removerEmpty(listValue=listValue)
# listValue = connect.formatListEqualValueLineTable(listValue=listValue)

# listValue = connect.formatListaColumnTable(listValue=listValue)

# table = connect.formatTable(listColumnTable=listColumnTable)
# conteudo = os.listdir('/')
# with open('listValue.txt', 'w') as listValue:
#     listValue.write(str(conteudo))


arquivo = open("listValue.txt", "w")
arquivo.write(str(listValue))
# print(listValue)

# connect.commissionSirconValue(listXpath=listXpath5)


# //*[@id="frm:pnlEsacalas"]/div[2]

# //*[@id="frm:j_idt124:1:j_idt156"]

# //*[@id="frm:j_idt124:2:j_idt156"]

# print(listValue)
sleep(3)