import pandas as pd
import math

table_full = pd.read_csv(
    "tables\\tableMerge.csv",
    sep=';',
    encoding='utf-8',
    dtype=str
)

meses = {
    'JANEIRO': 1,
    'FEVEREIRO': 2,
    'MARÇO': 3,
    'ABRIL': 4,
    'MAIO': 5,
    'JUNHO': 6,
    'JULHO': 7,
    'AGOSTO': 8,
    'SETEMBRO': 9,
    'OUTUBRO': 10,
    'NOVEMBRO': 11,
    'DEZEMBRO': 12}


name_columns = table_full.columns.tolist()
quantity_line = table_full.shape[0]
list_vendedor_diaUtil = []
list_vendedor_porAta = []
list_vendedor_diaSemana = []
list_columns_ata = ['ATA Entrega', 'ATA Cad Adm', 'ATA 2º Parc', 'ATA 3º Parc',
                    'ATA 4º Parc', 'ATA 5º Parc', 'ATA 6º Parc']
list_ata = []

for key in range(quantity_line):
    vendedor = table_full.iloc[key]['Vendedor']
    dt_pag_por = table_full.iloc[key]['Dt pag. por']
    list_dt_pag_por = ['DIA ÚTIL', 'POR ATA', 'DIA DA SEMANA']
    if dt_pag_por == list_dt_pag_por[0]:
        if vendedor not in list_vendedor_diaUtil:
            list_vendedor_diaUtil.append(vendedor)
    elif dt_pag_por == list_dt_pag_por[1]:
        if vendedor not in list_vendedor_porAta:
            list_vendedor_porAta.append(vendedor)
    elif dt_pag_por == list_dt_pag_por[2]:
        if vendedor not in list_vendedor_diaSemana:
            list_vendedor_diaSemana.append(vendedor)
    for column_ata in list_columns_ata:
        ata = table_full.iloc[key][column_ata]
        if ata not in list_ata and not pd.isna(ata):
            list_ata.append(ata)

list_vendedor_diaUtil.sort()
list_vendedor_porAta.sort()
list_vendedor_diaSemana.sort()
list_ata = sorted(list_ata,
                  key=lambda x: (x.split('/')[1], meses[x.split('/')[0]])
                  )


print(list_vendedor_diaUtil)
print(list_vendedor_porAta)
print(list_vendedor_diaSemana)
print(list_ata)


# self.table.loc[key_1, column] = self.table_2.iloc[key_2][column]
