# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCalendarWidget, QCheckBox,
    QComboBox, QDateEdit, QDateTimeEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(582, 779)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(80, 0))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(20, 20, 20);\n"
"	color: rgb(255, 255, 255);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"\n"
"QPushButton{\n"
" width: 100%;\n"
"  padding: 10px;\n"
"  background-color: rgba(255, 255, 255, 0.8);\n"
"  color: rgb(22, 22, 22);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  cursor: pointer;\n"
"  box-shadow: 0px -80px 60px rgba(195, 195, 195, 0.9); \n"
"  transform: translate(-3px, -2px);\n"
"  font-size: 1.2em;\n"
"}\n"
"\n"
"QPushButton:hover:enabled {\n"
"  background-color: rgba(255, 255, 255, 0.5);\n"
"  box-shadow: -10px 10px 50px rgba(255, 255, 255, 0.7); \n"
"  color: rgb(245, 245, 245);\n"
"  transform: translate(3px, -3px);\n"
"  font-size: 1.2em;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(40, 40, 40, 0.5);\n"
"    color: rgb(150, 150, 150);\n"
"    cursor: not-allowed; \n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(255,102, 0);\n"
"}\n"
"\n"
"QDateEdit,\n"
"QComboBox {\n"
"    color: rgb(255,102, 0);\n"
""
                        "    background-color: rgba(20, 20, 20, 1);\n"
"    border: 2px solid #ffffff;  \n"
"    border-radius: 5px;\n"
"}\n"
"QTextEdit{\n"
"	color: rgb(255, 255, 0);    \n"
"    background-color: rgba(20, 20, 20, 1);\n"
"    border: 2px solid #ffffff;  \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTextEdit QAbstractItemView,\n"
"QDateEdit QAbstractItemView,\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255,102, 0);\n"
"    background-color: rgb(20, 20, 20);\n"
"    selection-background-color: rgb(00, 255, 33); \n"
"    selection-color: #ffffff; \n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton::indicator ,\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked{\n"
"	background-color: rgb(20, 20, 20);\n"
" }\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(00, 255, 33);\n"
"}\n"
"\n"
"\n"
"/* Estilo para a b"
                        "arra de rolagem vertical */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(20,20, 20, 1);  /* Cor de fundo da barra */\n"
