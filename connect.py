# "ferramenta de captura"  do windows para pegar imagens
from ast import Break
from asyncio.windows_events import NULL
# from cgitb import text
from contextlib import nullcontext
import re
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
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException, InvalidArgumentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


excecaoAll = (NoSuchElementException
            , ElementNotInteractableException
            , ElementClickInterceptedException
            , StaleElementReferenceException
            , InvalidArgumentException
            )

class Connect:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.df = pd.DataFrame()
        self.dfNew = None
        self.listValue = None
        self.table = None

    def logarSircon(self, security, listXpath):
        func = MouseKeyboard(driver=self.driver)
        for xpath in listXpath: 
            indexNumber = listXpath.index(xpath)
            try:
                writeSec = security[indexNumber]
            except IndexError:
                writeSec = False
            if writeSec is not False:
                func.keys(xpath, writeSec)
            else:
                clickOk = False
                while clickOk is False:
                    clickOk = func.clickXpath(xpath)
                    # sleep(0.5)

    def locateXpath(self, xpath):
        xpathManip = XpathManip(driver=self.driver)
        xpathManip.locate = xpath
        xpathOk = xpathManip.locate
        return xpathOk
    
    def dfSircon(self, arqCons, months, listXpath):  
        file = FileManip(arqCons)
        for lastMonth in range(months, -1, -1):
            file.delete
            fileNotExist = True
            func = MouseKeyboard(driver=self.driver)  
            # beginMonth = False 
            for key, xpath in enumerate(listXpath):
                butt = ButtonsSpecial(lastMonth=lastMonth, func=func, xpath=xpath) 
                clickOk = False
                while clickOk is False:
                    if key == 3 or key == 7:
                        clickOk = butt.clickLeftArrow()
                    elif key == 4:
                        clickOk = butt.clickDayStartMonth()
                    elif key == 8:
                        clickOk = butt.clickDayEndMonth()
                    else:
                        clickOk = func.clickXpath(xpath)
                        if clickOk >= 10:
                            clickOk = True
                            fileNotExist = False
            if fileNotExist is True:
                self.df = file.readCsv
                table = TableManip(self.dfNew, self.df)
                self.dfNew = table.merge
        file.delete
        file.writeCsv = self.dfNew

    def pressListXpath(self, listXpath):
        mousekeyboard = MouseKeyboard(driver=self.driver)
        for key, xpath in enumerate(listXpath): 
            clickOk = False
            while clickOk is False:
                if clickOk >= 10:
                    break
                clickOk = mousekeyboard.clickXpath(xpath)

    def pressXpathReturnListValue(self, xpath):
        mousekeyboard = MouseKeyboard(driver=self.driver)
        returnValue = ReturnValue(driver=self.driver)
        # returnValue.tagValueGet = 'value'
        clickOk = False
        while clickOk is False:
            if clickOk >= 10:
                break
            clickOk = mousekeyboard.clickXpath(xpath)
            returnValue.tagSonValue = 'option'
            returnValue.tagFatherValue = 'select'
            returnValue.tagValueGet = 'outerHTML'
            returnValue.tagValue = xpath
            listValue = returnValue.tagValue
        return listValue

    # def commissionSircon(self, listXpath):
    #     mousekeyboard = MouseKeyboard(driver=self.driver)
    #     returnValue = ReturnValue(driver=self.driver)
    #     # for xpathAdm in listXpath[5]:  # list de administradoras
    #     for key, xpath in enumerate(listXpath): 
    #         clickOk = False
    #         while clickOk is False:
    #             if clickOk >= 10:
    #                 break
    #             clickOk = mousekeyboard.clickXpath(xpath)
    #             if key == 4:
    #                 returnValue.tagSonValue = 'option'
    #                 returnValue.tagFatherValue = 'select'
    #                 returnValue.tagValue = xpath
    #                 listValue = returnValue.tagValue
    #     return listValue

    def pressListValueXpathReturnListValue(self, xpath, listValue, tagSon, tagFather):
        listValueAdministradoraTablarecebimento = []
        for valueAdministradora in listValue:
            mousekeyboard = MouseKeyboard(driver=self.driver)
            mousekeyboard.locationSearchTag = tagSon

            if valueAdministradora != 'DISAL':
                continue
            
            while True:
                mousekeyboard.clickValue = valueAdministradora
                clickOk = mousekeyboard.clickValue
                if clickOk is True:
                    break
            while True:
                returnValue = ReturnValue(driver=self.driver)
                clickOk = mousekeyboard.clickXpath(xpath)
                returnValue.tagSonValue = tagSon
                returnValue.tagFatherValue = tagFather
                returnValue.tagValueGet = 'outerHTML'
                returnValue.tagValue = xpath
                listValueTablarecebimento = returnValue.tagValue
                listValueAdministradoraTablarecebimento.append([valueAdministradora, listValueTablarecebimento])
                if clickOk >= 10 or clickOk is True:
                    break
                # sleep(1)
        return listValueAdministradoraTablarecebimento

    def pressListValueXpathReturnListValueDouble(self, xpath, listValue, tagSon, tagFather):
        listValueTemp = []
        mousekeyboard = MouseKeyboard(driver=self.driver)
        mousekeyboard.locationSearchTag = tagSon
        for listValueAdministradoraTablarecebimento in listValue:
            # mousekeyboard = MouseKeyboard(driver=self.driver)
            # mousekeyboard.locationSearchTag = tagSon
            valueAdministradora = listValueAdministradoraTablarecebimento[0]
            while True:
                mousekeyboard.clickValue = valueAdministradora
                clickOk = mousekeyboard.clickValue
                if clickOk is True:
                    break
            listValueTabelarecebimentoCargo = []
            sleep(0.5)
            for valueTablarecebimento in listValueAdministradoraTablarecebimento[1]:
                # mousekeyboard = MouseKeyboard(driver=self.driver)
                # mousekeyboard.locationSearchTag = tagSon
                while True:
                    mousekeyboard.clickValue = valueTablarecebimento
                    clickOk = mousekeyboard.clickValue
                    if clickOk is True:
                        break
                while True:
                    returnValue = ReturnValue(driver=self.driver)
                    clickOk = mousekeyboard.clickXpath(xpath)
                    returnValue.tagSonValue = tagSon
                    returnValue.tagFatherValue = tagFather
                    returnValue.tagValueGet = 'outerHTML'
                    returnValue.tagValue = xpath
                    listValueCargo = returnValue.tagValue
                    listValueTabelarecebimentoCargo.append([valueTablarecebimento, listValueCargo])
                    if clickOk >= 10 or clickOk is True:
                        break
                    # sleep(1)
            listValueTemp.append([valueAdministradora, listValueTabelarecebimentoCargo])
        return listValueTemp
    
    def pressListValueReturnListValueTriple(self, listXpath, listValue, tagSon):
        listValueTemp = []
        mousekeyboard = MouseKeyboard(driver=self.driver)
        mousekeyboard.locationSearchTag = tagSon
        returnValue = ReturnValue(driver=self.driver)
        renameText = RenameText()
        for listValueAdministradoraTablarecebimentoCargo in listValue:
            valueAdministradora = listValueAdministradoraTablarecebimentoCargo[0]
            while True:
                mousekeyboard.clickValue = valueAdministradora
                clickOk = mousekeyboard.clickValue
                if clickOk is True:
                    break
            sleep(0.5)
            for listValueTablarecebimentoCargo in listValueAdministradoraTablarecebimentoCargo[1]:
                valueTablarecebimento = listValueTablarecebimentoCargo[0]
                while True:
                    mousekeyboard.clickValue = valueTablarecebimento
                    clickOk = mousekeyboard.clickValue
                    if clickOk is True:
                        break
                sleep(0.5)
                for valueCargo in listValueTablarecebimentoCargo[1]:
                    # if valueCargo != 'CONSULTOR CLT - A PARTIR JAN-2018':
                    #     continue
                    while True:
                        mousekeyboard.clickValue = valueCargo
                        clickOk = mousekeyboard.clickValue
                        if clickOk is True:
                            break
                        sleep(0.5)
                    listCampoParcela = []
                    for key, xpathCampoParcela in enumerate(listXpath):
                        returnValue.xpathFatherValue = xpathCampoParcela[0]
                        returnValue.xpathValueText = xpathCampoParcela[0]
                        valueHeader = returnValue.xpathValueText
                        if valueHeader is False:
                            break
                        renameText.renameHeader = valueHeader
                        valueHeader = renameText.renameHeader
                        listCampoParcela.append(valueHeader)
                        returnValue.tagValueGet = 'value'
                        # listParcela = []
                        for xpathParcela in xpathCampoParcela[1]:
                            returnValue.xpathValue = xpathParcela
                            value = returnValue.xpathValue
                            if value is False:
                                break
                            listCampoParcela.append(value)
                        # listCampoParcela.append([valueHeader, listParcela])        
                    listValueTemp.append([valueAdministradora, valueTablarecebimento, valueCargo, listCampoParcela])
        return listValueTemp
    
    @property
    def removeListInside(self):
        return self.listValue
    
    @removeListInside.setter
    def removeListInside(self, listValue):
        self.listValue = []
        for listValueTemp in listValue:
            listLineTemp = []
            for key, value in enumerate(listValueTemp):
                if key == 3:  # local que esta o valor que é outra lista
                    for valuePercentage in value:
                        listLineTemp.append(valuePercentage)
                else: 
                    listLineTemp.append(value)
            self.listValue.append(listLineTemp)
    
    @property
    def killAllEmpty(self):
        return self.listValue
    
    @killAllEmpty.setter
    def killAllEmpty(self, listValue):
        self.listValue = []
        for listValueTemp in listValue:
            listValueNoEmpty = []
            haveValueNoEmpty = False
            for value in listValueTemp:
                listValueNoEmpty.append(value)
                if value != '':
                    haveValueNoEmpty = True
            if haveValueNoEmpty is True:
                self.listValue.append(listValueNoEmpty)

    @property
    def addNone(self):
        return self.listValue
    
    @addNone.setter
    def addNone(self, listValue):
        maximumNumberColumm = 0
        for listValueTemp in listValue:
            if maximumNumberColumm < len(listValueTemp):
                maximumNumberColumm = len(listValueTemp)
        maximumNumberColumm += 1

        self.listValue = []
        for listValueTemp in listValue:
            listValueTemp.append('None')  
            listLineTemp = []
            for valueTemp in listValueTemp:
                listLineTemp.append(valueTemp)
                if valueTemp == 'None':
                    numberColumnMiss = maximumNumberColumm - len(listValueTemp)
                    for _ in range(numberColumnMiss):
                        listLineTemp.append('None')
            self.listValue.append(listLineTemp)

    @property
    def addIndex(self):
        return self.listValue
    
    @addIndex.setter
    def addIndex(self, listValue):
        self.listValue = []
        for key, listValueTemp in enumerate(listValue):
            key = str(key)
            key = key.rjust(6, '0') 
            listValueTemp[-1] = key  # substituir o ultimo 'None' pelo key
            self.listValue.append(listValueTemp)
    
    @property
    def addEnd(self):
        return self.listValue
    
    @addEnd.setter
    def addEnd(self, listValue):
        self.listValue = []
        for listValueTemp in listValue:
            listValueTemp.append('endValue')
            self.listValue.append(listValueTemp)
        self.listValue[-1][-1] = 'endValueLast'

    @property
    def lineToColumn(self):
        return self.listValue
    
    @lineToColumn.setter
    def lineToColumn(self, listValue):
        self.listValue = []
        line = -1
        column = 0
        listValueTemp = []
        while True:
            line += 1
            if listValue[line][column] == 'endValue':
                break
            listValueTemp.append(listValue[line][column])
            if listValue[line][-1] == 'endValueLast':
                self.listValue.append(listValueTemp)
                listValueTemp = []
                line = -1
                column += 1 

    @property
    def noneToEmpty(self):
        return self.listValue
    
    @lineToColumn.setter
    def noneToEmpty(self, listValue):
        self.listValue = []
        for listValueTemp in listValue:
            listValueEmpty = []
            for value in listValueTemp:
                if value == 'None':
                    listValueEmpty.append('')
                else:
                    listValueEmpty.append(value)
            self.listValue.append(listValueEmpty)

    @property
    def listToTable(self):
        return self.table
    
    @listToTable.setter
    def listToTable(self, listValue):
        self.table = pd.DataFrame(index=listValue[-1], columns=['Index'])
        self.table['Index'] = listValue[-1]
        for number in range(100):
            if len(listValue)/(10**number) < 1:
                nStr = number
                break
        for key, column in enumerate(listValue):
            if column == listValue[-1]:
                break
            key = str(key)
            key = key.rjust(nStr, '0') 
            nameColumn = 'Column' + '-' + key
            self.table[nameColumn] = column

    def commissionSirconValue(self, listXpath):
        # func = MouseKeyboard(driver=self.driver) 
        listComission = []
        for key, xpathFather in enumerate(listXpath[0]):
            listComission.append(key+1)
            returnValue = ReturnValue(driver=self.driver)
            returnValue.xpathFatherValue = xpathFather
            for xpath in listXpath[1][key]:
                returnValue.xpathValue = xpath
                value = returnValue.xpathValue
                listComission.append(value)
        print(f'##################### {listComission} #####################')


