# # Para executar o if __name__ == '__main__':
# from IPython.display import display
import pandas as pd
from bs4 import BeautifulSoup  # Analisar documentos HTML e XML
import urllib.request  # importar a biblioteca que usamos para abrir URLs
import re
# import unicodedata
import sys
# from tratar import Tratar
# from renomear import Renomear
# from Select.DISAL import renomear
# from time import sleep


class Tags_to_table:
    def __init__(self, *args, **kwargs):
        self.html = None
        self.url = None
        self.num_column = 0
        self.num_row = 0
        self.celula = None
        self.inf = None
        self.table_new = None
        self.numberCab = 0
        self.count = 0
        self.tag_table = None
        self.tag_row = None
        self.tag_data = None
        self.tag_cab = None
        self.df_inf = False
        self.erro = ''
        self.last_num_index = None

    @property
    def tag_tables(self):
        return None

    @tag_tables.setter
    def tag_tables(self, tag_table):
        self.tag_table = tag_table

    @property
    def tag_rows(self):
        return None

    @tag_rows.setter
    def tag_rows(self, tag_row):
        self.tag_row = tag_row

    @property
    def tag_datas(self):
        return None

    @tag_datas.setter
    def tag_datas(self, tag_data):
        self.tag_data = tag_data

    @property
    def tag_cabs(self):
        return None

    @tag_cabs.setter
    def tag_cabs(self, tag_cab):
        self.tag_cab = tag_cab

    @property
    def htmls(self):
        return None

    @htmls.setter
    def htmls(self, html):
        self.html = html

    @property
    def urls(self):
        return None

    @urls.setter
    def urls(self, url):
        self.url = url

    @property
    def last_num_indexs(self):
        return None

    @last_num_indexs.setter
    def last_num_indexs(self, last_num_index):
        self.last_num_index = last_num_index

    def tabela(self):
        # add inf list
        # def informacaoCelula(*args, **kwargs):

        # Criar um dicionário vazio para armazenar as listas
        az = {}
        # Adicionar listas ao dicionário usando letras do alfabeto como chaves
        for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            az[letra] = []
        # Adicionar uma lista adicional para 'lista'
        az['lista'] = []

        # Obter uma lista de todas as chaves no dicionário
        keys = list(az.keys())

        try:
            # define html or URL
            if self.html is not None:
                beautifulSoup = BeautifulSoup(self.html, "lxml")
                table_tag = beautifulSoup.find(self.tag_table)
            elif self.url is not None:
                url = urllib.request.urlopen(self.url)
                beautifulSoup = BeautifulSoup(url, "lxml")
                table_tag = beautifulSoup.find('table', class_='wikitable sortable')
            else:
                print(f'TABELASITE ERRO NAO DEFINIDO HTML ({self.html}) OU URL ({self.url})')
                sys.exit()
        except (ValueError, TypeError) as e:
            print(f'TABELA ERRO: ( {e.__class__.__name__} )'
                  f'O HTML ({self.html}) OU URL ({self.url})')
            return

        # numbre column
        if self.tag_cab is not None:
            # all <th>
            for name_column in table_tag.findAll(self.tag_cab):
                self.numberCab += 1

        # all row <tr>    
        for linha in table_tag.findAll(self.tag_row):
            self.num_row += 1
            # find data <td>
            self.celula = linha.findAll(self.tag_data)
            if len(self.celula) == self.numberCab:  # number columns
                self.count = 0
                while True:
                    # informacaoCelula()
                    try:
                        self.inf = self.celula[self.count].find(string=True)
                        az[keys[self.count]].append(self.inf)
                        self.df_inf = True
                    except (IndexError, AttributeError) as e:
                        self.num_column = self.count
                        self.count = 25
                        self.erro = e.__class__.__name__
                    
                    if self.count >= 25:
                        break
                    self.count += 1

        # necessary if index is not zero
        if self.last_num_index is None:
            self.last_num_index = 0
        else:
            self.last_num_index = int(self.last_num_index)
        self.num_row += self.last_num_index
        self.last_num_index += 1
        # add list ordem crecente
        while self.num_row > self.last_num_index:  
            az[keys[self.num_column]].append(self.last_num_index)
            self.last_num_index += 1
        name_column = 'Index'
        # add name column
        self.table_new = pd.DataFrame(index=az[keys[self.num_column]], columns=[name_column])
        # add list column
        self.table_new[name_column] = az[keys[self.num_column]]
        # add name  column table <th>
        for key, name_column in enumerate(table_tag.findAll(self.tag_cab)):
            name_text = name_column.find(string=True)
            name_column = re.sub('\n', '', re.sub('  ', '', name_text))
            try:
                self.table_new[name_column] = az[keys[key]]
            except ValueError as e:
                self.erro = e.__class__.__name__
        return self.table_new

if __name__ == '__main__':
    url = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea'
    html = '''
        <table class="aligncenter nitro-offscreen" style="height:89px;"
          border="1" width="195"> 
          <tbody> 
            <tr> 
                <th style="text-align:left;">Nome</th> 
                <th style="text-align:left;">Idade</th> 
                <th style="text-align:left;">Profissão</th> 
            </tr> 
            <tr> 
                <td>Albert</td> <td>27</td> <td>Escritor</td> 
            </tr> 
            <tr> 
                <td>Jim</td> <td>57</td> <td>Ator</td> 
            </tr> 
          </tbody> 
        </table>
            '''
    tagTable = 'table'
    tagRow = 'tr'
    tagData = 'td'
    tagCab = 'th'
    last_num_index = 0
    # colunaIndex=2
    tags_to_tab = Tags_to_table()
    tags_to_tab.last_num_indexs = last_num_index
    tags_to_tab.urls = url
    # tags_to_tab.htmls = html
    tags_to_tab.tag_tables = tagTable
    tags_to_tab.tag_rows = tagRow
    tags_to_tab.tag_datas = tagData
    tags_to_tab.tag_cabs = tagCab
    tabela_fim = tags_to_tab.tabela()
    print(tabela_fim)
