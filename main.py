# flake8: noqa
# pyright: # type: ignore

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
from PySide6.QtGui import QIcon, QPixmap
from login import Ui_login
from main_window import MainWindow
from components.cryptography_utils import Key_encrypt
import sys
import time
import os


def resource_path(relative_path):
    """Obtem o caminho absoluto para o recurso, trabalhando para dev e
    PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login Select")
        self.adjust_image_paths()

        self.btnEntrar.clicked.connect(self.open_system)

    def adjust_image_paths(self):
        # Ajuste os caminhos das imagens:
        image_path = resource_path('img/icon.png')
        icon = QIcon(image_path)
        self.setWindowIcon(icon),
        image_path = resource_path('img/login1.png')
        self.label.setPixmap(QPixmap(image_path))

    # def keyPressEvent(self, event):
    #     # if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
    #     if event.key() in [16777220, 16777221]:
    #         self.open_system()

    def open_system(self):
        inf = 'Processando'
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
            self.btnEntrar.setDisabled(True)
            time.sleep(5)
            inf = 'Usuário e/ou senha inválido'
            self.lb_user_password.setText(inf)
            self.user.clear()
            self.password.clear()
            self.btnEntrar.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
