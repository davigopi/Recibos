from time import sleep
from bs4 import BeautifulSoup
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    InvalidArgumentException,
    InvalidSelectorException,
    TimeoutException
)
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

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
        self.tagSon = ''
        self.tagFather = ''
        self.tagGet = ''
        self.tagSelected = ''
        self.value = None
        self.timeSleep: float = 0
        self.attempt = 0

    @property
    def xpathXpathTag(self):
        return self.value

    @xpathXpathTag.setter
    def xpathXpathTag(self, xpath):
        count = 0
        while True:
            try:
                count += 1
                self.value = self.driver.find_element(  # type: ignore
                    By.XPATH, self.xpathFather).find_element(
                        By.XPATH, xpath).get_attribute(self.tagGet)
                break
            except excecaoAll:
                if count >= self.attempt:
                    self.value = False
                    break
                sleep(0.2)

    @property
    def xpathXpathTagSelected(self):
        return self.value

    @xpathXpathTagSelected.setter
    def xpathXpathTagSelected(self, xpath):
        count = 0
        xpath += self.tagSelected
        while True:
            try:
                count += 1
                self.value = self.driver.find_element(  # type: ignore
                    By.XPATH, self.xpathFather).find_element(
                        By.XPATH, xpath).text
                break
            except excecaoAll:
                if count >= 3:
                    self.value = False
                    break
                sleep(self.timeSleep)

    @property
    def xpathNameTag(self):
        return self.value

    @xpathNameTag.setter
    def xpathNameTag(self, name):
        count = 0
        while True:
            try:
                count += 1
                self.value = self.driver.find_element(  # type: ignore
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
                self.value = self.driver.find_element(By.XPATH, xpath).text  # type: ignore # noqa
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
                self.value = self.driver.find_element(  # type: ignore
                    By.XPATH, xpath).get_attribute(
                        self.tagGet)  # retornar o outerHTML
                # pip install lxml
                self.value = BeautifulSoup(
                    self.value, "lxml").find(
                        self.tagFather).findAll(  # type: ignore
                            self.tagSon)  # formatar outerHTMl
                listValue = []
                for key in range(1, len(self.value), 1):
                    listValue.append(
                        self.value[key].find(
                            text=True))  # pega cada valro
                self.value = listValue
                break
            except (AttributeError, Exception):
                sleep(0.2)

    @property
    def xpath_to_tags(self):
        return self.value

    @xpath_to_tags.setter
    def xpath_to_tags(self, xpath):
        count = 0
        while True:
            count += 1
            try:
                # return all tags
                self.value = self.driver.find_element(  # type: ignore
                    By.XPATH, xpath).get_attribute(self.tagGet)
                # Erro (FeatureNotFound) if not install: pip install lxml
                # test loading table
                BeautifulSoup(self.value, "lxml").find(
                    self.tagFather).findAll(self.tagSon)  # type: ignore
                break
            except (AttributeError, Exception):
                if count >= 5:
                    self.value = False
                    break
                sleep(0.2)
