# "ferramenta de captura"  do windows para pegar imagens
# from ast import Break
# from asyncio.windows_events import NULL
# from cgitb import text
# from contextlib import nullcontext
# from mailbox import NotEmptyError
# from contextlib import contextmanager
# from msilib.text import tables
# import re
# import sys
# from msilib.schema import Property
# import ssl
# from time import sleep
# from types import NoneType
# from numpy import NaN
# import pyautogui
import pandas as pd
from typing import List, Union
# from pandas.errors import EmptyDataError
# import os
# import random
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.common.exceptions import (
#     NoSuchElementException,
#     ElementNotInteractableException,
#     ElementClickInterceptedException
# )
# from selenium.common.exceptions import (
#     StaleElementReferenceException,
#     InvalidArgumentException,
#     InvalidSelectorException,
#     TimeoutException
# )
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from components.returnValue import ReturnValue
from components.renemaText import RenameText
from components.dateMonthYear import DateMonthYear
from components.mouseKeyboard import MouseKeyboard
from components.tableManip import TableManip
from components.table_from_tags import Table_from_tags
from components.buttonsSpecial import ButtonsSpecial
from components.fileManip import FileManip
# from xpathManip import XpathManip
# from imageManip import ImageManip

# excecaoAll = (
#     NoSuchElementException,
#     ElementNotInteractableException,
#     ElementClickInterceptedException,
#     StaleElementReferenceException,
#     InvalidArgumentException,
#     InvalidSelectorException,
#     TimeoutException
# )


class Connect:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.df: Union[pd.DataFrame, bool] = pd.DataFrame()
        self.dfNew: Union[pd.DataFrame, bool] = pd.DataFrame()
        self.listValue = []
        self.table: pd.DataFrame = pd.DataFrame()
        self.clickOk = None
        self.xpathOk = None
        self.user = None
        self.password = None
        self.tagSon = None
        self.tagFather = None
        self.tagGet = None
        self.tagSelected = None
        self.file = None
        self.month = 0
        self.valueAdministradora = None
        self.valueCargo = None
        self.mouseKeyboard = MouseKeyboard(driver=self.driver)
        self.returnValue = ReturnValue(driver=self.driver)
        self.dateMonthYear = DateMonthYear()
        self.table_from_tags = Table_from_tags()
        self.tableManip = TableManip()
        self.listExistCargos = None
        self.listExistAdministradoras: list = []
        self.listExistTabelarecebimento = None

    @property
    def users(self):
        return None

    @users.setter
    def users(self, user):
        self.user = user

    @property
    def passwords(self):
        return None

    @passwords.setter
    def passwords(self, password):
        self.password = password

    @property
    def tagSons(self):
        return None

    @tagSons.setter
    def tagSons(self, tagSon):
        self.tagSon = tagSon

    @property
    def tagFathers(self):
        return None

    @tagFathers.setter
    def tagFathers(self, tagFather):
        self.tagFather = tagFather

    @property
    def tagGets(self):
        return None

    @tagGets.setter
    def tagGets(self, tagGet):
        self.tagGet = tagGet

    @property
    def tagSelecteds(self):
        return None

    @tagSelecteds.setter
    def tagSelecteds(self, tagSelected):
        self.tagSelected = tagSelected

    @property
    def listValues(self):
        return None

    @listValues.setter
    def listValues(self, listValue):
        self.listValue = listValue

    @property
    def files(self):
        return None

    @files.setter
    def files(self, file):
        self.file = file

    @property
    def months(self):
        return None

    @months.setter
    def months(self, month):
        self.month = month

    @property
    def tables(self):
        return None

    @tables.setter
    def tables(self, table):
        self.table = table

    @property
    def valueChooseAdministradoras(self):
        return None

    @valueChooseAdministradoras.setter
    def valueChooseAdministradoras(self, valueAdministradora):
        self.valueAdministradora = valueAdministradora

    @property
    def valueChooseCargos(self):
        return None

    @valueChooseCargos.setter
    def valueChooseCargos(self, valueCargo):
        self.valueCargo = valueCargo

    @property
    def tagReturnValue(self):
        self.returnValue.tagSons = self.tagSon
        self.returnValue.tagFathers = self.tagFather
        self.returnValue.tagGets = self.tagGet
        self.returnValue.tagSelecteds = self.tagSelected

    @property
    def valueExistAdministradoras(self):
        return None

    @valueExistAdministradoras.setter
    def valueExistAdministradoras(self, table_Cadastro_Consorciado):
        nLine = table_Cadastro_Consorciado[
            table_Cadastro_Consorciado.columns[0]].count()
        listFullAdministradora = []
        for i in range(nLine):
            listFullAdministradora.append(
                table_Cadastro_Consorciado.at[i, 'Administradora'])
        self.listExistAdministradoras = list(set(listFullAdministradora))
        self.listExistAdministradoras.sort()

    @property
    def valueExistCargos(self):
        return None

    @valueExistCargos.setter
    def valueExistCargos(self, table_Cadastro_Funcionario):
        nLine = table_Cadastro_Funcionario[
            table_Cadastro_Funcionario.columns[0]].count()
        listFullCargos = []
        for i in range(nLine):
            listFullCargos.append(table_Cadastro_Funcionario.at[i, 'Cargo'])
        self.listExistCargos = list(set(listFullCargos))
        self.listExistCargos.sort()

    @property
    def valueExistTabelarecebimento(self):
        return None

    @valueExistTabelarecebimento.setter
    def valueExistTabelarecebimento(self, valueChooseTabelarecebimento):
        self.listExistTabelarecebimento = valueChooseTabelarecebimento

    ''' ###########  logar  ###############'''
    @property
    def logarSircon(self):
        return None

    @logarSircon.setter
    def logarSircon(self, listXpath):
        for xpath in listXpath:
            indexNumber = listXpath.index(xpath)
            if indexNumber == 0:
                self.mouseKeyboard.writeSecs = self.user
                while True:
                    self.mouseKeyboard.keys = xpath
                    self.clickOk = self.mouseKeyboard.keys
                    if self.clickOk is True:
                        break
            elif indexNumber == 1:
                self.mouseKeyboard.writeSecs = self.password
                while True:
                    self.mouseKeyboard.keys = xpath
                    self.clickOk = self.mouseKeyboard.keys
                    if self.clickOk is True:
                        break
            else:
                while True:
                    self.mouseKeyboard.clickXpath = xpath
                    self.clickOk = self.mouseKeyboard.clickXpath
                    if self.clickOk is True:
                        break

    @property
    def sales(self):
        return self.dfNew

    @sales.setter
    def sales(self, listXpath):
        file = FileManip()
        file.arqConss = self.file
        for lastMonth in range(self.month, -1, -1):
            file.delete
            fileNotExist = True
            for key, xpath in enumerate(listXpath):
                func = self.mouseKeyboard
                butt = ButtonsSpecial(
                    lastMonth=lastMonth,
                    func=func,
                    xpath=xpath
                )
                clickOk = False
                while clickOk is False:
                    if key == 3 or key == 7:   # botao seta para esquerda
                        clickOk = butt.clickLeftArrow
                    elif key == 4:  # linha coluna calendario inicio
                        clickOk = butt.clickDayStartMonth
                    elif key == 8:  # linha coluna calendario fim
                        clickOk = butt.clickDayEndMonth
                    else:
                        self.mouseKeyboard.clickXpath = xpath
                        clickOk = self.mouseKeyboard.clickXpath
                    if key == 11:  # botao de download
                        self.df = file.readCsv
                    if self.df is False:  # Repetir se download nao exis
                        clickOk = False
            if fileNotExist is True:
                tableManip = TableManip()
                tableManip.df = self.df
                tableManip.dfNew = self.dfNew
                self.dfNew = tableManip.merge
        file.delete
        file.writeCsv = self.dfNew

    @property
    def function(self):
        return self.dfNew

    @function.setter
    def function(self, listXpath):
        file = FileManip()
        file.arqConss = self.file
        file.delete
        # fileNotExist = True
        for key, xpath in enumerate(listXpath):
            clickOk = False
            while clickOk is False:
                self.mouseKeyboard.clickXpath = xpath
                clickOk = self.mouseKeyboard.clickXpath
                if key == 3:  # botao de download
                    self.df = file.readCsv
                if self.df is False:  # tem que repetir se download nao exis
                    clickOk = False
        self.dfNew = self.df

    @property
    def minutes(self):
        return self.table

    @minutes.setter
    def minutes(self, listXpath):
        # returnValue = ReturnValue()
        self.dateMonthYear.listMonthYear = self.month
        listMonthYear: List = self.dateMonthYear.listMonthYear  # type: ignore
        for key, xpath in enumerate(listXpath):
            clickOk = False
            while clickOk is False:
                if key in (0, 1):
                    self.mouseKeyboard.clickXpath = xpath
                    clickOk = self.mouseKeyboard.clickXpath
                if key == 2:  # selecionar ano
                    xpathYear = xpath
                    clickOk = True
                if key == 3:
                    xpathTableMinutes = xpath
                    clickOk = True
                if key == 4:
                    tableComplete: pd.DataFrame = pd.DataFrame()
                    for administradora in self.listExistAdministradoras:
                        self.mouseKeyboard.clickXpath = xpath
                        # clickOk = self.mouseKeyboard.clickXpath
                        self.mouseKeyboard.clickValue = administradora
                        for listYear in listMonthYear[0]:
                            self.mouseKeyboard.clickXpath = xpathYear
                            clickOk = self.mouseKeyboard.clickXpath
                            self.mouseKeyboard.clickValue = listYear
                            self.returnValue.xpath_to_tags = xpathTableMinutes
                            html = self.returnValue.xpath_to_tags
                            if html is not False:
                                self.table_from_tags.tables = html
                                table = self.table_from_tags.tables
                                self.tableManip.renemar_data = table
                                self.tableManip.del_column = 'Ações'
                                self.tableManip.column_clone = 'Período'
                                self.tableManip.add_column_clone = 'Período final'
                                self.tableManip.rename_name_column_origin = 'Período'
                                self.tableManip.rename_name_column_destiny = 'Período inicial'
                                self.tableManip.value_separate = 'à'
                                self.tableManip.rename_value_column_before = 'Período inicial'
                                self.tableManip.rename_value_column_after = 'Período final'
                                self.tableManip.value_fixed_column = administradora
                                self.tableManip.add_value_fixed_column = 'Administradora'
                                self.tableManip.value_fixed_column = listYear
                                self.tableManip.add_value_fixed_column = 'Ano'
                                table: pd.DataFrame = self.tableManip.return_table
                                if tableComplete.empty:
                                    tableComplete = table
                                else:
                                    tableComplete = pd.concat([tableComplete, table])
        self.table = tableComplete

    @property
    def pressListXpath(self):
        return self.clickOk

    @pressListXpath.setter
    def pressListXpath(self, listXpath):
        for xpath in listXpath:
            while True:
                self.mouseKeyboard.clickXpath = xpath
                self.clickOk = self.mouseKeyboard.clickXpath
                if self.clickOk is True:
                    break

    '''# pegar os valores administradoras'''
    @property
    def pressXpathResultListValue(self):
        return self.listValue

    @pressXpathResultListValue.setter
    def pressXpathResultListValue(self, xpath):
        while True:
            self.mouseKeyboard.clickXpath = xpath
            self.clickOk = self.mouseKeyboard.clickXpath
            if self.clickOk is True:
                break
        self.returnValue.xpathTag = xpath
        listValue = self.returnValue.xpathTag
        listValueTemp = []
        # limitar
        for valueAdministradora in listValue:
            # limita se a pessoa colocar na lista as administradora
            if self.valueAdministradora is not None:
                if valueAdministradora not in self.valueAdministradora:
                    continue
            # limita apenas as administradoras que existe nas vendas existentes
            if self.listExistAdministradoras != []:
                if valueAdministradora not in self.listExistAdministradoras:
                    continue
            listValueTemp.append(valueAdministradora)
        self.listValue = listValueTemp

     # com valores da administradoras ira acrecentar valor tabela de recebimento
    @property
    def pressListValueXpathResultListValue(self):
        return self.listValue

    @pressListValueXpathResultListValue.setter
    def pressListValueXpathResultListValue(self, xpath):
        listValueAdministradoraTablarecebimento = []
        for valueAdministradora in self.listValue:
            self.mouseKeyboard.locationSearchTag = self.tagSon
            self.mouseKeyboard.clickValue = valueAdministradora
            while True:
                self.mouseKeyboard.clickXpath = xpath
                self.clickOk = self.mouseKeyboard.clickXpath
                if self.clickOk is True:
                    break
            self.returnValue.xpathTag = xpath
            listValueTabelarecebimento = self.returnValue.xpathTag
            listValueTemp = []
            # limitar
            if self.listExistTabelarecebimento is not None:
                for valueTabelarecebimento in listValueTabelarecebimento:
                    existWord = False
                    for wordDelete in self.listExistTabelarecebimento:
                        if wordDelete in valueTabelarecebimento:
                            existWord = True
                            break
                    if existWord is False:
                        listValueTemp.append(valueTabelarecebimento)
                listValueTabelarecebimento = listValueTemp
            listValueAdministradoraTablarecebimento.append(
                [valueAdministradora, listValueTabelarecebimento])
        self.listValue = listValueAdministradoraTablarecebimento

    # com valores da administ. e tabela receb ira acrecentar valores do cargo
    @property
    def pressListValueXpathResultListValueDouble(self):
        return self.listValue

    @pressListValueXpathResultListValueDouble.setter
    def pressListValueXpathResultListValueDouble(self, xpath):
        listValueTemp = []
        self.mouseKeyboard.locationSearchTag = self.tagSon
        for listValueAdministradoraTablarecebimento in self.listValue:
            valueAdministradora = listValueAdministradoraTablarecebimento[0]
            self.mouseKeyboard.clickValue = valueAdministradora
            listValueTabelarecebimentoCargo = []
            for valueTablarecebimento in listValueAdministradoraTablarecebimento[1]:
                self.mouseKeyboard.clickValue = valueTablarecebimento
                while True:
                    self.mouseKeyboard.clickXpath = xpath
                    self.clickOk = self.mouseKeyboard.clickXpath
                    if self.clickOk is True:
                        break
                self.returnValue.xpathTag = xpath
                listValueCargo = self.returnValue.xpathTag
                listValueCargoTemp = []
                # limitar
                for valueCargo in listValueCargo:
                    # limita se a pessoa digita os cargos
                    if self.valueCargo is not None:  # limitar pesquis
                        if valueCargo not in self.valueCargo:
                            continue
                    # limitar apenas o que existe nos cargo da lista de funcion
                    if self.listExistCargos is not None:
                        if valueCargo not in self.listExistCargos:
                            continue
                    listValueCargoTemp.append(valueCargo)
                listValueCargo = listValueCargoTemp
                listValueTabelarecebimentoCargo.append(
                    [valueTablarecebimento, listValueCargo])
            listValueTemp.append(
                [valueAdministradora, listValueTabelarecebimentoCargo])
        self.listValue = listValueTemp

    @property
    def pressListValueResultListValueTriple(self):
        return self.listValue

    @pressListValueResultListValueTriple.setter
    def pressListValueResultListValueTriple(self, listXpath):
        listValueTemp = []
        self.mouseKeyboard.locationSearchTag = self.tagSon
        renameText = RenameText()
        for listValueAdminTablecebCargo in self.listValue:
            self.mouseKeyboard.clickValue = listValueAdminTablecebCargo[0]
            for listValueTabelarecebimentoCargo in listValueAdminTablecebCargo[1]:
                self.mouseKeyboard.clickValue = listValueTabelarecebimentoCargo[0]
                for valueCargo in listValueTabelarecebimentoCargo[1]:
                    self.mouseKeyboard.clickValue = valueCargo
                    listValueTemp2 = []
                    listValueTemp2.append(listValueAdminTablecebCargo[0])
                    listValueTemp2.append(listValueTabelarecebimentoCargo[0])
                    listValueTemp2.append(valueCargo)
                    listEnd = False
                    for campoCotaPeriodoParcela in listXpath:
                        if listEnd is True:
                            break
                        for key, xpathCampoCotaPeriodoParcela in enumerate(
                                campoCotaPeriodoParcela):
                            if key == 0:
                                # indica qual cabecalho pai
                                self.returnValue.xpathFathers = xpathCampoCotaPeriodoParcela
                                # seleciona o texto da xpath
                                self.returnValue.xpathTexts = xpathCampoCotaPeriodoParcela
                                # retorna texto do cabecalho
                                value = self.returnValue.xpathTexts
                                if value is False:
                                    listEnd = True
                                    break
                                renameText.renameHeader = value
                                value = renameText.renameHeader  # salvando cabeçalho
                            elif key == 1 or key == 2:
                                for xpathParcela in xpathCampoCotaPeriodoParcela:
                                    self.returnValue.xpathNameTag = xpathParcela
                                    value = self.returnValue.xpathNameTag
                                    if value is False:
                                        continue
                                    else:
                                        break
                            else:
                                self.returnValue.xpathXpathTag = xpathCampoCotaPeriodoParcela
                                value = self.returnValue.xpathXpathTag
                            if value is False:
                                break
                            listValueTemp2.append(value)
                    listValueTemp.append(listValueTemp2)
        self.listValue = listValueTemp

    @property
    def pressListXpathReturnListValue(self):
        return self.listValue

    @pressListXpathReturnListValue.setter
    def pressListXpathReturnListValue(self, listXpath):
        listTemp = []
        for key, xpath in enumerate(listXpath):
            while True:
                self.mouseKeyboard.clickXpath = xpath
                self.clickOk = self.mouseKeyboard.clickXpath
                if self.clickOk is True:
                    break
            self.returnValue.xpathTag = xpath
            listValueTemp = []
            # limitar
            for value in self.returnValue.xpathTag:
                if key == 0:
                    # limita se a pessoa digita os cargos
                    if self.valueCargo is not None:  # limitar pesquis
                        if value not in self.valueCargo:
                            continue
                    # limitar apenas o que existe nos cargo da lista de funcion
                    if self.listExistCargos is not None:
                        if value not in self.listExistCargos:
                            continue
                elif key == 1:
                    # limita se a pessoa colocar na lista as administradora
                    if self.valueAdministradora is not None:
                        if value not in self.valueAdministradora:
                            continue
                    # limita administradoras que existe nas vendas existentes
                    if self.listExistAdministradoras != []:
                        if value not in self.listExistAdministradoras:
                            continue
                listValueTemp.append(value)
            listTemp.append(listValueTemp)
        self.listValue = listTemp

    @property
    def pressListValueReturnListValue(self):
        return self.listValue

    @pressListValueReturnListValue.setter
    def pressListValueReturnListValue(self, listXpath):
        listCargo = self.listValue[0]
        listAdministradora = self.listValue[1]
        listPagamento = self.listValue[2]
        listValueTemp1 = []
        for cargo in listCargo:
            self.mouseKeyboard.clickValue = cargo
            listValueTemp2 = []
            for administradora in listAdministradora:
                self.mouseKeyboard.clickValue = administradora
                listValueTemp3 = []
                for pagamento in listPagamento:
                    self.mouseKeyboard.clickValue = pagamento
                    listValueTemp4 = []
                    for key, xpathConsole in enumerate(listXpath):
                        # o primeiro xpath é o pai
                        if key == 0:
                            self.returnValue.xpathFathers = xpathConsole
                            self.returnValue.timeSleeps = 0.5
                            self.returnValue.attempts = 6
                            continue
                        if key in [2, 6, 8, 12, 14, 18, 20]:
                            self.returnValue.timeSleeps = 0
                            self.returnValue.attempts = 1
                            for xpathConsoleSingle in xpathConsole:
                                self.returnValue.xpathXpathTagSelected = xpathConsoleSingle
                                value = self.returnValue.xpathXpathTagSelected
                                if value is not False:
                                    break
                        else:
                            self.returnValue.xpathXpathTagSelected = xpathConsole
                            value = self.returnValue.xpathXpathTagSelected
                        listValueTemp4.append(value)
                    listValueTemp3.append([pagamento, listValueTemp4])
                listValueTemp2.append([administradora, listValueTemp3])
            listValueTemp1.append([cargo, listValueTemp2])
        self.listValue = listValueTemp1

    @property
    def organizeListLine(self):
        return self.listValue

    @organizeListLine.setter
    def organizeListLine(self, headerDtPagamentoParcelas):
        listValueTemp = []
        listValueTemp.append(headerDtPagamentoParcelas)
        key = 0
        for cargoOutros in self.listValue:
            cargo = cargoOutros[0]
            for administradoraOutros in cargoOutros[1]:
                administradora = administradoraOutros[0]
                for tipopagamentoOutros in administradoraOutros[1]:
                    tipopagamento = tipopagamentoOutros[0]
                    listValueTemp2 = []
                    listValueTemp2.append(cargo)
                    listValueTemp2.append(administradora)
                    listValueTemp2.append(tipopagamento)
                    for outros in tipopagamentoOutros[1]:
                        listValueTemp2.append(outros)
                    key += 1
                    strKey = str(key)
                    listValueTemp2.append(strKey)
                    listValueTemp.append(listValueTemp2)
        self.listValue = listValueTemp

    @property
    def listLineToTable(self):
        for key, line in enumerate(self.listValue):
            if key == 0:
                # Criar um DataFrame vazio
                self.table = pd.DataFrame(index=[line[-1]], columns=line)
                continue
            # Adicionar a nova linha ao DataFrame existente
            self.table.loc[len(self.table)] = line
        return self.table

    @property
    def addNone(self):
        # ira mostra o maior numero de quantidade de lelemnetos list da list
        maximumNumberColumm = 0
        for listValueTemp in self.listValue:
            if maximumNumberColumm < len(listValueTemp):
                maximumNumberColumm = len(listValueTemp)
        maximumNumberColumm += 1
        listValue = []
        # adiciona 'None' no maior quantidade e tambem completa os restante
        for listValueTemp in self.listValue:
            listValueTemp.append('None')
            listLineTemp = []
            for valueTemp in listValueTemp:
                listLineTemp.append(valueTemp)
                if valueTemp == 'None':
                    numberColumnMiss = maximumNumberColumm - len(listValueTemp)
                    for _ in range(numberColumnMiss):
                        listLineTemp.append('None')
            listValue.append(listLineTemp)
        self.listValue = listValue

    @property
    def addIndex(self):
        listValue = []
        for key, listValueTemp in enumerate(self.listValue):
            key = str(key)
            key = key.rjust(6, '0')
            listValueTemp[-1] = key  # substituir o ultimo 'None' pelo key
            listValue.append(listValueTemp)
        self.listValue = listValue

    @property
    def addEnd(self):
        listValue = []
        for listValueTemp in self.listValue:
            listValueTemp.append('endValue')
            listValue.append(listValueTemp)
        listValue[-1][-1] = 'endValueLast'
        self.listValue = listValue

    @property
    def lineToColumn(self):
        listValue = []
        line = -1
        column = 0
        listValueTemp = []
        while True:
            line += 1
            if self.listValue[line][column] == 'endValue':
                break
            listValueTemp.append(self.listValue[line][column])
            if self.listValue[line][-1] == 'endValueLast':
                listValue.append(listValueTemp)
                listValueTemp = []
                line = -1
                column += 1
        self.listValue = listValue

    @property
    def noneToEmpty(self):
        listValue = []
        for listValueTemp in self.listValue:
            listValueEmpty = []
            for value in listValueTemp:
                if value == 'None':
                    listValueEmpty.append('')
                else:
                    listValueEmpty.append(value)
            listValue.append(listValueEmpty)
        self.listValue = listValue

    @property
    def killAllEmpty(self):
        listValue = []
        for listValueTemp in self.listValue:
            listValueNoEmpty = []
            haveValueNoEmpty = False
            for value in listValueTemp:
                listValueNoEmpty.append(value)
                if value != '':
                    haveValueNoEmpty = True
            if haveValueNoEmpty is True:
                listValue.append(listValueNoEmpty)
        self.listValue = listValue

    @property
    def listColunmToTable(self):
        self.table = pd.DataFrame(index=self.listValue[-1], columns=['Index'])
        self.table['Index'] = self.listValue[-1]
        for number in range(100):
            if len(self.listValue) / (10**number) < 1:
                nStr = number
                break
        del self.listValue[-1]
        for key, column in enumerate(self.listValue):
            key = str(key)
            key = key.rjust(nStr, '0')
            nameNumberColumn = 'Column' + '-' + key
            self.table[nameNumberColumn] = column
        return self.table

    @property
    def renameColumn(self):
        tableManip = TableManip()
        countColumn = 0
        dateStart = True
        parcStart = False
        qtvVendas = 0
        nameNumberColumn1 = False
        while True:
            try:
                self.table.columns.values[countColumn]
            except IndexError:
                break
            match countColumn:
                case 0:
                    nameNumberColumn = 'Index'
                case 1:
                    nameNumberColumn = 'Administradora'
                case 2:
                    nameNumberColumn = 'Tabela de recebimento'
                case 3:
                    nameNumberColumn = 'Cargo'
                case _:
                    tableManip.nameNumberColumns = countColumn
                    countLine = 0
                    while True:
                        tableManip.nameNumberlines = countLine
                        tableManip.infTable = self.table
                        value = tableManip.infTable
                        value = str(value)
                        if value != '' and value != 'nan':
                            word = ''
                            key2Barra = False
                            for key, letter in enumerate(value):
                                word += letter
                                if word == 'Período Venda' or word == 'PerÃ­odo Venda:':
                                    qtvVendas += 1
                                    nameNumberColumn = str(
                                        qtvVendas) + ' Periodo valor qtd vendas'
                                    nameNumberColumn1 = str(qtvVendas) + ' Qtd. Cotas Inicial'
                                    nameNumberColumn2 = str(qtvVendas) + ' Qtd. Cotas Final'
                                    nParc = 1
                                    parcStart = False
                                    break
                                if key == 2 and letter == '/':
                                    key2Barra = True
                                if key == 5 and letter == '/' and key2Barra is True:
                                    if dateStart is True:
                                        nameNumberColumn = str(qtvVendas) + ' Data inicial'
                                        dateStart = False
                                    else:
                                        nameNumberColumn = str(qtvVendas) + ' Data final'
                                        dateStart = True
                                        parcStart = True
                                    key2Barra = False
                                    break
                                if value == word:  # fim. palavra completa
                                    if parcStart is True:
                                        nameNumberColumn = str(qtvVendas) + ' Parc ' + str(nParc)
                                        nParc += 1
                                    else:
                                        nameNumberColumn = self.table.columns.values[countColumn]
                                    break
                            break
                        else:
                            countLine += 1
            self.table.columns.values[countColumn] = nameNumberColumn
            if nameNumberColumn1 is not False:
                self.table.columns.values[countColumn + 1] = nameNumberColumn1
                self.table.columns.values[countColumn + 2] = nameNumberColumn2
                nameNumberColumn1 = False
            countColumn += 1
        return self.table


if __name__ == '__main__':
    from .. import main  # noqa
