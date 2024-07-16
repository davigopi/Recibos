from time import sleep
from selenium.webdriver.common.by import By
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


class XpathManip:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = kwargs.get('driver')
        self.excecao = (
            NoSuchElementException,
            ElementNotInteractableException,
            ElementClickInterceptedException,
            StaleElementReferenceException,
            InvalidArgumentException,
            InvalidSelectorException,
            TimeoutException
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
                self.driver.find_element(  # type:ignore
                    By.XPATH, xpath).location_once_scrolled_into_view
                self.xpathOk = True
                break
            except self.excecao:
                if count >= 5:
                    self.xpathOk = False
                    break
                count += 1
                sleep(1)
                continue