class ReturnValue:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.xpathFather = None
        self.tagFather = None
        self.tagSon = None
        self.tagGet = None
        self.value = None
       
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
    def xpathValueText(self):
        return self.value
    @xpathValueText.setter
    def xpathValueText(self, xpath):
        count = 0
        while True:
            count += 1
            try:
                self.value = self.driver.find_element(By.XPATH, xpath).text
                break
            except excecaoAll as e:
                if count >= 3:
                    self.value = False
                    break
                sleep(0.5)

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
                pass

    @property
    def xpathFatherValue(self):
        return self.xpathFather
    @xpathFatherValue.setter
    def xpathFatherValue(self, xpathFather):
        self.xpathFather = xpathFather

    @property
    def tagFatherValue(self):
        return self.tagFather
    @tagFatherValue.setter
    def tagFatherValue(self, tagFather):
        self.tagFather = tagFather

    @property
    def tagSonValue(self):
        return self.tagSon
    @tagSonValue.setter
    def tagSonValue(self, tagSon):
        self.tagSon = tagSon

    @property
    def tagValueGet(self):
        return self.tagGet
    @tagValueGet.setter
    def tagValueGet(self, tagValue):
        self.tagGet = tagValue

class RenameText:
    def __init__(self, *args, **kwargs) -> None:
        self.text = None

    @property
    def renameHeader(self):
        return self.text
    
    @renameHeader.setter
    def renameHeader(self, text):
        text = text.replace('\n', '&&&&&')
        for key in range(10):
            text = text.replace('  ', ' ')
        text = text.replace('- ', '#####')
        self.text = ''
        countStart = 0
        countEnd = 0
        textStart = False
        for letter in text:
            if letter == '#':
                countStart += 1
                if countStart >= 3:
                    textStart = True
                continue
            elif letter == '&':
                countEnd += 1
                if countEnd >= 3:
                    break
                continue
            else: 
                if textStart is True:
                    self.text += letter
                countStart = 0
                countEnd = 0

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
                count += 1
                if count >= 3:
                    self.xpathOk = False
                    break
                sleep(0.5)
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

    @property
    def merge(self):
        if self._dfNew is None:
            self._dfNew = self._df
        else:
            self._dfNew = pd.merge(self._dfNew, self._df, how='outer')            
        return self._dfNew


