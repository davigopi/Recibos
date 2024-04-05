from time import sleep


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