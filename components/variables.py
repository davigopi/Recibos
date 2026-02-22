# flake8: noqa
# pyright: # type: ignore

import os
import pandas as pd
import locale
from datetime import datetime
from path_file import Path_file

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

path_file = Path_file()

siteSircon = "https://app.sistemasircon.com.br/login"
connected = True
start = True

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
porcentagem_Entrega = '100'
number_Line = 0
number_Column = 0

size_font = 8
size_font2 = 7
size_line = 6
space_paragraph = 2
begin = True

text_size_head = 12
text_size_footer = 10
text_size_table = 6
cell_height = 4
space_columns = 4

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

word_profissao = ''
word_Valor_Qtd_Vendas_Inicial_profissao = ''


clickOk = None

tagSon = ''
tagFather = ''
tagGet = ''
tagSelected = ''


number_in_column = 0

sum_comissao = 0
sum_comissao_adimplencia = 0
sum_all_comissao = 0
sum_all_comissao_gerente = 0
sum_credito = 0
adimplencias = ''

date_ata_single = 'MAIO/2024'
date_sma_single = '1ª/MAIO/2024'

# PALAVRAS
word_Appdata = 'Appdata'
word_tables = 'tables'
word_log = 'log'
word_CADASTRO = 'CADASTRO'
word_DIA_DA_SEMANA = 'DIA DA SEMANA'

word_Adimplencia = 'Adimplência'
word_Acoes = 'Ações'
word_a = 'à'
word_Ano = 'Ano'
word_Cliente = 'Cliente'
word_Parceiro = 'Parceiro'
word_Vendas = 'Vendas'
word_Cotas = 'Cotas'
word_Recebera = 'Recebera'
word_Referencia = 'Referencia'
word_Parcela = 'Parcela'
word_RECIBO_DE_PAGAMENTO = 'RECIBO DE PAGAMENTO'
word_RESUMO = 'RESUMO:'
word_PARCEIRO = 'PARCEIRO:'
word_FUNCIONARIO = 'FUNCIONÁRIO:'
word_TOTAL = 'TOTAL'
word_CREDITO = 'CRÉDITO'
word_COMISSAO = 'COMISSÃO'
word_ADIMPLENCIA = 'ADIMPLÊNCIA'
word_COMISSAO_ADIMPLENTE = 'COMISSÃO ADIMPLENTE'
word_PAGAMENTOS_ATRASADOS = 'PAGAMENTOS ATRASADOS:'
word_RESUMO_PAGAMENTOS_ATRASADOS = 'RESUMO PAGAMENTOS ATRASADOS:'
word_PAGA = 'PAGA'
word_NORMAL = 'NORMAL'
word_SIM = 'SIM'
word_ESTAGIARIO = 'ESTAGIÁRIO'
word_ZERADO = 'ZERADO'
word_Situacoes = 'Situações'


word_ponto = '.'
word_cifrao = '$$$ '

