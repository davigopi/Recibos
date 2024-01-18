# "ferramenta de captura"  do windows para pegar imagens
from ast import Break
from asyncio.windows_events import NULL
# from cgitb import text
from contextlib import nullcontext
# import re
import sys
# from msilib.schema import Property
# import ssl
from time import sleep
import pyautogui
import pandas as pd
from pandas.errors import EmptyDataError
import os
# import random
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException, InvalidArgumentException, InvalidSelectorException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


excecaoAll = (NoSuchElementException
            , ElementNotInteractableException
            , ElementClickInterceptedException
            , StaleElementReferenceException
            , InvalidArgumentException
            , InvalidSelectorException
            , TimeoutException
            )

class Connect:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.df = pd.DataFrame()
        self.dfNew = None
        self.listValue = None
        self.table = None
        self.clickOk = None
        self.xpathOk = None
        self.user = None
        self.password = None
        self.tagSon = None
        self.tagFather = None
        self.tagGet = None
        self.file = None
        self.month = None
        self.valueAdministradora = None
        self.valueCargo = None
        self.mouseKeyboard = MouseKeyboard(driver=self.driver)
        self.returnValue = ReturnValue(driver=self.driver)

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
    def valueAdministradoras(self):
        return None
    
    @valueAdministradoras.setter
    def valueAdministradoras(self, valueAdministradora):
        self.valueAdministradora = valueAdministradora

    @property
    def valueCargos(self):
        return None
    
    @valueCargos.setter
    def valueCargos(self, valueCargo):
        self.valueCargo = valueCargo

    @property
    def tagReturnValue(self):
        self.returnValue.tagSons = self.tagSon
        self.returnValue.tagFathers = self.tagFather
        self.returnValue.tagGets = self.tagGet

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
    def dfSircon(self): 
        return self.dfNew
    
    @dfSircon.setter
    def dfSircon(self, listXpath):  
        file = FileManip(self.file)
        for lastMonth in range(self.month, -1, -1):
            file.delete
            fileNotExist = True
            for key, xpath in enumerate(listXpath):
                butt = ButtonsSpecial(lastMonth=lastMonth, func=self.mouseKeyboard, xpath=xpath) 
                clickOk = False
                while clickOk is False:
                    if key == 3 or key == 7:
                        clickOk = butt.clickLeftArrow
                    elif key == 4:
                        clickOk = butt.clickDayStartMonth
                    elif key == 8:
                        clickOk = butt.clickDayEndMonth
                    else:
                        self.mouseKeyboard.clickXpath = xpath
                        clickOk = self.mouseKeyboard.clickXpath
            if fileNotExist is True:
                self.df = file.readCsv
                table = TableManip(self.dfNew, self.df)
                self.dfNew = table.merge
        file.delete
        file.writeCsv = self.dfNew

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

    @property
    def pressXpathReturnListValue(self):
        return self.listValue

    @pressXpathReturnListValue.setter
    def pressXpathReturnListValue(self, xpath):
        while True:
            self.mouseKeyboard.clickXpath = xpath
            self.clickOk = self.mouseKeyboard.clickXpath
            if self.clickOk is True:
                break
        self.returnValue.tagValue = xpath
        self.listValue = self.returnValue.tagValue

    @property
    def pressListValueXpathReturnListValue(self):
        return self.listValue
    
    @pressListValueXpathReturnListValue.setter
    def pressListValueXpathReturnListValue(self, xpath):
        listValueAdministradoraTablarecebimento = []
        for valueAdministradora in self.listValue:
            if self.valueAdministradora is not None:
                jumpAdministradora = True
                for valueAdministradora2 in self.valueAdministradora:
                    if valueAdministradora2 == valueAdministradora:
                        jumpAdministradora = False
                if jumpAdministradora is True:
                    continue
            self.mouseKeyboard.locationSearchTag = self.tagSon
            self.mouseKeyboard.clickValue = valueAdministradora
            while True:
                self.mouseKeyboard.clickXpath = xpath
                self.clickOk = self.mouseKeyboard.clickXpath
                if self.clickOk is True:
                    break
            self.returnValue.tagValue = xpath
            listValueTablarecebimento = self.returnValue.tagValue
            listValueAdministradoraTablarecebimento.append([valueAdministradora, listValueTablarecebimento])
        self.listValue = listValueAdministradoraTablarecebimento

    @property
    def pressListValueXpathReturnListValueDouble(self):
        return self.listValue

    @pressListValueXpathReturnListValueDouble.setter
    def pressListValueXpathReturnListValueDouble(self, xpath):
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
                self.returnValue.tagValue = xpath
                listValueCargo = self.returnValue.tagValue
                listValueTabelarecebimentoCargo.append([valueTablarecebimento, listValueCargo])
            listValueTemp.append([valueAdministradora, listValueTabelarecebimentoCargo])
        self.listValue = listValueTemp
    
    @property
    def pressListValueReturnListValueTriple(self):
        return self.listValue

    @pressListValueReturnListValueTriple.setter
    def pressListValueReturnListValueTriple(self, listXpath):
        listValueTemp = []
        self.mouseKeyboard.locationSearchTag = self.tagSon
        renameText = RenameText()
        for listValueAdministradoraTablarecebimentoCargo in self.listValue:
            self.mouseKeyboard.clickValue = listValueAdministradoraTablarecebimentoCargo[0]
            for listValueTablarecebimentoCargo in listValueAdministradoraTablarecebimentoCargo[1]:
                self.mouseKeyboard.clickValue = listValueTablarecebimentoCargo[0]
                for valueCargo in listValueTablarecebimentoCargo[1]:
                    if self.valueCargo is not None:  # limitar pesquisa
                        jumpCargo = True
                        for valueCargo2 in self.valueCargo:  
                            if valueCargo2 == valueCargo:
                                jumpCargo = False
                        if jumpCargo is True:
                            continue
                    self.mouseKeyboard.clickValue = valueCargo
                    listValueTemp2 = []
                    listValueTemp2.append(listValueAdministradoraTablarecebimentoCargo[0])
                    listValueTemp2.append(listValueTablarecebimentoCargo[0])
                    listValueTemp2.append(valueCargo)
                    listEnd = False
                    for campoCotaPeriodoParcela in listXpath:
                        if listEnd is True:
                            break
                        for key, xpathCampoCotaPeriodoParcela in enumerate(campoCotaPeriodoParcela):
                            if key == 0:
                                self.returnValue.xpathFathers = xpathCampoCotaPeriodoParcela  # indica qual cabecalho pai
                                self.returnValue.xpathTexts = xpathCampoCotaPeriodoParcela  # seleciona o texto da xpath
                                value = self.returnValue.xpathTexts  # retorna texto do cabecalho
                                if value is False:
                                    listEnd = True
                                    break
                                renameText.renameHeader = value
                                value = renameText.renameHeader  # salvando cabeçalho
                            elif key == 1 or key == 2:
                                for xpathParcela in xpathCampoCotaPeriodoParcela:
                                    self.returnValue.nameValue = xpathParcela
                                    value = self.returnValue.nameValue
                                    if value is False:
                                        continue
                                    else:
                                        # if value == '':
                                        #     value = 0
                                        break
                            else:
                                self.returnValue.xpathValue = xpathCampoCotaPeriodoParcela
                                value = self.returnValue.xpathValue
                            if value is False:
                                break
                            listValueTemp2.append(value)
                    listValueTemp.append(listValueTemp2)
        self.listValue = listValueTemp

    @property
    def addNone(self):
        maximumNumberColumm = 0
        for listValueTemp in self.listValue:
            if maximumNumberColumm < len(listValueTemp):
                maximumNumberColumm = len(listValueTemp)
        maximumNumberColumm += 1
        listValue = []
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
    def listToTable(self):
        self.table = pd.DataFrame(index=self.listValue[-1], columns=['Index'])
        self.table['Index'] = self.listValue[-1]
        for number in range(100):
            if len(self.listValue)/(10**number) < 1:
                nStr = number
                break
        for key, column in enumerate(self.listValue):
            key = str(key)
            key = key.rjust(nStr, '0') 
            nameNumberColumn = 'Column' + '-' + key
            self.table[nameNumberColumn] = column
        # return self.table

    @property
    def renameColumn(self):
        countColumn = 0
        while True:
            try:
                self.table.columns.values[count]
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
                    nameValue = self.table.columns.values[count]
                    print(nameValue)
                    TableManip.nameNumberColumns = count
                    TableManip.nameNumberlines

                    work = ''
                    for letter in nameValue:
                        work += letter
            self.table.columns.values[count] = nameNumberColumn
            countColumn += 1


        #             for column1 in column:
        #                 nameNumberColumnCondition = False
        #                 if column1 != '':
        #                     word = ''
        #                     dataCondition = 0
        #                     for key, letter in enumerate(column1):
        #                         word += letter
        #                         if word == 'Período Venda':
        #                             print(f'################# {word} #################')
        #                             nameNumberColumn = 'Periodo valor qtd vendas ' + str(nPeriodo)
        #                             nPeriodo += 1
        #                             nameNumberColumnCondition = True
        #                             break
        #                         if key == 2 or key == 5:
        #                             if letter == '/':
        #                                 dataCondition += 1
        #                         if dataCondition == 2:
        #                             print(f'################# {word} #################')
        #                             if dateStart is True:
        #                                 nameNumberColumn = 'Data inicial ' + str(nDate)
        #                                 dateStart = False
        #                             else:
        #                                 nameNumberColumn = 'Data final ' + str(nDate)
        #                                 dateStart = True
        #                                 nDate += 1
        #                             nameNumberColumnCondition = True
        #                             break
        #                     # column1 = column1.replace('.', '')
        #                     # column1 = column1.replace(',', '.')
        #                 if nameNumberColumnCondition is False:
        #                     print(column1)              
        #                 else:
        #                     break


        return self.table

        # nPeriodo = 1
        # nDate = 1
        # dateStart = True
        # for key, column in enumerate(self.listValue):
        #     if column == self.listValue[-1]:
        #         break
        #     match key:
        #         case 0:
        #             nameNumberColumn = '
        #         case 1:
        #             nameNumberColumn = 
        #         case 2:
        #             nameNumberColumn = 
        #         
       


