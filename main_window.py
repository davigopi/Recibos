# flake8: noqa
# pyright: # type: ignore

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QDate, QObject, QThread, Signal
from PySide6.QtGui import QIcon, QPixmap
from ui_main import Ui_MainWindow
import sys
import os
from main_table import Main_table
from main_recibo import Main_recibo
import time


def resource_path(relative_path):
    # Obter caminho absoluto para o recurso, trabalhando para dev e PyInstaller
    try:
        base_path = sys._MEIPASS  # type: ignore[attr-defined]
        # base_path = os.path.appdata()
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Worker1(QObject):
    started1 = Signal()
    progressed1 = Signal(str)
    finished1 = Signal()

    def prog1(self, text):
        self.progressed1.emit(text)

    def scall_main_table(self, *args, **kwargs) -> None:
        self.prog1('Iniciar')
        self.started1.emit()
        user = kwargs.get('user')
        password = kwargs.get('password')
        months = kwargs.get('months')
        cadastro_consorciado = kwargs.get('cadastro_consorciado')
        cadastro_funcionaio = kwargs.get('cadastro_funcionaio')
        cadastro_ata = kwargs.get('cadastro_ata')
        comissoes_configuracao = kwargs.get('comissoes_configuracao')
        comissoes_configPagamento = kwargs.get('comissoes_configPagamento')
        mix = kwargs.get('mix')
        main_table = Main_table(father=self)
        if user is not None:
            main_table.user = user
        if password is not None:
            main_table.password = password
        if months is not None:
            main_table.month = months
        if cadastro_consorciado is not None:
            main_table.new_table_Cadastro_Consorciado = cadastro_consorciado
        if cadastro_funcionaio is not None:
            main_table.new_table_Cadastro_Funcionario = cadastro_funcionaio
        if cadastro_ata is not None:
            main_table.new_table_Cadastro_Ata = cadastro_ata
        if comissoes_configuracao is not None:
            main_table.new_table_Comissoes_Configuracao = comissoes_configuracao
        if comissoes_configPagamento is not None:
            main_table.new_table_Comissoes_ConfigPagamento = comissoes_configPagamento
        if mix is not None:
            main_table.mix = mix
            # print(mix)
        main_table.log_start_end()
        main_table.create_table_Cadastro_Consorciado()
        main_table.create_table_Cadastro_Funcionario()
        main_table.create_table_Cadastro_Ata()
        main_table.create_table_Comissoes_Configuracao()
        main_table.create_table_Comissoes_ConfigPagamento()
        main_table.create_table_gerente()
        main_table.create_date_weekly_new()
        main_table.merge_table_Cadastro_Ata_table_date_weekly()
        main_table.table_manip_funcionario()
        main_table.table_manip_cadastro_consorciado()
        main_table.table_manip_comissoes_configuracao()
        main_table.test_table_Comissoes_ConfigPagamento()
        main_table.table_manip_Cadastro_funcionario_gerente()
        main_table.test_table_Cadastro_Funcionario()
        main_table.table_manip_comissoes_configuracao_gerente()
        main_table.merge_star()
        main_table.merge_consorciado_funcionario()
        main_table.merge_consorciado_funcionario_gerente()
        main_table.merge_full_comissoes_configuracao()
        main_table.merge_full_comissoes_configuracao_gerente()
        main_table.merge_full_comissoes_configuracao_gerente_geral()
        main_table.create_columns_ata()
        main_table.merge_full_ata_weekly_month()
        # main_table.merge_full_ata()
        main_table.merge_full_configPagamento()
        main_table.column_add()
        main_table.order_column()
        main_table.save_full()
        main_table.test_full_double()
        main_table.test_primary_key()
        main_table.log_start_end()
        self.finished1.emit()