word_porc = '%'
word_porc_ = word_porc + ' '
word_Dia = 'Dia'
word_Dia_ = word_Dia + ' '
word_Situacao = 'Situação'
word_Situacao_ = word_Situacao + ' '
word_Comissao = 'Comissão'
word_Comissao_ = word_Comissao + ' '
word_Atrasada = 'Atrasada'
word__Atrasada = ' ' + word_Atrasada
word__porc = ' ' + word_porc
word_Escala = 'Escala'
word_Escala_ = word_Escala + ' '
word_PK = 'PK'
word_PK_ = word_PK + ' '
word_Num = 'Num' + word_ponto
word_Num_ = word_Num + ' '
word_Qtd = 'Qtd' + word_ponto
word_Qtd_ = word_Qtd + ' '
word_Parc = 'Parc'  # não pode colocar . devido a relatorio da sircon
word_Parc_ = word_Parc + ' '
word_º_Parc = 'º ' + word_Parc
word__Parc_ = ' ' + word_Parc + ' '
word_Venc = 'Venc' + word_ponto
word_Venc_ = word_Venc + ' '
word_Pag = 'Pag' + word_ponto
word_Pag_ = word_Pag + ' '
word_Periodo = 'Período'
word_Periodo_ = word_Periodo + ' '
word__Periodo = ' ' + word_Periodo
word_Data = 'Data'
word_Data_ = word_Data + ' '
word__Data_ = ' ' + word_Data + ' '
word_Mes = 'Mes'
word_Mes_ = word_Mes + ' '
word_Sma = 'Sma'
word_Sma_ = word_Sma + ' '
word_Semana = 'Semana'
word_Semana_ = word_Semana + ' '
word_Valor = 'Valor'
word_Valor_ = word_Valor + ' '
word__Valor_ = ' ' + word_Valor + ' '
word_Venda = 'Venda'
word_Venda_ = word_Venda + ' '
word_Vendedor = 'Vendedor'
word__Vendedor = ' ' + word_Vendedor
word_Vend = 'Vend' + word_ponto
word_Vend_ = word_Vend + ' '
word_Supervisor = 'Supervisor'
word__Supervisor = ' ' + word_Supervisor
word_Gerencia = 'Gerencia'
word__Gerencia = ' ' + word_Gerencia
word_Total = 'Total'
word_Total_ = word_Total + ' '
word_ATA = 'ATA'
word_ATA_ = word_ATA + ' '
word_Entrega = 'Entrega'
word_Entrega_ = word_Entrega + ' '
word_Cad_Adm = 'Cad' + word_ponto + ' Adm'
word_Cad_Adm_ = word_Cad_Adm + ' '
word_1_Parcela = '1ª ' + word_Parcela
word_1_Parcela_ = word_1_Parcela + ' '
word_Demais = 'Demais'
word_Demais_ = word_Demais + ' '
word_FAT = 'FAT'
word_FAT_ = word_FAT + ' '
word_Inicial = 'Inicial'
word_Inicial_ = word_Inicial + ' '
word_Final = 'Final'
word_Final_ = word_Final + ' '
word_Nao = 'Não'
word_Nao_ = word_Nao + ' '
word_Encontrada = 'Encontrada'

word_ATA_Nao_Encontrada = word_ATA_ + word_Nao_ + word_Encontrada
word_Parc_ponto_ = word_Parc + word_ponto + ' '
word_Qtd_Vendas = word_Qtd_ + word_Vendas
word_Qtd_Vendas_ = word_Qtd_Vendas + ' '
word_Valor_Qtd_Vendas = word_Valor_ + word_Qtd_Vendas
word_Valor_Qtd_Vendas_ = word_Valor_ + word_Qtd_Vendas_
word__Valor_Qtd_Vendas_ = ' ' + word_Valor_Qtd_Vendas_
word__Valor_Qtd_Vendas = ' ' + word_Valor_Qtd_Vendas

word_ATA_Atrasada = word_ATA + word__Atrasada
word__1_ATA_Atrasada = ' 1 ' + word_ATA_Atrasada
word__2_ATA_Atrasada = ' 2 ' + word_ATA_Atrasada
word_Data_Pag_Errada = word_Data_ + word_Pag_ + 'Errada'
word_Pag_Comissao_ = word_Pag_ + word_Comissao_
word_Pag_Mesma_ATA = word_Pag_ + 'Mesma ' + word_ATA
word_Pag_Adiantado_ATA = word_Pag_ + word_ATA_Atrasada
word_Pag_Atrasado_ATA = word_Pag_ + word_ATA_Atrasada

word__Data_Inicial = word__Data_ + word_Inicial
word__Data_Final = word__Data_ + word_Final
word__Valor_Qtd_Vendas_Inicial = word__Valor_Qtd_Vendas_ + word_Inicial
word__Valor_Qtd_Vendas_Final = word__Valor_Qtd_Vendas_ + word_Final
word__Valor_Qtd_Vendas_Inicial_Supervisor = word__Valor_Qtd_Vendas_ + word_Inicial_ + word_Supervisor
word__Valor_Qtd_Vendas_Final_Supervisor = word__Valor_Qtd_Vendas_ + word_Final_ + word_Supervisor
word__Data_Inicial_Supervisor = word__Data_ + word_Inicial_ + word_Supervisor
word__Data_Final_Supervisor = word__Data_ + word_Final_ + word_Supervisor
word__Valor_Qtd_Vendas_Inicial_Gerencia = word__Valor_Qtd_Vendas_ + word_Inicial_ + word_Gerencia
word__Valor_Qtd_Vendas_Final_Gerencia = word__Valor_Qtd_Vendas_ + word_Final_ + word_Gerencia
word__Data_Inicial_Gerencia = word__Data_ + word_Inicial_ + word_Gerencia
word__Data_Final_Gerencia = word__Data_ + word_Final_ + word_Gerencia
word_Periodo_final = word_Periodo_ + word_Final
word_Periodo_inicial = word_Periodo_ + word_Inicial
word_Periodo_Venda = word_Periodo_ + word_Venda
word_Periodo_Venda2 = 'PerÃ­odo ' + word_Venda + ':'
word__Periodo_Valor_Qtd_Vendas = word__Periodo + word__Valor_ + word_Qtd_Vendas

