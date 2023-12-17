# "ferramenta de captura"  do windows para pegar imagens
from asyncio.windows_events import NULL
from contextlib import nullcontext
import re
# from msilib.schema import Property
# import ssl
from time import sleep
import pyautogui
import pandas as pd
from pandas.errors import EmptyDataError
import os
# import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
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
                click = False
                while click is False:
                    click = func.click(xpath)
                    # sleep(0.5)

    def dfSircon(self, arqCons, months, listXpath):  
        file = FileManip(arqCons)
        for lastMonth in range(months, -1, -1):
            file.delete
            fileNotExist = True
            func = MouseKeyboard(driver=self.driver)  
            # beginMonth = False 
            for key, xpath in enumerate(listXpath):
                butt = ButtonsSpecial(lastMonth=lastMonth, func=func, xpath=xpath) 
                click = False
                while click is False:
                    if key == 3 or key == 7:
                        click = butt.clickLeftArrow()
                    elif key == 4:
                        click = butt.clickDayStartMonth()
                    elif key == 8:
                        click = butt.clickDayEndMonth()
                    else:
                        # func.locate(xpath)
                        click = func.click(xpath)
                        if click >= 10:
                            click = True
                            fileNotExist = False
                        print(click)
            if fileNotExist is True:
                self.df = file.readCsv
                table = TableManip(self.dfNew, self.df)
                self.dfNew = table.merge
            print(self.dfNew)
        file.delete
        file.writeCsv = self.dfNew

    def commissionSircon(self, listXpath):
        func = MouseKeyboard(driver=self.driver)  
        for key, xpath in enumerate(listXpath):
            click = False
            while click is False:
                if click >= 10:
                    break
                print(click)
                click = func.click(xpath)
                # sleep(0.5)

    def commissionSirconValue(self, listXpath):
        # func = MouseKeyboard(driver=self.driver) 
        for xpathFather in listXpath[0]:
            print(xpathFather)
            for xpathSon in listXpath[1]:
                print(xpathSon)
                valueRetorno = ValueRetorno(driver=self.driver)
                print('entrar no father')
                valueRetorno.xpathFatherValue = xpathFather
                print('entrar no son')
                valueRetorno.xpathSonValue = xpathSon
                value = valueRetorno.xpathValue
                print(f'##################### {value} #####################')


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
                print('Arquivo nao exite')
                break
            except PermissionError:
                print(f'Fechar o arquivo: {self._arqCons}')
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
                print(f'O arquivo: {self._arqCons} sendo criado! Erro de permissão: {e}')
                sleep(1)
            except EmptyDataError:
                print('Arquivo nao foi excluido e gerado corretamente')

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
    def click(self):
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


class ValueRetorno:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.xpathFather = None
        self.xpathSon = None
        self.value = None

    @property
    def xpathValue(self):
        return self.value
        
    @xpathValue.setter
    def xpathValue(self, xpathFather, xpathSon):
        print(f'############ xpathFather: {xpathFather} #####  xpathSon: {xpathSon} ##########')
        self.value = self.xpathSon.get_attribute('value')
        print(self.value)
    
    @property
    def xpathFatherValue(self):
        return self.xpathFather
    
    @xpathFatherValue.setter
    def xpathFatherValue(self, xpathFather):
        print(f'########111 xpathFather: ({xpathFather})')
        self.xpathFather = self.driver.find_element(By.XPATH, xpathFather)
        print(f' 1##########11111111111 self.xpathFather: ({self.xpathFather})  #################')
        sleep(5)

    @property
    def xpathSonValue(self):
        return self.xpathSon
    
    @xpathSonValue.setter
    def xpathSonValue(self, xpathSon):
        print(f' 2##########2222 self.xpathFather: ({self.xpathFather})   #################')
        sleep(5)
        self.xpathSon = self.xpathFather.find_element(By.XPATH, xpathSon)

        



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
        # self.exitInfiniteLoop = 0

    def click(self, xpath):   
        while True:
            try:
                print(f'Clicar no xpath: {xpath}    self.numberTimesRepeated: {self.numberTimesRepeated}')
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

    def keys(self, xpath, writeSec):
        while True:
            try:
                self.driver.find_element(By.XPATH, xpath).send_keys(writeSec)
                break
            except self.excecao:
                sleep(1)

    def locate(self, xpath):
        while True:
            try:   
                self.driver.find_element(By.XPATH, xpath).location_once_scrolled_into_view
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
                print(f'Erro: {e}')
                sleep(1)


class ButtonsSpecial:
    def __init__(self, lastMonth, func, xpath) -> None:
        self.lastMonth = lastMonth
        self.func = func
        self.xpath = xpath

    def clickLeftArrow(self):
        if self.lastMonth != 0:
            for clickNumberSameButton in range(self.lastMonth):  # quantidade de vezes que tem que reotrnar
                click = self.func.click(self.xpath)
        else:
            click = True  # ultimo mes nao precisa click
        return click
    
    def clickDayStartMonth(self):
        line = 1
        column = 7
        while True:
            self.xpath = f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{line}]/td[{column}]'
            click = self.func.click(self.xpath) 
            column -= 1 
            if column == 0:
                break  
        sleep(3)
        return click
    
    def clickDayEndMonth(self):
        if self.lastMonth != 0:
            line = 4
            column = 7
            while True:
                self.xpath = f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{line}]/td[{column}]'
                click = self.func.click(self.xpath) 
                column += 1
                if (column == 3 and line == 6) or click is False:
                    click = True
                    break
                if column == 8:
                    line += 1
                    column = 1  
        else:
            click = True
        sleep(3)
        return click
    

if __name__ == '__main__':
    import main