from urllib.error import URLError
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import re

class Tags_to_table:
    def __init__(self):
        self.table_new = None

    @property
    def tables(self):
        return self.table_new

    @tables.setter
    def tables(self, url_html):
        try:
            url = urllib.request.urlopen(url_html)
            bs = BeautifulSoup(url, "html.parser")
            table_tag = bs.find('table', id='lista')  # Encontrar a tabela pelo ID
        except (URLError, ValueError, AttributeError) as e:
            table_tag = None
            try:
                bs = BeautifulSoup(url_html, "html.parser")
                table_tag = bs.find('table', id='lista')  # Encontrar a tabela pelo ID
            except TypeError:
                pass
            if table_tag is None:
                print(f'Erro na URL: {e.__class__.__name__}\n'
                      f'Erro no HTML: Vazio\n'
                      f'Não é HTML nem URL, mas é obrigatório ter')
                return

        data = []
        for row in table_tag.find_all('tr'):
            cells = row.find_all('td')  # Selecionar todas as células da linha
            if len(cells) == 3:  # Verificar se há 3 células em cada linha
                mes = cells[0].get_text().strip()
                periodo = cells[1].get_text().strip()
                periodo = periodo.replace('\n', '').replace('\t', '').replace('  ', '')
                data.append((mes, periodo))
        self.table_new = pd.DataFrame(data, columns=['Mês', 'Período'])
        return self.table_new

if __name__ == '__main__':
    url_html = '''
<table cellpadding="0" cellspacing="0" border="0" class="table table-striped table-bordered bootstrap-datatable" id="lista">
				                      <thead>
				                          <tr>
				                              <th class="center">Mês</th>
				                              <th class="center">Período</th>
				                              	<th class="center">Ações</th>
				                          </tr>
				                      </thead>
				                      <tbody>
					                        <tr>
					                        	<td class="center">JANEIRO
					                        	</td>
					                        	<td class="center">20/12/2023
												    <b> à </b>19/01/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:0:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:0:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">FEVEREIRO
					                        	</td>
					                        	<td class="center">20/01/2024
												    <b> à </b>19/02/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:1:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:1:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">MARÇO
					                        	</td>
					                        	<td class="center">20/02/2024
												    <b> à </b>19/03/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:2:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:2:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">ABRIL
					                        	</td>
					                        	<td class="center">20/03/2024
												    <b> à </b>19/04/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:3:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:3:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">MAIO
					                        	</td>
					                        	<td class="center">20/04/2024
												    <b> à </b>19/05/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:4:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:4:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">JUNHO
					                        	</td>
					                        	<td class="center">20/05/2024
												    <b> à </b>19/06/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:5:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:5:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">JULHO
					                        	</td>
					                        	<td class="center">20/06/2024
												    <b> à </b>19/07/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:6:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:6:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">AGOSTO
					                        	</td>
					                        	<td class="center">20/07/2024
												    <b> à </b>19/08/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:7:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:7:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">SETEMBRO
					                        	</td>
					                        	<td class="center">20/08/2024
												    <b> à </b>19/09/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:8:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:8:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">OUTUBRO
					                        	</td>
					                        	<td class="center">20/09/2024
												    <b> à </b>19/10/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:9:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:9:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">NOVEMBRO
					                        	</td>
					                        	<td class="center">20/10/2024
												    <b> à </b>19/11/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:10:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:10:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
					                        <tr>
					                        	<td class="center">DEZEMBRO
					                        	</td>
					                        	<td class="center">20/11/2024
												    <b> à </b>19/12/2024
					                        	</td>
						                        	<td class="center">
						                        		<div class="btn-group"><a id="frm:j_idt115:11:excluirlink" href="#" class="ui-commandlink fa fa-lg" onclick="PrimeFaces.ab({source:'frm:j_idt115:11:excluirlink',update:'frm:cbMes frm:dtInicio frm:dtFim frm:pnlLista'});return false;">
																<i class="ace-icon fa fa-trash-o bigger-120"></i></a>
														</div>
						                        	</td>
					                        </tr>
									  </tbody>
									</table>
'''  # Seu HTML aqui
    url = 'https://pt.wikipedia.org/'
    url += 'wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea'
    tags_to_tab = Tags_to_table()
    tags_to_tab.tables = url_html
    tabela_fim = tags_to_tab.tables
    print(tabela_fim)