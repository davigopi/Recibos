# flake8: noqa
# pyright: # type: ignore

import os
from datetime import datetime

# from components.fileManip import FileManip
# from components.connect import Connect
from path_file import Path_file
# from components.creat_table_gerencia import Creat_table_gerencia

# from components.tableManip import TableManip
# from main_table import Main_table
import pandas as pd
# from typing import Optional
# from selenium import webdriver

# from time import ctime
import locale
# import sys
# Definir a localidade para Português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


# class Variables:
#     def __init__(self, *args, **kwargs) -> None:


# main_table = Main_table()
# connect = Connect()
# tableManip = TableManip()
# fileManip = FileManip()
path_file = Path_file()
# creat_table_gerencia = Creat_table_gerencia()
# Variaveis

user = 'usuario@gmail.com'
password = 'Senha'
month = 1
new_table_Cadastro_Consorciado = False
new_table_Cadastro_Funcionario = False
new_table_Cadastro_Ata = False
new_table_Comissoes_Configuracao = False
new_table_Comissoes_ConfigPagamento = False
mix = False
porcentagem_Vendas = 50
number_Line = 0
number_Column = 0

siteSircon = "https://app.sistemasircon.com.br/login"
connected = True
start = True


# para calcular maiores comissões
comissao_anterior1 = 0
vendedor_anterior1 = ''
comissao_anterior2 = 0
vendedor_anterior2 = ''
comissao_anterior3 = 0
vendedor_anterior3 = ''
error = False
value = None
value_separate = ''
value_fixed_column = ''  # por padrao ''
column_clone = ''
rename_name_column_origin = ''


clickOk = None

tagSon = ''
tagFather = ''
tagGet = ''
tagSelected = ''

#        '1' ou '2'
model = '2'

number_in_column = 0


date_ata_single = 'MAIO/2024'
date_sma_single = '1ª/MAIO/2024'

# PALAVRAS
word_Appdata = 'Appdata'
word_tables = 'tables'
word_log = 'log'
word_Qtd_Vendas = 'Qtd. Vendas'
word_CADASTRO = 'CADASTRO'
word_DIA_DA_SEMANA = 'DIA DA SEMANA'
# word__Qtd_Cotas_Inicial = ' Qtd. Cotas Inicial'
word_Periodo_Venda = 'Período Venda'
word_Periodo_Venda2 = 'PerÃ­odo Venda:'
word__Periodo_Valor_Qtd_Vendas = ' Periodo Valor Qtd Vendas'
word__Valor_Qtd_Vendas_Inicial = ' Valor Qtd Vendas Inicial'
word__Valor_Qtd_Vendas_Final = ' Valor Qtd Vendas Final'
word__Data_Inicial = ' Data inicial'
word__Data_Final = ' Data final'
word__Valor_Qtd_Vendas_Inicial_Supervisor = ' Valor Qtd Vendas Inicial Supervisor'
word__Valor_Qtd_Vendas_Final_Supervisor = ' Valor Qtd Vendas Final Supervisor'
word__Data_Inicial_Supervisor = ' Data inicial Supervisor'
word__Data_Final_Supervisor = ' Data final Supervisor'
word__Valor_Qtd_Vendas_Inicial_Gerencia = ' Valor Qtd Vendas Inicial Gerencia'
word__Valor_Qtd_Vendas_Final_Gerencia = ' Valor Qtd Vendas Final Gerencia'
word__Data_Inicial_Gerencia = ' Data inicial Gerencia'
word__Data_Final_Gerencia = ' Data final Gerencia'
word__Parc_ = ' Parc '
word_Parc = 'Parc'
word_Acoes = 'Ações'
word_a = 'à'
word_Periodo = 'Período'
word_Periodo_final = 'Período final'
word_Periodo_inicial = 'Período inicial'
word_Data_ = 'Data '
word_Ano = 'Ano'
word_Mes = 'Mes'
word_Mes_ = 'Mes '
word_Sma_ = 'Sma '
word_Vendedor = 'Vendedor'
word_Supervisor = 'Supervisor'
word_Gerencia = 'Gerencia'
word_Parceiro = 'Parceiro'
word_Cliente = 'Cliente'
word__Vend = ' Vend'
word__Sup = ' Sup'
word__Ger = ' Ger'
word__Qtd_Cotas = ' Qtd Cotas'
word_Total = 'Total'
word_Venc_ = 'Venc. '
word_Pag_ = 'Pag. '
word_º_Parc = 'º Parc'
word_ATA_ = 'ATA '
word_Cad_Adm = 'Cad. Adm'
word_Situacao_ = 'Situação '
word_Num_ = 'Num. '
word_1_Porc_ = '1º % '
word_2_Porc_ = '2º % '
word_3_Porc_ = '3º % '
word__Atrasado = ' Atrasado'
word__Atrasado_1_ATA = word__Atrasado + ' 1 ATA'
word__Atrasado_2_ATAs = word__Atrasado + ' 2 ATAs'
word_Data_Pag_Errada = 'Data Pag. Errada'
word_Pag_Mesma_ATA = 'Pag. Mesma ATA'
word_Pag_Adiantado_ATA = 'Pag. Adiantado ATA'
word_Pag_Atrasado_ATA = 'Pag. Atrasado ATA'
word_1_Parcela = '1ª Parcela'
word_Demais = 'Demais'
word_FAT = 'FAT'
word_Pagar_Comissao_ = 'Pagar Comissao '
word_Entrega = 'Entrega'


