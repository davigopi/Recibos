# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(311, 391)
        login.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(20, 20, 20);\n"
"	color: rgb(240, 240, 240);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"QPushButton{\n"
" width: 100%;\n"
"  padding: 10px;\n"
"  background-color: rgba(255, 255, 255, 0.8);\n"
"  color: rgb(22, 22, 22);\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  cursor: pointer;\n"
"  box-shadow: 0px -80px 60px rgba(195, 195, 195, 0.9); \n"
"  transform: translate(-3px, -2px);\n"
"  font-size: 1.2em;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgba(255, 255, 255, 0.5);\n"
"  box-shadow: -10px 10px 50px rgba(255, 255, 255, 0.7); \n"
"  color: rgb(245, 245, 245);\n"
"  transform: translate(3px, -3px);\n"
"  font-size: 1.2em;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"  	color: rgb(245, 245, 245);\n"
" }")
        self.horizontalLayout = QHBoxLayout(login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(24, 25, 262, 334))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"img/login1.png"))

        self.verticalLayout.addWidget(self.label)

        self.user = QLineEdit(self.widget)
        self.user.setObjectName(u"user")
        font = QFont()
        font.setPointSize(11)
        self.user.setFont(font)
        self.user.setStyleSheet(u"")
        self.user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.user)

        self.password = QLineEdit(self.widget)
        self.password.setObjectName(u"password")
        self.password.setFont(font)
        self.password.setStyleSheet(u"")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.password)

        self.btnEntrar = QPushButton(self.widget)
        self.btnEntrar.setObjectName(u"btnEntrar")
        self.btnEntrar.setFont(font)
        self.btnEntrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEntrar.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.btnEntrar)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.label.setText("")
        self.user.setPlaceholderText(QCoreApplication.translate("login", u"Digite seu usu\u00e1rio:", None))
        self.password.setPlaceholderText(QCoreApplication.translate("login", u"Digite sua senha:", None))
        self.btnEntrar.setText(QCoreApplication.translate("login", u"Entrar", None))
    # retranslateUi