class ImageManip:
    def __init__(self, img) -> None:
        self._img = img

    @property
    def clickImg(self):
        while True:
            try:
                # tem que instalar 'pip install opencv-python' , em alguns programa usa confidencialidade
                x, y = pyautogui.locateCenterOnScreen(self._img, confidence=0.9)
                pyautogui.click(x, y)
                return True
            except Exception:
                return False

    @property
    def wait(self):
        try:
            x, y = pyautogui.locateCenterOnScreen(self._img, confidence=0.9)
            return True
        except Exception:
            return False
        





class MouseKeyboard:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        # self.xpath = kwargs.get('xpath')
        self.excecao = (NoSuchElementException
                        , ElementNotInteractableException
                        , ElementClickInterceptedException
                        , StaleElementReferenceException
                        )
        self.numberTimesRepeated = 0
        self.clickOk = None
        self.locationSearch = '*'

        # //*[@id="frm:pnlBloco"]/div[2]

    @property
    def locationSearchTag(self):
        return  self.locationSearch
    
    @locationSearchTag.setter
    def locationSearchTag(self, xpath):
         self.locationSearch = xpath

    def clickXpath(self, xpath):   
        while True:
            try:
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                # wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                element = self.driver.find_element(By.XPATH, xpath)
                element.click()
                self.numberTimesRepeated = 0
                return True
            except self.excecao:
                sleep(0.5)
                self.numberTimesRepeated += 1
                if self.numberTimesRepeated >= 4:
                    if self.numberTimesRepeated >= 10:
                        return self.numberTimesRepeated  # botao nao exite e nem vai existir
                    return False

    @property
    def clickValue(self):
        return self.clickOk
    
    @clickValue.setter
    def clickValue(self, value):
        self.clickOk = False
        try:
            self.driver.find_element(By.XPATH, f"//{self.locationSearchTag}[contains(text(),'{value}')]").click()
            self.clickOk = True
        except self.excecao:
            pass
            

    def keys(self, xpath, writeSec):
        while True:
            try:
                self.driver.find_element(By.XPATH, xpath).clear()
                self.driver.find_element(By.XPATH, xpath).send_keys(writeSec)
                break
            except self.excecao:
                sleep(1)

    def scroll(self, xpath, vertical):
        while True:
            try:
                iframe = self.driver.find_element(By.XPATH, xpath)
                # ActionChains(self.driver).scroll_to_element(iframe).perform()
                scroll_origin = ScrollOrigin.from_element(iframe)
                ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, int(vertical)).perform()
                break
            except self.excecao as e:
                sleep(1)


class ButtonsSpecial:
    def __init__(self, lastMonth, func, xpath) -> None:
        self.lastMonth = lastMonth
        self.func = func
        self.xpath = xpath

    def clickLeftArrow(self):
        if self.lastMonth != 0:
            for clickNumberSameButton in range(self.lastMonth):  # quantidade de vezes que tem que reotrnar
                clickOk = self.func.click(self.xpath)
        else:
            clickOk = True  # ultimo mes nao precisa click
        return clickOk
    
    def clickDayStartMonth(self):
        line = 1
        column = 7
        while True:
            self.xpath = f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{line}]/td[{column}]'
            clickOk = self.func.click(self.xpath) 
            column -= 1 
            if column == 0:
                break  
        sleep(3)
        return clickOk
    
    def clickDayEndMonth(self):
        if self.lastMonth != 0:
            line = 4
            column = 7
            while True:
                self.xpath = f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{line}]/td[{column}]'
                clickOk = self.func.click(self.xpath) 
                column += 1
                if (column == 3 and line == 6) or click is False:
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