column_Parcela = 'Parcela'
column_Data_de_Entrega = 'Data de Entrega'
column_Porcentagem = '%'
column_Comissao = 'Comissão'
column_Adimplencia = 'Adimplência'
column_ATA_Entrega_Qtd_Cotas_Vend = 'ATA Entrega Qtd Cotas Vend'
column_ATA_Entrega_Qtd_Cotas_Sup = 'ATA Entrega Qtd Cotas Sup'
column_ATA_Entrega_Qtd_Cotas_Ger = 'ATA Entrega Qtd Cotas Ger'
column_ATA_Cad_Adm_Qtd_Cotas_Vend = 'ATA Cad. Adm Qtd Cotas Vend'
column_ATA_Cad_Adm_Qtd_Cotas_Sup = 'ATA Cad. Adm Qtd Cotas Ger'
column_ATA_Cad_Adm_Qtd_Cotas_Ger = 'ATA Cad. Adm Qtd Cotas Ger Ger'
column_Mes_Entrega_Qtd_Cotas_Vend = 'Mes Entrega Qtd Cotas Vend'
column_Mes_Entrega_Qtd_Cotas_Sup = 'Mes Entrega Qtd Cotas Sup'
column_Mes_Entrega_Qtd_Cotas_Ger = 'Mes Entrega Qtd Cotas Ger'
column_Mes_Cad_Adm_Qtd_Cotas_Vend = 'Mes Cad. Adm Qtd Cotas Vend'
column_Mes_Cad_Adm_Qtd_Cotas_Sup = 'Mes Cad. Adm Qtd Cotas Sup'
column_Mes_Cad_Adm_Qtd_Cotas_Ger = 'Mes Cad. Adm Qtd Cotas Ger'
word_DIA_DA_SEMANA = 'DIA DA SEMANA'
word_CADASTRO = 'CADASTRO'
column_Total_Sma_Cad_Adm_Vend = 'Total Sma Cad Adm Vend'
column_Total_Sma_Cad_Adm_Sup = 'Total Sma Cad Adm Sup'
column_Total_Sma_Cad_Adm_Ger = 'Total Sma Cad Adm Ger'
column_Total_ATA_Cad_Adm_Vend = 'Total ATA Cad Adm Vend'
column_Total_ATA_Cad_Adm_Sup = 'Total ATA Cad Adm Sup'
column_Total_ATA_Cad_Adm_Ger = 'Total ATA Cad Adm Ger'
column_Total_Sma_Entrega_Vend = 'Total Sma Entrega Vend'
column_Total_Sma_Entrega_Sup = 'Total Sma Entrega Sup'
column_Total_Sma_Entrega_Ger = 'Total Sma Entrega Ger'
column_Total_ATA_Entrega_Vend = 'Total ATA Entrega Vend'
column_Total_ATA_Entrega_Sup = 'Total ATA Entrega Sup'
column_Total_ATA_Entrega_Ger = 'Total ATA Entrega Ger'
column_profissao = ''

