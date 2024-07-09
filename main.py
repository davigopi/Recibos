from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget  # noqa
from PySide6.QtGui import QIcon
from login import Ui_login
from main_window import MainWindow
import sys
import requests


class Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login Select")

        # Carregar o ícone e definir para a janela
        icon = QIcon('img/icon.png')
        self.setWindowIcon(icon)

        self.btnEntrar.clicked.connect(self.open_system)

    def open_system(self):
        username = self.user.text()
        password = self.password.text()
        if password == '123':
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print('senha inválida')

        self.authenticate(username, password)

    def authenticate(self, username, password):
        print(username)
        print(password)
        url = 'URL_DO_SEU_ARQUIVO_DE_AUTENTICACAO'
        response = requests.get(url)

        if response.status_code == 200:
            auth_data = response.json()  # Assumindo que o arquivo na web é um JSON com usuários e senhas

            if username in auth_data and auth_data[username] == password:
                return True

        return False


# class MainWindow_login(QMainWindow, MainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)
#         self.setWindowTitle("Sistema de gerenciamaneto")

#         # # Criar um QStackedWidget para gerenciar as páginas
#         # self.stacked_widget = QStackedWidget()
#         # self.setCentralWidget(self.stacked_widget)

#         # # Adicionar as páginas ao QStackedWidget
#         # self.stacked_widget.addWidget(self.pg_home)
#         # self.stacked_widget.addWidget(self.pg_table)
#         # self.stacked_widget.addWidget(self.pg_contato)
#         # self.stacked_widget.addWidget(self.pg_sobre)
#         # self.stacked_widget.addWidget(self.pg_cadastro)

#         # paguinaas d osistema
#         self.btn_home.clicked.connect(
#             lambda: self.pages.setCurrentWidget(self.pg_home))
#         self.btn_tables.clicked.connect(
#             lambda: self.pages.setCurrentWidget(self.pg_table))
#         self.btn_contato.clicked.connect(
#             lambda: self.pages.setCurrentWidget(self.pg_contato))
#         self.btn_sobre.clicked.connect(
#             lambda: self.pages.setCurrentWidget(self.pg_sobre))
#         self.btn_cadastro.clicked.connect(
#             lambda: self.pages.setCurrentWidget(self.pg_cadastro))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