class ReturnValue:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.xpathFather = None
        self.tagFather = None
        self.tagSon = None
        self.tagGet = None
        self.value = None

    @property
    def xpathFathers(self):
        return None
    
    @xpathFathers.setter
    def xpathFathers(self, xpathFather):
        self.xpathFather = xpathFather

    @property
    def tagFathers(self):
        return None
    
    @tagFathers.setter
    def tagFathers(self, tagFather):
        self.tagFather = tagFather

    @property
    def tagSons(self):
        return None
    
    @tagSons.setter
    def tagSons(self, tagSon):
        self.tagSon = tagSon

    @property
    def tagGets(self):
        return None
    
    @tagGets.setter
    def tagGets(self, tagValue):
        self.tagGet = tagValue

    @property
    def xpathValue(self):
        return self.value
    
    @xpathValue.setter
    def xpathValue(self, xpath):
        count = 0
        while True:
            try:
                count += 1
                self.value = self.driver.find_element(By.XPATH, self.xpathFather).find_element(By.XPATH, xpath).get_attribute(self.tagGet)
                break
            except excecaoAll:
                if count >= 3:
                    self.value = False
                    break
                sleep(0.2)

    @property
    def nameValue(self):
        return self.value
    
    @nameValue.setter
    def nameValue(self, name):
        count = 0
        while True:
            try:
                count += 1
                self.value = self.driver.find_element(By.XPATH, self.xpathFather).find_element(By.NAME, name).get_attribute(self.tagGet)
                break
            except excecaoAll:
                if count >= 3:
                    self.value = False
                    break
                sleep(0.2)

    @property
    def xpathTexts(self):
        return self.value
    
    @xpathTexts.setter
    def xpathTexts(self, xpath):
        count = 0
        while True:
            count += 1
            try:
                self.value = self.driver.find_element(By.XPATH, xpath).text
                break
            except excecaoAll:
                if count >= 3:
                    self.value = False
                    break
                sleep(0.2)

    @property
    def tagValue(self):
        return self.value
    
    @tagValue.setter
    def tagValue(self, xpath):
        while True:
            try: 
                self.value = self.driver.find_element(By.XPATH, xpath).get_attribute(self.tagGet)  # retornar o outerHTML
                # pip install lxml
                self.value = BeautifulSoup(self.value, "lxml").find(self.tagFather).findAll(self.tagSon)  # formatar outerHTMl
                listValue = []
                for key in range(1, len(self.value), 1):
                    listValue.append(self.value[key].find(text=True))  # pega cada valro 
                self.value = listValue
                break  
            except (AttributeError, Exception) as e:
                sleep(0.2)
   

