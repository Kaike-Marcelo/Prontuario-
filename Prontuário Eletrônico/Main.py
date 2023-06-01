import json
import requests

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

from ui_Login import Ui_Principal_Login
from ui_Main import Ui_Principal_Main
from MessageBox import *


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicializa a tela de login
        self.login_ui = Ui_Principal_Login()
        self.login_ui.setupUi(self)

        # Conecta o botão de login com a função que fecha a tela de login e abre a tela principal
        self.login_ui.btn_Entrar.clicked.connect(self.login)

    def login(self) -> dict:

        try:
            # Cria um objeto Session para manter a conexão com o servidor
            session = requests.Session()

            # Faz a autenticação utilizando o HTTP Basic Authentication
            email = 'Paulo@gmail.comm'
            senha = 'carvalho1000'
            dados = {"email": email, "password": senha}

            try:
                con = requests.post(
                    'http://127.0.0.1:8000/api/token', data=dados)

            except:
                self.showErrorMessage("Erro de Login. Tente Novamente.")

            # print(con)

            self.Principal_Main()
            self.show()  # Exibe a janela principal

        except requests.exceptions.HTTPError as e:
            self.showErrorMessage(f"Erro de HTTP: {e}")

        except requests.exceptions.RequestException as e:
            self.showErrorMessage(f"Erro de requisição: {e}")

    def Principal_Main(self):
        self.login_ui.centralwidget_Login.close()  # Fecha a tela de login
        self.main_ui = Ui_Principal_Main()  # Atualiza a interface da janela principal
        self.main_ui.setupUi(self)
        self.showMaximized()  # Configura a janela principal como maximizada

        '''
        self.main_ui.btn_Inicio.clicked.connect(
            lambda: self.main_ui.PaginasPrincipais.setCurrentWidget(self.main_ui.pg_Inicial))
        '''
        self.main_ui.btn_Paciente.clicked.connect(
            lambda: self.main_ui.PaginasPrincipais.setCurrentWidget(self.main_ui.pg_Paciente))

        self.main_ui.btn_NovoPaciente.clicked.connect(
            lambda: self.btn_novo_paciente_clicked())

        self.main_ui.btn_DadosPrincipais.clicked.connect(
            lambda: self.main_ui.Paginas_Formulario.setCurrentWidget(self.main_ui.pg_DadosPrincipais))
        self.main_ui.btn_OutrosDados.clicked.connect(
            lambda: self.main_ui.Paginas_Formulario.setCurrentWidget(self.main_ui.pg_OutrosDados))

        self.main_ui.btn_Prontuario.clicked.connect(
            lambda: self.main_ui.PaginasPrincipais.setCurrentWidget(self.main_ui.pg_Prontuario))

        self.main_ui.btn_Menu.clicked.connect(lambda: self.menu_vertical())
        self.main_ui.btn_Paciente.clicked.connect(
            lambda: self.lista_de_pacientes())

        # Desativa o botão SALVAR inicialmente
        self.main_ui.btn_Salvar.setEnabled(False)

        # Conecta o sinal textChanged do QLineEdit ao slot que habilita ou desabilita o botão "Salvar"
        self.main_ui.lineEdit_Nome.textChanged.connect(
            self.atualizaBotaoSalvar)
        self.main_ui.btn_Salvar.clicked.connect(
            lambda: self.Salvar_NovoPaciente())

        self.main_ui.lineEdit_PesquisarPaciente.returnPressed.connect(
            self.pesquisar_paciente)

        # Definir o modo de seleção para seleção de linhas inteiras
        self.main_ui.tableWidget_ListaPacientes.setSelectionBehavior(
            QAbstractItemView.SelectRows)

        # Conectar o sinal cellClicked ao slot selecionar_linha
        self.main_ui.tableWidget_ListaPacientes.cellClicked.connect(
            self.controle_de_clicks_ListaPacientes)
        

        # Definir o modo de seleção para seleção de linhas inteiras
        self.main_ui.tableWidget_ListaPacientes.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Conectar o sinal cellClicked ao slot selecionar_linha
        self.main_ui.tableWidget_ListaPacientes.cellDoubleClicked.connect(lambda: self.selecionar_linha)
    

        self.ultima_coluna_clicada = -1 #Atributo de método de clicks


    def atualizaBotaoSalvar(self): # Habilita o botão "Salvar" apenas se houver algum texto no QLineEdit

        if self.main_ui.lineEdit_Nome.text():
            self.main_ui.btn_Salvar.setEnabled(True)
        else:
            self.main_ui.btn_Salvar.setEnabled(False)


    def pesquisar_paciente(self):
        pesquisar_paciente = self.main_ui.lineEdit_PesquisarPaciente.text()

        if pesquisar_paciente:
            print("FUNCIONAAAA")
        # Aqui vai a lógica para pesquisar com base no texto inserido na lineedit


    def keyPressEvent(self, event):  # Pesquisar quando clicar na tecla 'ENTER'
        if event.key() == Qt.Key_Return:
            self.pesquisar_paciente()
        else:
            super().keyPressEvent(event)


    def menu_vertical(self):

        visivel = self.main_ui.frame_BarraMenuVertical.width() > 60
        nova_largura = 60 if visivel else 140 # define a nova largura da barra de menu com base em seu estado atual
        self.main_ui.frame_BarraMenuVertical.setFixedWidth(nova_largura)

    '''
    def verificar(self):

        log = self.login()
        if log is not None:
            self.Principal_Main()

        self.show()  # Exibe a janela principal
    '''

    def btn_novo_paciente_clicked(self):
        self.main_ui.btn_Prontuario.setEnabled(False)
        self.main_ui.PaginasPrincipais.setCurrentWidget(
            self.main_ui.pgFormulario_NovoPaciente)

    def Salvar_NovoPaciente(self) -> dict:

        senha = (self.main_ui.lineEdit_Nome.text() + "A72A12")

        dados = {
            "login": {
                "name": self.main_ui.lineEdit_Nome.text() + "A72A12",
                "last_name": "aelson",
                "password": senha,
                "email": self.main_ui.lineEdit_Email.text(),
                "doctor": 1,
                "admin": 1
            },

            "informacao": {
                "data_nascimento": "2018-12-10",
                "telefone": "12345678",
                "foto": "3fdkfjsdldgdsg",
                "cns": "374885995",
                "rg": "488599604",
                "sexo": "masculino",
                "endereco": "uma rua qualquer",
                "numero": "234",
                "cidade": "Eunapolis",
                "bairro": "nao sei",
                "estado": "bahia"
            }

        }

        con = requests.post('http://127.0.0.1:8000/api/user/post',
                            data=json.dumps(dados), headers={'Content-type': 'application/json'})

        self.main_ui.btn_Prontuario.setEnabled(True)
        showInfoMessage("Formulário Salvo.")
        self.main_ui.PaginasPrincipais.setCurrentWidget(
            self.main_ui.pg_Paciente)


    def lista_de_pacientes(self) -> dict:

        con = requests.get('http://127.0.0.1:8000/api/user')
        pacientes = json.loads(con.text)
        self.main_ui.tableWidget_ListaPacientes.setRowCount(len(pacientes))
        self.main_ui.tableWidget_ListaPacientes.setColumnCount(4)

        # print(dados)
        # print(con.text)
        for linha, paciente in enumerate(pacientes):
            print()
            # dados_paciente = paciente.get("id")  # Substitua "id" pelo nome do atributo do dicionário que você deseja exibir

            # item = QTableWidgetItem(str(dados_paciente))

            # print(f"{coluna} : {paciente.get(coluna)}")
            self.main_ui.tableWidget_ListaPacientes.setItem(
                linha, 0, QTableWidgetItem(str(paciente.get("id"))))
            self.main_ui.tableWidget_ListaPacientes.setItem(
                linha, 1, QTableWidgetItem(str(paciente.get("email"))))
            self.main_ui.tableWidget_ListaPacientes.setItem(
                linha, 2, QTableWidgetItem(str(paciente.get("last_name"))))
            self.main_ui.tableWidget_ListaPacientes.setItem(
                linha, 3, QTableWidgetItem(str(paciente.get("name"))))
            # print(f"TERMINAL: {paciente} : {paciente.get('id')} -> {paciente.get('name')}")


    def selecionar_linha(self, item):
        
        index = self.main_ui.tableWidget_ListaPacientes.currentIndex() # Obter o índice da célula clicada
        row = index.row()  # Obter a linha correspondente ao índice
        num_colunas = self.main_ui.tableWidget_ListaPacientes.columnCount() # Obter o número de colunas da tabela
        
        self.main_ui.tableWidget_ListaPacientes.clearSelection() # Limpar a seleção atual da tabela

        for coluna in range(num_colunas): # Selecionar todas as colunas da linha clicada
            item = self.main_ui.tableWidget_ListaPacientes.item(row, coluna)
            item.setSelected(True)


    def click_duplo_ListaPacientes(self): # Lógica a ser executada quando ocorrer um duplo clique na célula
        
        if self.clicked_item:
            row = self.clicked_item.row()
            item_nome = self.item(row, 3)  # Assumindo que o item "nome" está na coluna 3
            valor_nome = item_nome.text()
            print("Valor do item 'nome':", valor_nome)
            #abrir_outra_pagina()

    
    def controle_de_clicks_ListaPacientes(self, event): #Controla o Double Click
        
        self.clicked_item = self.itemAt(event.pos())
        if self.clicked_item:
            self.double_click_timer.start(300)  # Defina o tempo máximo entre os cliques para reconhecer um duplo clique (em milissegundos)
        super().mouseDoubleClickEvent(event)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # Inicializa o gerenciador de login
    login_manager = Login()
    login_manager.show()

    app.exec_()
