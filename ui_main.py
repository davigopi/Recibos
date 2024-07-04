# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(459, 520)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(20, 20, 20);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setStyleSheet(u"background-color: rgb(245, 245, 245);")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setStyleSheet(u"background-color: rgb(245, 245, 245);")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_recibo = QPushButton(self.frame)
        self.btn_recibo.setObjectName(u"btn_recibo")
        self.btn_recibo.setStyleSheet(u"background-color: rgb(245, 245, 245);")

        self.horizontalLayout.addWidget(self.btn_recibo)


        self.verticalLayout.addWidget(self.frame)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Gabriola"])
        font.setPointSize(18)
        self.pages.setFont(font)
        self.pages.setStyleSheet(u"color: rgb(240, 240, 240);")
        self.pg_recibo = QWidget()
        self.pg_recibo.setObjectName(u"pg_recibo")
        self.pg_recibo.setFont(font)
        self.verticalLayout_11 = QVBoxLayout(self.pg_recibo)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_14 = QLabel(self.pg_recibo)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setFamilies([u"Gabriola"])
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_14.setFont(font1)
        self.label_14.setMidLineWidth(1)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_recibo)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(0, 20))
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.cb_todos = QCheckBox(self.pg_recibo)
        self.cb_todos.setObjectName(u"cb_todos")
        self.cb_todos.setFont(font)

        self.verticalLayout_7.addWidget(self.cb_todos)

        self.cb_funcionario = QCheckBox(self.pg_recibo)
        self.cb_funcionario.setObjectName(u"cb_funcionario")
        self.cb_funcionario.setFont(font)

        self.verticalLayout_7.addWidget(self.cb_funcionario)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cb_vendedor = QCheckBox(self.pg_recibo)
        self.cb_vendedor.setObjectName(u"cb_vendedor")
        self.cb_vendedor.setFont(font)

        self.verticalLayout_10.addWidget(self.cb_vendedor)

        self.cb_supervisor = QCheckBox(self.pg_recibo)
        self.cb_supervisor.setObjectName(u"cb_supervisor")
        self.cb_supervisor.setFont(font)

        self.verticalLayout_10.addWidget(self.cb_supervisor)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.pg_recibo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_7)

        self.cbb_funcionario = QComboBox(self.pg_recibo)
        self.cbb_funcionario.addItem("")
        self.cbb_funcionario.addItem("")
        self.cbb_funcionario.setObjectName(u"cbb_funcionario")
        self.cbb_funcionario.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cbb_funcionario.sizePolicy().hasHeightForWidth())
        self.cbb_funcionario.setSizePolicy(sizePolicy3)
        self.cbb_funcionario.setFont(font)
        self.cbb_funcionario.setCursor(QCursor(Qt.CursorShape.SplitVCursor))

        self.horizontalLayout_12.addWidget(self.cbb_funcionario)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_15 = QLabel(self.pg_recibo)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_14.addWidget(self.label_15)

        self.btn_gerar = QPushButton(self.pg_recibo)
        self.btn_gerar.setObjectName(u"btn_gerar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_gerar.sizePolicy().hasHeightForWidth())
        self.btn_gerar.setSizePolicy(sizePolicy4)
        self.btn_gerar.setFont(font)
        self.btn_gerar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(20, 20, 20);")

        self.horizontalLayout_14.addWidget(self.btn_gerar)

        self.label_16 = QLabel(self.pg_recibo)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.label_16)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

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
        font2 = QFont()
        font2.setFamilies([u"Alef"])
        font2.setPointSize(72)
        self.pg_home.setFont(font2)
        self.pg_home.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"img/select4.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)

        self.horizontalLayout_7.addWidget(self.label)

        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Gabriola"])
        font3.setPointSize(48)
        font3.setBold(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.pages.addWidget(self.pg_home)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.pg_table.setStyleSheet(u"color: rgb(240, 240, 240);")
        self.verticalLayout_9 = QVBoxLayout(self.pg_table)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.pg_table)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setFamilies([u"Gabriola"])
        font4.setPointSize(24)
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_8)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_23 = QLabel(self.pg_table)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_23)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_24 = QLabel(self.pg_table)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_24)

        self.le_usuario = QLineEdit(self.pg_table)
        self.le_usuario.setObjectName(u"le_usuario")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.le_usuario.sizePolicy().hasHeightForWidth())
        self.le_usuario.setSizePolicy(sizePolicy6)
        self.le_usuario.setFont(font)

        self.horizontalLayout_4.addWidget(self.le_usuario)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_25 = QLabel(self.pg_table)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_25)

        self.le_senha = QLineEdit(self.pg_table)
        self.le_senha.setObjectName(u"le_senha")
        sizePolicy6.setHeightForWidth(self.le_senha.sizePolicy().hasHeightForWidth())
        self.le_senha.setSizePolicy(sizePolicy6)
        self.le_senha.setFont(font)
        self.le_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_5.addWidget(self.le_senha)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.pg_table)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_26)

        self.data_inicial = QDateEdit(self.pg_table)
        self.data_inicial.setObjectName(u"data_inicial")
        sizePolicy6.setHeightForWidth(self.data_inicial.sizePolicy().hasHeightForWidth())
        self.data_inicial.setSizePolicy(sizePolicy6)
        self.data_inicial.setFont(font)
        self.data_inicial.setDateTime(QDateTime(QDate(2001, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_16.addWidget(self.data_inicial)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.pg_table)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 20, -1)
        self.label_5 = QLabel(self.pg_table)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamilies([u"Gabriola"])
        font5.setPointSize(18)
        font5.setBold(False)
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.cb_cadastro_consorciado = QCheckBox(self.pg_table)
        self.cb_cadastro_consorciado.setObjectName(u"cb_cadastro_consorciado")
        self.cb_cadastro_consorciado.setFont(font)
        self.cb_cadastro_consorciado.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_cadastro_consorciado.setText(u"Consorciado")
        self.cb_cadastro_consorciado.setIconSize(QSize(16, 16))
        self.cb_cadastro_consorciado.setChecked(False)
        self.cb_cadastro_consorciado.setAutoRepeat(False)
        self.cb_cadastro_consorciado.setAutoExclusive(False)
        self.cb_cadastro_consorciado.setAutoRepeatDelay(300)
        self.cb_cadastro_consorciado.setAutoRepeatInterval(100)

        self.verticalLayout_3.addWidget(self.cb_cadastro_consorciado)

        self.cb_cadastro_funcionaio = QCheckBox(self.pg_table)
        self.cb_cadastro_funcionaio.setObjectName(u"cb_cadastro_funcionaio")
        self.cb_cadastro_funcionaio.setFont(font)
        self.cb_cadastro_funcionaio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout_3.addWidget(self.cb_cadastro_funcionaio)

        self.cb_cadastro_ata = QCheckBox(self.pg_table)
        self.cb_cadastro_ata.setObjectName(u"cb_cadastro_ata")
        self.cb_cadastro_ata.setFont(font)
        self.cb_cadastro_ata.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout_3.addWidget(self.cb_cadastro_ata)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_19 = QLabel(self.pg_table)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_19)

        self.cb_comissoes_configuracao = QCheckBox(self.pg_table)
        self.cb_comissoes_configuracao.setObjectName(u"cb_comissoes_configuracao")
        self.cb_comissoes_configuracao.setFont(font)
        self.cb_comissoes_configuracao.setIconSize(QSize(1600, 1600))

        self.verticalLayout_2.addWidget(self.cb_comissoes_configuracao)

        self.cb_comissoes_configPagamento = QCheckBox(self.pg_table)
        self.cb_comissoes_configPagamento.setObjectName(u"cb_comissoes_configPagamento")
        self.cb_comissoes_configPagamento.setFont(font)

        self.verticalLayout_2.addWidget(self.cb_comissoes_configPagamento)

        self.label_20 = QLabel(self.pg_table)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_2.addWidget(self.label_20)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_21 = QLabel(self.pg_table)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_3.addWidget(self.label_21)

        self.btn_carregar = QPushButton(self.pg_table)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setFont(font)
        self.btn_carregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_carregar.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"color: rgb(22, 22, 22);")

        self.horizontalLayout_3.addWidget(self.btn_carregar)

        self.label_22 = QLabel(self.pg_table)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_3.addWidget(self.label_22)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.pages.addWidget(self.pg_table)

        self.verticalLayout.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Tabela", None))
        self.btn_recibo.setText(QCoreApplication.translate("MainWindow", u"Recibo", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Recibo</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Gerar recibos</p></body></html>", None))
        self.cb_todos.setText(QCoreApplication.translate("MainWindow", u"Todos os funcion\u00e1rios", None))
        self.cb_funcionario.setText(QCoreApplication.translate("MainWindow", u"Por funcion\u00e1rio", None))
        self.cb_vendedor.setText(QCoreApplication.translate("MainWindow", u"Vendedores", None))
        self.cb_supervisor.setText(QCoreApplication.translate("MainWindow", u"Supervisores", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Selecionar usu\u00e1rio: ", None))
        self.cbb_funcionario.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o Funcion\u00e1rio", None))
        self.cbb_funcionario.setItemText(1, "")

        self.label_15.setText("")
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar", None))
        self.label_16.setText("")
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt; color:#f0f0f0;\">S E L E C T</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tabela", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Dados do sistema Sircon:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.le_senha.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Data inicial das vendas:", None))
        self.data_inicial.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/yyyy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Selecione abaixo as tabelas que ser\u00e3o carregadas:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cadastro:", None))
        self.cb_cadastro_funcionaio.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None))
        self.cb_cadastro_ata.setText(QCoreApplication.translate("MainWindow", u"Ata", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Comiss\u00f5es:", None))
        self.cb_comissoes_configuracao.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.cb_comissoes_configPagamento.setText(QCoreApplication.translate("MainWindow", u"Config. Pagamento", None))
        self.label_20.setText("")
        self.label_21.setText("")
        self.btn_carregar.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
        self.label_22.setText("")
    # retranslateUi

