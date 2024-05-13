# "ferramenta de captura"  do windows para pegar imagens
# from ast import Break
# from asyncio.windows_events import NULL
# # from cgitb import text
# from contextlib import nullcontext
# from mailbox import NotEmptyError
# from contextlib import contextmanager
# # from msilib.text import tables
# import re
import sys
# from msilib.schema import Property
# import ssl
from time import sleep
# from numpy import NaN
# import pyautogui
# import pandas as pd
# from pandas.errors import EmptyDataError
# import os
# # import random
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException
)
from selenium.common.exceptions import (
    StaleElementReferenceException,
    InvalidArgumentException,
    InvalidSelectorException,
    TimeoutException
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from returnValue import ReturnValue
# from renemaText import RenameText
# from dateMonthYear import DateMonthYear

excecaoAll = (
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    InvalidArgumentException,
    InvalidSelectorException,
    TimeoutException
)


class MouseKeyboard:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        # self.xpath = kwargs.get('xpath')
        self.excecao = (NoSuchElementException,
                        ElementNotInteractableException,
                        ElementClickInterceptedException,
                        StaleElementReferenceException,
                        InvalidArgumentException,
                        TimeoutException
                        )
        self.clickOk = None
        self.locationSearch = '*'
        self.writeSec = None
        self.info = ''
        self.numberTimesRepeated = 0

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
        # return self.clickOk
        return None

    @clickXpath.setter
    def clickXpath(self, xpath):
        wait = WebDriverWait(self.driver, 1)
        numberTimesRepeated = 0
        info = ''
        self.info = ''
        while True:
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                element = self.driver.find_element(By.XPATH, xpath)
                element.click()
                numberTimesRepeated = 0
                self.clickOk = True
                info = f'Sucesso click xpath: {xpath}'
                self.info = info
                break
            except self.excecao:
                numberTimesRepeated += 1
                if numberTimesRepeated >= 3:
                    if numberTimesRepeated >= 8:
                        self.clickOk = False
                        info += 'Erro, mais de'
                        info += f' {numberTimesRepeated} tentativas, '
                        info += f'em click no xpath: ({xpath}).'
                        self.info = info
                        break
                        # sys.exit()
                    else:
                        sleep(1)
                        break

    @property
    def clickValue(self):
        return None

    @clickValue.setter
    def clickValue(self, text):
        numberTimesRepeated = 0
        info = ''
        while True:
            try:
                self.driver.find_element(
                    By.XPATH, f"//{self.locationSearchTag}[contains(text(),'{text}')]").click()
                sleep(0.5)
                break
            except self.excecao:
                numberTimesRepeated += 1
                if numberTimesRepeated >= 4:
                    if numberTimesRepeated >= 10:
                        info += 'Erro, mais de'
                        info += f' {numberTimesRepeated} tentativas, '
                        info += f'em click no xpath: ({xpath}).'
                        self.info = info
                        print(info)
                        sys.exit()
                    else:
                        sleep(1)

    @property
    def keys(self):
        return self.clickOk

    @keys.setter
    def keys(self, xpath):
        self.info = ''
        while True:
            try:
                self.driver.find_element(By.XPATH, xpath).clear()
                self.driver.find_element(By.XPATH, xpath).send_keys(self.writeSec)
                self.clickOk = True
                break
            except self.excecao:
                sleep(0.2)
                numberTimesRepeated += 1
                if numberTimesRepeated >= 4:
                    if numberTimesRepeated >= 10:
                        print(f'Erro, mais de dez tentativas, em click do xpath {xpath}')
                        sys.exit()
                    else:
                        sleep(1)
                        self.clickOk = False
                        break
