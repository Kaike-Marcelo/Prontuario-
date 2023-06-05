# Importa outras Bibs #########################################################
import json
import requests
#######################################################################################

# Importa o PyQt5######################################################################
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox
#######################################################################################

# Importa as Interfaces ###############################################################
from Arquivos.Main_ui import Ui_JanelaPrincipal
from Arquivos.ui_Login import Ui_Principal_Login
#######################################################################################


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicia a tela de login
        self.login_ui = Ui_Principal_Login()
        self.login_ui.setupUi(self)

        self.login_ui.btn_Entrar.clicked.connect(self.login)

    # Em Manutenção ###########################################################################
    def login(self) -> dict:

        try:
            email = 'Paulo@gmail.comm'
            senha = 'carvalho1000'
            dados = {"email": email, "password": senha}

            con = requests.post(
                'http://127.0.0.1:8000/api/token', data=dados)

            self.Janela_Principal()
            self.show()

        except requests.exceptions.RequestException as e:
            self.showErrorMessage(f"Erro de requisição: {e}")
        #######################################################################################

    def Janela_Principal(self):

        # Fecha a janela de Login e Abre a Janela Principal ###################################
        self.login_ui.centralwidget_Login.close()
        self.main_ui = Ui_JanelaPrincipal()
        self.main_ui.setupUi(self)
        self.showMaximized()  # Configura a janela principal como maximizada
        #######################################################################################

        # Páginas do Menu #####################################################################
        self.main_ui.btn_Principal.clicked.connect(
            lambda: self.Pagina_Principal())

        self.main_ui.btn_Pacientes.clicked.connect(
            lambda: self.Pagina_Pacientes())
        self.main_ui.btn_Pacientes.clicked.connect(
            lambda: self.lista_de_pacientes())
        #######################################################################################

        self.main_ui.btn_NovoPaciente.clicked.connect(
            lambda: self.btn_NovoPacienteClicked())

        self.main_ui.btn_DadosPrincipais.clicked.connect(
            lambda: self.main_ui.pg_DadosDoPaciente.setCurrentWidget(self.main_ui.pg_DadosPrincipais))
        self.main_ui.btn_OutrosDados.clicked.connect(
            lambda: self.main_ui.pg_DadosDoPaciente.setCurrentWidget(self.main_ui.pg_OutrosDados))

        self.main_ui.btn_Prontuario.clicked.connect(
            lambda: self.main_ui.Paginas_Principais.setCurrentWidget(self.main_ui.pg_Consulta))

        # Menu Vertical #######################################################################
        self.main_ui.btn_Menu.clicked.connect(lambda: self.menu_vertical())
        #######################################################################################

        # Desativa o Botão Salvar #############################################################
        self.main_ui.btn_SalvarFormulario.setEnabled(False)
        #######################################################################################

        # Envia sinal que hab. ou desa. os botões #############################################
        self.main_ui.lineEdit_Nome.textChanged.connect(
            self.atualizaBotaoSalvar)
        self.main_ui.lineEdit_Email.textChanged.connect(
            self.atualizaBotaoSalvar)
        self.main_ui.lineEdit_Telefone.textChanged.connect(
            self.atualizaBotaoSalvar)
        self.main_ui.lineEdit_Sobrenome.textChanged.connect(
            self.atualizaBotaoSalvar)
        #######################################################################################

        self.main_ui.btn_SalvarFormulario.clicked.connect(
            lambda: self.Salvar_NovoPaciente())

        self.main_ui.btn_VoltarFormulario.clicked.connect(
            lambda: self.btn_Voltar_Formulario())
        self.main_ui.btn_VoltarConsulta.clicked.connect(
            lambda: self.btn_Voltar_Consulta())

        self.main_ui.lineEdit_PesquisarPaciente.returnPressed.connect(
            self.pesquisar_paciente)

        # Configura a tabela de pacientes #####################################################
        self.main_ui.tableWidget_ListaPacientes.setSelectionBehavior(
            QAbstractItemView.SelectRows)  # Define o modo de seleção de linhas inteiras

        self.main_ui.tableWidget_ListaPacientes.doubleClicked.connect(
            self.abrir_formulario_do_paciente)  # Conecta o sinal doubleClicked ao slot selecionar_linha

        self.main_ui.tableWidget_ListaPacientes.setSelectionBehavior(
            QAbstractItemView.SelectRows)  # Define o modo de seleção para seleção de linhas inteiras

        self.main_ui.tableWidget_ListaPacientes.cellDoubleClicked.connect(
            lambda: self.selecionar_linha)  # Conecta o sinal cellClicked ao slot selecionar_linha
        #######################################################################################

        self.main_ui.btn_NovaConsulta.clicked.connect(
            lambda: self.main_ui.Paginas_Consultas.setCurrentWidget(self.main_ui.pg_NovaConsulta))

        self.main_ui.btn_Receitas.clicked.connect(
            lambda: self.main_ui.Paginas_Consulta.setCurrentWidget(self.main_ui.pg_Receitas))
        self.main_ui.btn_Atestados.clicked.connect(
            lambda: self.main_ui.Paginas_Consulta.setCurrentWidget(self.main_ui.pg_Atestados))
        self.main_ui.btn_Laudos.clicked.connect(
            lambda: self.main_ui.Paginas_Consulta.setCurrentWidget(self.main_ui.pg_Laudos))

        self.main_ui.btn_SalvarConsulta.clicked.connect(
            lambda: self.salvar_Receitas())

    # Configura o Menu ####################################################################
    def menu_vertical(self):
        visivel = self.main_ui.frame_MenuVertical.width() > 61
        nova_largura = 61 if visivel else 140
        self.main_ui.frame_MenuVertical.setFixedWidth(nova_largura)

    def Pagina_Principal(self):
        self.main_ui.btn_Principal.setIcon(
            QIcon(":/Icons/icon_InicioAberto.png"))
        self.main_ui.btn_Pacientes.setIcon(QIcon(":/Icons/icon_Pacientes.png"))
        self.main_ui.Paginas_Principais.setCurrentWidget(
            self.main_ui.pg_Principal)

    def Pagina_Pacientes(self):
        self.main_ui.btn_Pacientes.setIcon(
            QIcon(":/Icons/icon_Pacientes2.png"))
        self.main_ui.btn_Principal.setIcon(
            QIcon(":/Icons/icon_InicioFechado.png"))
        self.main_ui.Paginas_Principais.setCurrentWidget(
            self.main_ui.pg_Pacientes)
    #######################################################################################

    def lista_de_pacientes(self) -> dict:

        con = requests.get('http://127.0.0.1:8000/api/user')
        pacientes = json.loads(con.text)
        self.main_ui.tableWidget_ListaPacientes.setRowCount(len(pacientes))
        self.main_ui.tableWidget_ListaPacientes.setColumnCount(4)

        for linha, paciente in enumerate(pacientes):
            self.main_ui.tableWidget_ListaPacientes.setItem(
                linha, 0, QTableWidgetItem(str(paciente.get("id"))))
            self.main_ui.tableWidget_ListaPacientes.setItem(
                linha, 1, QTableWidgetItem(str(paciente.get("cpf"))))
            self.main_ui.tableWidget_ListaPacientes.setItem(
                linha, 2, QTableWidgetItem(str(paciente.get("data_nascimento"))))

            nome_completo = f"{paciente['name']} {paciente['last_name']}"
            nome_completo_paciente = QTableWidgetItem(nome_completo)
            self.main_ui.tableWidget_ListaPacientes.setItem(
                linha, 3, nome_completo_paciente)

    # Configura a tabela de pacientes ####################################################
    def selecionar_linha(self, item):
        # Obtem o índice da célula clicada
        index = self.main_ui.tableWidget_ListaPacientes.currentIndex()
        linha = index.row()  # Obtem a linha correspondente ao índice
        # Obtem o número de colunas da tabela
        num_colunas = self.main_ui.tableWidget_ListaPacientes.columnCount()

        # Limpa a seleção atual da tabela
        self.main_ui.tableWidget_ListaPacientes.clearSelection()

        # Seleciona todas as colunas da linha clicada
        for coluna in range(num_colunas):
            item = self.main_ui.tableWidget_ListaPacientes.item(linha, coluna)
            item.setSelected(True)

    def abrir_formulario_do_paciente(self, event):

        index = self.main_ui.tableWidget_ListaPacientes.currentIndex()
        linha = index.row()
        item = self.main_ui.tableWidget_ListaPacientes.item(linha, 0)

        self.id_paciente = item.text()

        con = requests.get(
            f'http://127.0.0.1:8000/api/user/{self.id_paciente}')

        if con.status_code == 200:
            paciente = con.json()

            self.main_ui.Paginas_Principais.setCurrentWidget(
                self.main_ui.pg_Formularios)

            # Preenche os campos do formulário ####################################################
            self.main_ui.lineEdit_Nome.setText(paciente['user']['name'])
            self.main_ui.lineEdit_Sobrenome.setText(
                paciente['user']['last_name'])
            self.main_ui.lineEdit_Email.setText(paciente['user']['email'])

            # Data Nascimento #####################################################################
            data_nascimento = paciente['user']['data_nascimento']
            dia, mes, ano = map(int, data_nascimento.split('-'))
            qdate_Nascimento = QDate(dia, mes, ano)
            self.main_ui.dateEdit_Nascimento.setDate(qdate_Nascimento)
            self.main_ui.dateEdit_Nascimento.setDate(
                QDate.fromString(data_nascimento, "dd/MM/yyyy"))
            #######################################################################################

            self.main_ui.lineEdit_CPF.setText(paciente['user']['cpf'])
            self.main_ui.lineEdit_CNS.setText(paciente['user']['cns'])
            self.main_ui.lineEdit_RG.setText(paciente['user']['rg'])
            self.main_ui.lineEdit_Telefone.setText(
                paciente['information']['telefone'])
            self.main_ui.comboBox_Sexo.setCurrentText(
                paciente['information']['sexo'])
            self.main_ui.lineEdit_Numero.setText(
                paciente['information']['numero'])
            self.main_ui.comboBox_UF.setCurrentText(
                paciente['information']['estado'])
            self.main_ui.lineEdit_Bairro.setText(
                paciente['information']['bairro'])
            self.main_ui.lineEdit_Cidade.setText(
                paciente['information']['cidade'])
            #######################################################################################

            self.main_ui.btn_Prontuario.setEnabled(True)

        else:
            self.showErrorMessage(
                "Não foi possível localizar o formulário do paciente.")
    #######################################################################################

    # Pesquisa Paciente na Lista ##########################################################
    def Pesquisar_Com_Enter(self, event):
        if event.key() == Qt.Key_Return:
            self.pesquisar_paciente()
        else:
            super().Pesquisar_Com_Enter(event)

    def pesquisar_paciente(self):
        nome_paciente = self.main_ui.lineEdit_PesquisarPaciente.text()

        con = requests.get(f'http://127.0.0.1:8000/api/user/')
        self.linha = 0

        if con.status_code == 200:
            pacientes = con.json()
            linha = 0

            self.main_ui.tableWidget_ListaPacientes.clearContents()

            if nome_paciente == '':
                self.lista_de_pacientes()
            else:
                for paciente in pacientes:
                    if nome_paciente == paciente.get("name"):
                        self.main_ui.tableWidget_ListaPacientes.setRowCount(
                            len(pacientes))
                        self.main_ui.tableWidget_ListaPacientes.setColumnCount(
                            4)

                        self.main_ui.tableWidget_ListaPacientes.setItem(
                            linha, 0, QTableWidgetItem(str(paciente.get("id"))))
                        self.main_ui.tableWidget_ListaPacientes.setItem(
                            linha, 1, QTableWidgetItem(str(paciente.get("cpf"))))
                        self.main_ui.tableWidget_ListaPacientes.setItem(
                            linha, 2, QTableWidgetItem(str(paciente.get("data_nascimento"))))

                        nome_completo = f"{paciente['name']} {paciente['last_name']}"
                        self.main_ui.tableWidget_ListaPacientes.setItem(
                            linha, 3, QTableWidgetItem(nome_completo))
                        linha += 1
                        self.linha = linha

                self.main_ui.tableWidget_ListaPacientes.setRowCount(self.linha)
    #######################################################################################

    def btn_NovoPacienteClicked(self):
        self.main_ui.btn_Prontuario.setEnabled(False)
        self.main_ui.Paginas_Principais.setCurrentWidget(
            self.main_ui.pg_Formularios)

    # Habilita ou Desabilita os botões ####################################################

    def atualizaBotaoSalvar(self):
        if self.main_ui.lineEdit_Nome.text() and self.main_ui.lineEdit_Email.text() and self.main_ui.lineEdit_Telefone.text() and self.main_ui.lineEdit_Sobrenome.text():
            self.main_ui.btn_SalvarFormulario.setEnabled(True)
        else:
            self.main_ui.btn_SalvarFormulario.setEnabled(False)
    #######################################################################################

    def btn_Voltar_Formulario(self):
        self.showYesNoMessage()
        if self.result == QMessageBox.Yes:
            try:
                self.Atualizar_Dados_Do_Paciente(self.id_paciente)
                self.lista_de_pacientes()
                self.main_ui.Paginas_Principais.setCurrentWidget(
                    self.main_ui.pg_Pacientes)
            except:
                self.main_ui.Paginas_Principais.setCurrentWidget(
                    self.main_ui.pg_Pacientes)

        elif self.result == QMessageBox.No:
            self.main_ui.Paginas_Principais.setCurrentWidget(
                self.main_ui.pg_Pacientes)

    def btn_Voltar_Consulta(self):

        # self.Atualizar_Dados_Do_Paciente(self.id_paciente)
        # self.lista_de_pacientes()
        self.main_ui.Paginas_Principais.setCurrentWidget(
            self.main_ui.pg_Formularios)

    def Salvar_NovoPaciente(self) -> dict:

        dados = {
            "login": {
                "name": f"{self.main_ui.lineEdit_Nome.text()}",
                "last_name": f"{self.main_ui.lineEdit_Sobrenome.text()}",
                "password": "padrao",
                "email": f"{self.main_ui.lineEdit_Email.text()}",
                "data_nascimento": self.main_ui.dateEdit_Nascimento.date().toString("yyyy/MM/dd") or '2000/01/01',
                "cns": f"{self.main_ui.lineEdit_CNS.text()}" or '-',
                "rg": f"{self.main_ui.lineEdit_RG.text()}" or '-',
                "cpf": f"{self.main_ui.lineEdit_CPF.text()}" or '-'
            },
            "informacao": {
                "telefone": f"{self.main_ui.lineEdit_Telefone.text()}" or '-',
                "foto": "vazio",
                "sexo": f"{self.main_ui.comboBox_Sexo.currentText()}" or '-',
                "endereco": "Não tem",
                "numero": f"{self.main_ui.lineEdit_Numero.text()}" or '-',
                "cidade": f'{self.main_ui.lineEdit_Cidade.text()}' or '-',
                "bairro": f"{self.main_ui.lineEdit_Bairro.text()}" or '-',
                "estado": f"{self.main_ui.comboBox_UF.currentText()}" or '-'
            },
            "doctor": {

            }
        }

        paciente = requests.post('http://127.0.0.1:8000/api/user/create',
                                 data=json.dumps(dados), headers={'Content-type': 'application/json'})

        if paciente.status_code == 200:

            self.showInfoMessage("Formulário Salvo.")
            self.main_ui.Paginas_Principais.setCurrentWidget(
                self.main_ui.pg_Pacientes)

            # Limpa todos os campos do Formulário #################################################
            self.main_ui.lineEdit_Nome.clear()
            self.main_ui.lineEdit_Sobrenome.clear()
            self.main_ui.lineEdit_Email.clear()
            self.main_ui.dateEdit_Nascimento.clear()
            self.main_ui.lineEdit_Telefone.clear()
            self.main_ui.lineEdit_CNS.clear()
            self.main_ui.lineEdit_RG.clear()
            self.main_ui.comboBox_Sexo.setCurrentIndex(-1)
            self.main_ui.lineEdit_Numero.clear()
            self.main_ui.lineEdit_Cidade.clear()
            self.main_ui.lineEdit_Bairro.clear()
            self.main_ui.comboBox_UF.setCurrentIndex(-1)
            #######################################################################################

            self.lista_de_pacientes()

        else:
            self.showErrorMessage(
                "Formulário não pôde ser salvo.\nVerifique os campos e tente novamente.")
            print(paciente.status_code)

    def Atualizar_Dados_Do_Paciente(self, id):

        try:
            dados = {
                "login": {
                    "name": f"{self.main_ui.lineEdit_Nome.text()}",
                    "last_name": f"{self.main_ui.lineEdit_Sobrenome.text()}",
                    "password": "padrao",
                    "email": f"{self.main_ui.lineEdit_Email.text()}",
                    "data_nascimento": self.main_ui.dateEdit_Nascimento.date().toString("yyyy/MM/dd") or '2000/01/01',
                    "cns": f"{self.main_ui.lineEdit_CNS.text()}" or '-',
                    "rg": f"{self.main_ui.lineEdit_RG.text()}" or '-',
                    "cpf": f"{self.main_ui.lineEdit_CPF.text()}" or '-'
                },
                "informacao": {
                    "telefone": f"{self.main_ui.lineEdit_Telefone.text()}" or '-',
                    "foto": "vazio",
                    "sexo": f"{self.main_ui.comboBox_Sexo.currentText()}" or '-',
                    "endereco": "Não tem",
                    "numero": f"{self.main_ui.lineEdit_Numero.text()}" or '-',
                    "cidade": f'{self.main_ui.lineEdit_Cidade.text()}' or '-',
                    "bairro": f"{self.main_ui.lineEdit_Bairro.text()}" or '-',
                    "estado": f"{self.main_ui.comboBox_UF.currentText()}" or '-'
                },
                "doctor": {

                }
            }

            response = requests.post(
                f'http://127.0.0.1:8000/api/user/update/{id}', json=dados, headers={'Content-type': 'application/json'})
            print(id)

            if response.status_code != 200:
                print('Resposta do servidor:', response.status_code)
                self.main_ui.lineEdit_Nome.clear()
                self.main_ui.lineEdit_Sobrenome.clear()
                self.main_ui.lineEdit_Email.clear()
                self.main_ui.dateEdit_Nascimento.clear()
                self.main_ui.lineEdit_Telefone.clear()
                self.main_ui.lineEdit_CNS.clear()
                self.main_ui.lineEdit_RG.clear()
                self.main_ui.comboBox_Sexo.setCurrentIndex(-1)
                self.main_ui.lineEdit_Numero.clear()
                self.main_ui.lineEdit_Cidade.clear()
                self.main_ui.lineEdit_Bairro.clear()
                self.main_ui.comboBox_UF.setCurrentIndex(-1)
        except:
            self.showErrorMessage(
                "Não é possível atualizar um paciente que não esteja cadastrado.")

    def salvar_Receitas(self) -> dict:

        receita = {
            'user_id': self.id_paciente,
            'doctor_id': "admn",
            'medicamento': "-",
            'observacoes': f"{self.main_ui.textEdit_Prescricao.toPlainText()}",
            'data_emissao': "-",
            'data_expiracao': "-",
        }
        print(receita)

        data = json.dumps(receita)  # Serializar o dicionário para JSON

        con = requests.post('http://127.0.0.1:8000/api/receita/create',
                            data=data, headers={'Content-type': 'application/json'})

        if con.status_code == 200:
            print(con.status_code)

            self.main_ui.Paginas_Principais.setCurrentWidget(
                self.main_ui.pg_Pacientes)
            self.main_ui.textEdit_Prescricao.clear()

        else:
            self.showErrorMessage("A consulta não pôde ser salva.")
            print(con.status_code)

    # Message Box #########################################################################

    def showInfoMessage(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Sucesso")
        msg_box.setText(message)
        msg_box.exec_()

    def showErrorMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Erro")
        msg.exec_()

    def showYesNoMessage(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Confirmação")
        msg_box.setText("Deseja salvar as alterações?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        self.result = msg_box.exec_()
    #######################################################################################


# Inicializa o gerenciador de login ###################################################
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    login_manager = Login()
    login_manager.show()

    app.exec_()
#######################################################################################
