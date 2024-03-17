from urllib.error import URLError
import pandas as pd
from bs4 import BeautifulSoup  # Analisar documentos HTML e XML
import urllib.request  # importar a biblioteca que usamos para abrir URLs


class Tags_to_table:
    def __init__(self):
        self.table_new = None
        self.last_num_index = 0

    @property
    def last_num_indexs(self):
        return None

    @last_num_indexs.setter
    def last_num_indexs(self, last_num_index):
        self.last_num_index = last_num_index

    @property
    def tables(self):
        return self.table_new

    @tables.setter
    def tables(self, url_html):
        # recognize if it is html or url
        try:
            url = urllib.request.urlopen(url_html)
            bs = BeautifulSoup(url, "lxml")
            table_tag = bs.find('table', class_='wikitable sortable')
        except (URLError, ValueError, AttributeError) as e:
            table_tag = None
            try:
                # erro no html
                bs = BeautifulSoup(url_html, "lxml")
                table_tag = bs.find('table')
            except TypeError:
                pass
            if table_tag is None:
                print(f'Erro na URL: {e.__class__.__name__}\n'
                      f'Erro no HTML: Vazio\n'
                      f'Não é HTML nem URL, mas é obrigatório ter')
                return
        az = {}
        for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            az[letra] = []
        az_keys = list(az.keys())
        num_cab = len(table_tag.findAll('th'))  # all <th> numbre column
        num_row = 0
        for linha in table_tag.findAll('tr'):
            num_row += 1
            cell = linha.findAll('td')  # find data <td>
            if len(cell) == num_cab:  # number columns
                key = 0
                while True:
                    try:
                        inf = cell[key].get_text().strip()
                        az[az_keys[key]].append(inf)  # add inf list
                    except (IndexError, AttributeError):
                        num_column = key
                        break
                    if key >= 25:  # limit column num 25 = num letters alphabet
                        break
                    key += 1
        # necessary if index is not zero
        self.last_num_index = int(self.last_num_index)
        num_row += self.last_num_index
        self.last_num_index += 1
        # add list ordem crecente
        while num_row > self.last_num_index:  
            az[az_keys[num_column]].append(self.last_num_index)
            self.last_num_index += 1
        name_column = 'Index'
        self.table_new = pd.DataFrame(
            index=az[az_keys[num_column]], 
            columns=[name_column])  # add name column
        self.table_new[name_column] = az[az_keys[num_column]]  # add list colum
        # add name  column table <th>
        for key, name_column in enumerate(table_tag.findAll('th')):
            name_column = name_column.find(string=True)
            try:
                self.table_new[name_column] = az[az_keys[key]]
            except ValueError:
                pass
        return self.table_new


if __name__ == '__main__':
    url = 'https://pt.wikipedia.org/'
    url += 'wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea'
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
    tags_to_tab = Tags_to_table()
    # tags_to_tab.last_num_indexs = 0
    tags_to_tab.tables = html
    tabela_fim = tags_to_tab.tables
    print(tabela_fim)
    tags_to_tab.tables = url
    tabela_fim = tags_to_tab.tables
    print(tabela_fim)