# O programa vai setar
seller_single = ''
date_atasma_single = ''
column_profissao = ''

# column_ATASma_EntregaCada_Adm = ''
# colunas criadas para calculos do PDF recibo
column_porc_ATA_Entrega = word_porc_ + word_ATA_ + word_Entrega
column_porc = word_porc
column_porc_Num = word_porc_ + word_Num
column_Comissao = word_Comissao
column_Comissao_50_porc = word_Comissao + ' 50' + word_porc
column_Parc = word_Parc + word_ponto
column_ATA_Venc_n_Parc = word_ATA_ + word_Venc_ + 'n ' + word_Parc
column_Adimplencia = word_Adimplencia
column_Pag_Comissao_1_Parc = word_Pag_ + word_Pag_Comissao_ + '1º ' + word_Parc
# column_ATA_Venc_pag = word_ATA_ + word_Venc_ + word_Pag

column_Escala_ATA_Entrega_Vendedor = word_Escala_ + word_ATA_ + word_Entrega_ + word_Vendedor
column_Escala_ATA_Entrega_Supervisor = word_Escala_ + word_ATA_ + word_Entrega_ + word_Supervisor
column_Escala_ATA_Entrega_Gerencia = word_Escala_ + word_ATA_ + word_Entrega_ + word_Gerencia

column_Escala_ATA_Cad_Adm_Vendedor = word_Escala_ + word_ATA_ + word_Cad_Adm_ + word_Vendedor
column_Escala_ATA_Cad_Adm_Supervisor = word_Escala_ + word_ATA_ + word_Cad_Adm_ + word_Supervisor
column_Escala_ATA_Cad_Adm_Gerencia = word_Escala_ + word_ATA_ + word_Cad_Adm_ + word_Gerencia

column_Escala_Mes_Entrega_Vendedor = word_Escala_ + word_Mes_ + word_Entrega_ + word_Vendedor
column_Escala_Mes_Entrega_Supervisor = word_Escala_ + word_Mes_ + word_Entrega_ + word_Supervisor
column_Escala_Mes_Entrega_Gerencia = word_Escala_ + word_Mes_ + word_Entrega_ + word_Gerencia

column_Escala_Mes_Cad_Adm_Vendedor = word_Escala_ + word_Mes_ + word_Cad_Adm_ + word_Vendedor
column_Escala_Mes_Cad_Adm_Supervisor = word_Escala_ + word_Mes_ + word_Cad_Adm_ + word_Supervisor
column_Escala_Mes_Cad_Adm_Gerencia = word_Escala_ + word_Mes_ + word_Cad_Adm_ + word_Gerencia

column_Total_Sma_Cad_Adm_Vendedor = word_Total_ + word_Sma_ + word_Cad_Adm_ + word_Vendedor
column_Total_Sma_Cad_Adm_Supervisor = word_Total_ + word_Sma_ + word_Cad_Adm_ + word_Supervisor
column_Total_Sma_Cad_Adm_Gerencia = word_Total_ + word_Sma_ + word_Cad_Adm_ + word_Gerencia

column_Total_ATA_Cad_Adm_Vendedor = word_Total_ + word_ATA_ + word_Cad_Adm_ + word_Vendedor
column_Total_ATA_Cad_Adm_Supervisor = word_Total_ + word_ATA_ + word_Cad_Adm_ + word_Supervisor
column_Total_ATA_Cad_Adm_Gerencia = word_Total_ + word_ATA_ + word_Cad_Adm_ + word_Gerencia

