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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(305, 436)
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
" }\n"
"\n"
"QLineEdit{\n"
"	color: rgb(255,102, 0);\n"
"}")
        self.horizontalLayout = QHBoxLayout(login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(8, 7, 271, 401))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"img/login1.png"))

        self.verticalLayout.addWidget(self.label)

        self.user = QLineEdit(self.layoutWidget)
        self.user.setObjectName(u"user")
        font = QFont()
        font.setPointSize(11)
        self.user.setFont(font)
        self.user.setStyleSheet(u"")
        self.user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.user)

        self.password = QLineEdit(self.layoutWidget)
        self.password.setObjectName(u"password")
        self.password.setFont(font)
        self.password.setStyleSheet(u"")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.password)

        self.btnEntrar = QPushButton(self.layoutWidget)
        self.btnEntrar.setObjectName(u"btnEntrar")
        self.btnEntrar.setFont(font)
        self.btnEntrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEntrar.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.btnEntrar)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lb_user_password = QLabel(self.layoutWidget)
        self.lb_user_password.setObjectName(u"lb_user_password")
        font1 = QFont()
        font1.setFamilies([u"Gabriola"])
        font1.setPointSize(18)
        self.lb_user_password.setFont(font1)
        self.lb_user_password.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lb_user_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_user_password)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 30)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 10)
        self.verticalLayout.setStretch(4, 10)
        self.verticalLayout.setStretch(5, 5)
        self.verticalLayout.setStretch(6, 10)

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
        self.lb_user_password.setText("")
    # retranslateUi

