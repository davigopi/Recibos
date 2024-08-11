import pandas as pd


def add_valor_list(list, repeat):
    for i in range(repeat):
        value = list[0]
        list.append(value)
    return list


def replace_semicolon(value):
    if isinstance(value, (int, float)):
        return str(value).replace('.', ',')
    return value


class Creat_table_gerente:
    def __init__(self, *args, **kwargs) -> None:
        self.table: pd.DataFrame = pd.DataFrame()
        list_cargo_gerente = [
            'GERENTE EQUIPE INTERNA',
            'SUPERVISOR CLT - INSIDE SALES',
            'SUPERVISOR EQUIPE CLT - JUNIOR A PARTIR DE 19/06/2018 ',
            'SUPERVISOR EQUIPE CLT - PLENO ATE DEZ 2017'
        ]
        # key = 0
        rep = 6
        for cargo_gerente in list_cargo_gerente:
            list_administrador = [
                'DISAL',
                'RENAULT / NISSAN',
                'VOLKSWAGEN',
                'EMBRACON IMOVEL',
                'VOLKS TABELA ACESSO',
                'EMBRACO IMOVEIS (TAB. DIFERENCIADA)',
                'VOLKS PESADOS (TAB. DIFERENCIADA)']
            list_cargo_gerente = add_valor_list([cargo_gerente], rep)
            list_cargo_gerente_geral = add_valor_list(['GERENTE GERAL'], rep)
            list_periodo_valor_qtd_vendas_gerente_1 = add_valor_list(
                ['Período Venda: 01/01/2000 à 31/03/2034 - Valor Vendas: 0,00 à 1.999.999,99'], rep)  # noqa
            list_periodo_valor_qtd_vendas_gerente_2 = add_valor_list(
                ['Período Venda: 01/01/2000 à 31/03/2034 - Valor Vendas: 2.000.000,00 à 4.999.999,99'], rep)  # noqa
            list_periodo_valor_qtd_vendas_gerente_3 = add_valor_list(
                ['Período Venda: 01/01/2000 à 30/04/2034 - Valor Vendas: 5.000.000,00 à 6.999.999,99'], rep)  # noqa
            list_periodo_valor_qtd_vendas_gerente_4 = add_valor_list(
                ['Período Venda: 01/01/2000 à 30/04/2034 - Valor Vendas: 7.000.000,00 à 9.999.999,99'], rep)  # noqa
            list_periodo_valor_qtd_vendas_gerente_5 = add_valor_list(
                ['Período Venda: 01/01/2000 à 30/04/2034 - Valor Vendas: 10.000.000,00 à 99.999.999,99'], rep)  # noqa
            qtd_cotas_inicial_gerente_1 = add_valor_list([0], rep)
            qtd_cotas_inicial_gerente_2 = add_valor_list([2000000], rep)
            qtd_cotas_inicial_gerente_3 = add_valor_list([5000000], rep)
            qtd_cotas_inicial_gerente_4 = add_valor_list([7000000], rep)
            qtd_cotas_inicial_gerente_5 = add_valor_list([10000000], rep)
            qtd_cotas_final_gerente_1 = add_valor_list([1999999.99], rep)
            qtd_cotas_final_gerente_2 = add_valor_list([4999999.99], rep)
            qtd_cotas_final_gerente_3 = add_valor_list([6999999.99], rep)
            qtd_cotas_final_gerente_4 = add_valor_list([9999999.99], rep)
            qtd_cotas_final_gerente_5 = add_valor_list([999999999.99], rep)
            data_inicial_gerente = add_valor_list(['01/01/2000'], rep)
            data_final_gerente = add_valor_list(['31/03/2034'], rep)
            # ['DISAL', 'RENAULT', 'VOLKS', 'EMBRACON IMOVEL', 'VOLKS', EMBRACO IMOVEIS E VOLKS (DIFERENCIADA)']  # NOQA
            parc_gerente_1 = ['', '', '', '', '', 0.015, 0.015]
            parc_gerente_2 = ['', '', '', '', 0.05, 0.015, 0.015]
            parc_gerente_3 = [0.05, 0.05, 0.05, '', '', 0.015, 0.015]
            parc_gerente_4 = [0.05, 0.05, 0.05, 0.05, 0.05, 0.015, 0.015]
            parc_gerente_5 = [0.07, 0.07, 0.07, 0.07, 0.05, 0.015, 0.015]
            parc_gerente_6 = [0.09, 0.09, 0.09, 0.09, 0.05, 0.015, 0.015]
            parc_gerente_7 = [0.1, 0.1, 0.1, 0.1, 0.05, 0.015, 0.015]

            table_gerente = {
                "Administradora": list_administrador,
                "Cargo_Gerente": list_cargo_gerente,
                "Cargo_Gerente_Geral": list_cargo_gerente_geral,

                "1 Periodo valor qtd vendas_Gerente_Geral": list_periodo_valor_qtd_vendas_gerente_1,  # noqa
                "1 Qtd. Cotas Inicial_Gerente_Geral": qtd_cotas_inicial_gerente_1,  # noqa
                "1 Qtd. Cotas Final_Gerente_Geral": qtd_cotas_final_gerente_1,
                "1 Data inicial_Gerente_Geral": data_inicial_gerente,
                "1 Data final_Gerente_Geral": data_final_gerente,
                "1 Parc 1_Gerente_Geral": parc_gerente_2,
                "1 Parc 2_Gerente_Geral": parc_gerente_2,
                "1 Parc 3_Gerente_Geral": parc_gerente_3,
                "1 Parc 4_Gerente_Geral": parc_gerente_1,
                "1 Parc 5_Gerente_Geral": parc_gerente_2,
                "1 Parc 6_Gerente_Geral": parc_gerente_1,
                "1 Parc 7_Gerente_Geral": parc_gerente_1,
                "1 Parc 8_Gerente_Geral": parc_gerente_1,
                "1 Parc 9_Gerente_Geral": parc_gerente_1,
                "1 Parc 10_Gerente_Geral": parc_gerente_1,

                "2 Periodo valor qtd vendas_Gerente_Geral": list_periodo_valor_qtd_vendas_gerente_2,  # noqa
                "2 Qtd. Cotas Inicial_Gerente_Geral": qtd_cotas_inicial_gerente_2,  # noqa
                "2 Qtd. Cotas Final_Gerente_Geral": qtd_cotas_final_gerente_2,
                "2 Data inicial_Gerente_Geral": data_inicial_gerente,
                "2 Data final_Gerente_Geral": data_final_gerente,
                "2 Parc 1_Gerente_Geral": parc_gerente_4,
                "2 Parc 2_Gerente_Geral": parc_gerente_2,
                "2 Parc 3_Gerente_Geral": parc_gerente_3,
                "2 Parc 4_Gerente_Geral": parc_gerente_1,
                "2 Parc 5_Gerente_Geral": parc_gerente_2,
                "2 Parc 6_Gerente_Geral": parc_gerente_1,
                "2 Parc 7_Gerente_Geral": parc_gerente_1,
                "2 Parc 8_Gerente_Geral": parc_gerente_1,
                "2 Parc 9_Gerente_Geral": parc_gerente_1,
                "2 Parc 10_Gerente_Geral": parc_gerente_1,

                "3 Periodo valor qtd vendas_Gerente_Geral": list_periodo_valor_qtd_vendas_gerente_3,  # noqa
                "3 Qtd. Cotas Inicial_Gerente_Geral": qtd_cotas_inicial_gerente_3,  # noqa
                "3 Qtd. Cotas Final_Gerente_Geral": qtd_cotas_final_gerente_3,
                "3 Data inicial_Gerente_Geral": data_inicial_gerente,
                "3 Data final_Gerente_Geral": data_final_gerente,
                "3 Parc 1_Gerente_Geral": parc_gerente_5,
                "3 Parc 2_Gerente_Geral": parc_gerente_2,
                "3 Parc 3_Gerente_Geral": parc_gerente_3,
                "3 Parc 4_Gerente_Geral": parc_gerente_1,
                "3 Parc 5_Gerente_Geral": parc_gerente_2,
                "3 Parc 6_Gerente_Geral": parc_gerente_1,
                "3 Parc 7_Gerente_Geral": parc_gerente_1,
                "3 Parc 8_Gerente_Geral": parc_gerente_1,
                "3 Parc 9_Gerente_Geral": parc_gerente_1,
                "3 Parc 10_Gerente_Geral": parc_gerente_1,

                "4 Periodo valor qtd vendas_Gerente_Geral": list_periodo_valor_qtd_vendas_gerente_4,  # noqa
                "4 Qtd. Cotas Inicial_Gerente_Geral": qtd_cotas_inicial_gerente_4,  # noqa
                "4 Qtd. Cotas Final_Gerente_Geral": qtd_cotas_final_gerente_4,
                "4 Data inicial_Gerente_Geral": data_inicial_gerente,
                "4 Data final_Gerente_Geral": data_final_gerente,
                "4 Parc 1_Gerente_Geral": parc_gerente_6,
                "4 Parc 2_Gerente_Geral": parc_gerente_2,
                "4 Parc 3_Gerente_Geral": parc_gerente_3,
                "4 Parc 4_Gerente_Geral": parc_gerente_1,
                "4 Parc 5_Gerente_Geral": parc_gerente_2,
                "4 Parc 6_Gerente_Geral": parc_gerente_1,
                "4 Parc 7_Gerente_Geral": parc_gerente_1,
                "4 Parc 8_Gerente_Geral": parc_gerente_1,
                "4 Parc 9_Gerente_Geral": parc_gerente_1,
                "4 Parc 10_Gerente_Geral": parc_gerente_1,

                "5 Periodo valor qtd vendas_Gerente_Geral": list_periodo_valor_qtd_vendas_gerente_5,  # noqa
                "5 Qtd. Cotas Inicial_Gerente_Geral": qtd_cotas_inicial_gerente_5,  # noqa
                "5 Qtd. Cotas Final_Gerente_Geral": qtd_cotas_final_gerente_5,
                "5 Data inicial_Gerente_Geral": data_inicial_gerente,
                "5 Data final_Gerente_Geral": data_final_gerente,
                "5 Parc 1_Gerente_Geral": parc_gerente_7,
                "5 Parc 2_Gerente_Geral": parc_gerente_2,
                "5 Parc 3_Gerente_Geral": parc_gerente_3,
                "5 Parc 4_Gerente_Geral": parc_gerente_1,
                "5 Parc 5_Gerente_Geral": parc_gerente_2,
                "5 Parc 6_Gerente_Geral": parc_gerente_1,
                "5 Parc 7_Gerente_Geral": parc_gerente_1,
                "5 Parc 8_Gerente_Geral": parc_gerente_1,
                "5 Parc 9_Gerente_Geral": parc_gerente_1,
                "5 Parc 10_Gerente_Geral": parc_gerente_1,
            }
            table_g = pd.DataFrame(table_gerente)
            if self.table.empty:
                self.table = table_g
            else:
                self.table = pd.concat([self.table, table_g], ignore_index=True)  # noqa
        self.table_salve = self.table.apply(lambda col: col.apply(replace_semicolon))  # type: ignore  # noqa


if __name__ == '__main__':
    creat_table_gerente = Creat_table_gerente()
    table = creat_table_gerente.table
    print(table)
