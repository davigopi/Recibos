from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)  # Chama construtor class base FPDF
        self.title = ''

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, self.title, 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')


# Cria uma instância da classe PDF
pdf = PDF()
pdf.title = 'Contra Cheque'
pdf.add_page()
pdf.set_font('Arial', '', 12)

text = 'testetet tett tt tt \n'
text += '121212121212121212 \n'
text += '232323232343435434343 \n'
# Adiciona texto ao PDF
pdf.multi_cell(0, 10, text)

# Salva o PDF

pdf.output('arquivo.pdf')