column_Total_Sma_Entrega_Vendedor = word_Total_ + word_Sma_ + word_Entrega_ + word_Vendedor
column_Total_Sma_Entrega_Supervisor = word_Total_ + word_Sma_ + word_Entrega_ + word_Supervisor
column_Total_Sma_Entrega_Gerencia = word_Total_ + word_Sma_ + word_Entrega_ + word_Gerencia

column_Total_ATA_Entrega_Vendedor = word_Total_ + word_ATA_ + word_Entrega_ + word_Vendedor
column_Total_ATA_Entrega_Supervisor = word_Total_ + word_ATA_ + word_Entrega_ + word_Supervisor
column_Total_ATA_Entrega_Gerencia = word_Total_ + word_ATA_ + word_Entrega_ + word_Gerencia

column_Qtd_Vendas_ATA_Entrega_Vendedor = word_Qtd_Vendas_ + word_ATA_ + word_Entrega_ + word_Vendedor


# COLUNAS
column_ATA = word_ATA
column_primary_key = word_PK
column_Vendedor = word_Vendedor
column_Supervisor = word_Supervisor
column_Situacao = word_Situacao
column_Situacoes = word_Situacoes
column_Index = 'Index'
column_Cliente = 'Cliente'
# column_Cliente_25 = 'Cliente 25' 
column_Gerente = 'Gerente'
column_Cargo = 'Cargo'
column_Nome = 'Nome'
column_Administradora = 'Administradora'
column_Grupo = 'Grupo'
column_Cota = 'Cota'
column_N_Contrato = 'Nº Contrato'
column_Tabela = 'Tabela'
column_Tabela_de_recebimento = 'Tabela de recebimento'  # table comissoes configuracao
column_Tipo_Pagamento = 'Tipo Pagamento'
column_Credito = 'Crédito'
column_CEP = 'CEP'
column_Nascimento = 'Nascimento'
column_Telefone = 'Telefone'
column_Celular = 'Celular'
column_WhatsApp = 'WhatsApp'
column_EMail = 'E-Mail'
column_Bairro = 'Bairro'
# COLUNAS MONTADAS
column_Data_Pag_Por = word_Data_ + word_Pag_ + 'Por'
column_Data_de_Entrega = word_Data_ + 'de ' + word_Entrega
column_Data_Cad_Adm = word_Data_ + word_Cad_Adm
column_N_Semana_Mes = 'N ' + word_Semana_ + word_Mes
column_Data_Semana = word_Data_ + word_Semana
column_Data_Pag_1_Parc = word_Data_ + word_Pag_ + '1º ' + word_Parc
column_Dia_Semana = word_Dia_ + word_Semana
column_Valor_Parc_Inicial = word_Valor_ + word_Parc_ponto_ + word_Inicial
column_Periodo_Valor_Qtd_Vendas = '1 ' + word_Periodo_ + word_Valor_ + word_Qtd_Vendas
column_Periodo_Valor_Qtd_Vendas_Supervisor = column_Periodo_Valor_Qtd_Vendas + word_Supervisor
column_Periodo_Valor_Qtd_Vendas_Gerencia = column_Periodo_Valor_Qtd_Vendas + word_Gerencia
column_Qtd_Valor_Vendedor = word_Qtd_ + word_Valor_ + word_Vendedor
column_Dia_Pag = word_Dia_ + word_Pag
column_Mes_ano = word_Mes_ + word_Ano
column_Periodo_Inicial = word_Periodo_ + word_Inicial
column_Periodo_Final = word_Periodo_ + word_Final
column_ATA_Entrega = word_ATA_ + word_Entrega
column_Mes_Entrega = word_Mes_ + word_Entrega
column_Sma_Entrega = word_Sma_ + word_Entrega
column_ATA_Cad_Adm = word_ATA_ + word_Cad_Adm
column_Mes_Cad_Adm = word_Mes_ + word_Cad_Adm
column_Sma_Cad_Adm = word_Sma_ + word_Cad_Adm
column_1_Parcela_Recebera = word_1_Parcela_ + word_Recebera
column_1_Parcela_Referencia = word_1_Parcela_ + word_Referencia
column_1_Parcela_Periodo_Inicial = word_1_Parcela_ + word_Periodo_ + word_Inicial
column_1_Parcela_Data_Inicial = word_1_Parcela_ + word_Data_ + word_Inicial
column_1_Parcela_Periodo_Final = word_1_Parcela_ + word_Periodo_ + word_Final
column_1_Parcela_Data_Final = word_1_Parcela_ + word_Data_ + word_Final
column_Demais_Recebera = word_Demais_ + word_Recebera
column_Demais_Referencia = word_Demais_ + word_Referencia
column_Demais_Periodo_Inicial = word_Demais_ + word_Periodo_ + word_Inicial
column_Demais_Data_Inicial = word_Demais_ + word_Data_ + word_Inicial
column_Demais_Periodo_Final = word_Demais_ + word_Periodo_ + word_Final
column_Demais_Data_Final = word_Demais_ + word_Data_ + word_Final
column_FAT_Recebera = word_FAT_ + word_Recebera
column_FAT_Referencia = word_FAT_ + word_Referencia
column_FAT_Periodo_Inicial = word_FAT_ + word_Periodo_ + word_Inicial
column_FAT_Data_Inicial = word_FAT_ + word_Data_ + word_Inicial
column_FAT_Periodo_Final = word_FAT_ + word_Periodo_ + word_Final
column_FAT_Data_Final = word_FAT_ + word_Data_ + word_Final
column_PK_Vend_ATA_Entrega = word_PK_ + word_Vend_ + word_ATA_ + word_Entrega
column_Nome_Vendedor = column_Nome + word__Vendedor
column_Cargo_Vendedor = column_Cargo + word__Vendedor
column_Nome_Supervisor = column_Nome + word__Supervisor
column_Cargo_Supervisor = column_Cargo + word__Supervisor
column_Administradora_Supervisor = column_Administradora + word__Supervisor
column_Tabela_Supervisor = column_Tabela + word__Supervisor
column_Periodo_Valor_Qtd_Vendas_Supervisor = column_Periodo_Valor_Qtd_Vendas + word__Supervisor
column_Periodo_Valor_Qtd_Vendas_Gerencia = column_Periodo_Valor_Qtd_Vendas + word__Gerencia
column_Cargo_Gerencia = column_Cargo + word__Gerencia
# COLUNAS EDITADAS N OPROGRAMA
column_Escala_ATAMes_EntregaCad_Adm = ''
# LISTAS
listValue = []
list_list_columns_venc = []
list_list_columns_situacao_num_ATA = []
list_list_columns_ATA_Venc_n_Parc_n_ATA_Atrasada = []
list_list_columns_comissao_atrasada = []
list_list_columns_num_ATA_atrasado = []
list_list_columns_percentage = []
list_list_order_columns_total = []
list_columns_full = []
list_one_two = []
list_name_change = []
list_one_two_three = []
list_administradora_limit = []
list_cargo_limit = []
list_cargos_limit_exist = []
list_administradoras_limit_exist = []
list_tabela_recebiemnto_limit_exist = []
list_columns_ATASma_Pag_n_Parc = []
list_columns_ATASma_Venc_n_Parc = []
list_name_columns_Pagar_Comissao_N_Parc = []
list_ata_sum_comissao_credito = []
list_unique_information = []
list_columns_ATASma_EntregaCad_AdmVenc_n_Parc = []
list_tables_venc = []
list_table_edit_all = []
list_table_edit_atrasada = []
list_line_delete = []
list_keys = []
list_key_single = []

