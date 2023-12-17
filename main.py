from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from connect import Connect
import os
from time import sleep

siteSircon = "https://app.sistemasircon.com.br/login"
user = 'davigopi@gmail.com'
password = '36vad28'
security = [user, password]

listXpath1 = [
            '//*[@id="form:txtUsuarioSircon"]'  # campo usuario
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


listXpath3 = [
            '//*[@id="menufinan"]'  # comissões
            , '//*[@id="menufinan"]/ul/li[2]'  # Configuração
            , '//*[@id="frm:tpComissao"]'  # Tipo Comissão
            , '//*[@id="frm:tpComissao"]/option[2]'  # Pagamento
            , '//*[@id="frm:cbAdministradora"]'  # Administradora
            , '//*[@id="frm:cbAdministradora"]/option[4]'  # Disal
            , '//*[@id="frm:cbTabelaRecebimento"]'  # Tabela de Recebimento
            , '//*[@id="frm:cbTabelaRecebimento"]/option[2]'  # Tabela disal normal
            , '//*[@id="frm:cbCargo"]'  # Cargo
            , '//*[@id="frm:cbCargo"]/option[5]'  # Consultor CLR - a partir jan-2018
            ]
listCampo = ['//*[@id="frm:pnlEsacalas"]/div[1]'  # campo de 0 a 2 
                , '//*[@id="frm:pnlEsacalas"]/div[2]'  # campo de 3 a 5
                , '//*[@id="frm:pnlEsacalas"]/div[3]'  # campo de 6 a 9
                , '//*[@id="frm:pnlEsacalas"]/div[4]'  # campo de 10 a 14
                , '//*[@id="frm:pnlEsacalas"]/div[5]'  # campo de 15 a 100000000
            ]
listParcela = ['//*[@id="frm:j_idt124:0:j_idt149"]'  # parcela 1
                , '//*[@id="frm:j_idt124:0:j_idt156"]'  # parcela 2
                , '//*[@id="frm:j_idt124:0:j_idt158"]'  # parcela 3
                , '//*[@id="frm:j_idt124:0:j_idt160"]'  # parcela 4
                , '//*[@id="frm:j_idt124:0:j_idt162"]'  # parcela 5
                , '//*[@id="frm:j_idt124:0:j_idt164"]'  # parcela 6
                , '//*[@id="frm:j_idt124:0:j_idt166"]'  # parcela 7
                , '//*[@id="frm:j_idt124:0:j_idt168"]'  # parcela 8
                , '//*[@id="frm:j_idt124:0:j_idt170"]'  # parcela 9
                , '//*[@id="frm:j_idt124:0:j_idt172"]'  # parcela 10
                , '//*[@id="frm:j_idt124:0:j_idt174"]'  # parcela 11
                , '//*[@id="frm:j_idt124:0:j_idt176"]'  # parcela 12
            ]  
listXpath4 = [listCampo, listParcela]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(siteSircon)
connect = Connect(driver=driver)
connect.logarSircon(security=security, listXpath=listXpath1)
# df = connect.dfSircon(arqCons=arqCons, months=months, listXpath=listXpath2)
# print(df)
connect.commissionSircon(listXpath=listXpath3)
connect.commissionSirconValue(listXpath=listXpath4)
sleep(600)