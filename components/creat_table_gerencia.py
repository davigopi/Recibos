# flake8: noqa
# pyright: # type: ignore
import pandas as pd
from components.variables import *


def add_valor_list(list, repeat):
    for i in range(repeat):
        value = list[0]
        list.append(value)
    return list


def replace_semicolon(value):
    if isinstance(value, (int, float)):
        return str(value).replace('.', ',')
    return value


class Creat_table_gerencia:
    def __init__(self, *args, **kwargs) -> None:
        self.table: pd.DataFrame = pd.DataFrame()
        # self.table_salve: pd.DataFrame = pd.DataFrame()

        # self.column_Administradora = ''
        # self.column_Cargo = ''
        # self.word_Supervisor = ''
        # # self.word_Geral = "Geral"
        # # self.word_Gerencia =  self.word_Supervisor + ' ' + self.word_Geral
        # self.word_Gerencia = ''
        # self.word__Periodo_Valor_Qtd_Vendas = ''
        # self.word__Valor_Qtd_Vendas_Inicial = ''
        # self.word__Valor_Qtd_Vendas_Final = ''
        # self.word__Data_Inicial = ''
        # self.word__Data_Final = ''
        # self.word__Parc_ = ''

        self.column_Administradora = column_Administradora
        self.column_Cargo = column_Cargo
        self.word_Supervisor = word_Supervisor
        self.word_Gerencia = word_Gerencia
        self.word__Periodo_Valor_Qtd_Vendas = word__Periodo_Valor_Qtd_Vendas
        self.word__Valor_Qtd_Vendas_Inicial = word__Valor_Qtd_Vendas_Inicial
        self.word__Valor_Qtd_Vendas_Final = word__Valor_Qtd_Vendas_Final
        self.word__Data_Inicial = word__Data_Inicial
        self.word__Data_Final = word__Data_Final
        self.word__Parc_ = word__Parc_

    def start_creat(self):
        list_cargo_supervisor = [
            'GERENTE EQUIPE INTERNA',
            'SUPERVISOR CLT - INSIDE SALES',
            'SUPERVISOR EQUIPE CLT - JUNIOR A PARTIR DE 19/06/2018 ',
            'SUPERVISOR EQUIPE CLT - PLENO ATE DEZ 2017'
        ]
        # key = 0
        rep = 6
        for cargo_gerente in list_cargo_supervisor:
            list_administrador = [
                'DISAL',
                'RENAULT / NISSAN',
                'VOLKSWAGEN',
                'EMBRACON IMOVEL',
                'VOLKS TABELA ACESSO',
                'EMBRACO IMOVEIS (TAB. DIFERENCIADA)',
                'VOLKS PESADOS (TAB. DIFERENCIADA)']
            list_cargo_supervisor = add_valor_list([cargo_gerente], rep)
            list_cargo_gerencia = add_valor_list(['GERENTE GERAL'], rep)
            list_periodo_valor_qtd_vendas_gerencia_1 = add_valor_list(
                ['Período Venda: 01/01/2000 à 31/03/2034 - Valor Vendas: 0,00 à 1.999.999,99'], rep)
            list_periodo_valor_qtd_vendas_gerencia_2 = add_valor_list(
                ['Período Venda: 01/01/2000 à 31/03/2034 - Valor Vendas: 2.000.000,00 à 4.999.999,99'], rep)
            list_periodo_valor_qtd_vendas_gerencia_3 = add_valor_list(
                ['Período Venda: 01/01/2000 à 30/04/2034 - Valor Vendas: 5.000.000,00 à 6.999.999,99'], rep)
            list_periodo_valor_qtd_vendas_gerencia_4 = add_valor_list(
                ['Período Venda: 01/01/2000 à 30/04/2034 - Valor Vendas: 7.000.000,00 à 9.999.999,99'], rep)
            list_periodo_valor_qtd_vendas_gerencia_5 = add_valor_list(
                ['Período Venda: 01/01/2000 à 30/04/2034 - Valor Vendas: 10.000.000,00 à 99.999.999,99'], rep)
            qtd_cotas_inicial_gerencia_1 = add_valor_list([0], rep)
            qtd_cotas_inicial_gerencia_2 = add_valor_list([2000000], rep)
            qtd_cotas_inicial_gerencia_3 = add_valor_list([5000000], rep)
            qtd_cotas_inicial_gerencia_4 = add_valor_list([7000000], rep)
            qtd_cotas_inicial_gerencia_5 = add_valor_list([10000000], rep)
            qtd_cotas_final_gerencia_1 = add_valor_list([1999999.99], rep)
            qtd_cotas_final_gerencia_2 = add_valor_list([4999999.99], rep)
            qtd_cotas_final_gerencia_3 = add_valor_list([6999999.99], rep)
            qtd_cotas_final_gerencia_4 = add_valor_list([9999999.99], rep)
            qtd_cotas_final_gerencia_5 = add_valor_list([999999999.99], rep)
            data_inicial_gerente = add_valor_list(['01/01/2000'], rep)
            data_final_gerente = add_valor_list(['31/03/2034'], rep)
            # ['DISAL', 'RENAULT', 'VOLKS', 'EMBRACON IMOVEL', 'VOLKS', EMBRACO IMOVEIS E VOLKS (DIFERENCIADA)']  # NOQA
            parc_gerencia_1 = ['', '', '', '', '', 0.015, 0.015]
            parc_gerencia_2 = ['', '', '', '', 0.05, 0.015, 0.015]
            parc_gerencia_3 = [0.05, 0.05, 0.05, '', '', 0.015, 0.015]
            parc_gerencia_4 = [0.05, 0.05, 0.05, 0.05, 0.05, 0.015, 0.015]
            parc_gerencia_5 = [0.07, 0.07, 0.07, 0.07, 0.05, 0.015, 0.015]
            parc_gerencia_6 = [0.09, 0.09, 0.09, 0.09, 0.05, 0.015, 0.015]
            parc_gerencia_7 = [0.1, 0.1, 0.1, 0.1, 0.05, 0.015, 0.015]

            table_gerencia = {
                self.column_Administradora: list_administrador,
                self.column_Cargo + " " + self.word_Supervisor: list_cargo_supervisor,
                self.column_Cargo + " " + self.word_Gerencia: list_cargo_gerencia,

                "1" + self.word__Periodo_Valor_Qtd_Vendas + " " + self.word_Gerencia: list_periodo_valor_qtd_vendas_gerencia_1,
                "1" + self.word__Valor_Qtd_Vendas_Inicial + " " + self.word_Gerencia: qtd_cotas_inicial_gerencia_1,
                "1" + self.word__Valor_Qtd_Vendas_Final + " " + self.word_Gerencia: qtd_cotas_final_gerencia_1,
                "1" + self.word__Data_Inicial + " " + self.word_Gerencia: data_inicial_gerente,
                "1" + self.word__Data_Final + " " + self.word_Gerencia: data_final_gerente,
                "1" + self.word__Parc_ + "1 " + self.word_Gerencia: parc_gerencia_2,
                "1" + self.word__Parc_ + "2 " + self.word_Gerencia: parc_gerencia_2,
                "1" + self.word__Parc_ + "3 " + self.word_Gerencia: parc_gerencia_3,
                "1" + self.word__Parc_ + "4 " + self.word_Gerencia: parc_gerencia_1,
                "1" + self.word__Parc_ + "5 " + self.word_Gerencia: parc_gerencia_2,
                "1" + self.word__Parc_ + "6 " + self.word_Gerencia: parc_gerencia_1,
                "1" + self.word__Parc_ + "7 " + self.word_Gerencia: parc_gerencia_1,
                "1" + self.word__Parc_ + "8 " + self.word_Gerencia: parc_gerencia_1,
                "1" + self.word__Parc_ + "9 " + self.word_Gerencia: parc_gerencia_1,
                "1" + self.word__Parc_ + "10 " + self.word_Gerencia: parc_gerencia_1,

                "2" + self.word__Periodo_Valor_Qtd_Vendas + " " + self.word_Gerencia: list_periodo_valor_qtd_vendas_gerencia_2,
                "2" + self.word__Valor_Qtd_Vendas_Inicial + " " + self.word_Gerencia: qtd_cotas_inicial_gerencia_2,
                "2" + self.word__Valor_Qtd_Vendas_Final + " " + self.word_Gerencia: qtd_cotas_final_gerencia_2,
                "2" + self.word__Data_Inicial + " " + self.word_Gerencia: data_inicial_gerente,
                "2" + self.word__Data_Final + " " + self.word_Gerencia: data_final_gerente,
                "2" + self.word__Parc_ + "1 " + self.word_Gerencia: parc_gerencia_4,
                "2" + self.word__Parc_ + "2 " + self.word_Gerencia: parc_gerencia_2,
                "2" + self.word__Parc_ + "3 " + self.word_Gerencia: parc_gerencia_3,
                "2" + self.word__Parc_ + "4 " + self.word_Gerencia: parc_gerencia_1,
                "2" + self.word__Parc_ + "5 " + self.word_Gerencia: parc_gerencia_2,
                "2" + self.word__Parc_ + "6 " + self.word_Gerencia: parc_gerencia_1,
                "2" + self.word__Parc_ + "7 " + self.word_Gerencia: parc_gerencia_1,
                "2" + self.word__Parc_ + "8 " + self.word_Gerencia: parc_gerencia_1,
                "2" + self.word__Parc_ + "9 " + self.word_Gerencia: parc_gerencia_1,
                "2" + self.word__Parc_ + "10 " + self.word_Gerencia: parc_gerencia_1,

                "3" + self.word__Periodo_Valor_Qtd_Vendas + " " + self.word_Gerencia: list_periodo_valor_qtd_vendas_gerencia_3,
                "3" + self.word__Valor_Qtd_Vendas_Inicial + " " + self.word_Gerencia: qtd_cotas_inicial_gerencia_3,
                "3" + self.word__Valor_Qtd_Vendas_Final + " " + self.word_Gerencia: qtd_cotas_final_gerencia_3,
                "3" + self.word__Data_Inicial + " " + self.word_Gerencia: data_inicial_gerente,
                "3" + self.word__Data_Final + " " + self.word_Gerencia: data_final_gerente,
                "3" + self.word__Parc_ + "1 " + self.word_Gerencia: parc_gerencia_5,
                "3" + self.word__Parc_ + "2 " + self.word_Gerencia: parc_gerencia_2,
                "3" + self.word__Parc_ + "3 " + self.word_Gerencia: parc_gerencia_3,
                "3" + self.word__Parc_ + "4 " + self.word_Gerencia: parc_gerencia_1,
                "3" + self.word__Parc_ + "5 " + self.word_Gerencia: parc_gerencia_2,
                "3" + self.word__Parc_ + "6 " + self.word_Gerencia: parc_gerencia_1,
                "3" + self.word__Parc_ + "7 " + self.word_Gerencia: parc_gerencia_1,
                "3" + self.word__Parc_ + "8 " + self.word_Gerencia: parc_gerencia_1,
                "3" + self.word__Parc_ + "9 " + self.word_Gerencia: parc_gerencia_1,
                "3" + self.word__Parc_ + "10 " + self.word_Gerencia: parc_gerencia_1,

                "4" + self.word__Periodo_Valor_Qtd_Vendas + " " + self.word_Gerencia: list_periodo_valor_qtd_vendas_gerencia_4,
                "4" + self.word__Valor_Qtd_Vendas_Inicial + " " + self.word_Gerencia: qtd_cotas_inicial_gerencia_4,
                "4" + self.word__Valor_Qtd_Vendas_Final + " " + self.word_Gerencia: qtd_cotas_final_gerencia_4,
                "4" + self.word__Data_Inicial + " " + self.word_Gerencia: data_inicial_gerente,
                "4" + self.word__Data_Final + " " + self.word_Gerencia: data_final_gerente,
                "4" + self.word__Parc_ + "1 " + self.word_Gerencia: parc_gerencia_6,
                "4" + self.word__Parc_ + "2 " + self.word_Gerencia: parc_gerencia_2,
                "4" + self.word__Parc_ + "3 " + self.word_Gerencia: parc_gerencia_3,
                "4" + self.word__Parc_ + "4 " + self.word_Gerencia: parc_gerencia_1,
                "4" + self.word__Parc_ + "5 " + self.word_Gerencia: parc_gerencia_2,
                "4" + self.word__Parc_ + "6 " + self.word_Gerencia: parc_gerencia_1,
                "4" + self.word__Parc_ + "7 " + self.word_Gerencia: parc_gerencia_1,
                "4" + self.word__Parc_ + "8 " + self.word_Gerencia: parc_gerencia_1,
                "4" + self.word__Parc_ + "9 " + self.word_Gerencia: parc_gerencia_1,
                "4" + self.word__Parc_ + "10 " + self.word_Gerencia: parc_gerencia_1,

                "5" + self.word__Periodo_Valor_Qtd_Vendas + " " + self.word_Gerencia: list_periodo_valor_qtd_vendas_gerencia_5,
                "5" + self.word__Valor_Qtd_Vendas_Inicial + " " + self.word_Gerencia: qtd_cotas_inicial_gerencia_5,
                "5" + self.word__Valor_Qtd_Vendas_Final + " " + self.word_Gerencia: qtd_cotas_final_gerencia_5,
                "5" + self.word__Data_Inicial + " " + self.word_Gerencia: data_inicial_gerente,
                "5" + self.word__Data_Final + " " + self.word_Gerencia: data_final_gerente,
                "5" + self.word__Parc_ + "1 " + self.word_Gerencia: parc_gerencia_7,
                "5" + self.word__Parc_ + "2 " + self.word_Gerencia: parc_gerencia_2,
                "5" + self.word__Parc_ + "3 " + self.word_Gerencia: parc_gerencia_3,
                "5" + self.word__Parc_ + "4 " + self.word_Gerencia: parc_gerencia_1,
                "5" + self.word__Parc_ + "5 " + self.word_Gerencia: parc_gerencia_2,
                "5" + self.word__Parc_ + "6 " + self.word_Gerencia: parc_gerencia_1,
                "5" + self.word__Parc_ + "7 " + self.word_Gerencia: parc_gerencia_1,
                "5" + self.word__Parc_ + "8 " + self.word_Gerencia: parc_gerencia_1,
                "5" + self.word__Parc_ + "9 " + self.word_Gerencia: parc_gerencia_1,
                "5" + self.word__Parc_ + "10 " + self.word_Gerencia: parc_gerencia_1,
            }
            table_g = pd.DataFrame(table_gerencia)
            if self.table.empty:
                self.table = table_g
            else:
                self.table = pd.concat([self.table, table_g], ignore_index=True)
        self.table = self.table.apply(lambda col: col.apply(replace_semicolon))


if __name__ == '__main__':
    creat_table_gerencia = Creat_table_gerencia()
    table = creat_table_gerencia.table
    print(table)