class RenameText:
    def __init__(self, *args, **kwargs) -> None:
        self.text = None

    @property
    def renameHeader(self):
        return self.text
    
    @renameHeader.setter
    def renameHeader(self, text):
        text = text.replace('\n', '&&&&&')
        for _ in range(10):
            text = text.replace('  ', ' ')
        self.text = ''
        countEnd = 0
        for letter in text:
            if letter == '&':
                countEnd += 1
                if countEnd >= 3:
                    break
                continue
            else: 
                self.text += letter

class XpathManip:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.excecao = (NoSuchElementException
                        , ElementNotInteractableException
                        , ElementClickInterceptedException
                        , StaleElementReferenceException
                        )
        self.xpathOk = None

    @property
    def locate(self):
        return self.xpathOk

    @locate.setter
    def locate(self, xpath):
        count = 0
        while True:
            try:   
                self.driver.find_element(By.XPATH, xpath).location_once_scrolled_into_view
                self.xpathOk = True
                break
            except excecaoAll:
                if count >= 5:
                    self.xpathOk = False
                    break
                count += 1
                sleep(1)
                continue


class FileManip:
    def __init__(self, arqCons) -> None:
        self._arqCons = arqCons
        self._dfnew = None
        pass
    
    @property
    def delete(self):
        while True:
            try:
                os.remove(self._arqCons)
                break
            except FileNotFoundError:  # caso arq nao exista
                break
            except PermissionError:
                sleep(5)

    @property
    def readCsv(self):
        while True:
            try:  # se não carregar é porque não completou download
                self._dfNew = pd.read_csv(self._arqCons, sep=';', encoding='utf-8', dtype=str)
                return self._dfNew
            except FileNotFoundError:
                pass
            except PermissionError as e:
                sleep(1)
            except EmptyDataError:
                pass

    @property
    def writeCsv(self):
        return self._df
        
    @writeCsv.setter
    def writeCsv(self, df):
        self._df = df
        self._df.to_csv(self._arqCons, index=False, header=True)