# COLUNAS
column_primary_key = 'PK'
column_Index = 'Index'
column_Cliente = 'Cliente'
column_Vendedor = 'Vendedor'
column_Gerente = 'Gerente'
column_Supervisor = 'Supervisor'
column_Cargo = 'Cargo'
column_Nome = 'Nome'
column_Administradora = 'Administradora'
column_Grupo = 'Grupo'
column_Cota = 'Cota'
column_N_Contrato = 'Nº Contrato'
column_Tabela_de_recebimento = 'Tabela de recebimento'
column_Tipo_Pagamento = 'Tipo Pagamento'
column_Valor_Parc_Inicial = 'Valor Parc. Inicial'
column_Periodo_Valor_Qtd_Vendas = '1 Periodo Valor Qtd Vendas'
column_Qtd_Valor_Vend = 'Qtd Valor Vend'
column_Tabela = 'Tabela'
column_Situacao = 'Situação'
column_Credito = 'Crédito'
column_CEP = 'CEP'
column_Nascimento = 'Nascimento'
column_Telefone = 'Telefone'
column_Celular = 'Celular'
column_WhatsApp = 'WhatsApp'
column_EMail = 'E-Mail'
column_Bairro = 'Bairro'
column_Data_Pag_Por = 'Data Pag. Por'
column_Data_de_Entrega = 'Data de Entrega'
column_Data_Cad_Adm = 'Data Cad. Adm'
column_N_Semana_Mes = 'N Semana Mes'
column_Data_Semana = 'Data Semana'
column_Data_Pag_1_Parc = 'Data Pag. 1º Parc'
column_Dia_semana = 'Dia semana'
column_Dia_Pag = 'Dia Pag.'
column_Mes_ano = 'Mes ano'
column_Periodo_final = 'Periodo_final'
column_Periodo_inicial = 'Periodo_inicial'
column_ATA = 'ATA'
column_Total_ATA_Entrega_Vend = 'Total ATA Entrega Vend'
column_ATA_Entrega = 'ATA Entrega'
column_Mes_Entrega = 'Mes Entrega'
column_Sma_Entrega = 'Sma Entrega'
column_ATA_Cad_Adm = 'ATA Cad. Adm'
column_Mes_Cad_Adm = 'Mes Cad. Adm'
column_Sma_Cad_Adm = 'Sma Cad. Adm'
column_1_Parcela_Recebera = '1ª Parcela Recebera'
column_1_Parcela_Referencia = '1ª Parcela Referencia'
column_1_Parcela_Periodo_Inicial = '1ª Parcela Periodo Inicial'
column_1_Parcela_Data_Inicial = '1ª Parcela Data Inicial'
column_1_Parcela_Periodo_Final = '1ª Parcela Periodo Final'
column_1_Parcela_Data_Final = '1ª Parcela Data Final'
column_Demais_Recebera = 'Demais Recebera'
column_Demais_Referencia = 'Demais Referencia'
column_Demais_Periodo_Inicial = 'Demais Periodo Inicial'
column_Demais_Data_Inicial = 'Demais Data Inicial'
column_Demais_Periodo_Final = 'Demais Periodo Final'
column_Demais_Data_Final = 'Demais Data Final'
column_FAT_Recebera = 'FAT Recebera'
column_FAT_Referencia = 'FAT Referencia'
column_FAT_Periodo_Inicial = 'FAT Periodo Inicial'
column_FAT_Data_Inicial = 'FAT Data Inicial'
column_FAT_Periodo_Final = 'FAT Periodo Final'
column_FAT_Data_Final = 'FAT Data Final'
column_PK_Vend_ATA_Entrega = 'PK Vend ATA Entrega'


