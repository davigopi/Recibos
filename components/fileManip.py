import pandas as pd
import os
from time import sleep
from pandas.errors import EmptyDataError


class FileManip:
    def __init__(self) -> None:
        self._arqCons: str = ''
        self._dfNew: pd.DataFrame = pd.DataFrame()

    @property
    def arqConss(self):
        return None

    @arqConss.setter
    def arqConss(self, arqCons):
        self._arqCons = arqCons

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
        count = 0
        while True:
            count += 1
            time = 'Tempo pecorrido: ' + str(count) + ' seg.'
            if count >= 10:
                return False
            try:  # se não carregar é porque não completou download
                self._dfNew = pd.read_csv(
                    self._arqCons,
                    sep=';',
                    encoding='utf-8',
                    dtype=str
                    )  # type: ignore
                return self._dfNew
            except FileNotFoundError as e1:
                print(f'ERRO FileNotFoundError arq não existe: {e1}. {time}')
                pass
            except PermissionError as e2:
                print(f'ERRO PermissionError permissoa no local: {e2}. {time}')
                sleep(1)
            except EmptyDataError as e3:
                print(f'ERRO EmptyDataError do arquivo: {e3}. {time}')
                pass
            sleep(1)

    @property
    def writeCsv(self):
        return self._df

    @writeCsv.setter
    def writeCsv(self, df):
        self._df = df
        self._df.to_csv(self._arqCons, index=False, header=True)