list_columns_Sma_Cad_AdmPag_n_Parc = [column_Sma_Cad_Adm]
list_columns_Sma_Cad_AdmVenc_n_Parc = [column_Sma_Cad_Adm]

list_columns_ATA_Cad_AdmPag_n_Parc = [column_ATA_Cad_Adm]
list_columns_ATA_Cad_AdmVenc_n_Parc = [column_ATA_Cad_Adm]

list_columns_Sma_EntregaPag_n_Parc = [column_Sma_Entrega]
list_columns_Sma_EntregaVenc_n_Parc = [column_Sma_Entrega]

list_columns_ATA_EntregaPag_n_Parc = [column_ATA_Entrega]
list_columns_ATA_EntregaVenc_n_Parc = [column_ATA_Entrega]

list_columns_ATA_n_Parc_1_Atrasada = [column_ATA_Entrega]
list_columns_ATA_n_Parc_2_Atrasada = [column_ATA_Entrega]

list_columns_porc_ATA_Pag_n_Parc = [column_porc_ATA_Entrega]
list_columns_porc_ATA_Pag_n_Parc_1_ATA_Atrasada = [column_porc_ATA_Entrega]
list_columns_porc_ATA_Pag_n_Parc_2_ATA_Atrasada = [column_porc_ATA_Entrega]