"    width: 14px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(255, 255, 255, 0.2);  /* Cor do manipulador (handle) */\n"
"    min-height: 20px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background:rgba(255, 255, 255, 0.4);  /* Cor do bt rolar para cima */\n"
"    height: 14px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background: rgba(255, 255, 255, 0.4);  /* Cor do bt rolar para baixo */\n"
"    height: 14px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 3px solid black;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: white;\n"
"}\n"
"\n"
"QScrollBar::add-pa"
                        "ge:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btn_tables)

        self.btn_recibo = QPushButton(self.frame)
        self.btn_recibo.setObjectName(u"btn_recibo")
        self.btn_recibo.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btn_recibo)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.pages = QStackedWidget(self.frame)
        self.pages.setObjectName(u"pages")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy1)
        self.pages.setMinimumSize(QSize(30, 0))
        font = QFont()
        font.setFamilies([u"Gabriola"])
        font.setPointSize(18)
        self.pages.setFont(font)
        self.pages.setStyleSheet(u"")
        self.pg_recibo = QWidget()
        self.pg_recibo.setObjectName(u"pg_recibo")
        self.pg_recibo.setFont(font)
        self.verticalLayout_12 = QVBoxLayout(self.pg_recibo)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.pg_recibo)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setPixmap(QPixmap(u"img/select2.png"))
        self.label_9.setScaledContents(False)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.label_14 = QLabel(self.pg_recibo)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Gabriola"])
        font1.setPointSize(22)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_14.setFont(font1)
        self.label_14.setMidLineWidth(1)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_14)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.label_6 = QLabel(self.pg_recibo)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setFamilies([u"Gabriola"])
        font2.setPointSize(16)
        self.label_6.setFont(font2)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.cb_vendedor = QCheckBox(self.pg_recibo)
        self.cb_vendedor.setObjectName(u"cb_vendedor")
        self.cb_vendedor.setFont(font)
        self.cb_vendedor.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_vendedor.setChecked(True)

        self.verticalLayout_7.addWidget(self.cb_vendedor)

        self.cb_supervisor = QCheckBox(self.pg_recibo)
        self.cb_supervisor.setObjectName(u"cb_supervisor")
        self.cb_supervisor.setFont(font)
        self.cb_supervisor.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_supervisor.setChecked(True)

        self.verticalLayout_7.addWidget(self.cb_supervisor)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cb_gerente = QCheckBox(self.pg_recibo)
        self.cb_gerente.setObjectName(u"cb_gerente")
        self.cb_gerente.setFont(font)
        self.cb_gerente.setChecked(True)

        self.verticalLayout_10.addWidget(self.cb_gerente)

        self.cb_parceiro = QCheckBox(self.pg_recibo)
        self.cb_parceiro.setObjectName(u"cb_parceiro")
        self.cb_parceiro.setFont(font)
        self.cb_parceiro.setChecked(True)

        self.verticalLayout_10.addWidget(self.cb_parceiro)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.horizontalLayout_8.setStretch(0, 50)
        self.horizontalLayout_8.setStretch(1, 5)
        self.horizontalLayout_8.setStretch(2, 50)

        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.label_7 = QLabel(self.pg_recibo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_7)

        self.cbb_funcionario = QComboBox(self.pg_recibo)
        self.cbb_funcionario.addItem("")
        self.cbb_funcionario.setObjectName(u"cbb_funcionario")
        self.cbb_funcionario.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cbb_funcionario.sizePolicy().hasHeightForWidth())
        self.cbb_funcionario.setSizePolicy(sizePolicy4)
        self.cbb_funcionario.setFont(font)
        self.cbb_funcionario.setCursor(QCursor(Qt.CursorShape.SplitVCursor))

        self.horizontalLayout_12.addWidget(self.cbb_funcionario)

        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(1, 11)
        self.horizontalLayout_12.setStretch(2, 36)

        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.pg_recibo)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.data_ata = QDateEdit(self.pg_recibo)
        self.data_ata.setObjectName(u"data_ata")
        self.data_ata.setFont(font)
        self.data_ata.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.data_ata.setAccelerated(True)
        self.data_ata.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.data_ata)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 11)
        self.horizontalLayout_6.setStretch(2, 26)

        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.pg_recibo)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_15)

        self.data_semana = QDateEdit(self.pg_recibo)
        self.data_semana.setObjectName(u"data_semana")
        font3 = QFont()
        font3.setFamilies([u"Gabriola"])
        font3.setPointSize(14)
        self.data_semana.setFont(font3)
        self.data_semana.setToolTipDuration(3)
        self.data_semana.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.data_semana.setAccelerated(True)
        self.data_semana.setCalendarPopup(True)

        self.horizontalLayout_11.addWidget(self.data_semana)

        self.horizontalLayout_11.setStretch(0, 11)
        self.horizontalLayout_11.setStretch(1, 11)

        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_gerar = QPushButton(self.pg_recibo)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.btn_gerar.sizePolicy().hasHeightForWidth())
        self.btn_gerar.setSizePolicy(sizePolicy3)
        self.btn_gerar.setMinimumSize(QSize(0, 40))
        self.btn_gerar.setFont(font)
        self.btn_gerar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_gerar)

        self.te_recibo = QTextEdit(self.pg_recibo)
        self.te_recibo.setObjectName(u"te_recibo")
        self.te_recibo.setFont(font3)

        self.verticalLayout_9.addWidget(self.te_recibo)

        self.verticalLayout_9.setStretch(0, 50)

        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.pages.addWidget(self.pg_recibo)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pg_home.sizePolicy().hasHeightForWidth())
        self.pg_home.setSizePolicy(sizePolicy5)
        self.pg_home.setMinimumSize(QSize(0, 0))
        self.pg_home.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Alef"])
        font4.setPointSize(72)
        self.pg_home.setFont(font4)
        self.pg_home.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.pg_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setSizeIncrement(QSize(0, 0))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"img/select.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)

        self.verticalLayout_8.addWidget(self.label)

        self.pages.addWidget(self.pg_home)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.pg_table.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.pg_table)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.pg_table)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(2, 0))
        self.label_11.setPixmap(QPixmap(u"img/select2.png"))
        self.label_11.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_8 = QLabel(self.pg_table)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamilies([u"Gabriola"])
        font5.setPointSize(22)
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.label_23 = QLabel(self.pg_table)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_23)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_24 = QLabel(self.pg_table)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setFont(font)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_24)

        self.le_usuario = QLineEdit(self.pg_table)
        self.le_usuario.setObjectName(u"le_usuario")
        sizePolicy.setHeightForWidth(self.le_usuario.sizePolicy().hasHeightForWidth())
        self.le_usuario.setSizePolicy(sizePolicy)
        self.le_usuario.setFont(font)

        self.horizontalLayout_4.addWidget(self.le_usuario)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.label_25 = QLabel(self.pg_table)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setFont(font)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_25)

        self.le_senha = QLineEdit(self.pg_table)
        self.le_senha.setObjectName(u"le_senha")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.le_senha.sizePolicy().hasHeightForWidth())
        self.le_senha.setSizePolicy(sizePolicy6)
        self.le_senha.setFont(font)
        self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_5.addWidget(self.le_senha)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.pg_table)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)
        self.label_26.setFont(font)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_26)

        self.data_inicial2 = QDateEdit(self.pg_table)
        self.data_inicial2.setObjectName(u"data_inicial2")
        sizePolicy6.setHeightForWidth(self.data_inicial2.sizePolicy().hasHeightForWidth())
        self.data_inicial2.setSizePolicy(sizePolicy6)
        self.data_inicial2.setFont(font)
        self.data_inicial2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.data_inicial2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.data_inicial2.setReadOnly(False)
        self.data_inicial2.setAccelerated(False)
        self.data_inicial2.setDateTime(QDateTime(QDate(2001, 1, 1), QTime(0, 0, 0)))
        self.data_inicial2.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.data_inicial2.setCalendarPopup(True)

        self.horizontalLayout_16.addWidget(self.data_inicial2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.data_inicial = QCalendarWidget(self.pg_table)
        self.data_inicial.setObjectName(u"data_inicial")

        self.verticalLayout_6.addWidget(self.data_inicial)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.pg_table)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.pg_table)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setFamilies([u"Gabriola"])
        font6.setPointSize(18)
        font6.setBold(False)
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.cb_cadastro_consorciado = QCheckBox(self.pg_table)
        self.cb_cadastro_consorciado.setObjectName(u"cb_cadastro_consorciado")
        sizePolicy.setHeightForWidth(self.cb_cadastro_consorciado.sizePolicy().hasHeightForWidth())
        self.cb_cadastro_consorciado.setSizePolicy(sizePolicy)
        self.cb_cadastro_consorciado.setMaximumSize(QSize(16777215, 16777215))
        self.cb_cadastro_consorciado.setFont(font)
        self.cb_cadastro_consorciado.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_cadastro_consorciado.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_cadastro_consorciado.setText(u"Consorciado")
        self.cb_cadastro_consorciado.setIconSize(QSize(16, 16))
        self.cb_cadastro_consorciado.setChecked(True)
        self.cb_cadastro_consorciado.setAutoRepeat(False)
        self.cb_cadastro_consorciado.setAutoExclusive(False)
        self.cb_cadastro_consorciado.setAutoRepeatDelay(300)
        self.cb_cadastro_consorciado.setAutoRepeatInterval(100)

        self.verticalLayout_5.addWidget(self.cb_cadastro_consorciado)

        self.cb_cadastro_funcionaio = QCheckBox(self.pg_table)
        self.cb_cadastro_funcionaio.setObjectName(u"cb_cadastro_funcionaio")
        sizePolicy.setHeightForWidth(self.cb_cadastro_funcionaio.sizePolicy().hasHeightForWidth())
        self.cb_cadastro_funcionaio.setSizePolicy(sizePolicy)
        self.cb_cadastro_funcionaio.setFont(font)
        self.cb_cadastro_funcionaio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_cadastro_funcionaio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_cadastro_funcionaio.setChecked(True)

        self.verticalLayout_5.addWidget(self.cb_cadastro_funcionaio)

        self.cb_cadastro_ata = QCheckBox(self.pg_table)
        self.cb_cadastro_ata.setObjectName(u"cb_cadastro_ata")
        sizePolicy.setHeightForWidth(self.cb_cadastro_ata.sizePolicy().hasHeightForWidth())
        self.cb_cadastro_ata.setSizePolicy(sizePolicy)
        self.cb_cadastro_ata.setFont(font)
        self.cb_cadastro_ata.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_cadastro_ata.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_cadastro_ata.setChecked(True)

        self.verticalLayout_5.addWidget(self.cb_cadastro_ata)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalSpacer = QSpacerItem(13, 125, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_19 = QLabel(self.pg_table)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_19)

        self.cb_comissoes_configuracao = QCheckBox(self.pg_table)
        self.cb_comissoes_configuracao.setObjectName(u"cb_comissoes_configuracao")
        sizePolicy.setHeightForWidth(self.cb_comissoes_configuracao.sizePolicy().hasHeightForWidth())
        self.cb_comissoes_configuracao.setSizePolicy(sizePolicy)
        self.cb_comissoes_configuracao.setFont(font)
        self.cb_comissoes_configuracao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_comissoes_configuracao.setIconSize(QSize(1600, 1600))
        self.cb_comissoes_configuracao.setChecked(True)
        self.cb_comissoes_configuracao.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.cb_comissoes_configuracao)

        self.cb_comissoes_configPagamento = QCheckBox(self.pg_table)
        self.cb_comissoes_configPagamento.setObjectName(u"cb_comissoes_configPagamento")
        sizePolicy.setHeightForWidth(self.cb_comissoes_configPagamento.sizePolicy().hasHeightForWidth())
        self.cb_comissoes_configPagamento.setSizePolicy(sizePolicy)
        self.cb_comissoes_configPagamento.setFont(font)
        self.cb_comissoes_configPagamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_comissoes_configPagamento.setChecked(True)

        self.verticalLayout_3.addWidget(self.cb_comissoes_configPagamento)

        self.label_20 = QLabel(self.pg_table)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_3.addWidget(self.label_20)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(55, 15, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(self.pg_table)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_12 = QLabel(self.pg_table)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.verticalLayout_2.addWidget(self.label_12)

        self.cb_juntar_tabela = QRadioButton(self.pg_table)
        self.cb_juntar_tabela.setObjectName(u"cb_juntar_tabela")
        sizePolicy.setHeightForWidth(self.cb_juntar_tabela.sizePolicy().hasHeightForWidth())
        self.cb_juntar_tabela.setSizePolicy(sizePolicy)
        self.cb_juntar_tabela.setFont(font)
        self.cb_juntar_tabela.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_juntar_tabela.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cb_juntar_tabela.setChecked(True)

        self.verticalLayout_2.addWidget(self.cb_juntar_tabela)

        self.label_10 = QLabel(self.pg_table)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_4 = QLabel(self.pg_table)
        self.label_4.setObjectName(u"label_4")
        font7 = QFont()
        font7.setFamilies([u"Gabriola"])
        font7.setPointSize(11)
        self.label_4.setFont(font7)

        self.verticalLayout_2.addWidget(self.label_4)


        self.horizontalLayout_10.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.btn_carregar = QPushButton(self.pg_table)
        self.btn_carregar.setObjectName(u"btn_carregar")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_carregar.sizePolicy().hasHeightForWidth())
        self.btn_carregar.setSizePolicy(sizePolicy7)
        self.btn_carregar.setMinimumSize(QSize(0, 40))
        self.btn_carregar.setFont(font)
        self.btn_carregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_carregar.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.btn_carregar.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_carregar)

        self.te_table = QTextEdit(self.pg_table)
        self.te_table.setObjectName(u"te_table")
        self.te_table.setFont(font3)
        self.te_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)

        self.verticalLayout_6.addWidget(self.te_table)

        self.pages.addWidget(self.pg_table)

        self.verticalLayout.addWidget(self.pages)


        self.verticalLayout_11.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Dados Sircon", None))
        self.btn_recibo.setText(QCoreApplication.translate("MainWindow", u"Recibos pagamentos", None))
        self.label_9.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>RECIBOS PAGAMENTOS</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Informa\u00e7\u00f5es necess\u00e1rias para gerar recibos de pagamento</p></body></html>", None))
        self.cb_vendedor.setText(QCoreApplication.translate("MainWindow", u"Vendedores", None))
        self.cb_supervisor.setText(QCoreApplication.translate("MainWindow", u"Supervisores", None))
        self.cb_gerente.setText(QCoreApplication.translate("MainWindow", u"Gerentes", None))
        self.cb_parceiro.setText(QCoreApplication.translate("MainWindow", u"Parceiros", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio: ", None))
        self.cbb_funcionario.setItemText(0, QCoreApplication.translate("MainWindow", u"TODOS OS FUNCION\u00c1RIOS", None))

        self.cbb_funcionario.setCurrentText(QCoreApplication.translate("MainWindow", u"TODOS OS FUNCION\u00c1RIOS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo ATA:   ", None))
        self.data_ata.setDisplayFormat(QCoreApplication.translate("MainWindow", u"'ATA  de '  MMMM   'de'   yyyy   ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo semanal:   ", None))
        self.data_semana.setDisplayFormat(QCoreApplication.translate("MainWindow", u"'Um dos dias da semana \u00e9 o dia 'd' de 'MMMM' de ' yyyy   ", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar", None))
        self.label.setText("")
        self.label_11.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"INFORMA\u00c7\u00d5ES DO SISTEMA SIRCON", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es necess\u00e1rias para preenchimento no site Sircon", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.le_senha.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"M\u00eas de in\u00edcio das vendas: ", None))
        self.data_inicial2.setSpecialValueText("")
        self.data_inicial2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MMMM  /  yyyy   ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Selecione as tabelas que ser\u00e3o carregadas:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cadastro:", None))
        self.cb_cadastro_funcionaio.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None))
        self.cb_cadastro_ata.setText(QCoreApplication.translate("MainWindow", u"Ata", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Comiss\u00f5es:", None))
        self.cb_comissoes_configuracao.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.cb_comissoes_configPagamento.setText(QCoreApplication.translate("MainWindow", u"Config. Pagamento", None))
        self.label_20.setText("")
        self.label_13.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Unir todas:", None))
        self.cb_juntar_tabela.setText(QCoreApplication.translate("MainWindow", u"Tabelas", None))
        self.label_10.setText("")
        self.label_4.setText("")
        self.btn_carregar.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
    # retranslateUi