class TableManip:
    def __init__(self, dfNew, df) -> None:
        self._df = df
        self._dfNew = dfNew
        self.nameNumberLine = None
        self.nameNumberColumn = None
        
        self.value = None

    @property
    def merge(self):
        if self._dfNew is None:
            self._dfNew = self._df
        else:
            self._dfNew = pd.merge(self._dfNew, self._df, how='outer')            
        return self._dfNew

    @property
    def nameNumberlines(self):
        return self.nameNumberLine
    
    @nameNumberlines.setter
    def nameNumberlines(self, nameNumberLine):
        self.nameNumberLine = nameNumberLine

    @property
    def nameNumberColumns(self):
        return self.nameNumberColumn
    
    @nameNumberColumns.setter
    def nameNumberColumns(self, nameNumberColumn):
        self.nameNumberColumn = nameNumberColumn

    @property
    def infTable(self):
        if type(self.nameNumberLine) == str and type(self.nameNumberColumn) == str:
            self.value = df.at[self.nameNumberLine, self.nameNumberColumn]  # pelo nome
        else:
            print(self.nameNumberLine, type(self.nameNumberLine), "###", self.nameNumberColumn, type(self.nameNumberColumn))
            self.value = df.iat[self.nameNumberLine, self.nameNumberColumn]  # pelo local
        return self.value

class ImageManip:
    def __init__(self) -> None:
        self.img = None

    @property
    def images(self):
        return self.img
    
    @images.setter
    def images(self, img):
        self.img = img

    @property
    def clickImg(self):
        similariyImg = 1
        waitImg = 0.9
        while True:
            try:
                # Instalar 'pip install opencv-python' 
                x, y = pyautogui.locateCenterOnScreen(self.img, confidence=similariyImg)
                pyautogui.click(x, y)
            except Exception:
                similariyImg -= 0.01
                if similariyImg <= waitImg:
                    sleep(1)
                    waitImg -= 0.1
                    if waitImg <= 0.6:
                        similariyImg = 1
                        waitImg = 0.9

    
