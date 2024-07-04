from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QStackedWidget
from PySide6.QtCore import QDate, QObject, QThread, Signal
# from distutils.log import Log
from ui_main import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamaneto")

        # Inicializar QDateEdit com a data atual
        self.data_inicial.setDate(QDate.currentDate())

        # Adiciona itens ao QComboBox
        self.cbb_funcionario.addItems(
            ["Funcionário 1", "funcionário 2", "Funcionário 3"]
        )

        # paguinaas d osistema
        self.btn_home.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_table))
        self.btn_recibo.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_recibo))

        self.btn_carregar.clicked.connect(self.carregar_btn)

        self.btn_gerar.clicked.connect(self.gerar_btn)

    def carregar_btn(self):
        # Obter o texto
        user = self.le_usuario.text()
        print(user)

        # Obter o texto
        password = self.le_senha.text()
        print(password)

        # Obter a data do QDateEdit
        date = self.data_inicial.date()
        date_str = date.toString('MM/yyyy')
        print(date_str)

        # Verificar se o QCheckBox está marcado
        if self.cb_cadastro_consorciado.isChecked():
            print("O cb_cadastro_consorciado está marcado.")
        else:
            print("O cb_cadastro_consorciado não está marcado.")

        if self.cb_cadastro_funcionaio.isChecked():
            print("O cb_cadastro_funcionaio está marcado.")
        else:
            print("O cb_cadastro_funcionaio não está marcado.")

        if self.cb_cadastro_ata.isChecked():
            print("O cb_cadastro_ata está marcado.")
        else:
            print("O cb_cadastro_ata não está marcado.")

        if self.cb_comissoes_configuracao.isChecked():
            print("O cb_comissoes_configuracao está marcado.")
        else:
            print("O cb_comissoes_configuracao não está marcado.")

        if self.cb_comissoes_configPagamento.isChecked():
            print("O cb_comissoes_configPagamento está marcado.")
        else:
            print("O cb_comissoes_configPagamento, não está marcado.")

    def gerar_btn(self):
        # Verificar se o QCheckBox está marcado
        if self.cb_todos.isChecked():
            print("O cb_todos está marcado.")
        else:
            print("O cb_todos, não está marcado.")

        if self.cb_funcionario.isChecked():
            print("O cb_funcionario está marcado.")
        else:
            print("O cb_funcionario, não está marcado.")

        if self.cb_vendedor.isChecked():
            print("O cb_vendedor está marcado.")
        else:
            print("O cb_vendedor, não está marcado.")

        if self.cb_supervisor.isChecked():
            print("O cb_supervisor está marcado.")
        else:
            print("O cb_supervisor, não está marcado.")

        # Obtém o texto do item selecionado no QComboBox e define no QLabel
        selected_text = self.cbb_funcionario.currentText()
        print(f"Selecionado: {selected_text}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