list_columns_Situacao_n_Parc = [column_Situacao]

list_columns_Pag_Comissao_n_Parc = [column_Pag_Comissao_1_Parc]

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
list_list_order_columns = [
    [column_Situacao, column_Data_de_Entrega, column_Data_Cad_Adm,
        column_ATA_Entrega, column_ATA_Cad_Adm, column_Sma_Entrega,
        column_Sma_Cad_Adm, column_Mes_Entrega, column_Mes_Cad_Adm]
]
list_list_columns_PK_Vend_ATA_n_Parc = [
    [column_ATA_Entrega, column_PK_Vend_ATA_Entrega]
]
list_order_columns_Valor_Qtd_Vendas_Vendedor = [
    column_Escala_ATA_Entrega_Vendedor,
    column_Escala_ATA_Cad_Adm_Vendedor,
    column_Escala_Mes_Entrega_Vendedor,
    column_Escala_Mes_Cad_Adm_Vendedor
]
list_order_columns_Valor_Qtd_Vendas_Supervisor = [
    column_Escala_ATA_Entrega_Supervisor,
    column_Escala_ATA_Cad_Adm_Supervisor,
    column_Escala_Mes_Entrega_Supervisor,
    column_Escala_Mes_Cad_Adm_Supervisor
]
list_order_columns_Valor_Qtd_Vendas_Gerencia = [
    column_Escala_ATA_Entrega_Gerencia,
    column_Escala_ATA_Cad_Adm_Gerencia,
    column_Escala_Mes_Entrega_Gerencia,
    column_Escala_Mes_Cad_Adm_Gerencia
]
list_order_columns_start = [
    column_PK_Vend_ATA_Entrega,
    column_Cliente,
    column_Administradora,
    column_Vendedor,
    column_Supervisor,
    column_Cargo,
    column_Cargo_Vendedor,
    column_Cargo_Supervisor,
    column_Cargo_Gerencia,
    column_Grupo,
    column_Cota,
    column_N_Contrato,
    column_Credito,
    column_Valor_Parc_Inicial,
    column_Data_Pag_1_Parc,
    column_Data_de_Entrega,
    column_Data_Cad_Adm,
    column_Dia_Pag,
    column_Qtd_Valor_Vendedor,
    column_Data_Pag_Por,
    column_1_Parcela_Recebera,
    column_Demais_Recebera,
    column_FAT_Recebera,
    column_1_Parcela_Referencia,
    column_Demais_Referencia,
    column_FAT_Referencia,
    column_ATA_Cad_Adm,
    column_ATA_Entrega,
    column_Total_ATA_Entrega_Vendedor,
    column_Qtd_Vendas_ATA_Entrega_Vendedor,
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
    column_Dia_Semana,
    column_Mes_ano
]
list_columns_end_pdf = [
    column_Parc,
    column_Situacoes,
    column_Administradora,
    column_N_Contrato,
    column_Data_de_Entrega,
    column_Cliente,
    column_Credito,
    column_porc,
    column_Comissao,
    column_Adimplencia
]
list_columns_Escala_ATA_Entrega = [
    column_Escala_ATA_Entrega_Vendedor,
    column_Escala_ATA_Entrega_Supervisor,
    column_Escala_ATA_Entrega_Gerencia
]
list_columns_Escala_ATA_Cad_Adm = [
    column_Escala_ATA_Cad_Adm_Vendedor,
    column_Escala_ATA_Cad_Adm_Supervisor,
    column_Escala_ATA_Cad_Adm_Gerencia
]
list_columns_Escala_Mes_Entrega = [
    column_Escala_Mes_Entrega_Vendedor,
    column_Escala_Mes_Entrega_Supervisor,
    column_Escala_Mes_Entrega_Gerencia
]
list_columns_Escala_Mes_Cad_Adm = [
    column_Escala_Mes_Cad_Adm_Vendedor,
    column_Escala_Mes_Cad_Adm_Supervisor,
    column_Escala_Mes_Cad_Adm_Gerencia
]

