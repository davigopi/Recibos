from fpdf import FPDF

# Cria uma classe para o PDF


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Contra Cheque', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')


# Cria uma instância da classe PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Adiciona texto ao PDF
pdf.multi_cell(0, 10, "Este é um exemplo de texto que será adicionado ao PDF.")

# Salva o PDF
pdf.output('arquivo.pdf')