class Worker2(QObject):
    started2 = Signal()
    progressed2 = Signal(str)
    finished2 = Signal()

    def prog2(self, text):
        self.progressed2.emit(text)

    def scall_main_table(self, *args, **kwargs) -> None:
        self.prog2('Iniciar')
        self.started2.emit()
        vendedores = kwargs.get('vendedores')
        supervisores = kwargs.get('supervisores')
        gerentes = kwargs.get('gerentes')
        parceiros = kwargs.get('parceiros')
        selecionado_funcionario = kwargs.get('selecionado_funcionario')
        data_ata = kwargs.get('data_ata')
        data_semana = kwargs.get('data_semana')
        main_gerar = Main_recibo(father=self)
        if vendedores is not None:
            main_gerar.is_vendedores = vendedores
        if supervisores is not None:
            main_gerar.is_supervisores = supervisores
        if gerentes is not None:
            main_gerar.is_gerentes = gerentes
        if parceiros is not None:
            main_gerar.is_parceiros = parceiros
        if selecionado_funcionario is not None:
            if selecionado_funcionario != 'TODOS OS FUNCIONÁRIOS':
                main_gerar.seller_single_unit = selecionado_funcionario
        if data_ata is not None and data_semana is not None:
            data_ata = data_ata.toPython()
            data_semana = data_semana.toPython()
            main_gerar.data_ata = data_ata
            main_gerar.data_semana = data_semana
            main_gerar.generate_date_ata()

        main_gerar.generate_is_vendedores()
        main_gerar.generate_is_supervisores()
        main_gerar.generate_is_gerentes()
        main_gerar.generate_is_parceiros()
        self.finished2.emit()
        self.prog2('Finalizado.')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        main_gerar = Main_recibo()
        # super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Select carregar informações e gerar recibos")
        self.adjust_image_paths()
        # Inicializar QDateEdit com a data atual
        self.data_inicial.setDate(QDate.currentDate().addYears(-1))
        self.data_ata.setDate(QDate.currentDate())
        self.data_semana.setDate(QDate.currentDate())
        # Adiciona itens ao QComboBox
        list_seller = main_gerar.generate_list_seller()
        # list_seller = list(list_seller)
        # list_seller = [str(item) for item in list_seller if item is not None]
        # list_seller.sort()
        self.cbb_funcionario.addItems(list_seller)
        # paguinaas do sistema
        self.btn_tables.clicked.connect(self.tables_btn)
        self.btn_recibo.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_recibo))
        self.btn_carregar.clicked.connect(self.carregar_btn)
        self.btn_gerar.clicked.connect(self.gerar_btn)
        self.thread1 = None
        self.thread2 = None

    def adjust_image_paths(self):
        # Ajuste os caminhos das imagens:
        image_path = resource_path('img/icon.png')
        icon = QIcon(image_path)
        self.setWindowIcon(icon)
        image_path = resource_path('img/select2.png')
        self.label_9.setPixmap(QPixmap(image_path))
        image_path = resource_path('img/select.png')
        self.label.setPixmap(QPixmap(image_path))
        image_path = resource_path('img/select2.png')
        self.label_11.setPixmap(QPixmap(image_path))

    def tables_btn(self):
        self.pages.setCurrentWidget(self.pg_table)
        self.te_table.setText('')
        self.date_path_file()

    def keyPressEvent(self, event):
        # if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
        if event.key() in [16777220, 16777221]:
            current_widget = self.pages.currentWidget()
            if current_widget == self.pg_table:
                self.carregar_btn()
            elif current_widget == self.pg_recibo:
                self.gerar_btn()

    def carregar_btn(self):
        self.worker1 = Worker1()
        self.thread1 = QThread()
        # Move o worker para a thread.
        self.worker1.moveToThread(self.thread1)
        self.te_table.clear()
        # Conecta os sinais e slots.,
        # Quando a thread iniciar, chama scall_main_table.
        self.thread1.started.connect(lambda: self.worker1.scall_main_table(
            user=self.le_usuario.text(),
            password=self.le_senha.text(),
            months=self.calculate_month(self.data_inicial.date()),
            cadastro_consorciado=self.cb_cadastro_consorciado.isChecked(),
            cadastro_funcionaio=self.cb_cadastro_funcionaio.isChecked(),
            cadastro_ata=self.cb_cadastro_ata.isChecked(),
            comissoes_configuracao=self.cb_comissoes_configuracao.isChecked(),
            comissoes_configPagamento=(self.cb_comissoes_configPagamento.isChecked()),
            mix=self.cb_juntar_tabela.isChecked()
        ))
        # Quando o worker terminar, para a thread.
        self.worker1.finished1.connect(self.thread1.quit)
        # Deleta a thread depois que ela termina.
        self.thread1.finished.connect(self.thread1.deleteLater)
        # Deleta o worker depois que ele termina.
        self.worker1.finished1.connect(self.worker1.deleteLater)
        # Conecta sinais do worker a métodos da interface.
        self.worker1.started1.connect(self.workStarted)
        self.worker1.progressed1.connect(self.worker1Progressed)
        self.worker1.finished1.connect(self.work1Finished)
        self.thread1.start()

    def gerar_btn(self):
        self.worker2 = Worker2()
        self.thread2 = QThread()
        # Move o worker para a thread.
        self.worker2.moveToThread(self.thread2)
        self.te_recibo.clear()
        self.thread2.started.connect(lambda: self.worker2.scall_main_table(
            vendedores=self.cb_vendedor.isChecked(),
            supervisores=self.cb_supervisor.isChecked(),
            gerentes=self.cb_gerente.isChecked(),
            parceiros=self.cb_parceiro.isChecked(),
            selecionado_funcionario=self.cbb_funcionario.currentText(),
            data_ata=self.data_ata.date(),
            data_semana=self.data_semana.date(),
        ))
        self.worker2.finished2.connect(self.thread2.quit)
        self.thread2.finished.connect(self.thread2.deleteLater)
        self.worker2.finished2.connect(self.worker2.deleteLater)
        self.worker2.started2.connect(self.workStarted)
        self.worker2.progressed2.connect(self.worker2Progressed)
        self.worker2.finished2.connect(self.work2Finished)

        self.thread2.start()

    def workStarted(self):
        self.btn_carregar.setDisabled(True)
        self.btn_gerar.setDisabled(True)
        self.btn_tables.setDisabled(True)
        self.btn_recibo.setDisabled(True)
        QApplication.processEvents()
        print('worker iniciado')

    def worker1Progressed(self, new_text):
        text_original = self.te_table.toPlainText()
        text = text_original + new_text + '\n'
        self.te_table.setText(text)
        self.scroll(40)
        QApplication.processEvents()
        time.sleep(0.5)

    def worker2Progressed(self, new_text):
        text_original = self.te_recibo.toPlainText()
        text = text_original + new_text + '\n'
        self.te_recibo.setText(text)
        QApplication.processEvents()
        self.scroll2()
        QApplication.processEvents()

    def work1Finished(self):
        self.btn_carregar.setDisabled(False)
        self.btn_gerar.setDisabled(False)
        self.btn_tables.setDisabled(False)
        self.btn_recibo.setDisabled(False)
        QApplication.processEvents()
        self.date_path_file()
        print('worker finalizado')

    def work2Finished(self):
        self.btn_carregar.setDisabled(False)
        self.btn_gerar.setDisabled(False)
        self.btn_tables.setDisabled(False)
        self.btn_recibo.setDisabled(False)
        self.scroll2()
        QApplication.processEvents()
        print('worker finalizado')

    def calculate_month(self, date_start):
        date_end = QDate.currentDate()
        total_years = date_end.year() - date_start.year()
        total_months = date_end.month() - date_start.month()
        months = total_years * 12 + total_months
        if months == 0:
            months = 1
        return (months)

    def date_path_file(self):
        main_table = Main_table(father=self)
        text_te = main_table.date_file()
        text_original = self.te_table.toPlainText()
        text = text_original + text_te + '\n'
        self.te_table.setText(text)
        self.scroll(70)
        QApplication.processEvents()

    def scroll(self, scroll_height):
        max_scroll = self.te_table.verticalScrollBar().maximum()
        self.te_table.verticalScrollBar().setValue(max_scroll - scroll_height)

    def scroll2(self):
        max_scroll = self.te_recibo.verticalScrollBar().maximum()
        self.te_recibo.verticalScrollBar().setValue(max_scroll)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
