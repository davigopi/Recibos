from datetime import date
from dateutil.relativedelta import relativedelta
from typing import List


class DateMonthYear:
    def __init__(self, *args, **kwargs) -> None:
        self._list: List = []

    @property
    def listMonthYear(self) -> List:
        return self._list

    @listMonthYear.setter
    def listMonthYear(self, nMonths) -> None:
        today = date.today()
        listAll = []
        for month in range(nMonths):
            dateMonthYearEdited = (today - relativedelta(months=month))
            dateMonthEdited = int(dateMonthYearEdited.strftime('%m'))
            dateYearEdited = int(dateMonthYearEdited.strftime('%Y'))
            listAll.append([dateMonthEdited, dateYearEdited])
        listAll.reverse()
        listMonth = []
        listYear = []
        yearDifferent = 0
        for m, y in listAll:
            if yearDifferent != y:
                yearDifferent = y
                listYear.append(yearDifferent)
            listMonth.append(m)
        self._list = [listYear, listMonth]


if __name__ == '__main__':
    dateMonthYear = DateMonthYear()
    dateMonthYear.listMonthYear = 7
    teste = dateMonthYear.listMonthYear
    print(teste)
