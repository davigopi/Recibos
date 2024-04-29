import pandas as pd
from pathlib import Path
# import math


column_vendedor = 'Vendedor'
column_administradora = 'Administradora'
column_dt_pag_por = 'Dt pag. por'
column_1p_referencia = '1P referencia'
column_credito = 'Crédito'
data_ata_single = 'MARÇO/2024'
seller_single = 'MARIA ILLYEDJA RODRIGUES DE SOUZA '
# seller = 'BRUNA ALINE DE AZEVEDO (ENIO)'
type_data_date_pay = 'DIA DA SEMANA'
cadastro = 'CADASTRO'
list_columns_full_ata = [
    'ATA Entrega', 'ATA Cad Adm', 'ATA 2º Parc', 'ATA 3º Parc',
    'ATA 4º Parc', 'ATA 5º Parc', 'ATA 6º Parc'
]
list_columns_full_semanas = [
    'Sem Ent', 'Sem Cad Adm', 'Sem 2º Parc', 'Sem 3º Parc',
    'Sem 4º Parc', 'Sem 5º Parc', 'Sem 6º Parc'
]
list_columns_full_ata_entrega = [
    item for item in list_columns_full_ata if item != 'ATA Cad Adm'
]
list_columns_full_ata_cadastro = [
    item for item in list_columns_full_ata if item != 'ATA Entrega'
]

list_columns_str_to_float = [
    column_credito,
    '1 Qtd. Cotas Inicial', '1 Qtd. Cotas Final',
    '2 Qtd. Cotas Inicial', '2 Qtd. Cotas Final',
    '3 Qtd. Cotas Inicial', '3 Qtd. Cotas Final',
    '4 Qtd. Cotas Inicial', '4 Qtd. Cotas Final',
    '5 Qtd. Cotas Inicial', '5 Qtd. Cotas Final',
]

months = {
    'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4, 'MAIO': 5,
    'JUNHO': 6, 'JULHO': 7, 'AGOSTO': 8, 'SETEMBRO': 9, 'OUTUBRO': 10,
    'NOVEMBRO': 11, 'DEZEMBRO': 12
}


pathTables = Path(__file__).parent.parent / 'tables'
name_arq = 'table_teste.csv'
arqTableTeste = pathTables / name_arq

table_full = pd.read_csv(
    "tables\\tableMerge.csv",
    sep=';',
    encoding='utf-8',
    dtype=str
)

for column in list_columns_str_to_float:
    table_full.loc[:, column] = table_full[column].str.replace('.', '')
    table_full.loc[:, column] = table_full[column].str.replace(',', '.')
    table_full.loc[:, column] = table_full[column].astype(float)
    table_full.loc[:, column] = table_full[column].round(2)

table_full_ata = table_full[
    table_full[column_dt_pag_por] != type_data_date_pay
]
table_full_weekly = table_full[
    table_full[column_dt_pag_por] == type_data_date_pay
]


name_columns = table_full.columns.tolist()
quantity_line_ata = table_full_ata.shape[0]
quantity_line_weekly = table_full_weekly.shape[0]


list_seller_ata = []
list_ata = []
for key in range(quantity_line_ata):
    seller = table_full_ata.iloc[key][column_vendedor]
    if seller not in list_seller_ata:
        list_seller_ata.append(seller)
    for column_ata in list_columns_full_ata:
        data_ata = table_full_ata.iloc[key][column_ata]
        if data_ata not in list_ata and not pd.isna(data_ata):
            list_ata.append(data_ata)
list_seller_ata.sort()
list_ata = sorted(
    list_ata, key=lambda x: (x.split('/')[1], months[x.split('/')[0]])
)
list_seller_weekly = []
list_weekly = []
for key in range(quantity_line_weekly):
    seller = table_full_weekly.iloc[key][column_vendedor]
    if seller not in list_seller_weekly:
        list_seller_weekly.append(seller)
    for column_semana in list_columns_full_semanas:
        weekly = table_full_weekly.iloc[key][column_semana]
        if weekly not in list_weekly and not pd.isna(weekly):
            list_weekly.append(weekly)
list_seller_weekly.sort()
list_weekly = sorted(
    list_weekly, key=lambda x: (
        x.split('/')[2], months[x.split('/')[1]], x.split('/')[0]
    )
)
# print(list_seller_ata)
# print('')
# print(list_seller_weekly)
# print('')
# print(list_ata)
# print('')
# print(list_weekly)


table_seller_single = table_full[table_full[column_vendedor] == seller_single]
# print(table_seller_single)
p1_referencia = table_seller_single.iloc[1][column_1p_referencia]
if cadastro in p1_referencia:
    list_columns_full_ata_single = list_columns_full_ata_cadastro
else:
    list_columns_full_ata_single = list_columns_full_ata_entrega


# salva as tabelas que as colunas sejao igual a ATA
table_single_ata = []
for column in list_columns_full_ata_single:
    table = table_seller_single[table_seller_single[column] == data_ata_single]
    sum_credito = table[column_credito].sum()
    list_single_administradora = table[column_administradora].unique()
    print(list_single_administradora)
    quantity_line_table = table.shape[0]
    for key in range(quantity_line_table):
        data_administradora = table.iloc[key][column_administradora]
        # if data_administradora in list_single_administradora:
        #     list_single_administradora.remove(data_administradora)

    table_single_ata.append([column, sum_credito, table])


# print(table_full)
# print(table_single_ata)
table_single_merge: pd.DataFrame = pd.DataFrame()
start = False
for column, sum_credito, table in table_single_ata:

    if not table.empty:
        # print(column)
        # print(sum_credito)
        # print(table)
        # if start is False:
        #     table_single_merge = table
        #     start = True
        # else:
        table_single_merge = pd.concat([table_single_merge, table])
# salvar a tabela
# print(table_single_merge)
table_single_merge.to_csv(
    arqTableTeste,
    index=False,
    header=True,
    sep=';'
)


# self.table.loc[key_1, column] = self.table_2.iloc[key_2][column]