list_columns_ATA_EntregaCad_Adm = [column_ATA_Entrega, column_ATA_Cad_Adm]
list_columns_Sma_EntregaCad_Adm = [column_Sma_Entrega, column_Sma_Cad_Adm]


list_words_ATA_Venc_º_Parc = [word_ATA_ + word_Venc_, word_º_Parc]
list_situacao_to_comission = [word_NORMAL, word_PAGA]
list_recebera_to_comission = [word_SIM]
list_cargo_not_calc_commis = [word_ESTAGIARIO, word_ZERADO]

disc_temp = {}
disc_all = {}
disc_atrasado = {}


dict_duplicate_sum = {}
dict_duplicate_total = {}
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


arqTableCadastroConsorciado = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Cadastro_Consorciado.csv')  
arqTableCadastroFuncionario = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Cadastro_Funcionario.csv')  
arqTableCadastroAta = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Cadastro_Ata.csv')  
arqTableComissoesConfiguracao = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Comissoes_Configuracao.csv')  
arqTableComissoesConfigPag = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Comissoes_ConfigPagamento.csv')  
# arqTableComissoesConfigPagTratada = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Comissoes_ConfigPagTratada.csv')  
arqTesteDuplTableComissoesConfigPag = path_file.path_file_create_user(word_Appdata, word_tables, 'Teste_Dupl_table_Comissoes_ConfigPagamento.csv')  
arqTableGerencia = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Gerencia.csv')  
arqTableComissoesConfigPagSupervisor = path_file.path_file_create_user(word_Appdata, word_tables, 'table_Comissoes_ConfigPagamento_supervisor.csv')  
arqTableMerge = path_file.path_file_create_user(word_Appdata, word_tables, 'tableMerge.csv')  
arqTableMergeOrder = path_file.path_file_create_user(word_Appdata, word_tables, 'tableMergeOrder.csv')  
arqTableDatasSemanais = path_file.path_file_create_user(word_Appdata, word_tables, 'table_datas_semanais.csv')  
arqTableDatasSemanaisInicial = path_file.path_file_create_user(word_Appdata, word_tables, 'table_datas_semanaisInicial.csv')  
arqTableTeste1 = path_file.path_file_create_user(word_Appdata, word_tables, 'table_teste1.csv')  
arqTableTeste2 = path_file.path_file_create_user(word_Appdata, word_tables, 'table_teste2.csv')  
arqTableTeste3 = path_file.path_file_create_user(word_Appdata, word_tables, 'table_teste3.csv')  
pathDonwload = os.environ['USERPROFILE'] + '\\Downloads'
arqDonwloadSales = pathDonwload + '\\consorciados.csv'
arqDonwloadFunction = pathDonwload + '\\funcionarios.csv'

arq_log = path_file.path_file_create_user(word_Appdata, word_log, 'log.txt')  

img_select = 'img/select.jpg'


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
        date_table_Cadastro_Consorciado = datetime.fromtimestamp(os.path.getmtime(arqTableCadastroConsorciado)).strftime('%c')  
        text_te += f'Cadastro de consorciado: {date_table_Cadastro_Consorciado} \n'
        date_table_Cadastro_Funcionario = datetime.fromtimestamp(os.path.getmtime(arqTableCadastroFuncionario)).strftime('%c')  
        text_te += f'Cadastro de funcionario: {date_table_Cadastro_Funcionario} \n'
        date_table_Cadastro_Ata = datetime.fromtimestamp(os.path.getmtime(arqTableCadastroAta)).strftime('%c')  
        text_te += f'Cadastro de ATAs: {date_table_Cadastro_Ata} \n'
        date_table_Comissoes_Configuracao = datetime.fromtimestamp(os.path.getmtime(arqTableComissoesConfiguracao)).strftime('%c')  
        text_te += f'Comissões configuração: {date_table_Comissoes_Configuracao} \n'
        date_table_Comissoes_ConfigPagamento = datetime.fromtimestamp(os.path.getmtime(arqTableComissoesConfigPag)).strftime('%c')  
        text_te += f'Comissões configuração de pagamento: {date_table_Comissoes_ConfigPagamento} \n'
        return (text_te)