class MouseKeyboard:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        # self.xpath = kwargs.get('xpath')
        self.excecao = (NoSuchElementException
                        , ElementNotInteractableException
                        , ElementClickInterceptedException
                        , StaleElementReferenceException
                        , InvalidArgumentException
                        , TimeoutException
                        )
        self.numberTimesRepeated = 0
        self.clickOk = None
        self.locationSearch = '*'
        self.writeSec = None

    @property
    def writeSecs(self):
        return self.writeSec
    
    @writeSecs.setter
    def writeSecs(self, writeSec):
        self.writeSec = writeSec

    @property
    def locationSearchTag(self):
        return self.locationSearch
    
    @locationSearchTag.setter
    def locationSearchTag(self, xpath):
        self.locationSearch = xpath

    @ property
    def clickXpath(self):
        return self.clickOk

    @clickXpath.setter
    def clickXpath(self, xpath):   
        wait = WebDriverWait(self.driver, 1)
        while True:
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                element = self.driver.find_element(By.XPATH, xpath)
                element.click()
                self.numberTimesRepeated = 0
                self.clickOk = True
                break
            except self.excecao:
                self.numberTimesRepeated += 1
                if self.numberTimesRepeated >= 4:
                    if self.numberTimesRepeated >= 10:
                        print(f'Erro, mais de dez tentativas, em click do xpath {xpath}')
                        sys.exit()
                    else:
                        sleep(1)
                        self.clickOk = False
                        break

    @property
    def clickValue(self):
        return None
    
    @clickValue.setter
    def clickValue(self, text):
        self.numberTimesRepeated = 0
        while True:
            try:
                self.driver.find_element(By.XPATH, f"//{self.locationSearchTag}[contains(text(),'{text}')]").click()
                sleep(0.5)
                break
            except self.excecao:
                self.numberTimesRepeated += 1
                if self.numberTimesRepeated >= 4:
                    if self.numberTimesRepeated >= 10:
                        print(f'Erro, mais de dez tentativas, em click no texto {text}')
                        sys.exit()
                    else:
                        sleep(1)
            
    @property
    def keys(self):
        return self.clickOk

    @keys.setter
    def keys(self, xpath):
        while True:
            try:
                self.driver.find_element(By.XPATH, xpath).clear()
                self.driver.find_element(By.XPATH, xpath).send_keys(self.writeSec)
                self.clickOk = True
                break
            except self.excecao:
                sleep(0.2)
                self.numberTimesRepeated += 1
                if self.numberTimesRepeated >= 4:
                    if self.numberTimesRepeated >= 10:
                        print(f'Erro, mais de dez tentativas, em click do xpath {xpath}')
                        sys.exit()
                    else:
                        sleep(1)
                        self.clickOk = False
                        break


class ButtonsSpecial:
    def __init__(self, lastMonth, func, xpath) -> None:
        self.lastMonth = lastMonth
        self.func = func
        self.xpath = xpath

    @property
    def clickLeftArrow(self):
        if self.lastMonth != 0:
            for _ in range(self.lastMonth):  # quantidade de vezes que tem que retornar
                self.func.clickXpath = self.xpath
                clickOk = self.func.clickXpath
        else:
            clickOk = True  # ultimo mes nao precisa click
        return clickOk
    
    @property
    def clickDayStartMonth(self):
        line = 1
        column = 7
        while True:
            self.xpath = f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{line}]/td[{column}]'
            self.func.clickXpath = self.xpath
            clickOk = self.func.clickXpath
            column -= 1 
            if column == 0:
                break 
        sleep(3) 
        return clickOk
    
    @property
    def clickDayEndMonth(self):
        if self.lastMonth != 0:
            line = 4
            column = 7
            while True:
                self.xpath = f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{line}]/td[{column}]'
                self.func.clickXpath = self.xpath
                clickOk = self.func.clickXpath
                column += 1
                if (column == 3 and line == 6) or clickOk is False:
                    clickOk = True
                    break
                if column == 8:
                    line += 1
                    column = 1  
        else:
            clickOk = True
        sleep(3)
        return clickOk
    

if __name__ == '__main__':
    import main