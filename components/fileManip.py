import pandas as pd
import sys
import os
from time import sleep
from pandas.errors import EmptyDataError
from pathlib import Path


class FileManip:
    def __init__(self) -> None:
        self.arq_cons: Path = Path()
        self.arq_log: Path = Path()
        self._dfNew: pd.DataFrame = pd.DataFrame()
        self.error = ''

    # @property
    # def arqConss(self):
    #     return None

    # @arqConss.setter
    # def arqConss(self, arqCons):
    #     self.arq_cons = arqCons

    @property
    def delete(self):
        while True:
            try:
                os.remove(self.arq_cons)
                break
            except FileNotFoundError:  # caso arq nao exista
                break
            except PermissionError:
                text = f'Você não tem permissão para apagar {self.arq_cons}'
                with open(self.arq_log, 'a') as arq:
                    arq.write(text)
                sys.exit()

    @property
    def readCsv(self):
        count = 0
        time_wait = 20
        text_error = ''
        error = ''
        type_error = ''
        while True:
            count += 1
            try:  # se não carregar é porque não completou download
                self._dfNew = pd.read_csv(
                    self.arq_cons,
                    sep=';',
                    encoding='utf-8',
                    dtype=str
                )  # type: ignore
                return self._dfNew
            except FileNotFoundError as e1:
                error = e1
                type_error = 'FileNotFoundError'
            except PermissionError as e2:
                error = e2
                type_error = 'PermissionError'
                sleep(1)
            except EmptyDataError as e3:
                error = e3
                type_error = 'EmptyDataError'
            except pd.errors.ParserError as e4:
                error = e4
                type_error = 'pd.errors.ParserError'
            if count >= time_wait:
                text_error += f'ERRO: ({type_error})'
                text_error += f'({error}). '
                text_error += f'Tempo pecorrido: {count} seg. '
                text_error += f'arq_cons: ({self.arq_cons}).'
                self.error = text_error
                return False
            sleep(1)

    @property
    def writeCsv(self):
        return self._df

    @writeCsv.setter
    def writeCsv(self, df):
        self._df = df
        self._df.to_csv(self.arq_cons, index=False, header=True)

    @property
    def writeLog(self):
        return None

    @writeLog.setter
    def writeLog(self, text):
        with open(self.arq_log, 'a') as arq:
            arq.write(text)
