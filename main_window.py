from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QStackedWidget  # noqa
from PySide6.QtCore import QDate, QObject, QThread, Signal
from PySide6.QtGui import QIcon
# from distutils.log import Log
from ui_main import Ui_MainWindow
import sys
from main_table import Main_table
from main_gerar import Main_gerar


class Worker1(QObject):
    started1 = Signal()
    progressed1 = Signal(str)
    finished1 = Signal()

    def scall_main_table(self, *args, **kwargs) -> None:
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
        main_table = Main_table()
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
            main_table.new_table_Comissoes_Configuracao = comissoes_configuracao  # noqa
        if comissoes_configPagamento is not None:
            main_table.new_table_Comissoes_ConfigPagamento = (
                comissoes_configPagamento)
        if mix is not None:
            main_table.mix = mix
            print(mix)
        main_table.log_start_end()
        main_table.create_table_Cadastro_Consorciado()
        main_table.create_table_Cadastro_Funcionario()
        main_table.create_table_Cadastro_Ata()
        main_table.create_table_Comissoes_Configuracao()
        main_table.create_table_Comissoes_ConfigPagamento()
        main_table.date_weekly_new()
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
        main_table.create_columns_ata()
        main_table.merge_full_weekly()
        main_table.merge_full_ata()
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

    def scall_main_table(self, *args, **kwargs) -> None:
        self.started2.emit()
        todos_funcionarios = kwargs.get('todos_funcionarios')
        por_funcionario = kwargs.get('por_funcionario')
        vendedores = kwargs.get('vendedores')
        supervisores = kwargs.get('supervisores')
        selecionado_funcionario = kwargs.get('selecionado_funcionario')
        data_ata = kwargs.get('data_ata')
        main_gerar = Main_gerar()
        if todos_funcionarios is not None:
            # main_gerar.todos_funcionarios = todos_funcionarios
            # print(todos_funcionarios)
            pass
        if por_funcionario is not None:
            # main_gerar.por_funcionario = por_funcionario
            # print(por_funcionario)
            pass
        if vendedores is not None:
            main_gerar.is_vendedores = vendedores
        if supervisores is not None:
            main_gerar.is_supervirores = supervisores
        if selecionado_funcionario is not None:
            # main_gerar.selecionado_funcionario = selecionado_funcionario
            # print(selecionado_funcionario)
            pass
        if data_ata is not None:
            data_ata = data_ata.toPython()
            main_gerar.data_ata = data_ata
            # print(data_ata)
        main_gerar.generate_date_ata()
        main_gerar.generate_is_vendedores()
        main_gerar.generate_is_supervisores()
        # main_gerar.generate_employee()
        self.finished2.emit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Select carregar informações e gerar recibos")

        # Carregar o ícone e definir para a janela
        icon = QIcon('img/icon.png')
        self.setWindowIcon(icon)

        # Inicializar QDateEdit com a data atual
        self.data_inicial.setDate(QDate.currentDate().addYears(-1))
        self.data_ata.setDate(QDate.currentDate())

        # Adiciona itens ao QComboBox
        self.cbb_funcionario.addItems(
            ["Funcionário 1", "funcionário 2", "Funcionário 3"]
        )

        # paguinaas do sistema
        self.btn_tables.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_table))
        self.btn_recibo.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_recibo))

        self.btn_carregar.clicked.connect(self.carregar_btn)

        self.btn_gerar.clicked.connect(self.gerar_btn)

        self.thread1 = None
        self.thread2 = None

    def carregar_btn(self):
        self.worker1 = Worker1()
        self.thread1 = QThread()
        # Move o worker para a thread.
        self.worker1.moveToThread(self.thread1)

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
            comissoes_configPagamento=(
                self.cb_comissoes_configPagamento.isChecked()),
            mix=self.cb_juntar_tabela.isChecked()
        ))

        # Quando o worker terminar, para a thread.
        self.worker1.finished1.connect(self.thread1.quit)
        # Deleta a thread depois que el§a termina.
        self.thread1.finished.connect(self.thread1.deleteLater)
        # Deleta o worker depois que ele termina.
        self.worker1.finished1.connect(self.worker1.deleteLater)
        # Conecta sinais do worker a métodos da interface.
        self.worker1.started1.connect(self.workStarted)
        # self.worker.progressed.connect(self.work1Progressed)
        self.worker1.finished1.connect(self.workFinished)

        self.thread1.start()  # Inicia a thread.

    def gerar_btn(self):
        self.worker2 = Worker2()
        self.thread2 = QThread()
        # Move o worker para a thread.
        self.worker2.moveToThread(self.thread2)

        self.thread2.started.connect(lambda: self.worker2.scall_main_table(
            todos_funcionarios=self.cb_todos.isChecked(),
            por_funcionario=self.cb_funcionario.isChecked(),
            vendedores=self.cb_vendedor.isChecked(),
            supervisores=self.cb_supervisor.isChecked(),
            selecionado_funcionario=self.cbb_funcionario.currentText(),
            data_ata=self.data_ata.date()
        ))

        # Quando o worker terminar, para a thread.
        self.worker2.finished2.connect(self.thread2.quit)
        # Deleta a thread depois que el§a termina.
        self.thread2.finished.connect(self.thread2.deleteLater)
        # Deleta o worker depois que ele termina.
        self.worker2.finished2.connect(self.worker2.deleteLater)
        # Conecta sinais do worker a métodos da interface.
        self.worker2.started2.connect(self.workStarted)
        # self.worker.progressed.connect(self.work1Progressed)
        self.worker2.finished2.connect(self.workFinished)

        self.thread2.start()  # Inicia a thread.

        # # Verificar se o QCheckBox está marcado
        # if self.cb_todos.isChecked():
        #     print("O cb_todos está marcado.")
        # else:
        #     print("O cb_todos, não está marcado.")

        # if self.cb_funcionario.isChecked():
        #     print("O cb_funcionario está marcado.")
        # else:
        #     print("O cb_funcionario, não está marcado.")

        # if self.cb_vendedor.isChecked():
        #     print("O cb_vendedor está marcado.")
        # else:
        #     print("O cb_vendedor, não está marcado.")

        # if self.cb_supervisor.isChecked():
        #     print("O cb_supervisor está marcado.")
        # else:
        #     print("O cb_supervisor, não está marcado.")

        # Obtém o texto do item selecionado no QComboBox e define no QLabel
        # selected_text = self.cbb_funcionario.currentText()
        # print(f"Selecionado: {selected_text}")

    def workStarted(self):
        self.btn_carregar.setDisabled(True)
        self.btn_gerar.setDisabled(True)
        self.btn_tables.setDisabled(True)
        self.btn_recibo.setDisabled(True)
        QApplication.processEvents()
        print('worker iniciado')

    def workFinished(self):
        self.btn_carregar.setDisabled(False)
        self.btn_gerar.setDisabled(False)
        self.btn_tables.setDisabled(False)
        self.btn_recibo.setDisabled(False)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