# COLUNAS MONTADAS
column_Nome_Vendedor = column_Nome + ' ' + word_Vendedor
column_Cargo_Vendedor = column_Cargo + ' ' + word_Vendedor
column_Nome_Supervisor = column_Nome + ' ' + word_Supervisor
column_Cargo_Supervisor = column_Cargo + ' ' + word_Supervisor
column_Administradora_Supervisor = column_Administradora + ' ' + word_Supervisor
column_Tabela_Supervisor = column_Tabela + ' ' + word_Supervisor
column_Periodo_Valor_Qtd_Vendas_Supervisor = column_Periodo_Valor_Qtd_Vendas + ' ' + word_Supervisor
column_Periodo_Valor_Qtd_Vendas_Gerencia = column_Periodo_Valor_Qtd_Vendas + ' ' + word_Gerencia
column_Cargo_Gerencia = column_Cargo + ' ' + word_Gerencia

# porcentagem_Vendas_1 = '1' + word__Atrasado + ' ' + str(porcentagem_Vendas)
# porcentagem_Vendas_2 = '2' + word__Atrasado + ' ' + str(porcentagem_Vendas)

# LISTAS
listValue = []
list_list_columns_venc = []
list_list_columns_situacao_num_ATA = []
list_list_columns_ata_pag_atrasado_n_ata = []
list_list_columns_comissao_atrasada = []
list_list_columns_num_ATA_atrasado = []
list_list_columns_percentage = []
list_list_column_orden_total = []
list_columns_full = []
list_one_two = []
list_name_change = []
list_one_two_three = []
list_administradora_limit = []
list_cargo_limit = []
list_cargos_limit_exist = []
list_administradoras_limit_exist = []
list_tabela_recebiemnto_limit_exist = []
list_cols_full_ata_sing_pag = []
list_cols_full_ata_sing_venc = []
list_name_columns_Pagar_Comissao_N_Parc = []
list_columns_full_ata_entrega_pag = [column_ATA_Entrega]
list_columns_full_ata_cadastro_pag = [column_ATA_Cad_Adm]
list_columns_full_sma_entrega_pag = [column_Sma_Entrega]
list_columns_full_sma_cadastro_pag = [column_Sma_Cad_Adm]
list_columns_full_ata_entrega_venc = [column_ATA_Entrega]
list_columns_full_ata_cadastro_venc = [column_ATA_Cad_Adm]
list_columns_full_sma_entrega_venc = [column_Sma_Entrega]
list_columns_full_sma_cadastro_venc = [column_Sma_Cad_Adm]
list_columns_cliente = [
    column_CEP, column_Nascimento, column_Telefone,
    column_Celular, column_WhatsApp, column_EMail,
    column_Bairro
]
list_columns_ata_mes_sma = [
    column_ATA_Entrega, column_Mes_Entrega, column_Sma_Entrega,
    column_ATA_Cad_Adm, column_Mes_Cad_Adm, column_Sma_Cad_Adm
]
list_list_columns_pag = [
    [column_Situacao, column_Data_de_Entrega, column_ATA_Entrega,
        column_Sma_Entrega, column_Mes_Entrega],
    [column_Situacao, column_Data_Cad_Adm, column_ATA_Cad_Adm,
        column_Sma_Cad_Adm, column_Mes_Cad_Adm]
]
list_list_columns_order = [
    [column_Situacao, column_Data_de_Entrega, column_Data_Cad_Adm,
        column_ATA_Entrega, column_ATA_Cad_Adm, column_Sma_Entrega,
        column_Sma_Cad_Adm, column_Mes_Entrega, column_Mes_Cad_Adm]
]
list_columns_start = [
    column_Administradora,
    column_Vendedor,
    column_Supervisor,
    column_Cargo,
    column_Cargo_Vendedor,
    column_Cargo_Supervisor,
    column_Cargo_Gerencia,
    column_Credito,
    column_Valor_Parc_Inicial,
    column_Data_Pag_1_Parc,
    column_Data_de_Entrega,
    column_Dia_Pag,
    column_Grupo,
    column_Cota,
    column_N_Contrato,
    column_1_Parcela_Recebera,
    column_Demais_Recebera,
    column_FAT_Recebera,
    column_Demais_Referencia,
    column_Qtd_Valor_Vend,
    column_Data_Pag_Por,
    column_1_Parcela_Referencia,
    column_ATA_Cad_Adm,
    column_ATA_Entrega,
    column_PK_Vend_ATA_Entrega
]
headerDtPagamentoParcelas = [
    column_Cargo,
    column_Administradora,
    column_Tipo_Pagamento,
    column_Data_Pag_Por,
    column_Dia_Pag,
    column_1_Parcela_Recebera,
    column_1_Parcela_Referencia,
    column_1_Parcela_Periodo_Inicial,
    column_1_Parcela_Data_Inicial,
    column_1_Parcela_Periodo_Final,
    column_1_Parcela_Data_Final,
    column_Demais_Recebera,
    column_Demais_Referencia,
    column_Demais_Periodo_Inicial,
    column_Demais_Data_Inicial,
    column_Demais_Periodo_Final,
    column_Demais_Data_Final,
    column_FAT_Recebera,
    column_FAT_Referencia,
    column_FAT_Periodo_Inicial,
    column_FAT_Data_Inicial,
    column_FAT_Periodo_Final,
    column_FAT_Data_Final,
    column_Index
]
list_columns_test_table_configPag_1 = [
    column_Cargo,
    column_Administradora,
    column_Tipo_Pagamento,
    column_Data_Pag_Por,
    column_Dia_Pag,
    column_1_Parcela_Recebera,
    column_Demais_Recebera,
    column_FAT_Recebera,
    column_Index
]
list_columns_test_table_configPag_2 = [
    column_Cargo,
    column_Administradora,
    column_Tipo_Pagamento
]
list_columns_date_weekly_new = [
    column_N_Semana_Mes,
    column_Data_Semana,
    column_Dia_semana,
    column_Mes_ano
]
list_columns_end = [
    column_Parcela,
    column_Administradora,
    column_N_Contrato,
    column_Data_de_Entrega,
    column_Cliente,
    column_Credito,
    column_Porcentagem,
    column_Comissao,
    column_Adimplencia,
]
list_columns_ATA_Entrega_Qtd_Cotas = [
    column_ATA_Entrega_Qtd_Cotas_Vend,
    column_ATA_Entrega_Qtd_Cotas_Sup,
    column_ATA_Entrega_Qtd_Cotas_Ger
]
list_columns_ATA_Cad_Adm_Qtd_Cotas = [
    column_ATA_Cad_Adm_Qtd_Cotas_Vend,
    column_ATA_Cad_Adm_Qtd_Cotas_Sup,
    column_ATA_Cad_Adm_Qtd_Cotas_Ger
]
list_columns_Mes_Entrega_Qtd_Cotas = [
    column_Mes_Entrega_Qtd_Cotas_Vend,
    column_Mes_Entrega_Qtd_Cotas_Sup,
    column_Mes_Entrega_Qtd_Cotas_Ger
]
list_columns_Mes_Cad_Adm_Qtd_Cotas = [
    column_Mes_Cad_Adm_Qtd_Cotas_Vend,
    column_Mes_Cad_Adm_Qtd_Cotas_Sup,
    column_Mes_Cad_Adm_Qtd_Cotas_Ger
]
# list_columns_Total_Sma_Cad_Adm = [
#     column_Total_Sma_Cad_Adm_Vend,
#     column_Total_Sma_Cad_Adm_Sup,
#     column_Total_Sma_Cad_Adm_Ger
# ]
# list_columns_Total_ATA_Cad_Adm = [
#     column_Total_ATA_Cad_Adm_Vend,
#     column_Total_ATA_Cad_Adm_Sup,
#     column_Total_ATA_Cad_Adm_Ger
# ]
# list_columns_Total_Sma_Entrega = [
#     column_Total_Sma_Entrega_Vend,
#     column_Total_Sma_Entrega_Sup,
#     column_Total_Sma_Entrega_Ger
# ]
# list_columns_Total_ATA_Entrega = [
#     column_Total_ATA_Entrega_Vend,
#     column_Total_ATA_Entrega_Sup,
#     column_Total_ATA_Entrega_Ger
# ]
# list_porcentagem_vendas = [
#     porcentagem_Vendas_1,
#     porcentagem_Vendas_2
# ]
list_columns_full_ata = [column_ATA_Entrega, column_ATA_Cad_Adm]
list_columns_full_weekly = [column_Sma_Entrega, column_Sma_Cad_Adm]


