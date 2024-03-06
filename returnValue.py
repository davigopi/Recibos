from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import (
    NoSuchElementException, 
    ElementNotInteractableException, 
    ElementClickInterceptedException,
    StaleElementReferenceException, 
    InvalidArgumentException, 
    InvalidSelectorException, 
    TimeoutException
    )
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

excecaoAll = (
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    InvalidArgumentException,
    InvalidSelectorException,
    TimeoutException
    )
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
    def xpathXpathTag(self):
        return self.value
    
    @xpathXpathTag.setter
    def xpathXpathTag(self, xpath):
        count = 0
        while True:
            try:
                count += 1
                self.value = self.driver.find_element(
                    By.XPATH, self.xpathFather).find_element(
                        By.XPATH, xpath).get_attribute(self.tagGet)
                break
            except excecaoAll:
                if count >= 3:
                    self.value = False
                    break
                sleep(0.2)

    @property
    def xpathNameTag(self):
        return self.value
    
    @xpathNameTag.setter
    def xpathNameTag(self, name):
        count = 0
        while True:
            try:
                count += 1
                self.value = self.driver.find_element(
                    By.XPATH, self.xpathFather).find_element(
                        By.NAME, name).get_attribute(self.tagGet)
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
    def xpathTag(self):
        return self.value
    
    @xpathTag.setter
    def xpathTag(self, xpath):
        while True:
            try: 
                self.value = self.driver.find_element(
                    By.XPATH, xpath).get_attribute(
                        self.tagGet)  # retornar o outerHTML
                # pip install lxml
                self.value = BeautifulSoup(
                    self.value, "lxml").find(
                        self.tagFather).findAll(
                            self.tagSon)  # formatar outerHTMl
                listValue = []
                for key in range(1, len(self.value), 1):
                    listValue.append(
                        self.value[key].find(
                            text=True))  # pega cada valro 
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
