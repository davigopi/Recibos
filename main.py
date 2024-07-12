from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget  # noqa
from PySide6.QtGui import QIcon
from login import Ui_login
from main_window import MainWindow
from components.cryptography_utils import Key_encrypt
import sys
import requests
import time


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
        inf = 'P☻rocessando'
        self.lb_user_password.setText(inf)
        username = self.user.text()
        password = self.password.text()
        self.authenticate(username, password)

    def authenticate(self, username, password):
        key_encrypt = Key_encrypt()
        key_encrypt.read_key_file()
        key_encrypt.read_user_crypt_web()
        if password == key_encrypt.password_decrypt(username):
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            inf = 'Usuário e/ou senha inválido'
            time.sleep(3)
            self.lb_user_password.setText(inf)
            self.user.clear()
            self.password.clear()

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