list_words_ATA_Venc_º_Parc = [word_ATA_ + word_Venc_, word_º_Parc]
list_situacao_to_comission = ['NORMAL', 'PAGA']
list_recebera_to_comission = ['SIM']
list_condition_ata = [word_Entrega, word_Cad_Adm, word_Parc, word_FAT]
list_cargo_not_calc_commis = ['ESTAGIÁRIO', 'ZERADO']
dict_duplicate_sum = {}
dict_duplicate_count = {}
dic_months = {
    'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4,
    'MAIO': 5, 'JUNHO': 6, 'JULHO': 7, 'AGOSTO': 8, 'SETEMBRO': 9,
    'OUTUBRO': 10, 'NOVEMBRO': 11, 'DEZEMBRO': 12
}
inverted_dic_months = {v: k for k, v in dic_months.items()}
salve_first = True
# TAGS
tag_option = 'option'
tag_select = 'select'
tag_outerHTML = 'outerHTML'
tag_value = 'value'
tag_selected = '/option[@selected="selected"]'
# tag_table = 'table'
tag_row = 'tr'
tag_data = 'td'
# tag_cab = 'th'
# XPATHS
listXpathLog = [
    '//*[@id="form:txtUsuarioSircon"]',  # campo usuario
    '//*[@id="form:txtSenhaSircon"]',  # campo senha
    '//*[@id="form:btLogar"]'  # botao confirmar
]
# linha coluna calendario
line_ = 1
column_ = 0
xp0_ = '//*[@id="menucadastro"]/a'  # menu cadastro
xp1_ = '//*[@id="menucadastro"]/ul/li[5]'  # menu consorciado
# cp entrega venda inici
xp2_ = '//*[@id="pnlBloco"]/div[6]/div/div[3]/div'
# bt seta para esquerda
xp3_ = '//*[@id="ui-datepicker-div"]/div[1]/a[1]'
text = '//*[@id="ui-datepicker-div"]/table/tbody'
xp4_ = f'{text}/tr[{line_}]/td[{column_}]'
# bt fechar calend
xp5_ = '//*[@id="ui-datepicker-div"]/div[3]/button[2]'
# cp entrega venda final
xp6_ = '//*[@id="pnlBloco"]/div[6]/div/div[4]/div'
xp7_ = '//*[@id="btnConsultar"]'  # botao consultar
xp8_ = '//*[@id="btnGerarXls"]'  # botao de download
listXpathSales = [
    xp0_, xp1_, xp2_, xp3_, xp4_, xp5_,
    xp6_, xp3_, xp4_, xp5_, xp7_, xp8_]
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
for num in range(99):  # quantidade de campos comissões configuracao
    listCampoCotaPeriodoParcela.append([
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
listXpathMinutes = [
    '//*[@id="menucadastro"]/a',  # menu cadastro
    '//*[@id="menucadastro"]/ul/li[2]/a',  # menu Ata
    '//*[@id="frm:cbAno"]',  # Ano
    '//*[@id="frm:pnlLista"]',   # informacao OBS: alterado ordem.
    '//*[@id="frm:cbAdministradora"]',  # administradora
]


arqTableCadastroConsorciado = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Cadastro_Consorciado.csv')  # noqa
arqTableCadastroFuncionario = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Cadastro_Funcionario.csv')  # noqa
arqTableCadastroAta = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Cadastro_Ata.csv')  # noqa
arqTableComissoesConfiguracao = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Comissoes_Configuracao.csv')  # noqa
arqTableComissoesConfigPag = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Comissoes_ConfigPagamento.csv')  # noqa
# arqTableComissoesConfigPagTratada = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Comissoes_ConfigPagTratada.csv')  # noqa
arqTesteDuplTableComissoesConfigPag = path_file.path_file_create_user(word_Appdata, word_tables, 'Teste_Dupl_table_Comissoes_ConfigPagamento.csv')  # noqa
arqTableGerencia = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Gerencia.csv')  # noqa
arqTableComissoesConfigPagSupervisor = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Comissoes_ConfigPagamento_supervisor.csv')  # noqa
arqtableMerge = path_file.path_file_create_user(word_Appdata, word_tables, 'tableMerge.csv')  # noqa
arqtableMergeOrder = path_file.path_file_create_user(word_Appdata, word_tables, 'tableMergeOrder.csv')  # noqa
arqTableDatasSemanais = path_file.path_file_create_user(word_Appdata, word_tables, 'table_datas_semanais.csv')  # noqa
arqTableTeste1 = path_file.path_file_create_user(word_Appdata, word_tables, 'table_teste1.csv')  # noqa
arqTableTeste2 = path_file.path_file_create_user(word_Appdata, word_tables, 'table_teste2.csv')  # noqa
arqTableTeste3 = path_file.path_file_create_user(word_Appdata, word_tables, 'table_teste3.csv')  # noqa
pathDonwload = os.environ['USERPROFILE'] + '\\Downloads'
arqDonwloadSales = pathDonwload + '\\consorciados.csv'
arqDonwloadFunction = pathDonwload + '\\funcionarios.csv'

arq_log = path_file.path_file_create_user(word_Appdata, word_log, 'log.txt')  # noqa


table_Cadastro_Consorciado: pd.DataFrame = pd.DataFrame()
table_Cadastro_Funcionario: pd.DataFrame = pd.DataFrame()
table_Cadastro_Ata: pd.DataFrame = pd.DataFrame()
table_Comissoes_Configuracao: pd.DataFrame = pd.DataFrame()
table_Comissoes_ConfigPagamento: pd.DataFrame = pd.DataFrame()
table_Gerencia: pd.DataFrame = pd.DataFrame()
table_date_weekly: pd.DataFrame = pd.DataFrame()
table_Cadastro_funcionario_supervisor: pd.DataFrame = pd.DataFrame()
table_Comissoes_Configuracao_supervisor: pd.DataFrame = pd.DataFrame()
table_full: pd.DataFrame = pd.DataFrame()
table_duplicate: pd.DataFrame = pd.DataFrame()


class Variables:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def date_file(self):
        text_te = 'Datas das tabelas de: \n'
        date_table_Cadastro_Consorciado = datetime.fromtimestamp(os.path.getmtime(arqTableCadastroConsorciado)).strftime('%c')  # noqa
        text_te += f'Cadastro de consorciado: {date_table_Cadastro_Consorciado} \n'
        date_table_Cadastro_Funcionario = datetime.fromtimestamp(os.path.getmtime(arqTableCadastroFuncionario)).strftime('%c')  # noqa
        text_te += f'Cadastro de funcionario: {date_table_Cadastro_Funcionario} \n'
        date_table_Cadastro_Ata = datetime.fromtimestamp(os.path.getmtime(arqTableCadastroAta)).strftime('%c')  # noqa
        text_te += f'Cadastro de ATAs: {date_table_Cadastro_Ata} \n'
        date_table_Comissoes_Configuracao = datetime.fromtimestamp(os.path.getmtime(arqTableComissoesConfiguracao)).strftime('%c')  # noqa
        text_te += f'Comissões configuração: {date_table_Comissoes_Configuracao} \n'
        date_table_Comissoes_ConfigPagamento = datetime.fromtimestamp(os.path.getmtime(arqTableComissoesConfigPag)).strftime('%c')  # noqa
        text_te += f'Comissões configuração de pagamento: {date_table_Comissoes_ConfigPagamento} \n'
        return (text_te)
