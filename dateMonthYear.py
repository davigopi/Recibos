from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class DateMonthYear:
    def __init__(self, *args, **kwargs) -> None:
        self.list = None
    
    @property
    def listMonthYear(self):
        return self.list

    @listMonthYear.setter 
    def listMonthYear(self, nMonths):
        today = date.today()
        listAll = []
        for month in range(nMonths):
            dateMonthYearEdited = (today - relativedelta(months=month))
            dateMonthEdited = dateMonthYearEdited.strftime('%m')
            dateYearEdited = dateMonthYearEdited.strftime('%Y')
            listAll.append([dateMonthEdited, dateYearEdited])
        listAll.reverse()
        listMonth = []
        listYear = []
        yearDifferent = ''
        for m, y in listAll:
            if yearDifferent != y:
                yearDifferent = y
                listYear.append(yearDifferent)
            listMonth.append(m)
        listAll = [listYear, listMonth]
        self.list = listAll


if __name__  == '__main__':
    dateMonthYear = DateMonthYear()
    dateMonthYear.listMonthYear = 7
    teste = dateMonthYear.listMonthYear
    print(teste)