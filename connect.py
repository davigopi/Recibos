# "ferramenta de captura"  do windows para pegar imagens
from asyncio.windows_events import NULL
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
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class Connect:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.df = pd.DataFrame()
        self.dfNew = None

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

    def pressXpathRetuneListValue(self, xpath):
        mousekeyboard = MouseKeyboard(driver=self.driver)
        returnValue = ReturnValue(driver=self.driver)
        clickOk = False
        while clickOk is False:
            if clickOk >= 10:
                break
            clickOk = mousekeyboard.clickXpath(xpath)
            returnValue.tagSonValue = 'option'
            returnValue.tagFatherValue = 'select'
            returnValue.tagValue = xpath
            listaValue = returnValue.tagValue
        return listaValue

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
    #                 listaValue = returnValue.tagValue
    #     return listaValue

    def pressListValueXpathRetuneListValueAll(self, xpath, listValue, tagSon, tagFather):
        listValueAll = []
        for value in listValue:
            mousekeyboard = MouseKeyboard(driver=self.driver)
            mousekeyboard.locationSearchTag = tagSon
            while True:
                mousekeyboard.clickValue = value
                clickOk = mousekeyboard.clickValue
                if clickOk is True:
                    break
            while True:
                returnValue = ReturnValue(driver=self.driver)
                clickOk = mousekeyboard.clickXpath(xpath)
                returnValue.tagSonValue = tagSon
                returnValue.tagFatherValue = tagFather
                returnValue.tagValue = xpath
                listValueTemporary = returnValue.tagValue
                listValueAll.append([value, listValueTemporary])
                if clickOk >= 10 or clickOk is True:
                    break
                # sleep(1)
        return listValueAll


    def pressListValueAllXpathRetuneListValueAllDoucle(self, xpath, listValueAll, tagSon, tagFather):
        listValueAllDouble = []
        for listValueAdministradoraTablarecebimento in listValueAll:
            mousekeyboard = MouseKeyboard(driver=self.driver)
            mousekeyboard.locationSearchTag = tagSon
            valueAdministradora = listValueAdministradoraTablarecebimento[0]
            while True:
                mousekeyboard.clickValue = valueAdministradora
                clickOk = mousekeyboard.clickValue
                if clickOk is True:
                    break
            listValue = listValueAdministradoraTablarecebimento[1]
            listValueAll2 = []
            for value in listValue:
                mousekeyboard = MouseKeyboard(driver=self.driver)
                mousekeyboard.locationSearchTag = tagSon
                while True:
                    mousekeyboard.clickValue = value
                    clickOk = mousekeyboard.clickValue
                    if clickOk is True:
                        break
                while True:
                    returnValue = ReturnValue(driver=self.driver)
                    clickOk = mousekeyboard.clickXpath(xpath)
                    returnValue.tagSonValue = tagSon
                    returnValue.tagFatherValue = tagFather
                    returnValue.tagValue = xpath
                    listValueTemporary = returnValue.tagValue
                    listValueAll2.append([value, listValueTemporary])
                    if clickOk >= 10 or clickOk is True:
                        break
                    # sleep(1)
            listValueAllDouble.append([valueAdministradora, listValueAll2])
        return listValueAllDouble
    
    def formatListaLineTable(self, listValueAllDouble):
        listLineTable = []
        index = 0
        for valueAdministradoraTabelaRecebimentoCargo in listValueAllDouble:
            valueAdministrador = valueAdministradoraTabelaRecebimentoCargo[0]
            for valueTabelaRecebimentoCargo in valueAdministradoraTabelaRecebimentoCargo[1]:
                valueTabelaRecebimento = valueTabelaRecebimentoCargo[0]
                for valueCargo in valueTabelaRecebimentoCargo[1]:
                    index += 1
                    listLineTable.append([index, valueAdministrador, valueTabelaRecebimento, valueCargo])
        return listLineTable

    def formatListaColumnTable(self, listLineTable):
        listColumnTable = []
        index = []
        column1 = []
        column2 = []
        column3 = []
        columns = [index, column1, column2, column3]
        for lineTable in listLineTable:
            for key in range(4):
                columns[key].append(lineTable[key])
        listColumnTable.append([index, column1, column2, column3])
        return listColumnTable    
    
    def formatTable(self, listColumnTable):
        for key, column in enumerate(listColumnTable):
            if key == 0:
                table = pd.DataFrame(index=column, columns=['index'])
                table['index'] = column
                continue
            nameColumn = 'column' + str(key)
            table[nameColumn] = column
        return table

    def commissionSirconValue(self, listXpath):
        # func = MouseKeyboard(driver=self.driver) 
        listComission = []
        for key, xpathFather in enumerate(listXpath[0]):
            listComission.append(key+1)
            for xpath in listXpath[1][key]:
                returnValue = ReturnValue(driver=self.driver)
                returnValue.xpathFatherValue = xpathFather
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
        self.value = None
       

    @property
    def xpathValue(self):
        return self.value
    @xpathValue.setter
    def xpathValue(self, xpath):
        while True:
            try:
                self.value = self.driver.find_element(By.XPATH, self.xpathFather).find_element(By.XPATH, xpath).get_attribute('value')
                break
            except NoSuchElementException:
                pass

    @property
    def xpathFatherValue(self):
        return self.xpathFather
    @xpathFatherValue.setter
    def xpathFatherValue(self, xpathFather):
        self.xpathFather = xpathFather

    @property
    def tagValue(self):
        return self.value
    @tagValue.setter
    def tagValue(self, xpath):
        while True:
            try:
                self.value = self.driver.find_element(By.XPATH, xpath).get_attribute('outerHTML')  # retornar o outerHTML
                self.value = BeautifulSoup(self.value, "lxml").find(self.tagFather).findAll(self.tagSon)  # formatar outerHTMl
                listValue = []
                for key in range(1, len(self.value), 1):
                    listValue.append(self.value[key].find(text=True))  # pega cada valro 
                self.value = listValue
                break  
            except (AttributeError, Exception) as e:
                pass

    @property
    def tagSonValue(self):
        return self.tagSon
    @tagSonValue.setter
    def tagSonValue(self, tagSon):
        self.tagSon = tagSon

    @property
    def tagFatherValue(self):
        return self.tagFather
    @tagFatherValue.setter
    def tagFatherValue(self, tagFather):
        self.tagFather = tagFather




class XpathManip:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.excecao = (NoSuchElementException
                        , ElementNotInteractableException
                        , ElementClickInterceptedException
                        , StaleElementReferenceException
                        )

    @property
    def locate(self):
        return True

    @locate.setter
    def locate(self, xpath):
        while True:
            try:   
                self.driver.find_element(By.XPATH, xpath).location_once_scrolled_into_view
                break
            except self.excecao:
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
        try:
            self.driver.find_element(By.XPATH, f"//{self.locationSearchTag}[contains(text(),'{value}')]").click()
            self.clickOk = True
        except self.excecao:
            self.clickOk = False

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