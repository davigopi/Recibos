import pandas as pd
import sys
import os
from time import sleep
from pandas.errors import EmptyDataError
from pathlib import Path
from fpdf import FPDF
import locale

# Configuração do local para formatação da moeda
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class FileManip:
    def __init__(self) -> None:
        self.arq_cons: Path = Path()
        self.arq_log: Path = Path()
        self._dfNew: pd.DataFrame = pd.DataFrame()
        self.error = ''
        self.time_wait = 20

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
        text += '\n'
        with open(self.arq_log, 'a') as arq:
            arq.write(text)

    @property
    def delete(self):
        while True:
            try:
                os.remove(self.arq_cons)
                break
            except FileNotFoundError:  # caso arq nao exista
                break
            except PermissionError:
                text_error = f'Não tem permissão para apagar: {self.arq_cons}.'
                FileManip().writeLog = text_error
                # with open(self.arq_log, 'a') as arq:
                #     arq.write(text)
                sys.exit()

    @property
    def readCsv(self):
        count = 0
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
            if count >= self.time_wait:
                text_error += f'ERRO: ({type_error})'
                text_error += f'({error}). '
                text_error += f'Tempo pecorrido: {count} seg. '
                text_error += f'arq_cons: ({self.arq_cons}).'
                FileManip().writeLog = text_error
                self.error = text_error
                return False
            sleep(1)


class PDF(FPDF):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)  # Chama o construtor da classe base FPDF
        self.title = ''
        self.text_size_head = 0
        self.text_size_footer = 0
        self.text_size_table = 0
        self.cell_height = 0
        self.space_columns = 0

    def header(self):
        self.set_font('Arial', 'B', self.text_size_head)
        self.cell(0, 10, self.title, 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', self.text_size_footer)
        self.cell(0, 2, f'Página {self.page_no()}', 0, 0, 'C')

    def add_table(self, dataframe):
        # Define a largura e altura das células
        col_widths = [self.get_string_width(str(col)) +
                      self.space_columns for col in dataframe.columns]
        # Define a fonte a ser usada para desenhar o texto na tabela
        self.set_font('Arial', '', self.text_size_table)
        # Itera sobre cada linha no DataFrame
        for row in dataframe.itertuples(index=False):
            # Itera sobre cada elemento (ou célula) em uma linha
            for i, cell in enumerate(row):
                # Calcula a largura da célula atual
                cell_width = self.get_string_width(str(cell)) + self.space_columns
                # Verifica se a largura da célula atual é maior do que a
                # largura atualmente armazenada para a coluna correspondente
                if cell_width > col_widths[i]:
                    col_widths[i] = cell_width
        # Adiciona o cabeçalho
        self.set_font('Arial', 'B', self.text_size_table)
        for i, col in enumerate(dataframe.columns):
            self.cell(col_widths[i], self.cell_height, str(col), border=1, align='C')
        self.ln(self.cell_height)

        # Adiciona as células da tabela
        self.set_font('Arial', '', self.text_size_table)
        for row in dataframe.itertuples(index=False):
            for i, cell in enumerate(row):
                self.cell(col_widths[i], self.cell_height, str(cell), border=1, align='C')
            self.ln(self.cell_height)

    def add_image(self, image_path, x, y, w, h):
        # Add an image to the PDF
        self.image(image_path, x, y, w, h)

    def add_underlined_text(self, text, size_font, size_line):
        self.set_font('Arial', '', size_font)

        # Guarda a posição inicial do texto
        initial_x = self.get_x()
        initial_y = self.get_y()
        # print(f'initial_x  {initial_x}')
        # print(f'initial_y  {initial_y}')
        cell_width = self.w - initial_x

        # Adiciona o texto em uma nova célula
        self.cell(0, size_line, text, ln=True)

        # Desenha a linha abaixo do texto
        final_x = self.get_x() + cell_width / 3
        final_y = self.get_y()
        self.line(initial_x, final_y, final_x, final_y)

    def add_content_in_columns(self, content_list, num_columns, size_font, size_line):
        self.set_font('Arial', '', size_font)
        page_width = self.w - 2 * self.l_margin  # Largura da página sem margens
        column_width = page_width / num_columns  # Largura de cada coluna

        # Calcula a posição inicial da coluna
        initial_y = self.get_y()

        for i, content in enumerate(content_list):
            column = i % num_columns
            row = i // num_columns

            x = self.l_margin + column * column_width
            y = initial_y + (row * size_line)

            self.set_xy(x, y)
            self.multi_cell(column_width, size_line, content, border=0)

        # # Move the cursor to the bottom of the last row of the columns
        # pdf.set_y(initial_y + ((len(content_list) // num_columns) + 1) * size_line)
            # Calcula a nova posição y
            current_y = self.get_y()
            if column == num_columns - 1:
                max_y = current_y

        # Ajusta o cursor para a posição correta após adicionar todo o conteúdo
        self.set_y(max_y)

    def add_text_to_bottom(self, text, size_font, size_line):
        self.set_font('Arial', '', size_font)
        # Define a posição y para o final da página menos a altura da linha
        y_position = self.h - self.b_margin - size_line
        self.set_y(y_position)
        self.cell(0, size_line, text, ln=True)

    def add_text_to_end_of_line(self, text, size_font, size_line):
        self.set_font('Arial', '', size_font)
        # Guarda a posição y atual
        current_y = self.get_y()
        # Define a posição x para a margem direita menos a largura do texto e a margem direita
        x_position = self.w - 2 * self.r_margin - self.get_string_width(text)
        # Define a posição y para garantir que o texto seja adicionado na linha atual
        self.set_xy(x_position, current_y)
        # Adiciona o texto
        self.cell(0, size_line, text, ln=False)
