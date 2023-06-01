import Img_Icons_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget


class Ui_Principal_Main(object):
    def setupUi(self, Principal_Main):
        Principal_Main.setObjectName("Principal_Main")
        Principal_Main.resize(768, 595)
        Principal_Main.setMinimumSize(QtCore.QSize(640, 480))
        Principal_Main.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Principal_Main.setDocumentMode(False)
        Principal_Main.setDockNestingEnabled(False)
        Principal_Main.setUnifiedTitleAndToolBarOnMac(False)
        self.Plano_de_Fundo = QtWidgets.QWidget(Principal_Main)
        self.Plano_de_Fundo.setStyleSheet("")
        self.Plano_de_Fundo.setObjectName("Plano_de_Fundo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Plano_de_Fundo)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_Cabecalho = QtWidgets.QFrame(self.Plano_de_Fundo)
        self.frame_Cabecalho.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_Cabecalho.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_Cabecalho.setStyleSheet("#frame_Cabecalho{background-color: rgb(13, 11, 189);\n"
                                           "}")
        self.frame_Cabecalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Cabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Cabecalho.setObjectName("frame_Cabecalho")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_Cabecalho)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_Menu = QtWidgets.QToolButton(self.frame_Cabecalho)
        self.btn_Menu.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_Menu.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_Menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Menu.setToolTipDuration(100000)
        self.btn_Menu.setStyleSheet("#btn_Menu:hover{\n"
                                    "background-color: rgb(41, 29, 128);\n"
                                    "border-color: None;\n"
                                    "border-top-right-radius: 12px;\n"
                                    "border-bottom-right-radius: 12px;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QToolButton:checked {\n"
                                    "    color: white;\n"
                                    "    background-color: rgb(18, 13, 129);\n"
                                    "    border:None;\n"
                                    "    border-radius: 5px;\n"
                                    "}\n"
                                    "QToolButton:!checked {\n"
                                    "    color: white;\n"
                                    "    background-color: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "#btn_Menu:pressed{\n"
                                    "background-color: darkblue;\n"
                                    "border-radius: 26px;\n"
                                    "}")
        self.btn_Menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icones/Icon_Menu_Normal.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Menu.setIcon(icon)
        self.btn_Menu.setIconSize(QtCore.QSize(50, 50))
        self.btn_Menu.setCheckable(True)
        self.btn_Menu.setAutoExclusive(True)
        self.btn_Menu.setAutoRaise(False)
        self.btn_Menu.setArrowType(QtCore.Qt.NoArrow)
        self.btn_Menu.setObjectName("btn_Menu")
        self.horizontalLayout_2.addWidget(self.btn_Menu)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_Perfil = QtWidgets.QToolButton(self.frame_Cabecalho)
        self.btn_Perfil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Perfil.setToolTipDuration(10000)
        self.btn_Perfil.setAutoFillBackground(False)
        self.btn_Perfil.setStyleSheet("#btn_Perfil{\n"
                                      "background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_Perfil:pressed{\n"
                                      "background-color: darkblue;\n"
                                      "border-radius: 24px;\n"
                                      "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icones/icon_Perfil.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Perfil.setIcon(icon1)
        self.btn_Perfil.setIconSize(QtCore.QSize(40, 40))
        self.btn_Perfil.setObjectName("btn_Perfil")
        self.horizontalLayout_2.addWidget(self.btn_Perfil)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_Minimizar = QtWidgets.QToolButton(self.frame_Cabecalho)
        self.btn_Minimizar.setMinimumSize(QtCore.QSize(50, 0))
        self.btn_Minimizar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_Minimizar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Minimizar.setToolTipDuration(10000)
        self.btn_Minimizar.setStyleSheet("#btn_Minimizar{\n"
                                         "background-color:transparent;\n"
                                         "}\n"
                                         "\n"
                                         "#btn_Minimizar:hover{\n"
                                         "background-color: rgb(24, 17, 254);\n"
                                         "border-radius: 26px;\n"
                                         "}\n"
                                         "\n"
                                         "#btn_Minimizar:pressed{\n"
                                         "background-color: darkblue;\n"
                                         "border-radius: 26px;\n"
                                         "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icones/icon_Minimizar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Minimizar.setIcon(icon2)
        self.btn_Minimizar.setIconSize(QtCore.QSize(20, 40))
        self.btn_Minimizar.setObjectName("btn_Minimizar")
        self.horizontalLayout_2.addWidget(self.btn_Minimizar)
        self.btn_Maximizar = QtWidgets.QToolButton(self.frame_Cabecalho)
        self.btn_Maximizar.setMinimumSize(QtCore.QSize(50, 0))
        self.btn_Maximizar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_Maximizar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Maximizar.setToolTipDuration(1000)
        self.btn_Maximizar.setStyleSheet("#btn_Maximizar{\n"
                                         "background-color:transparent;\n"
                                         "}\n"
                                         "\n"
                                         "#btn_Maximizar:hover{\n"
                                         "background-color: rgb(24, 17, 254);\n"
                                         "border-radius: 26px;\n"
                                         "}\n"
                                         "\n"
                                         "#btn_Maximizar:pressed{\n"
                                         "background-color: darkblue;\n"
                                         "border-radius: 26px;\n"
                                         "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icones/icon_Maximizar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Maximizar.setIcon(icon3)
        self.btn_Maximizar.setIconSize(QtCore.QSize(20, 40))
        self.btn_Maximizar.setObjectName("btn_Maximizar")
        self.horizontalLayout_2.addWidget(self.btn_Maximizar)
        self.btn_Fechar = QtWidgets.QToolButton(self.frame_Cabecalho)
        self.btn_Fechar.setMinimumSize(QtCore.QSize(50, 0))
        self.btn_Fechar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_Fechar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Fechar.setToolTipDuration(1000)
        self.btn_Fechar.setStyleSheet("#btn_Fechar{\n"
                                      "background-color:transparent;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_Fechar:hover{\n"
                                      "background-color: rgb(24, 17, 254);\n"
                                      "border-radius: 26px;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_Fechar:pressed{\n"
                                      "background-color: darkblue;\n"
                                      "border-radius: 26px;\n"
                                      "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icones/icon_Fechar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Fechar.setIcon(icon4)
        self.btn_Fechar.setIconSize(QtCore.QSize(20, 40))
        self.btn_Fechar.setObjectName("btn_Fechar")
        self.horizontalLayout_2.addWidget(self.btn_Fechar)
        self.verticalLayout.addWidget(self.frame_Cabecalho)
        self.frame_CorpoGeral = QtWidgets.QFrame(self.Plano_de_Fundo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_CorpoGeral.sizePolicy().hasHeightForWidth())
        self.frame_CorpoGeral.setSizePolicy(sizePolicy)
        self.frame_CorpoGeral.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_CorpoGeral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CorpoGeral.setObjectName("frame_CorpoGeral")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_CorpoGeral)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_BarraMenuVertical = QtWidgets.QFrame(self.frame_CorpoGeral)
        self.frame_BarraMenuVertical.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_BarraMenuVertical.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frame_BarraMenuVertical.setAutoFillBackground(False)
        self.frame_BarraMenuVertical.setStyleSheet("#frame_BarraMenuVertical{\n"
                                                   "background-color: qlineargradient(spread:pad, x1:0.293, y1:1, x2:0.279, y2:0, stop:0 rgba(13, 11, 189, 255), stop:0.487562 rgba(24, 17, 255, 255), stop:1 rgba(13, 11, 189, 255));\n"
                                                   "\n"
                                                   "border: None;\n"
                                                   "\n"
                                                   "border-top: 1px solid rgba(0,0,0,70);\n"
                                                   "border-right: 1px solid rgba(0,0,0,70);\n"
                                                   "\n"
                                                   "}\n"
                                                   "\n"
                                                   "QToolButton:checked {\n"
                                                   "background: rgb(13, 11, 189);\n"
                                                   "color: white;\n"
                                                   "border: None;\n"
                                                   "\n"
                                                   "}\n"
                                                   "QToolButton:!checked {\n"
                                                   "background: transparent;\n"
                                                   "color: white;\n"
                                                   "border: None\n"
                                                   "\n"
                                                   "}")
        self.frame_BarraMenuVertical.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_BarraMenuVertical.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_BarraMenuVertical.setObjectName("frame_BarraMenuVertical")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.frame_BarraMenuVertical)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 143, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        '''
        self.btn_Inicio = QtWidgets.QToolButton(self.frame_BarraMenuVertical)
        '''

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        '''
        sizePolicy.setHeightForWidth(
            self.btn_Inicio.sizePolicy().hasHeightForWidth())
        self.btn_Inicio.setSizePolicy(sizePolicy)
        self.btn_Inicio.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_Inicio.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Inicio.setFont(font)
        self.btn_Inicio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Inicio.setToolTipDuration(100000)
        self.btn_Inicio.setAutoFillBackground(False)
        self.btn_Inicio.setStyleSheet("#btn_Inicio:hover{\n"
                                      "background-color: rgb(41, 29, 128);\n"
                                      "border-top-right-radius: 12px;\n"
                                      "border-bottom-right-radius: 12px;\n"
                                      "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icones/icone_Inicio.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Inicio.setIcon(icon5)
        self.btn_Inicio.setIconSize(QtCore.QSize(50, 50))
        self.btn_Inicio.setCheckable(True)
        self.btn_Inicio.setChecked(True)
        self.btn_Inicio.setAutoExclusive(True)
        self.btn_Inicio.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_Inicio.setObjectName("btn_Inicio")
        '''
        self.buttonGroup_MenuVertical = QtWidgets.QButtonGroup(Principal_Main)
        self.buttonGroup_MenuVertical.setObjectName("buttonGroup_MenuVertical")
        #self.buttonGroup_MenuVertical.addButton(self.btn_Inicio)
        #self.verticalLayout_2.addWidget(self.btn_Inicio)
        

        self.btn_Paciente = QtWidgets.QToolButton(self.frame_BarraMenuVertical)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Paciente.sizePolicy().hasHeightForWidth())
        self.btn_Paciente.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Paciente.setFont(font)
        self.btn_Paciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Paciente.setToolTipDuration(10000)
        self.btn_Paciente.setStyleSheet("#btn_Paciente:hover{\n"
                                        "background-color: rgb(41, 29, 128);\n"
                                        "border-top-right-radius: 12px;\n"
                                        "border-bottom-right-radius: 12px;\n"
                                        "}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icones/icone_Pacientes.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Paciente.setIcon(icon6)
        self.btn_Paciente.setIconSize(QtCore.QSize(50, 50))
        self.btn_Paciente.setCheckable(True)
        self.btn_Paciente.setChecked(True)
        self.btn_Paciente.setAutoExclusive(True)
        self.btn_Paciente.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_Paciente.setObjectName("btn_Paciente")
        self.buttonGroup_MenuVertical.addButton(self.btn_Paciente)
        self.verticalLayout_2.addWidget(self.btn_Paciente)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 143, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.frame_BarraMenuVertical)

        self.PaginasPrincipais = QtWidgets.QStackedWidget(
            self.frame_CorpoGeral)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.PaginasPrincipais.sizePolicy().hasHeightForWidth())
        self.PaginasPrincipais.setSizePolicy(sizePolicy)
        self.PaginasPrincipais.setAutoFillBackground(True)
        self.PaginasPrincipais.setStyleSheet("#pg_Inicial{\n"
                                             "border-image: url(:/Imagens/Background_Geral.png);\n"
                                             "}\n"
                                             "\n"
                                             "#pg_Paciente{\n"
                                             "border-image: url(:/Imagens/Background_Geral.png);\n"
                                             "}\n"
                                             "\n"
                                             "#pgFormulario_NovoPaciente{\n"
                                             "border-image: url(:/Imagens/Background_Geral.png);\n"
                                             "}")
        self.PaginasPrincipais.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PaginasPrincipais.setFrameShadow(QtWidgets.QFrame.Plain)
        self.PaginasPrincipais.setObjectName("PaginasPrincipais")
        '''
        self.pg_Inicial = QtWidgets.QWidget()
        self.pg_Inicial.setMinimumSize(QtCore.QSize(0, 0))
        self.pg_Inicial.setObjectName("pg_Inicial")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.pg_Inicial)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(40)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.scrollArea_Inicial = QtWidgets.QScrollArea(self.pg_Inicial)
        self.scrollArea_Inicial.setStyleSheet("#scrollAreaWidget_Inicial{\n"
                                              "background-color: transparent;\n"
                                              "border-top-right-radius: 12px;\n"
                                              "border-bottom-right-radius: 12px;\n"
                                              "border-bottom-left-radius: 12px;\n"
                                              "}\n"
                                              "\n"
                                              "QAbstractScrollArea#scrollArea_Inicial {\n"
                                              "    background-color: transparent;\n"
                                              "}")
        self.scrollArea_Inicial.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_Inicial.setWidgetResizable(True)
        self.scrollArea_Inicial.setObjectName("scrollArea_Inicial")
        self.scrollAreaWidget_Inicial = QtWidgets.QWidget()
        self.scrollAreaWidget_Inicial.setGeometry(QtCore.QRect(0, 0, 830, 524))
        self.scrollAreaWidget_Inicial.setObjectName("scrollAreaWidget_Inicial")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(
            self.scrollAreaWidget_Inicial)
        self.horizontalLayout_19.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_19.setSpacing(30)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frameInicioEsquerda = QtWidgets.QFrame(
            self.scrollAreaWidget_Inicial)
        self.frameInicioEsquerda.setMinimumSize(QtCore.QSize(0, 0))
        self.frameInicioEsquerda.setMaximumSize(QtCore.QSize(460, 16777215))
        self.frameInicioEsquerda.setStyleSheet("background-color: transparent;\n"
                                               " color: white;")
        self.frameInicioEsquerda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameInicioEsquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInicioEsquerda.setObjectName("frameInicioEsquerda")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameInicioEsquerda)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.label_Calendario = QtWidgets.QLabel(self.frameInicioEsquerda)
        self.label_Calendario.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Calendario.setFont(font)
        self.label_Calendario.setStyleSheet("#label_AcessosRecentes{\n"
                                            "color: white;\n"
                                            "}")
        self.label_Calendario.setTextFormat(QtCore.Qt.AutoText)
        self.label_Calendario.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Calendario.setObjectName("label_Calendario")
        self.verticalLayout_6.addWidget(self.label_Calendario)
        self.calendario_Inicio = QtWidgets.QCalendarWidget(
            self.frameInicioEsquerda)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.calendario_Inicio.sizePolicy().hasHeightForWidth())
        self.calendario_Inicio.setSizePolicy(sizePolicy)
        self.calendario_Inicio.setMinimumSize(QtCore.QSize(340, 0))
        self.calendario_Inicio.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.calendario_Inicio.setFont(font)
        self.calendario_Inicio.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calendario_Inicio.setMouseTracking(False)
        self.calendario_Inicio.setTabletTracking(False)
        self.calendario_Inicio.setFocusPolicy(QtCore.Qt.NoFocus)
        self.calendario_Inicio.setAcceptDrops(False)
        self.calendario_Inicio.setStyleSheet("#calendario_Inicio QAbstractItemView:enabled {\n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             "    color: blue;\n"
                                             "}\n"
                                             "\n"
                                             "#calendario_Inicio QAbstractItemView:selected {\n"
                                             "    background-color: #1E90FF;\n"
                                             "    color: white;\n"
                                             "}")
        self.calendario_Inicio.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendario_Inicio.setGridVisible(False)
        self.calendario_Inicio.setSelectionMode(
            QtWidgets.QCalendarWidget.SingleSelection)
        self.calendario_Inicio.setHorizontalHeaderFormat(
            QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendario_Inicio.setVerticalHeaderFormat(
            QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendario_Inicio.setObjectName("calendario_Inicio")
        self.verticalLayout_6.addWidget(self.calendario_Inicio)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_19.addWidget(self.frameInicioEsquerda)
        self.frame_InicialDireita = QtWidgets.QFrame(
            self.scrollAreaWidget_Inicial)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_InicialDireita.sizePolicy().hasHeightForWidth())
        self.frame_InicialDireita.setSizePolicy(sizePolicy)
        self.frame_InicialDireita.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_InicialDireita.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.frame_InicialDireita.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_InicialDireita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_InicialDireita.setObjectName("frame_InicialDireita")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(
            self.frame_InicialDireita)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(
            373, 317, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.label_AcessosRecentes = QtWidgets.QLabel(
            self.frame_InicialDireita)
        self.label_AcessosRecentes.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_AcessosRecentes.setFont(font)
        self.label_AcessosRecentes.setStyleSheet("#label_AcessosRecentes{\n"
                                                 "color: white;\n"
                                                 "}")
        self.label_AcessosRecentes.setTextFormat(QtCore.Qt.AutoText)
        self.label_AcessosRecentes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_AcessosRecentes.setObjectName("label_AcessosRecentes")
        self.verticalLayout_8.addWidget(self.label_AcessosRecentes)
        self.frame_ultimosAcessos = QtWidgets.QFrame(self.frame_InicialDireita)
        self.frame_ultimosAcessos.setMinimumSize(QtCore.QSize(0, 260))
        self.frame_ultimosAcessos.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_ultimosAcessos.setAutoFillBackground(False)
        self.frame_ultimosAcessos.setStyleSheet("#frame_ultimosAcessos{\n"
                                                "background-color: rgba(255, 255, 255, 204);\n"
                                                "border-radius: 12px;\n"
                                                "}")
        self.frame_ultimosAcessos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ultimosAcessos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ultimosAcessos.setObjectName("frame_ultimosAcessos")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(
            self.frame_ultimosAcessos)
        self.verticalLayout_9.setContentsMargins(50, 20, 40, 20)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tableWidget_AcessosRecentes = QtWidgets.QTableWidget(
            self.frame_ultimosAcessos)
        self.tableWidget_AcessosRecentes.setStyleSheet("#tableWidget_AcessosRecentes{\n"
                                                       " background-color: transparent;\n"
                                                       "gridline-color: blue;}\n"
                                                       "\n"
                                                       "QHeaderView::section {\n"
                                                       "    background-color: rgb(13, 11, 189);\n"
                                                       "    color: white;\n"
                                                       "    font-weight: bold;\n"
                                                       "    font-size: 12px;\n"
                                                       "    height: 25px;\n"
                                                       "    padding-left: 5px;\n"
                                                       "    border: none;\n"
                                                       "}\n"
                                                       "")
        self.tableWidget_AcessosRecentes.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.tableWidget_AcessosRecentes.setObjectName(
            "tableWidget_AcessosRecentes")
        self.tableWidget_AcessosRecentes.setColumnCount(2)
        self.tableWidget_AcessosRecentes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AcessosRecentes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_AcessosRecentes.setHorizontalHeaderItem(1, item)
        self.tableWidget_AcessosRecentes.horizontalHeader().setVisible(False)
        self.tableWidget_AcessosRecentes.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_AcessosRecentes.horizontalHeader().setHighlightSections(True)
        self.tableWidget_AcessosRecentes.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_AcessosRecentes.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_AcessosRecentes.verticalHeader().setVisible(False)
        self.tableWidget_AcessosRecentes.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_9.addWidget(self.tableWidget_AcessosRecentes)
        self.verticalLayout_8.addWidget(self.frame_ultimosAcessos)
        spacerItem8 = QtWidgets.QSpacerItem(
            373, 317, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(
            373, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_19.addWidget(self.frame_InicialDireita)
        self.scrollArea_Inicial.setWidget(self.scrollAreaWidget_Inicial)
        self.horizontalLayout_18.addWidget(self.scrollArea_Inicial)
        self.PaginasPrincipais.addWidget(self.pg_Inicial)
        '''
        

        self.pg_Paciente = QtWidgets.QWidget()
        self.pg_Paciente.setObjectName("pg_Paciente")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pg_Paciente)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frameEsquerda_Pacientes = QtWidgets.QFrame(self.pg_Paciente)
        self.frameEsquerda_Pacientes.setMinimumSize(QtCore.QSize(0, 0))
        self.frameEsquerda_Pacientes.setMaximumSize(
            QtCore.QSize(400, 16777215))
        self.frameEsquerda_Pacientes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameEsquerda_Pacientes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEsquerda_Pacientes.setObjectName("frameEsquerda_Pacientes")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.frameEsquerda_Pacientes)
        self.verticalLayout_4.setContentsMargins(0, 35, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frameEsquerda_PesquisarAdicionar = QtWidgets.QFrame(
            self.frameEsquerda_Pacientes)
        self.frameEsquerda_PesquisarAdicionar.setMinimumSize(
            QtCore.QSize(0, 170))
        self.frameEsquerda_PesquisarAdicionar.setAutoFillBackground(False)
        self.frameEsquerda_PesquisarAdicionar.setStyleSheet("#frameEsquerda_PesquisarAdicionar{\n"
                                                            "background-color: rgba(255, 255, 255, 204);\n"
                                                            "border-radius: 12px;\n"
                                                            "}")
        self.frameEsquerda_PesquisarAdicionar.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.frameEsquerda_PesquisarAdicionar.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.frameEsquerda_PesquisarAdicionar.setObjectName(
            "frameEsquerda_PesquisarAdicionar")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.frameEsquerda_PesquisarAdicionar)
        self.verticalLayout_5.setContentsMargins(10, 5, 10, 10)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_BtnNovoPaciente = QtWidgets.QFrame(
            self.frameEsquerda_PesquisarAdicionar)
        self.frame_BtnNovoPaciente.setMinimumSize(QtCore.QSize(0, 68))
        self.frame_BtnNovoPaciente.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_BtnNovoPaciente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BtnNovoPaciente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BtnNovoPaciente.setObjectName("frame_BtnNovoPaciente")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(
            self.frame_BtnNovoPaciente)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.btn_NovoPaciente = QtWidgets.QToolButton(
            self.frame_BtnNovoPaciente)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_NovoPaciente.sizePolicy().hasHeightForWidth())
        self.btn_NovoPaciente.setSizePolicy(sizePolicy)
        self.btn_NovoPaciente.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_NovoPaciente.setFont(font)
        self.btn_NovoPaciente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_NovoPaciente.setToolTipDuration(100000)
        self.btn_NovoPaciente.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_NovoPaciente.setAutoFillBackground(False)
        self.btn_NovoPaciente.setStyleSheet("#btn_NovoPaciente{\n"
                                            "background-color: #0D0BBD;\n"
                                            "border-radius: 26px;\n"
                                            "color: white;\n"
                                            "}\n"
                                            "\n"
                                            "#btn_NovoPaciente:hover{\n"
                                            "background-color: rgb(24, 17, 254);\n"
                                            "border-radius: 26px;\n"
                                            "}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(
            ":/Icones/icon_Novo_Paciente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_NovoPaciente.setIcon(icon8)
        self.btn_NovoPaciente.setIconSize(QtCore.QSize(60, 60))
        self.btn_NovoPaciente.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_NovoPaciente.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_NovoPaciente.setAutoRaise(False)
        self.btn_NovoPaciente.setArrowType(QtCore.Qt.NoArrow)
        self.btn_NovoPaciente.setObjectName("btn_NovoPaciente")
        self.horizontalLayout_5.addWidget(self.btn_NovoPaciente)
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout_5.addWidget(self.frame_BtnNovoPaciente)
        self.frame_PesqusarPaciente = QtWidgets.QFrame(
            self.frameEsquerda_PesquisarAdicionar)
        self.frame_PesqusarPaciente.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_PesqusarPaciente.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame_PesqusarPaciente.setAutoFillBackground(False)
        self.frame_PesqusarPaciente.setStyleSheet("#frame_PesqusarPaciente{\n"
                                                  "background-color: #0D0BBD;\n"
                                                  "border-radius: 26px;\n"
                                                  "}")
        self.frame_PesqusarPaciente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_PesqusarPaciente.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_PesqusarPaciente.setObjectName("frame_PesqusarPaciente")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(
            self.frame_PesqusarPaciente)
        self.horizontalLayout_6.setContentsMargins(5, 0, 13, 0)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_IconePesquisarPaciente = QtWidgets.QFrame(
            self.frame_PesqusarPaciente)
        self.frame_IconePesquisarPaciente.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_IconePesquisarPaciente.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_IconePesquisarPaciente.setStyleSheet(
            "border-image: url(:/Icones/icon_Pesquisar_Pacientes.png);")
        self.frame_IconePesquisarPaciente.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.frame_IconePesquisarPaciente.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_IconePesquisarPaciente.setObjectName(
            "frame_IconePesquisarPaciente")
        self.horizontalLayout_6.addWidget(self.frame_IconePesquisarPaciente)
        self.lineEdit_PesquisarPaciente = QtWidgets.QLineEdit(
            self.frame_PesqusarPaciente)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_PesquisarPaciente.setFont(font)
        self.lineEdit_PesquisarPaciente.setToolTipDuration(100000)
        self.lineEdit_PesquisarPaciente.setStyleSheet("#lineEdit_PesquisarPaciente{\n"
                                                      "background-color: transparent;\n"
                                                      "color: white;\n"
                                                      "padding: 4px;\n"
                                                      "border-radius: 5px;\n"
                                                      "border-style: solid;\n"
                                                      "border-width: 2px;\n"
                                                      "border-color: white; \n"
                                                      "}")
        self.lineEdit_PesquisarPaciente.setObjectName(
            "lineEdit_PesquisarPaciente")
        self.horizontalLayout_6.addWidget(self.lineEdit_PesquisarPaciente)
        self.verticalLayout_5.addWidget(self.frame_PesqusarPaciente)
        self.verticalLayout_4.addWidget(self.frameEsquerda_PesquisarAdicionar)
        spacerItem12 = QtWidgets.QSpacerItem(
            20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.horizontalLayout_3.addWidget(self.frameEsquerda_Pacientes)
        self.frameDireita_Pacientes = QtWidgets.QFrame(self.pg_Paciente)
        self.frameDireita_Pacientes.setMinimumSize(QtCore.QSize(0, 0))
        self.frameDireita_Pacientes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameDireita_Pacientes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDireita_Pacientes.setObjectName("frameDireita_Pacientes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.frameDireita_Pacientes)
        self.verticalLayout_3.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameTopoDaDireita_Cabecalho = QtWidgets.QFrame(
            self.frameDireita_Pacientes)
        self.frameTopoDaDireita_Cabecalho.setMaximumSize(
            QtCore.QSize(16777215, 30))
        self.frameTopoDaDireita_Cabecalho.setAutoFillBackground(False)
        self.frameTopoDaDireita_Cabecalho.setStyleSheet(
            "background-color: transparent;")
        self.frameTopoDaDireita_Cabecalho.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.frameTopoDaDireita_Cabecalho.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frameTopoDaDireita_Cabecalho.setObjectName(
            "frameTopoDaDireita_Cabecalho")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self.frameTopoDaDireita_Cabecalho)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(25)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3.addWidget(self.frameTopoDaDireita_Cabecalho)
        self.frameDireitaBottom_ListaPacientes = QtWidgets.QFrame(
            self.frameDireita_Pacientes)
        self.frameDireitaBottom_ListaPacientes.setAutoFillBackground(False)
        self.frameDireitaBottom_ListaPacientes.setStyleSheet("#frameDireitaBottom_ListaPacientes{\n"
                                                             "background-color: rgba(255, 255, 255, 204);\n"
                                                             "border-radius: 12px;\n"
                                                             "}")
        self.frameDireitaBottom_ListaPacientes.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.frameDireitaBottom_ListaPacientes.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frameDireitaBottom_ListaPacientes.setObjectName(
            "frameDireitaBottom_ListaPacientes")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(
            self.frameDireitaBottom_ListaPacientes)
        self.verticalLayout_39.setContentsMargins(0, 11, 0, 11)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.tableWidget_ListaPacientes = QtWidgets.QTableWidget(
            self.frameDireitaBottom_ListaPacientes)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_ListaPacientes.setFont(font)
        self.tableWidget_ListaPacientes.setStyleSheet("#tableWidget_ListaPacientes{\n"
                                                      " background-color: transparent;\n"
                                                      "gridline-color: blue;}\n"
                                                      "\n"
                                                      "QHeaderView::section {\n"
                                                      "    background-color: rgb(13, 11, 189);\n"
                                                      "    color: white;\n"
                                                      "    font-weight: bold;\n"
                                                      "    font-size: 12px;\n"
                                                      "    height: 25px;\n"
                                                      "    padding-left: 10px;\n"
                                                      "    border: none;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QtableWidget QTableCornerButton::section{\n"
                                                      "background-color: rgb(0,0,0); \n"
                                                      "border: 1px solid rgb(0, 206, 151);\n"
                                                      "}")
        self.tableWidget_ListaPacientes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_ListaPacientes.setAutoScroll(True)
        self.tableWidget_ListaPacientes.setTabKeyNavigation(True)
        self.tableWidget_ListaPacientes.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_ListaPacientes.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_ListaPacientes.setShowGrid(False)
        self.tableWidget_ListaPacientes.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_ListaPacientes.setWordWrap(True)
        self.tableWidget_ListaPacientes.setCornerButtonEnabled(True)
        self.tableWidget_ListaPacientes.setObjectName(
            "tableWidget_ListaPacientes")
        self.tableWidget_ListaPacientes.setColumnCount(4)
        self.tableWidget_ListaPacientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_ListaPacientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_ListaPacientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_ListaPacientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_ListaPacientes.setHorizontalHeaderItem(3, item)
        self.tableWidget_ListaPacientes.horizontalHeader().setVisible(True)
        self.tableWidget_ListaPacientes.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ListaPacientes.horizontalHeader().setHighlightSections(True)
        self.tableWidget_ListaPacientes.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_ListaPacientes.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ListaPacientes.verticalHeader().setVisible(False)
        self.tableWidget_ListaPacientes.verticalHeader().setHighlightSections(True)
        self.tableWidget_ListaPacientes.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_ListaPacientes.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_39.addWidget(self.tableWidget_ListaPacientes)
        self.verticalLayout_3.addWidget(self.frameDireitaBottom_ListaPacientes)
        self.horizontalLayout_3.addWidget(self.frameDireita_Pacientes)
        self.PaginasPrincipais.addWidget(self.pg_Paciente)


        
        self.pg_Prontuario = QtWidgets.QWidget()
        self.pg_Prontuario.setStyleSheet("#pg_Prontuario{\n"
                                         "border-image: url(:/Imagens/Background_Geral.png);\n"
                                         "}")
        self.pg_Prontuario.setObjectName("pg_Prontuario")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.pg_Prontuario)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.frame_PerfilPaciente = QtWidgets.QFrame(self.pg_Prontuario)
        self.frame_PerfilPaciente.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_PerfilPaciente.setAutoFillBackground(False)
        self.frame_PerfilPaciente.setStyleSheet("#frame_PerfilPaciente{\n"
                                                "background-color: rgba(255, 255, 255, 204);\n"
                                                "border-radius: 12px;\n"
                                                "}")
        self.frame_PerfilPaciente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_PerfilPaciente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_PerfilPaciente.setObjectName("frame_PerfilPaciente")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(
            self.frame_PerfilPaciente)
        self.horizontalLayout_21.setContentsMargins(40, -1, -1, -1)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.labelPerfilPaciente = QtWidgets.QLabel(self.frame_PerfilPaciente)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelPerfilPaciente.setFont(font)
        self.labelPerfilPaciente.setStyleSheet("#labelPerfilPaciente{\n"
                                               "color: blue;\n"
                                               "}")
        self.labelPerfilPaciente.setObjectName("labelPerfilPaciente")
        self.horizontalLayout_21.addWidget(self.labelPerfilPaciente)
        self.verticalLayout_29.addWidget(self.frame_PerfilPaciente)
        self.frame_CorpoProntuario = QtWidgets.QFrame(self.pg_Prontuario)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_CorpoProntuario.sizePolicy().hasHeightForWidth())
        self.frame_CorpoProntuario.setSizePolicy(sizePolicy)
        self.frame_CorpoProntuario.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_CorpoProntuario.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_CorpoProntuario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CorpoProntuario.setObjectName("frame_CorpoProntuario")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(
            self.frame_CorpoProntuario)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.btn_NovaConsulta = QtWidgets.QToolButton(
            self.frame_CorpoProntuario)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_NovaConsulta.sizePolicy().hasHeightForWidth())
        self.btn_NovaConsulta.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_NovaConsulta.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_NovaConsulta.setFont(font)
        self.btn_NovaConsulta.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_NovaConsulta.setStyleSheet("#btn_NovaConsulta{\n"
                                            "background-color: rgb(0, 170, 255);\n"
                                            "border-radius: 12px;\n"
                                            "color: white;\n"
                                            "}\n"
                                            "\n"
                                            "#btn_NovaConsulta:hover{\n"
                                            "border-radius: 12px;\n"
                                            "background-color: rgb(75, 183, 255);\n"
                                            "}\n"
                                            "\n"
                                            "#btn_NovaConsulta:pressed{\n"
                                            "border-radius: 20px;\n"
                                            "background-color: rgb(0, 138, 207);\n"
                                            "}\n"
                                            "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(
            ":/Icones/icon_NovaConsulta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_NovaConsulta.setIcon(icon7)
        self.btn_NovaConsulta.setIconSize(QtCore.QSize(80, 80))
        self.btn_NovaConsulta.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_NovaConsulta.setAutoRaise(False)
        self.btn_NovaConsulta.setObjectName("btn_NovaConsulta")
        self.horizontalLayout_20.addWidget(self.btn_NovaConsulta)
        self.verticalLayout_29.addWidget(self.frame_CorpoProntuario)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 428, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem4)
        self.PaginasPrincipais.addWidget(self.pg_Prontuario)


        self.pgFormulario_NovoPaciente = QtWidgets.QWidget()
        self.pgFormulario_NovoPaciente.setMinimumSize(QtCore.QSize(0, 0))
        self.pgFormulario_NovoPaciente.setObjectName(
            "pgFormulario_NovoPaciente")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(
            self.pgFormulario_NovoPaciente)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frameFormulario_Btns = QtWidgets.QFrame(
            self.pgFormulario_NovoPaciente)
        self.frameFormulario_Btns.setMinimumSize(QtCore.QSize(0, 40))
        self.frameFormulario_Btns.setAutoFillBackground(False)
        self.frameFormulario_Btns.setStyleSheet("\n"
                                                "QToolButton:checked {\n"
                                                "    color: white;\n"
                                                "    background-color: rgba(45, 161, 239, 204);\n"
                                                "    border-top-right-radius: 5px;\n"
                                                "    border-top-left-radius: 5px;\n"
                                                "}\n"
                                                "QToolButton:!checked {\n"
                                                "    color: white;\n"
                                                "    background-color: rgba(23, 16, 69, 128);\n"
                                                "    border-top-right-radius: 5px;\n"
                                                "    border-top-left-radius: 5px;\n"
                                                "}")
        self.frameFormulario_Btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameFormulario_Btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFormulario_Btns.setObjectName("frameFormulario_Btns")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(
            self.frameFormulario_Btns)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_DadosPrincipais = QtWidgets.QToolButton(
            self.frameFormulario_Btns)
        self.btn_DadosPrincipais.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_DadosPrincipais.sizePolicy().hasHeightForWidth())
        self.btn_DadosPrincipais.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_DadosPrincipais.setFont(font)
        self.btn_DadosPrincipais.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_DadosPrincipais.setStyleSheet("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(
            ":/Icones/icon_DadosPrincipais.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_DadosPrincipais.setIcon(icon9)
        self.btn_DadosPrincipais.setIconSize(QtCore.QSize(50, 50))
        self.btn_DadosPrincipais.setCheckable(True)
        self.btn_DadosPrincipais.setChecked(True)
        self.btn_DadosPrincipais.setAutoExclusive(True)
        self.btn_DadosPrincipais.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_DadosPrincipais.setObjectName("btn_DadosPrincipais")
        self.buttonGroup_BtnFormulario = QtWidgets.QButtonGroup(Principal_Main)
        self.buttonGroup_BtnFormulario.setObjectName(
            "buttonGroup_BtnFormulario")
        self.buttonGroup_BtnFormulario.addButton(self.btn_DadosPrincipais)
        self.horizontalLayout_7.addWidget(self.btn_DadosPrincipais)
        self.btn_OutrosDados = QtWidgets.QToolButton(self.frameFormulario_Btns)
        self.btn_OutrosDados.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_OutrosDados.sizePolicy().hasHeightForWidth())
        self.btn_OutrosDados.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_OutrosDados.setFont(font)
        self.btn_OutrosDados.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_OutrosDados.setStyleSheet("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(
            ":/Icones/icon_OutrosDados.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_OutrosDados.setIcon(icon10)
        self.btn_OutrosDados.setIconSize(QtCore.QSize(50, 50))
        self.btn_OutrosDados.setCheckable(True)
        self.btn_OutrosDados.setChecked(False)
        self.btn_OutrosDados.setAutoExclusive(True)
        self.btn_OutrosDados.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_OutrosDados.setObjectName("btn_OutrosDados")
        self.buttonGroup_BtnFormulario.addButton(self.btn_OutrosDados)
        self.horizontalLayout_7.addWidget(self.btn_OutrosDados)
        self.btn_Consultas = QtWidgets.QToolButton(self.frameFormulario_Btns)
        self.btn_Consultas.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Consultas.sizePolicy().hasHeightForWidth())
        self.btn_Consultas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Consultas.setFont(font)
        self.btn_Consultas.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Consultas.setStyleSheet("#btn_Consultas{\n"
                                         "color: white;\n"
                                         "background-color: rgba(23, 16, 69, 128);\n"
                                         "border-top-right-radius: 5px;\n"
                                         "border-top-left-radius: 5px;\n"
                                         "}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(
            ":/Icones/icon_Consultas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Consultas.setIcon(icon11)
        self.btn_Consultas.setIconSize(QtCore.QSize(50, 50))
        self.btn_Consultas.setCheckable(True)
        self.btn_Consultas.setChecked(False)
        self.btn_Consultas.setAutoExclusive(True)
        self.btn_Consultas.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_Consultas.setObjectName("btn_Consultas")
        self.buttonGroup_BtnFormulario.addButton(self.btn_Consultas)
        self.horizontalLayout_7.addWidget(self.btn_Consultas)
        spacerItem13 = QtWidgets.QSpacerItem(
            528, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.frame_BtnsPront_Canc_Salve = QtWidgets.QFrame(
            self.frameFormulario_Btns)
        self.frame_BtnsPront_Canc_Salve.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_BtnsPront_Canc_Salve.setStyleSheet("#frame_BtnsPront_Canc_Salve{\n"
                                                      "background-color: rgba(46, 168, 241, 204);\n"
                                                      "border-top-left-radius: 5px;\n"
                                                      "border-top-right-radius: 5px;\n"
                                                      "}")
        self.frame_BtnsPront_Canc_Salve.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_BtnsPront_Canc_Salve.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BtnsPront_Canc_Salve.setObjectName(
            "frame_BtnsPront_Canc_Salve")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(
            self.frame_BtnsPront_Canc_Salve)
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_Salvar = QtWidgets.QToolButton(
            self.frame_BtnsPront_Canc_Salve)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Salvar.setFont(font)
        self.btn_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet("#btn_Salvar{\n"
                                      "background-color: rgb(26, 200, 219);\n"
                                      "color: white;\n"
                                      "border-radius: 10px;\n"
                                      "}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Icones/icon_Salvar.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Salvar.setIcon(icon12)
        self.btn_Salvar.setIconSize(QtCore.QSize(40, 40))
        self.btn_Salvar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_Salvar.setObjectName("btn_Salvar")
        self.horizontalLayout_8.addWidget(self.btn_Salvar)
        self.btn_Cancelar = QtWidgets.QToolButton(
            self.frame_BtnsPront_Canc_Salve)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Cancelar.sizePolicy().hasHeightForWidth())
        self.btn_Cancelar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cancelar.setFont(font)
        self.btn_Cancelar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Cancelar.setStyleSheet("#btn_Cancelar{\n"
                                        "background-color: rgb(242, 81, 101);\n"
                                        "color: white;\n"
                                        "border-radius: 10px;\n"
                                        "}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Icones/icon_Cancelar.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Cancelar.setIcon(icon13)
        self.btn_Cancelar.setIconSize(QtCore.QSize(40, 40))
        self.btn_Cancelar.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_Cancelar.setObjectName("btn_Cancelar")
        self.horizontalLayout_8.addWidget(self.btn_Cancelar)
        self.btn_Prontuario = QtWidgets.QToolButton(
            self.frame_BtnsPront_Canc_Salve)
        self.btn_Prontuario.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Prontuario.sizePolicy().hasHeightForWidth())
        self.btn_Prontuario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Prontuario.setFont(font)
        self.btn_Prontuario.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Prontuario.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_Prontuario.setStyleSheet("#btn_Prontuario{\n"
                                          "background-color: rgb(13, 10, 237);\n"
                                          "color: white;\n"
                                          "border-radius: 10px;\n"
                                          "}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(
            ":/Icones/icon_Prontuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Prontuario.setIcon(icon14)
        self.btn_Prontuario.setIconSize(QtCore.QSize(35, 40))
        self.btn_Prontuario.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_Prontuario.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_Prontuario.setObjectName("btn_Prontuario")
        self.horizontalLayout_8.addWidget(self.btn_Prontuario)
        self.horizontalLayout_7.addWidget(self.frame_BtnsPront_Canc_Salve)
        self.verticalLayout_7.addWidget(self.frameFormulario_Btns)
        self.Paginas_Formulario = QtWidgets.QStackedWidget(
            self.pgFormulario_NovoPaciente)
        self.Paginas_Formulario.setMinimumSize(QtCore.QSize(0, 0))
        self.Paginas_Formulario.setAutoFillBackground(False)
        self.Paginas_Formulario.setStyleSheet("")
        self.Paginas_Formulario.setObjectName("Paginas_Formulario")
        self.pg_DadosPrincipais = QtWidgets.QWidget()
        self.pg_DadosPrincipais.setAutoFillBackground(False)
        self.pg_DadosPrincipais.setStyleSheet("#pg_DadosPrincipais{\n"
                                              " background-color: rgba(46, 168, 241, 204)\n"
                                              "}\n"
                                              "")
        self.pg_DadosPrincipais.setObjectName("pg_DadosPrincipais")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.pg_DadosPrincipais)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.scrollArea_DadosPrincipais = QtWidgets.QScrollArea(
            self.pg_DadosPrincipais)
        self.scrollArea_DadosPrincipais.setAutoFillBackground(False)
        self.scrollArea_DadosPrincipais.setStyleSheet("#scrollAreaWidget_DadosPrincipais{\n"
                                                      "background-color: transparent;\n"
                                                      "border-top-right-radius: 12px;\n"
                                                      "border-bottom-right-radius: 12px;\n"
                                                      "border-bottom-left-radius: 12px;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QAbstractScrollArea#scrollArea_DadosPrincipais {\n"
                                                      "    background-color: transparent;\n"
                                                      "}")
        self.scrollArea_DadosPrincipais.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_DadosPrincipais.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_DadosPrincipais.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_DadosPrincipais.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_DadosPrincipais.setWidgetResizable(True)
        self.scrollArea_DadosPrincipais.setObjectName(
            "scrollArea_DadosPrincipais")
        self.scrollAreaWidget_DadosPrincipais = QtWidgets.QWidget()
        self.scrollAreaWidget_DadosPrincipais.setGeometry(
            QtCore.QRect(0, 0, 643, 801))
        self.scrollAreaWidget_DadosPrincipais.setStyleSheet("")
        self.scrollAreaWidget_DadosPrincipais.setObjectName(
            "scrollAreaWidget_DadosPrincipais")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidget_DadosPrincipais)
        self.verticalLayout_36.setSpacing(15)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.label_Identificacao = QtWidgets.QLabel(
            self.scrollAreaWidget_DadosPrincipais)
        self.label_Identificacao.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Identificacao.setFont(font)
        self.label_Identificacao.setStyleSheet("#label_Identificacao{\n"
                                               "color: white;\n"
                                               "}")
        self.label_Identificacao.setObjectName("label_Identificacao")
        self.verticalLayout_36.addWidget(self.label_Identificacao)
        self.frame_Identificacao = QtWidgets.QFrame(
            self.scrollAreaWidget_DadosPrincipais)
        self.frame_Identificacao.setMaximumSize(QtCore.QSize(16777215, 230))
        self.frame_Identificacao.setAutoFillBackground(False)
        self.frame_Identificacao.setStyleSheet("#frame_Identificacao{\n"
                                               "background-color: rgba(255, 255, 255, 229);\n"
                                               "border-radius: 12px;\n"
                                               "}")
        self.frame_Identificacao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Identificacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Identificacao.setObjectName("frame_Identificacao")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(
            self.frame_Identificacao)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_Identificacao_Coluna1 = QtWidgets.QFrame(
            self.frame_Identificacao)
        self.frame_Identificacao_Coluna1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Identificacao_Coluna1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_Identificacao_Coluna1.setStyleSheet("#label_Nome{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "#label_NomeSocial{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "#label_Naturalidade{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "#lineEdit_Nome{\n"
                                                       "color: white;\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "#lineEdit_NomeSocial{\n"
                                                       "color: white;\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "#lineEdit_Naturalidade{\n"
                                                       "color: white;\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}")
        self.frame_Identificacao_Coluna1.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.frame_Identificacao_Coluna1.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_Identificacao_Coluna1.setObjectName(
            "frame_Identificacao_Coluna1")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(
            self.frame_Identificacao_Coluna1)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_Nome = QtWidgets.QLabel(self.frame_Identificacao_Coluna1)
        self.label_Nome.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Nome.setFont(font)
        self.label_Nome.setObjectName("label_Nome")
        self.verticalLayout_10.addWidget(self.label_Nome)
        self.lineEdit_Nome = QtWidgets.QLineEdit(
            self.frame_Identificacao_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Nome.setFont(font)
        self.lineEdit_Nome.setObjectName("lineEdit_Nome")
        self.verticalLayout_10.addWidget(self.lineEdit_Nome)
        self.label_NomeSocial = QtWidgets.QLabel(
            self.frame_Identificacao_Coluna1)
        self.label_NomeSocial.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NomeSocial.setFont(font)
        self.label_NomeSocial.setObjectName("label_NomeSocial")
        self.verticalLayout_10.addWidget(self.label_NomeSocial)
        self.lineEdit_NomeSocial = QtWidgets.QLineEdit(
            self.frame_Identificacao_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_NomeSocial.setFont(font)
        self.lineEdit_NomeSocial.setObjectName("lineEdit_NomeSocial")
        self.verticalLayout_10.addWidget(self.lineEdit_NomeSocial)
        self.label_Naturalidade = QtWidgets.QLabel(
            self.frame_Identificacao_Coluna1)
        self.label_Naturalidade.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Naturalidade.setFont(font)
        self.label_Naturalidade.setObjectName("label_Naturalidade")
        self.verticalLayout_10.addWidget(self.label_Naturalidade)
        self.lineEdit_Naturalidade = QtWidgets.QLineEdit(
            self.frame_Identificacao_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Naturalidade.setFont(font)
        self.lineEdit_Naturalidade.setObjectName("lineEdit_Naturalidade")
        self.verticalLayout_10.addWidget(self.lineEdit_Naturalidade)
        self.horizontalLayout_9.addWidget(self.frame_Identificacao_Coluna1)
        self.frame_Identificacao_Coluna2 = QtWidgets.QFrame(
            self.frame_Identificacao)
        self.frame_Identificacao_Coluna2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Identificacao_Coluna2.setMaximumSize(
            QtCore.QSize(200, 16777215))
        self.frame_Identificacao_Coluna2.setStyleSheet("#label_CPF{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "#label_RG{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "#label_Emissor{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "#lineEdit_CPF{\n"
                                                       "color: white;\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "#lineEdit_RG{\n"
                                                       "color: white;\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "#lineEdit_Emissor{\n"
                                                       "color: white;\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}")
        self.frame_Identificacao_Coluna2.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.frame_Identificacao_Coluna2.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_Identificacao_Coluna2.setObjectName(
            "frame_Identificacao_Coluna2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(
            self.frame_Identificacao_Coluna2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_CPF = QtWidgets.QLabel(self.frame_Identificacao_Coluna2)
        self.label_CPF.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CPF.setFont(font)
        self.label_CPF.setObjectName("label_CPF")
        self.verticalLayout_11.addWidget(self.label_CPF)
        self.lineEdit_CPF = QtWidgets.QLineEdit(
            self.frame_Identificacao_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_CPF.setFont(font)
        self.lineEdit_CPF.setObjectName("lineEdit_CPF")
        self.verticalLayout_11.addWidget(self.lineEdit_CPF)
        self.label_RG = QtWidgets.QLabel(self.frame_Identificacao_Coluna2)
        self.label_RG.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_RG.setFont(font)
        self.label_RG.setObjectName("label_RG")
        self.verticalLayout_11.addWidget(self.label_RG)
        self.lineEdit_RG = QtWidgets.QLineEdit(
            self.frame_Identificacao_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_RG.setFont(font)
        self.lineEdit_RG.setObjectName("lineEdit_RG")
        self.verticalLayout_11.addWidget(self.lineEdit_RG)
        self.label_Emissor = QtWidgets.QLabel(self.frame_Identificacao_Coluna2)
        self.label_Emissor.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Emissor.setFont(font)
        self.label_Emissor.setObjectName("label_Emissor")
        self.verticalLayout_11.addWidget(self.label_Emissor)
        self.lineEdit_Emissor = QtWidgets.QLineEdit(
            self.frame_Identificacao_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Emissor.setFont(font)
        self.lineEdit_Emissor.setObjectName("lineEdit_Emissor")
        self.verticalLayout_11.addWidget(self.lineEdit_Emissor)
        self.horizontalLayout_9.addWidget(self.frame_Identificacao_Coluna2)
        self.frame_Identificacao_Coluna3 = QtWidgets.QFrame(
            self.frame_Identificacao)
        self.frame_Identificacao_Coluna3.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_Identificacao_Coluna3.setStyleSheet("#label_DataNascimento{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "#label_Sexo{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "#label_EstadoCivil{\n"
                                                       "color: rgb(43, 64, 205);\n"
                                                       "background-color: transparent;\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "#dateEdit_Nascimento{\n"
                                                       "color: white;\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "#comboBox_Sexo{\n"
                                                       "color: white;\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "#comboBox_EstadoCivil{\n"
                                                       "color: rgb(255, 255, 255);\n"
                                                       "padding: 5px;\n"
                                                       "border-radius: 5px;\n"
                                                       "background-color: rgba(43, 64, 205, 128);\n"
                                                       "}")
        self.frame_Identificacao_Coluna3.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.frame_Identificacao_Coluna3.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_Identificacao_Coluna3.setObjectName(
            "frame_Identificacao_Coluna3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(
            self.frame_Identificacao_Coluna3)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_DataNascimento = QtWidgets.QLabel(
            self.frame_Identificacao_Coluna3)
        self.label_DataNascimento.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_DataNascimento.setFont(font)
        self.label_DataNascimento.setObjectName("label_DataNascimento")
        self.verticalLayout_12.addWidget(self.label_DataNascimento)
        self.dateEdit_Nascimento = QtWidgets.QDateEdit(
            self.frame_Identificacao_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_Nascimento.setFont(font)
        self.dateEdit_Nascimento.setObjectName("dateEdit_Nascimento")
        self.verticalLayout_12.addWidget(self.dateEdit_Nascimento)
        self.label_Sexo = QtWidgets.QLabel(self.frame_Identificacao_Coluna3)
        self.label_Sexo.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Sexo.setFont(font)
        self.label_Sexo.setObjectName("label_Sexo")
        self.verticalLayout_12.addWidget(self.label_Sexo)
        self.comboBox_Sexo = QtWidgets.QComboBox(
            self.frame_Identificacao_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Sexo.setFont(font)
        self.comboBox_Sexo.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_Sexo.setObjectName("comboBox_Sexo")
        self.comboBox_Sexo.addItem("")
        self.comboBox_Sexo.setItemText(0, "")
        self.comboBox_Sexo.addItem("")
        self.comboBox_Sexo.addItem("")
        self.comboBox_Sexo.addItem("")
        self.verticalLayout_12.addWidget(self.comboBox_Sexo)
        self.label_EstadoCivil = QtWidgets.QLabel(
            self.frame_Identificacao_Coluna3)
        self.label_EstadoCivil.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_EstadoCivil.setFont(font)
        self.label_EstadoCivil.setObjectName("label_EstadoCivil")
        self.verticalLayout_12.addWidget(self.label_EstadoCivil)
        self.comboBox_EstadoCivil = QtWidgets.QComboBox(
            self.frame_Identificacao_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_EstadoCivil.setFont(font)
        self.comboBox_EstadoCivil.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_EstadoCivil.setObjectName("comboBox_EstadoCivil")
        self.comboBox_EstadoCivil.addItem("")
        self.comboBox_EstadoCivil.setItemText(0, "")
        self.comboBox_EstadoCivil.addItem("")
        self.comboBox_EstadoCivil.addItem("")
        self.comboBox_EstadoCivil.addItem("")
        self.comboBox_EstadoCivil.addItem("")
        self.verticalLayout_12.addWidget(self.comboBox_EstadoCivil)
        self.horizontalLayout_9.addWidget(self.frame_Identificacao_Coluna3)
        self.verticalLayout_36.addWidget(self.frame_Identificacao)
        self.label_Endereco = QtWidgets.QLabel(
            self.scrollAreaWidget_DadosPrincipais)
        self.label_Endereco.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Endereco.setFont(font)
        self.label_Endereco.setStyleSheet("#label_Endereco{\n"
                                          "color: white;\n"
                                          "}")
        self.label_Endereco.setObjectName("label_Endereco")
        self.verticalLayout_36.addWidget(self.label_Endereco)
        self.frame_Endereco = QtWidgets.QFrame(
            self.scrollAreaWidget_DadosPrincipais)
        self.frame_Endereco.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Endereco.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_Endereco.setAutoFillBackground(False)
        self.frame_Endereco.setStyleSheet("#frame_Endereco{\n"
                                          "background-color: rgba(255, 255, 255, 229);\n"
                                          "border-radius: 12px;\n"
                                          "}")
        self.frame_Endereco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Endereco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Endereco.setObjectName("frame_Endereco")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_Endereco)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_Endereco_Coluna1 = QtWidgets.QFrame(self.frame_Endereco)
        self.frame_Endereco_Coluna1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Endereco_Coluna1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_Endereco_Coluna1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_Endereco_Coluna1.setStyleSheet("#label_CEP{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "#label_UF{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "#lineEdit_CEP{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "#comboBox_UF{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}")
        self.frame_Endereco_Coluna1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Endereco_Coluna1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Endereco_Coluna1.setObjectName("frame_Endereco_Coluna1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(
            self.frame_Endereco_Coluna1)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_CEP = QtWidgets.QLabel(self.frame_Endereco_Coluna1)
        self.label_CEP.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CEP.setFont(font)
        self.label_CEP.setObjectName("label_CEP")
        self.verticalLayout_13.addWidget(self.label_CEP)
        self.lineEdit_CEP = QtWidgets.QLineEdit(self.frame_Endereco_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_CEP.setFont(font)
        self.lineEdit_CEP.setObjectName("lineEdit_CEP")
        self.verticalLayout_13.addWidget(self.lineEdit_CEP)
        self.label_UF = QtWidgets.QLabel(self.frame_Endereco_Coluna1)
        self.label_UF.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_UF.setFont(font)
        self.label_UF.setObjectName("label_UF")
        self.verticalLayout_13.addWidget(self.label_UF)
        self.comboBox_UF = QtWidgets.QComboBox(self.frame_Endereco_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_UF.setFont(font)
        self.comboBox_UF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_UF.setObjectName("comboBox_UF")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.setItemText(0, "")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.comboBox_UF.addItem("")
        self.verticalLayout_13.addWidget(self.comboBox_UF)
        self.horizontalLayout_10.addWidget(self.frame_Endereco_Coluna1)
        self.frame_Endereco_Coluna2 = QtWidgets.QFrame(self.frame_Endereco)
        self.frame_Endereco_Coluna2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Endereco_Coluna2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_Endereco_Coluna2.setStyleSheet("#label_Cidade{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "#label_Bairro{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "#lineEdit_Cidade{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "#lineEdit_Bairro{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}")
        self.frame_Endereco_Coluna2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Endereco_Coluna2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Endereco_Coluna2.setObjectName("frame_Endereco_Coluna2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(
            self.frame_Endereco_Coluna2)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_Cidade = QtWidgets.QLabel(self.frame_Endereco_Coluna2)
        self.label_Cidade.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Cidade.setFont(font)
        self.label_Cidade.setObjectName("label_Cidade")
        self.verticalLayout_14.addWidget(self.label_Cidade)
        self.lineEdit_Cidade = QtWidgets.QLineEdit(self.frame_Endereco_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Cidade.setFont(font)
        self.lineEdit_Cidade.setObjectName("lineEdit_Cidade")
        self.verticalLayout_14.addWidget(self.lineEdit_Cidade)
        self.label_Bairro = QtWidgets.QLabel(self.frame_Endereco_Coluna2)
        self.label_Bairro.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Bairro.setFont(font)
        self.label_Bairro.setObjectName("label_Bairro")
        self.verticalLayout_14.addWidget(self.label_Bairro)
        self.lineEdit_Bairro = QtWidgets.QLineEdit(self.frame_Endereco_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Bairro.setFont(font)
        self.lineEdit_Bairro.setObjectName("lineEdit_Bairro")
        self.verticalLayout_14.addWidget(self.lineEdit_Bairro)
        self.horizontalLayout_10.addWidget(self.frame_Endereco_Coluna2)
        self.frame_Endereco_Coluna3 = QtWidgets.QFrame(self.frame_Endereco)
        self.frame_Endereco_Coluna3.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_Endereco_Coluna3.setStyleSheet("#label_Numero{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "#label_Logradouro{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "#lineEdit_Numero{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "#lineEdit_Logradouro{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}")
        self.frame_Endereco_Coluna3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Endereco_Coluna3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Endereco_Coluna3.setObjectName("frame_Endereco_Coluna3")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(
            self.frame_Endereco_Coluna3)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_Numero = QtWidgets.QLabel(self.frame_Endereco_Coluna3)
        self.label_Numero.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Numero.setFont(font)
        self.label_Numero.setObjectName("label_Numero")
        self.verticalLayout_15.addWidget(self.label_Numero)
        self.lineEdit_Numero = QtWidgets.QLineEdit(self.frame_Endereco_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Numero.setFont(font)
        self.lineEdit_Numero.setObjectName("lineEdit_Numero")
        self.verticalLayout_15.addWidget(self.lineEdit_Numero)
        self.label_Logradouro = QtWidgets.QLabel(self.frame_Endereco_Coluna3)
        self.label_Logradouro.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Logradouro.setFont(font)
        self.label_Logradouro.setObjectName("label_Logradouro")
        self.verticalLayout_15.addWidget(self.label_Logradouro)
        self.lineEdit_Logradouro = QtWidgets.QLineEdit(
            self.frame_Endereco_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Logradouro.setFont(font)
        self.lineEdit_Logradouro.setObjectName("lineEdit_Logradouro")
        self.verticalLayout_15.addWidget(self.lineEdit_Logradouro)
        self.horizontalLayout_10.addWidget(self.frame_Endereco_Coluna3)
        self.frame_Endereco_Coluna4 = QtWidgets.QFrame(self.frame_Endereco)
        self.frame_Endereco_Coluna4.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_Endereco_Coluna4.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_Endereco_Coluna4.setStyleSheet("#label_Complemento{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "#textEdit_Complemento{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}")
        self.frame_Endereco_Coluna4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Endereco_Coluna4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Endereco_Coluna4.setObjectName("frame_Endereco_Coluna4")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(
            self.frame_Endereco_Coluna4)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_Complemento = QtWidgets.QLabel(self.frame_Endereco_Coluna4)
        self.label_Complemento.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Complemento.setFont(font)
        self.label_Complemento.setObjectName("label_Complemento")
        self.verticalLayout_16.addWidget(self.label_Complemento)
        self.textEdit_Complemento = QtWidgets.QTextEdit(
            self.frame_Endereco_Coluna4)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_Complemento.setFont(font)
        self.textEdit_Complemento.setObjectName("textEdit_Complemento")
        self.verticalLayout_16.addWidget(self.textEdit_Complemento)
        self.horizontalLayout_10.addWidget(self.frame_Endereco_Coluna4)
        self.verticalLayout_36.addWidget(self.frame_Endereco)
        self.label_Contato = QtWidgets.QLabel(
            self.scrollAreaWidget_DadosPrincipais)
        self.label_Contato.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Contato.setFont(font)
        self.label_Contato.setStyleSheet("#label_Contato{\n"
                                         "color: white;\n"
                                         "}")
        self.label_Contato.setObjectName("label_Contato")
        self.verticalLayout_36.addWidget(self.label_Contato)
        self.frame_Contato = QtWidgets.QFrame(
            self.scrollAreaWidget_DadosPrincipais)
        self.frame_Contato.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_Contato.setAutoFillBackground(False)
        self.frame_Contato.setStyleSheet("#frame_Contato{\n"
                                         "background-color: rgba(255, 255, 255, 229);\n"
                                         "border-radius: 12px;\n"
                                         "}")
        self.frame_Contato.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Contato.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Contato.setObjectName("frame_Contato")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_Contato)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_Contato_Coluna1 = QtWidgets.QFrame(self.frame_Contato)
        self.frame_Contato_Coluna1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Contato_Coluna1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_Contato_Coluna1.setStyleSheet("#label_Celular{\n"
                                                 "color: rgb(43, 64, 205);\n"
                                                 "background-color: transparent;\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "#lineEdit_Celular{\n"
                                                 "color: white;\n"
                                                 "padding: 5px;\n"
                                                 "border-radius: 5px;\n"
                                                 "background-color: rgba(43, 64, 205, 128);\n"
                                                 "}\n"
                                                 "")
        self.frame_Contato_Coluna1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Contato_Coluna1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Contato_Coluna1.setObjectName("frame_Contato_Coluna1")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(
            self.frame_Contato_Coluna1)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_Celular = QtWidgets.QLabel(self.frame_Contato_Coluna1)
        self.label_Celular.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Celular.setFont(font)
        self.label_Celular.setObjectName("label_Celular")
        self.verticalLayout_18.addWidget(self.label_Celular)
        self.lineEdit_Celular = QtWidgets.QLineEdit(self.frame_Contato_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Celular.setFont(font)
        self.lineEdit_Celular.setObjectName("lineEdit_Celular")
        self.verticalLayout_18.addWidget(self.lineEdit_Celular)
        self.horizontalLayout_11.addWidget(self.frame_Contato_Coluna1)
        self.frame_Contato_Coluna2 = QtWidgets.QFrame(self.frame_Contato)
        self.frame_Contato_Coluna2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_Contato_Coluna2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_Contato_Coluna2.setStyleSheet("#label_Telefone{\n"
                                                 "color: rgb(43, 64, 205);\n"
                                                 "background-color: transparent;\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "#lineEdit_Telefone{\n"
                                                 "color: white;\n"
                                                 "padding: 5px;\n"
                                                 "border-radius: 5px;\n"
                                                 "background-color: rgba(43, 64, 205, 128);\n"
                                                 "}\n"
                                                 "\n"
                                                 "")
        self.frame_Contato_Coluna2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Contato_Coluna2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Contato_Coluna2.setObjectName("frame_Contato_Coluna2")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(
            self.frame_Contato_Coluna2)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_Telefone = QtWidgets.QLabel(self.frame_Contato_Coluna2)
        self.label_Telefone.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Telefone.setFont(font)
        self.label_Telefone.setObjectName("label_Telefone")
        self.verticalLayout_19.addWidget(self.label_Telefone)
        self.lineEdit_Telefone = QtWidgets.QLineEdit(
            self.frame_Contato_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Telefone.setFont(font)
        self.lineEdit_Telefone.setObjectName("lineEdit_Telefone")
        self.verticalLayout_19.addWidget(self.lineEdit_Telefone)
        self.horizontalLayout_11.addWidget(self.frame_Contato_Coluna2)
        self.frame_Contato_Coluna3 = QtWidgets.QFrame(self.frame_Contato)
        self.frame_Contato_Coluna3.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_Contato_Coluna3.setStyleSheet("#label_Email{\n"
                                                 "color: rgb(43, 64, 205);\n"
                                                 "background-color: transparent;\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "#lineEdit_Email{\n"
                                                 "color: white;\n"
                                                 "padding: 5px;\n"
                                                 "border-radius: 5px;\n"
                                                 "background-color: rgba(43, 64, 205, 128);\n"
                                                 "}")
        self.frame_Contato_Coluna3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Contato_Coluna3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Contato_Coluna3.setObjectName("frame_Contato_Coluna3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(
            self.frame_Contato_Coluna3)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_Email = QtWidgets.QLabel(self.frame_Contato_Coluna3)
        self.label_Email.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Email.setFont(font)
        self.label_Email.setObjectName("label_Email")
        self.verticalLayout_20.addWidget(self.label_Email)
        self.lineEdit_Email = QtWidgets.QLineEdit(self.frame_Contato_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Email.setFont(font)
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.verticalLayout_20.addWidget(self.lineEdit_Email)
        self.horizontalLayout_11.addWidget(self.frame_Contato_Coluna3)
        self.verticalLayout_36.addWidget(self.frame_Contato)
        self.label_Atendimento = QtWidgets.QLabel(
            self.scrollAreaWidget_DadosPrincipais)
        self.label_Atendimento.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Atendimento.setFont(font)
        self.label_Atendimento.setStyleSheet("#label_Atendimento{\n"
                                             "color: white;\n"
                                             "}")
        self.label_Atendimento.setObjectName("label_Atendimento")
        self.verticalLayout_36.addWidget(self.label_Atendimento)
        self.frame_Atendimento = QtWidgets.QFrame(
            self.scrollAreaWidget_DadosPrincipais)
        self.frame_Atendimento.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_Atendimento.setAutoFillBackground(False)
        self.frame_Atendimento.setStyleSheet("#frame_Atendimento{\n"
                                             "background-color: rgba(255, 255, 255, 229);\n"
                                             "border-radius: 12px;\n"
                                             "}")
        self.frame_Atendimento.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Atendimento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Atendimento.setObjectName("frame_Atendimento")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(
            self.frame_Atendimento)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_Atendimento_Linha1 = QtWidgets.QFrame(
            self.frame_Atendimento)
        self.frame_Atendimento_Linha1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Atendimento_Linha1.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_Atendimento_Linha1.setStyleSheet("#label_Profissional{\n"
                                                    "color: rgb(43, 64, 205);\n"
                                                    "background-color: transparent;\n"
                                                    "}\n"
                                                    "\n"
                                                    "\n"
                                                    "\n"
                                                    "#comboBox_Profissional{\n"
                                                    "color: white;\n"
                                                    "padding: 5px;\n"
                                                    "border-radius: 5px;\n"
                                                    "background-color: rgba(43, 64, 205, 128);\n"
                                                    "}\n"
                                                    "")
        self.frame_Atendimento_Linha1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Atendimento_Linha1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Atendimento_Linha1.setObjectName("frame_Atendimento_Linha1")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(
            self.frame_Atendimento_Linha1)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_Profissional = QtWidgets.QLabel(
            self.frame_Atendimento_Linha1)
        self.label_Profissional.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Profissional.setFont(font)
        self.label_Profissional.setObjectName("label_Profissional")
        self.verticalLayout_21.addWidget(self.label_Profissional)
        self.comboBox_Profissional = QtWidgets.QComboBox(
            self.frame_Atendimento_Linha1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Profissional.setFont(font)
        self.comboBox_Profissional.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_Profissional.setObjectName("comboBox_Profissional")
        self.comboBox_Profissional.addItem("")
        self.comboBox_Profissional.setItemText(0, "")
        self.verticalLayout_21.addWidget(self.comboBox_Profissional)
        self.horizontalLayout_12.addWidget(self.frame_Atendimento_Linha1)
        self.frame_Atendimento_Linha2 = QtWidgets.QFrame(
            self.frame_Atendimento)
        self.frame_Atendimento_Linha2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_Atendimento_Linha2.setStyleSheet("#label_Categoria{\n"
                                                    "color: rgb(43, 64, 205);\n"
                                                    "background-color: transparent;\n"
                                                    "}\n"
                                                    "\n"
                                                    "\n"
                                                    "\n"
                                                    "\n"
                                                    "#comboBox_Categoria{\n"
                                                    "color: white;\n"
                                                    "padding: 5px;\n"
                                                    "border-radius: 5px;\n"
                                                    "background-color: rgba(43, 64, 205, 128);\n"
                                                    "}")
        self.frame_Atendimento_Linha2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Atendimento_Linha2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Atendimento_Linha2.setObjectName("frame_Atendimento_Linha2")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(
            self.frame_Atendimento_Linha2)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_Categoria = QtWidgets.QLabel(self.frame_Atendimento_Linha2)
        self.label_Categoria.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Categoria.setFont(font)
        self.label_Categoria.setObjectName("label_Categoria")
        self.verticalLayout_23.addWidget(self.label_Categoria)
        self.comboBox_Categoria = QtWidgets.QComboBox(
            self.frame_Atendimento_Linha2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Categoria.setFont(font)
        self.comboBox_Categoria.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_Categoria.setObjectName("comboBox_Categoria")
        self.comboBox_Categoria.addItem("")
        self.comboBox_Categoria.setItemText(0, "")
        self.comboBox_Categoria.addItem("")
        self.comboBox_Categoria.addItem("")
        self.verticalLayout_23.addWidget(self.comboBox_Categoria)
        self.horizontalLayout_12.addWidget(self.frame_Atendimento_Linha2)
        self.verticalLayout_36.addWidget(self.frame_Atendimento)
        self.scrollArea_DadosPrincipais.setWidget(
            self.scrollAreaWidget_DadosPrincipais)
        self.verticalLayout_28.addWidget(self.scrollArea_DadosPrincipais)
        self.Paginas_Formulario.addWidget(self.pg_DadosPrincipais)
        self.pg_OutrosDados = QtWidgets.QWidget()
        self.pg_OutrosDados.setStyleSheet("#pg_OutrosDados{\n"
                                          " background-color: rgba(46, 168, 241, 204)\n"
                                          "}\n"
                                          "")
        self.pg_OutrosDados.setObjectName("pg_OutrosDados")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.pg_OutrosDados)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.scrollArea_OutrosDados = QtWidgets.QScrollArea(
            self.pg_OutrosDados)
        self.scrollArea_OutrosDados.setStyleSheet("#scrollAreaWidget_OutrosDados{\n"
                                                  "background-color: transparent;\n"
                                                  "border-top-right-radius: 12px;\n"
                                                  "border-bottom-right-radius: 12px;\n"
                                                  "border-bottom-left-radius: 12px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QAbstractScrollArea#scrollArea_OutrosDados {\n"
                                                  "    background-color: transparent;\n"
                                                  "}")
        self.scrollArea_OutrosDados.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_OutrosDados.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_OutrosDados.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_OutrosDados.setWidgetResizable(True)
        self.scrollArea_OutrosDados.setObjectName("scrollArea_OutrosDados")
        self.scrollAreaWidget_OutrosDados = QtWidgets.QWidget()
        self.scrollAreaWidget_OutrosDados.setGeometry(
            QtCore.QRect(0, 0, 678, 931))
        self.scrollAreaWidget_OutrosDados.setObjectName(
            "scrollAreaWidget_OutrosDados")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidget_OutrosDados)
        self.verticalLayout_38.setSpacing(15)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.label_Cadastro = QtWidgets.QLabel(
            self.scrollAreaWidget_OutrosDados)
        self.label_Cadastro.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Cadastro.setFont(font)
        self.label_Cadastro.setStyleSheet("#label_Cadastro{\n"
                                          "color: white;\n"
                                          "}")
        self.label_Cadastro.setObjectName("label_Cadastro")
        self.verticalLayout_38.addWidget(self.label_Cadastro)
        self.frame_Cadastro = QtWidgets.QFrame(
            self.scrollAreaWidget_OutrosDados)
        self.frame_Cadastro.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_Cadastro.setAutoFillBackground(False)
        self.frame_Cadastro.setStyleSheet("#frame_Cadastro{\n"
                                          "background-color: rgba(255, 255, 255, 229);\n"
                                          "border-radius: 12px;\n"
                                          "}\n"
                                          "\n"
                                          "#label_DataCadastro{\n"
                                          "color: rgb(43, 64, 205);\n"
                                          "background-color: transparent;\n"
                                          "}\n"
                                          "\n"
                                          "#label_FatorSanguineo{\n"
                                          "color: rgb(43, 64, 205);\n"
                                          "background-color: transparent;\n"
                                          "}\n"
                                          "\n"
                                          "#label_CNS{\n"
                                          "color: rgb(43, 64, 205);\n"
                                          "background-color: transparent;\n"
                                          "}\n"
                                          "\n"
                                          "#label_Raca{\n"
                                          "color: rgb(43, 64, 205);\n"
                                          "background-color: transparent;\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "#dateEdit_DataCadastro{\n"
                                          "color: white;\n"
                                          "background-color: rgba(43, 64, 205, 128);\n"
                                          "border-radius: 5px;\n"
                                          "padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "#comboBox_FatorSanguineo{\n"
                                          "color: white;\n"
                                          "padding: 5px;\n"
                                          "border-radius: 5px;\n"
                                          "background-color: rgba(43, 64, 205, 128);\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "#lineEdit_CNS{\n"
                                          "color: white;\n"
                                          "padding: 5px;\n"
                                          "border-radius: 5px;\n"
                                          "background-color: rgba(43, 64, 205, 128);\n"
                                          "}\n"
                                          "\n"
                                          "#comboBox_Raca{\n"
                                          "color: white;\n"
                                          "padding: 5px;\n"
                                          "border-radius: 5px;\n"
                                          "background-color: rgba(43, 64, 205, 128);\n"
                                          "}")
        self.frame_Cadastro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Cadastro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Cadastro.setObjectName("frame_Cadastro")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_Cadastro)
        self.horizontalLayout_14.setSpacing(25)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_Cadastro_Coluna1 = QtWidgets.QFrame(self.frame_Cadastro)
        self.frame_Cadastro_Coluna1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Cadastro_Coluna1.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_Cadastro_Coluna1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_Cadastro_Coluna1.setStyleSheet("")
        self.frame_Cadastro_Coluna1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Cadastro_Coluna1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Cadastro_Coluna1.setObjectName("frame_Cadastro_Coluna1")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(
            self.frame_Cadastro_Coluna1)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_DataCadastro = QtWidgets.QLabel(self.frame_Cadastro_Coluna1)
        self.label_DataCadastro.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_DataCadastro.setFont(font)
        self.label_DataCadastro.setObjectName("label_DataCadastro")
        self.verticalLayout_26.addWidget(self.label_DataCadastro)
        self.dateEdit_DataCadastro = QtWidgets.QDateEdit(
            self.frame_Cadastro_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_DataCadastro.setFont(font)
        self.dateEdit_DataCadastro.setObjectName("dateEdit_DataCadastro")
        self.verticalLayout_26.addWidget(self.dateEdit_DataCadastro)
        self.horizontalLayout_14.addWidget(self.frame_Cadastro_Coluna1)
        self.frame_Cadastro_Coluna2 = QtWidgets.QFrame(self.frame_Cadastro)
        self.frame_Cadastro_Coluna2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Cadastro_Coluna2.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_Cadastro_Coluna2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_Cadastro_Coluna2.setStyleSheet("")
        self.frame_Cadastro_Coluna2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Cadastro_Coluna2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Cadastro_Coluna2.setObjectName("frame_Cadastro_Coluna2")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(
            self.frame_Cadastro_Coluna2)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(5)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_FatorSanguineo = QtWidgets.QLabel(
            self.frame_Cadastro_Coluna2)
        self.label_FatorSanguineo.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_FatorSanguineo.setFont(font)
        self.label_FatorSanguineo.setObjectName("label_FatorSanguineo")
        self.verticalLayout_30.addWidget(self.label_FatorSanguineo)
        self.comboBox_FatorSanguineo = QtWidgets.QComboBox(
            self.frame_Cadastro_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_FatorSanguineo.setFont(font)
        self.comboBox_FatorSanguineo.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_FatorSanguineo.setObjectName("comboBox_FatorSanguineo")
        self.comboBox_FatorSanguineo.addItem("")
        self.comboBox_FatorSanguineo.setItemText(0, "")
        self.comboBox_FatorSanguineo.addItem("")
        self.comboBox_FatorSanguineo.addItem("")
        self.comboBox_FatorSanguineo.addItem("")
        self.comboBox_FatorSanguineo.addItem("")
        self.comboBox_FatorSanguineo.addItem("")
        self.comboBox_FatorSanguineo.addItem("")
        self.comboBox_FatorSanguineo.addItem("")
        self.comboBox_FatorSanguineo.addItem("")
        self.verticalLayout_30.addWidget(self.comboBox_FatorSanguineo)
        self.horizontalLayout_14.addWidget(self.frame_Cadastro_Coluna2)
        self.frame_Cadastro_Coluna3 = QtWidgets.QFrame(self.frame_Cadastro)
        self.frame_Cadastro_Coluna3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Cadastro_Coluna3.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_Cadastro_Coluna3.setStyleSheet("")
        self.frame_Cadastro_Coluna3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Cadastro_Coluna3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Cadastro_Coluna3.setObjectName("frame_Cadastro_Coluna3")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(
            self.frame_Cadastro_Coluna3)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_CNS = QtWidgets.QLabel(self.frame_Cadastro_Coluna3)
        self.label_CNS.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CNS.setFont(font)
        self.label_CNS.setObjectName("label_CNS")
        self.verticalLayout_27.addWidget(self.label_CNS)
        self.lineEdit_CNS = QtWidgets.QLineEdit(self.frame_Cadastro_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_CNS.setFont(font)
        self.lineEdit_CNS.setObjectName("lineEdit_CNS")
        self.verticalLayout_27.addWidget(self.lineEdit_CNS)
        self.horizontalLayout_14.addWidget(self.frame_Cadastro_Coluna3)
        self.frame_Cadastro_Coluna4 = QtWidgets.QFrame(self.frame_Cadastro)
        self.frame_Cadastro_Coluna4.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_Cadastro_Coluna4.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_Cadastro_Coluna4.setStyleSheet("")
        self.frame_Cadastro_Coluna4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Cadastro_Coluna4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Cadastro_Coluna4.setObjectName("frame_Cadastro_Coluna4")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(
            self.frame_Cadastro_Coluna4)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(5)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_Raca = QtWidgets.QLabel(self.frame_Cadastro_Coluna4)
        self.label_Raca.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Raca.setFont(font)
        self.label_Raca.setObjectName("label_Raca")
        self.verticalLayout_31.addWidget(self.label_Raca)
        self.comboBox_Raca = QtWidgets.QComboBox(self.frame_Cadastro_Coluna4)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Raca.setFont(font)
        self.comboBox_Raca.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_Raca.setObjectName("comboBox_Raca")
        self.comboBox_Raca.addItem("")
        self.comboBox_Raca.setItemText(0, "")
        self.comboBox_Raca.addItem("")
        self.comboBox_Raca.addItem("")
        self.comboBox_Raca.addItem("")
        self.comboBox_Raca.addItem("")
        self.comboBox_Raca.addItem("")
        self.verticalLayout_31.addWidget(self.comboBox_Raca)
        self.horizontalLayout_14.addWidget(self.frame_Cadastro_Coluna4)
        self.verticalLayout_38.addWidget(self.frame_Cadastro)
        self.label_DadosFamiliares = QtWidgets.QLabel(
            self.scrollAreaWidget_OutrosDados)
        self.label_DadosFamiliares.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_DadosFamiliares.setFont(font)
        self.label_DadosFamiliares.setStyleSheet("#label_DadosFamiliares{\n"
                                                 "color: white;\n"
                                                 "}")
        self.label_DadosFamiliares.setObjectName("label_DadosFamiliares")
        self.verticalLayout_38.addWidget(self.label_DadosFamiliares)
        self.frame_DadosFamiliares = QtWidgets.QFrame(
            self.scrollAreaWidget_OutrosDados)
        self.frame_DadosFamiliares.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_DadosFamiliares.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_DadosFamiliares.setAutoFillBackground(False)
        self.frame_DadosFamiliares.setStyleSheet("#frame_DadosFamiliares{\n"
                                                 "background-color: rgba(255, 255, 255, 229);\n"
                                                 "border-radius: 12px;\n"
                                                 "}")
        self.frame_DadosFamiliares.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DadosFamiliares.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_DadosFamiliares.setObjectName("frame_DadosFamiliares")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(
            self.frame_DadosFamiliares)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_DadosFamiliares_Coluna1 = QtWidgets.QFrame(
            self.frame_DadosFamiliares)
        self.frame_DadosFamiliares_Coluna1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_DadosFamiliares_Coluna1.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_DadosFamiliares_Coluna1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_DadosFamiliares_Coluna1.setStyleSheet("#label_NomeMae{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "#label_NomePai{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "#label_QuantFilhos{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "#lineEdit_NomeMae{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}\n"
                                                         "\n"
                                                         "#lineEdit_NomePai{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}\n"
                                                         "\n"
                                                         "#lineEdit_QuantFilhos{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}")
        self.frame_DadosFamiliares_Coluna1.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.frame_DadosFamiliares_Coluna1.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_DadosFamiliares_Coluna1.setObjectName(
            "frame_DadosFamiliares_Coluna1")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(
            self.frame_DadosFamiliares_Coluna1)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_NomeMae = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna1)
        self.label_NomeMae.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NomeMae.setFont(font)
        self.label_NomeMae.setObjectName("label_NomeMae")
        self.verticalLayout_17.addWidget(self.label_NomeMae)
        self.lineEdit_NomeMae = QtWidgets.QLineEdit(
            self.frame_DadosFamiliares_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_NomeMae.setFont(font)
        self.lineEdit_NomeMae.setObjectName("lineEdit_NomeMae")
        self.verticalLayout_17.addWidget(self.lineEdit_NomeMae)
        self.label_NomePai = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna1)
        self.label_NomePai.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NomePai.setFont(font)
        self.label_NomePai.setObjectName("label_NomePai")
        self.verticalLayout_17.addWidget(self.label_NomePai)
        self.lineEdit_NomePai = QtWidgets.QLineEdit(
            self.frame_DadosFamiliares_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_NomePai.setFont(font)
        self.lineEdit_NomePai.setObjectName("lineEdit_NomePai")
        self.verticalLayout_17.addWidget(self.lineEdit_NomePai)
        self.label_QuantFilhos = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna1)
        self.label_QuantFilhos.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_QuantFilhos.setFont(font)
        self.label_QuantFilhos.setObjectName("label_QuantFilhos")
        self.verticalLayout_17.addWidget(self.label_QuantFilhos)
        self.lineEdit_QuantFilhos = QtWidgets.QLineEdit(
            self.frame_DadosFamiliares_Coluna1)
        self.lineEdit_QuantFilhos.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_QuantFilhos.setFont(font)
        self.lineEdit_QuantFilhos.setObjectName("lineEdit_QuantFilhos")
        self.verticalLayout_17.addWidget(self.lineEdit_QuantFilhos)
        self.horizontalLayout_13.addWidget(self.frame_DadosFamiliares_Coluna1)
        self.frame_DadosFamiliares_Coluna2 = QtWidgets.QFrame(
            self.frame_DadosFamiliares)
        self.frame_DadosFamiliares_Coluna2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_DadosFamiliares_Coluna2.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_DadosFamiliares_Coluna2.setStyleSheet("#label_NomeConjuge{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "#label_CPFconjuge{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "#label_NascimentoConjuge{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "#lineEdit_NomeConjuge{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}\n"
                                                         "\n"
                                                         "\n"
                                                         "#lineEdit_CPFconjuge{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}\n"
                                                         "\n"
                                                         "#dateEdit_NascimentoConjuge{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}")
        self.frame_DadosFamiliares_Coluna2.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.frame_DadosFamiliares_Coluna2.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_DadosFamiliares_Coluna2.setObjectName(
            "frame_DadosFamiliares_Coluna2")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(
            self.frame_DadosFamiliares_Coluna2)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_NomeConjuge = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna2)
        self.label_NomeConjuge.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NomeConjuge.setFont(font)
        self.label_NomeConjuge.setObjectName("label_NomeConjuge")
        self.verticalLayout_22.addWidget(self.label_NomeConjuge)
        self.lineEdit_NomeConjuge = QtWidgets.QLineEdit(
            self.frame_DadosFamiliares_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_NomeConjuge.setFont(font)
        self.lineEdit_NomeConjuge.setObjectName("lineEdit_NomeConjuge")
        self.verticalLayout_22.addWidget(self.lineEdit_NomeConjuge)
        self.label_CPFconjuge = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna2)
        self.label_CPFconjuge.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CPFconjuge.setFont(font)
        self.label_CPFconjuge.setObjectName("label_CPFconjuge")
        self.verticalLayout_22.addWidget(self.label_CPFconjuge)
        self.lineEdit_CPFconjuge = QtWidgets.QLineEdit(
            self.frame_DadosFamiliares_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_CPFconjuge.setFont(font)
        self.lineEdit_CPFconjuge.setObjectName("lineEdit_CPFconjuge")
        self.verticalLayout_22.addWidget(self.lineEdit_CPFconjuge)
        self.label_NascimentoConjuge = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna2)
        self.label_NascimentoConjuge.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NascimentoConjuge.setFont(font)
        self.label_NascimentoConjuge.setObjectName("label_NascimentoConjuge")
        self.verticalLayout_22.addWidget(self.label_NascimentoConjuge)
        self.dateEdit_NascimentoConjuge = QtWidgets.QDateEdit(
            self.frame_DadosFamiliares_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_NascimentoConjuge.setFont(font)
        self.dateEdit_NascimentoConjuge.setObjectName(
            "dateEdit_NascimentoConjuge")
        self.verticalLayout_22.addWidget(self.dateEdit_NascimentoConjuge)
        self.horizontalLayout_13.addWidget(self.frame_DadosFamiliares_Coluna2)
        self.frame_DadosFamiliares_Coluna3 = QtWidgets.QFrame(
            self.frame_DadosFamiliares)
        self.frame_DadosFamiliares_Coluna3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_DadosFamiliares_Coluna3.setStyleSheet("#label_NomeResponsavel{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "#label_CPFResponsavel{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "#label_TelefoneResponsavel{\n"
                                                         "color: rgb(43, 64, 205);\n"
                                                         "background-color: transparent;\n"
                                                         "}\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "#lineEdit_NomeResponsavel{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}\n"
                                                         "\n"
                                                         "\n"
                                                         "#lineEdit_CPFResponsavel{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}\n"
                                                         "\n"
                                                         "#lineEdit_TelefoneResponsavel{\n"
                                                         "color: white;\n"
                                                         "padding: 5px;\n"
                                                         "border-radius: 5px;\n"
                                                         "background-color: rgba(43, 64, 205, 128);\n"
                                                         "}")
        self.frame_DadosFamiliares_Coluna3.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.frame_DadosFamiliares_Coluna3.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_DadosFamiliares_Coluna3.setObjectName(
            "frame_DadosFamiliares_Coluna3")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(
            self.frame_DadosFamiliares_Coluna3)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_NomeResponsavel = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna3)
        self.label_NomeResponsavel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NomeResponsavel.setFont(font)
        self.label_NomeResponsavel.setObjectName("label_NomeResponsavel")
        self.verticalLayout_24.addWidget(self.label_NomeResponsavel)
        self.lineEdit_NomeResponsavel = QtWidgets.QLineEdit(
            self.frame_DadosFamiliares_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_NomeResponsavel.setFont(font)
        self.lineEdit_NomeResponsavel.setObjectName("lineEdit_NomeResponsavel")
        self.verticalLayout_24.addWidget(self.lineEdit_NomeResponsavel)
        self.label_CPFResponsavel = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna3)
        self.label_CPFResponsavel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CPFResponsavel.setFont(font)
        self.label_CPFResponsavel.setObjectName("label_CPFResponsavel")
        self.verticalLayout_24.addWidget(self.label_CPFResponsavel)
        self.lineEdit_CPFResponsavel = QtWidgets.QLineEdit(
            self.frame_DadosFamiliares_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_CPFResponsavel.setFont(font)
        self.lineEdit_CPFResponsavel.setObjectName("lineEdit_CPFResponsavel")
        self.verticalLayout_24.addWidget(self.lineEdit_CPFResponsavel)
        self.label_TelefoneResponsavel = QtWidgets.QLabel(
            self.frame_DadosFamiliares_Coluna3)
        self.label_TelefoneResponsavel.setMaximumSize(
            QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_TelefoneResponsavel.setFont(font)
        self.label_TelefoneResponsavel.setObjectName(
            "label_TelefoneResponsavel")
        self.verticalLayout_24.addWidget(self.label_TelefoneResponsavel)
        self.lineEdit_TelefoneResponsavel = QtWidgets.QLineEdit(
            self.frame_DadosFamiliares_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_TelefoneResponsavel.setFont(font)
        self.lineEdit_TelefoneResponsavel.setObjectName(
            "lineEdit_TelefoneResponsavel")
        self.verticalLayout_24.addWidget(self.lineEdit_TelefoneResponsavel)
        self.horizontalLayout_13.addWidget(self.frame_DadosFamiliares_Coluna3)
        self.verticalLayout_38.addWidget(self.frame_DadosFamiliares)
        self.label_DadosEmergencia = QtWidgets.QLabel(
            self.scrollAreaWidget_OutrosDados)
        self.label_DadosEmergencia.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_DadosEmergencia.setFont(font)
        self.label_DadosEmergencia.setStyleSheet("#label_DadosEmergencia{\n"
                                                 "color: white;\n"
                                                 "}")
        self.label_DadosEmergencia.setObjectName("label_DadosEmergencia")
        self.verticalLayout_38.addWidget(self.label_DadosEmergencia)
        self.frame_DadosEmergencia = QtWidgets.QFrame(
            self.scrollAreaWidget_OutrosDados)
        self.frame_DadosEmergencia.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_DadosEmergencia.setAutoFillBackground(False)
        self.frame_DadosEmergencia.setStyleSheet("#frame_DadosEmergencia{\n"
                                                 "background-color: rgba(255, 255, 255, 229);\n"
                                                 "border-radius: 12px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "#label_NomeContatoEmergencia{\n"
                                                 "color: rgb(43, 64, 205);\n"
                                                 "background-color: transparent;\n"
                                                 "}\n"
                                                 "\n"
                                                 "#label_TelefoneEmergencia{\n"
                                                 "color: rgb(43, 64, 205);\n"
                                                 "background-color: transparent;\n"
                                                 "}\n"
                                                 "\n"
                                                 "#label_CelularEmergencia{\n"
                                                 "color: rgb(43, 64, 205);\n"
                                                 "background-color: transparent;\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "#lineEdit_NomeContatoEmergencia{\n"
                                                 "color: white;\n"
                                                 "padding: 5px;\n"
                                                 "border-radius: 5px;\n"
                                                 "background-color: rgba(43, 64, 205, 128);\n"
                                                 "}\n"
                                                 "\n"
                                                 "#lineEdit_TelefoneEmergencia{\n"
                                                 "color: white;\n"
                                                 "padding: 5px;\n"
                                                 "border-radius: 5px;\n"
                                                 "background-color: rgba(43, 64, 205, 128);\n"
                                                 "}\n"
                                                 "\n"
                                                 "#lineEdit_CelularEmergencia{\n"
                                                 "color: white;\n"
                                                 "padding: 5px;\n"
                                                 "border-radius: 5px;\n"
                                                 "background-color: rgba(43, 64, 205, 128);\n"
                                                 "}")
        self.frame_DadosEmergencia.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_DadosEmergencia.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_DadosEmergencia.setObjectName("frame_DadosEmergencia")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(
            self.frame_DadosEmergencia)
        self.horizontalLayout_15.setSpacing(25)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_DadosEmergencia_Coluna1 = QtWidgets.QFrame(
            self.frame_DadosEmergencia)
        self.frame_DadosEmergencia_Coluna1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_DadosEmergencia_Coluna1.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_DadosEmergencia_Coluna1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_DadosEmergencia_Coluna1.setStyleSheet("")
        self.frame_DadosEmergencia_Coluna1.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.frame_DadosEmergencia_Coluna1.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_DadosEmergencia_Coluna1.setObjectName(
            "frame_DadosEmergencia_Coluna1")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(
            self.frame_DadosEmergencia_Coluna1)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_NomeContatoEmergencia = QtWidgets.QLabel(
            self.frame_DadosEmergencia_Coluna1)
        self.label_NomeContatoEmergencia.setMaximumSize(
            QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NomeContatoEmergencia.setFont(font)
        self.label_NomeContatoEmergencia.setObjectName(
            "label_NomeContatoEmergencia")
        self.verticalLayout_32.addWidget(self.label_NomeContatoEmergencia)
        self.lineEdit_NomeContatoEmergencia = QtWidgets.QLineEdit(
            self.frame_DadosEmergencia_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_NomeContatoEmergencia.setFont(font)
        self.lineEdit_NomeContatoEmergencia.setObjectName(
            "lineEdit_NomeContatoEmergencia")
        self.verticalLayout_32.addWidget(self.lineEdit_NomeContatoEmergencia)
        self.horizontalLayout_15.addWidget(self.frame_DadosEmergencia_Coluna1)
        self.frame_DadosEmergencia_Coluna2 = QtWidgets.QFrame(
            self.frame_DadosEmergencia)
        self.frame_DadosEmergencia_Coluna2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_DadosEmergencia_Coluna2.setMaximumSize(
            QtCore.QSize(200, 16777215))
        self.frame_DadosEmergencia_Coluna2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_DadosEmergencia_Coluna2.setStyleSheet("")
        self.frame_DadosEmergencia_Coluna2.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.frame_DadosEmergencia_Coluna2.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_DadosEmergencia_Coluna2.setObjectName(
            "frame_DadosEmergencia_Coluna2")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(
            self.frame_DadosEmergencia_Coluna2)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(5)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_TelefoneEmergencia = QtWidgets.QLabel(
            self.frame_DadosEmergencia_Coluna2)
        self.label_TelefoneEmergencia.setMaximumSize(
            QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_TelefoneEmergencia.setFont(font)
        self.label_TelefoneEmergencia.setObjectName("label_TelefoneEmergencia")
        self.verticalLayout_33.addWidget(self.label_TelefoneEmergencia)
        self.lineEdit_TelefoneEmergencia = QtWidgets.QLineEdit(
            self.frame_DadosEmergencia_Coluna2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_TelefoneEmergencia.setFont(font)
        self.lineEdit_TelefoneEmergencia.setObjectName(
            "lineEdit_TelefoneEmergencia")
        self.verticalLayout_33.addWidget(self.lineEdit_TelefoneEmergencia)
        self.horizontalLayout_15.addWidget(self.frame_DadosEmergencia_Coluna2)
        self.frame_DadosEmergencia_Coluna3 = QtWidgets.QFrame(
            self.frame_DadosEmergencia)
        self.frame_DadosEmergencia_Coluna3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_DadosEmergencia_Coluna3.setMaximumSize(
            QtCore.QSize(200, 16777215))
        self.frame_DadosEmergencia_Coluna3.setStyleSheet("")
        self.frame_DadosEmergencia_Coluna3.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.frame_DadosEmergencia_Coluna3.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_DadosEmergencia_Coluna3.setObjectName(
            "frame_DadosEmergencia_Coluna3")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(
            self.frame_DadosEmergencia_Coluna3)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_CelularEmergencia = QtWidgets.QLabel(
            self.frame_DadosEmergencia_Coluna3)
        self.label_CelularEmergencia.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CelularEmergencia.setFont(font)
        self.label_CelularEmergencia.setObjectName("label_CelularEmergencia")
        self.verticalLayout_35.addWidget(self.label_CelularEmergencia)
        self.lineEdit_CelularEmergencia = QtWidgets.QLineEdit(
            self.frame_DadosEmergencia_Coluna3)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_CelularEmergencia.setFont(font)
        self.lineEdit_CelularEmergencia.setObjectName(
            "lineEdit_CelularEmergencia")
        self.verticalLayout_35.addWidget(self.lineEdit_CelularEmergencia)
        self.horizontalLayout_15.addWidget(self.frame_DadosEmergencia_Coluna3)
        self.verticalLayout_38.addWidget(self.frame_DadosEmergencia)
        self.label_EducacaoTrabalho = QtWidgets.QLabel(
            self.scrollAreaWidget_OutrosDados)
        self.label_EducacaoTrabalho.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_EducacaoTrabalho.setFont(font)
        self.label_EducacaoTrabalho.setStyleSheet("#label_EducacaoTrabalho{\n"
                                                  "color: white;\n"
                                                  "}")
        self.label_EducacaoTrabalho.setObjectName("label_EducacaoTrabalho")
        self.verticalLayout_38.addWidget(self.label_EducacaoTrabalho)
        self.frame_EducacaoTrabalho = QtWidgets.QFrame(
            self.scrollAreaWidget_OutrosDados)
        self.frame_EducacaoTrabalho.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_EducacaoTrabalho.setAutoFillBackground(False)
        self.frame_EducacaoTrabalho.setStyleSheet("#frame_EducacaoTrabalho{\n"
                                                  "background-color: rgba(255, 255, 255, 229);\n"
                                                  "border-radius: 12px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "#label_Escolaridade{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "#label_Empresa{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "#label_Profissao{\n"
                                                  "color: rgb(43, 64, 205);\n"
                                                  "background-color: transparent;\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "#comboBox_Escolaridade{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "#lineEdit_Empresa{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "#lineEdit_Profissao{\n"
                                                  "color: white;\n"
                                                  "padding: 5px;\n"
                                                  "border-radius: 5px;\n"
                                                  "background-color: rgba(43, 64, 205, 128);\n"
                                                  "}")
        self.frame_EducacaoTrabalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_EducacaoTrabalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_EducacaoTrabalho.setObjectName("frame_EducacaoTrabalho")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(
            self.frame_EducacaoTrabalho)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_EducacaoTrabalho_Coluna1 = QtWidgets.QFrame(
            self.frame_EducacaoTrabalho)
        self.frame_EducacaoTrabalho_Coluna1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_EducacaoTrabalho_Coluna1.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_EducacaoTrabalho_Coluna1.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_EducacaoTrabalho_Coluna1.setStyleSheet("")
        self.frame_EducacaoTrabalho_Coluna1.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.frame_EducacaoTrabalho_Coluna1.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_EducacaoTrabalho_Coluna1.setObjectName(
            "frame_EducacaoTrabalho_Coluna1")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(
            self.frame_EducacaoTrabalho_Coluna1)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem14 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem14)
        self.label_Empresa = QtWidgets.QLabel(
            self.frame_EducacaoTrabalho_Coluna1)
        self.label_Empresa.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Empresa.setFont(font)
        self.label_Empresa.setObjectName("label_Empresa")
        self.horizontalLayout_16.addWidget(self.label_Empresa)
        self.lineEdit_Empresa = QtWidgets.QLineEdit(
            self.frame_EducacaoTrabalho_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Empresa.setFont(font)
        self.lineEdit_Empresa.setObjectName("lineEdit_Empresa")
        self.horizontalLayout_16.addWidget(self.lineEdit_Empresa)
        spacerItem15 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem15)
        self.label_Profissao = QtWidgets.QLabel(
            self.frame_EducacaoTrabalho_Coluna1)
        self.label_Profissao.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Profissao.setFont(font)
        self.label_Profissao.setObjectName("label_Profissao")
        self.horizontalLayout_16.addWidget(self.label_Profissao)
        self.lineEdit_Profissao = QtWidgets.QLineEdit(
            self.frame_EducacaoTrabalho_Coluna1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Profissao.setFont(font)
        self.lineEdit_Profissao.setObjectName("lineEdit_Profissao")
        self.horizontalLayout_16.addWidget(self.lineEdit_Profissao)
        spacerItem16 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem16)
        self.verticalLayout_25.addWidget(self.frame_EducacaoTrabalho_Coluna1)
        self.frame_EducacaoTrabalho_Coluna1_2 = QtWidgets.QFrame(
            self.frame_EducacaoTrabalho)
        self.frame_EducacaoTrabalho_Coluna1_2.setMinimumSize(
            QtCore.QSize(0, 0))
        self.frame_EducacaoTrabalho_Coluna1_2.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.frame_EducacaoTrabalho_Coluna1_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_EducacaoTrabalho_Coluna1_2.setStyleSheet("")
        self.frame_EducacaoTrabalho_Coluna1_2.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.frame_EducacaoTrabalho_Coluna1_2.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.frame_EducacaoTrabalho_Coluna1_2.setObjectName(
            "frame_EducacaoTrabalho_Coluna1_2")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(
            self.frame_EducacaoTrabalho_Coluna1_2)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_Escolaridade = QtWidgets.QLabel(
            self.frame_EducacaoTrabalho_Coluna1_2)
        self.label_Escolaridade.setMaximumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Escolaridade.setFont(font)
        self.label_Escolaridade.setObjectName("label_Escolaridade")
        self.horizontalLayout_17.addWidget(self.label_Escolaridade)
        self.comboBox_Escolaridade = QtWidgets.QComboBox(
            self.frame_EducacaoTrabalho_Coluna1_2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Escolaridade.setFont(font)
        self.comboBox_Escolaridade.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_Escolaridade.setObjectName("comboBox_Escolaridade")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.setItemText(0, "")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.addItem("")
        self.comboBox_Escolaridade.addItem("")
        self.horizontalLayout_17.addWidget(self.comboBox_Escolaridade)
        self.verticalLayout_25.addWidget(self.frame_EducacaoTrabalho_Coluna1_2)
        self.verticalLayout_38.addWidget(self.frame_EducacaoTrabalho)
        self.label_Observacoes = QtWidgets.QLabel(
            self.scrollAreaWidget_OutrosDados)
        self.label_Observacoes.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Observacoes.setFont(font)
        self.label_Observacoes.setStyleSheet("#label_Observacoes{\n"
                                             "color: white;\n"
                                             "}")
        self.label_Observacoes.setObjectName("label_Observacoes")
        self.verticalLayout_38.addWidget(self.label_Observacoes)
        self.frame_Observacoes = QtWidgets.QFrame(
            self.scrollAreaWidget_OutrosDados)
        self.frame_Observacoes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_Observacoes.setAutoFillBackground(False)
        self.frame_Observacoes.setStyleSheet("#frame_Observacoes{\n"
                                             "background-color: rgba(255, 255, 255, 229);\n"
                                             "border-radius: 12px;\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "#textEdit_Observacoes{\n"
                                             "color: white;\n"
                                             "padding: 5px;\n"
                                             "border-radius: 5px;\n"
                                             "background-color: rgba(43, 64, 205, 128);\n"
                                             "}")
        self.frame_Observacoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Observacoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Observacoes.setObjectName("frame_Observacoes")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_Observacoes)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.textEdit_Observacoes = QtWidgets.QTextEdit(self.frame_Observacoes)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_Observacoes.setFont(font)
        self.textEdit_Observacoes.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_Observacoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_Observacoes.setObjectName("textEdit_Observacoes")
        self.verticalLayout_34.addWidget(self.textEdit_Observacoes)
        self.verticalLayout_38.addWidget(self.frame_Observacoes)
        self.scrollArea_OutrosDados.setWidget(
            self.scrollAreaWidget_OutrosDados)
        self.verticalLayout_37.addWidget(self.scrollArea_OutrosDados)
        self.Paginas_Formulario.addWidget(self.pg_OutrosDados)
        self.verticalLayout_7.addWidget(self.Paginas_Formulario)
        self.PaginasPrincipais.addWidget(self.pgFormulario_NovoPaciente)
        self.horizontalLayout.addWidget(self.PaginasPrincipais)
        self.verticalLayout.addWidget(self.frame_CorpoGeral)
        Principal_Main.setCentralWidget(self.Plano_de_Fundo)

        self.retranslateUi(Principal_Main)
        self.PaginasPrincipais.setCurrentIndex(0)
        self.Paginas_Formulario.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Principal_Main)

    def retranslateUi(self, Principal_Main):
        _translate = QtCore.QCoreApplication.translate
        Principal_Main.setWindowTitle(
            _translate("Principal_Main", "MainWindow"))
        self.btn_Menu.setToolTip(_translate("Principal_Main", "Menu"))
        self.btn_Perfil.setToolTip(_translate("Principal_Main", "Perfil"))
        self.btn_Perfil.setText(_translate("Principal_Main", "..."))
        self.btn_Minimizar.setToolTip(
            _translate("Principal_Main", "Minimizar"))
        self.btn_Minimizar.setText(_translate("Principal_Main", "..."))
        self.btn_Maximizar.setToolTip(
            _translate("Principal_Main", "Maximizar"))
        self.btn_Maximizar.setText(_translate("Principal_Main", "..."))
        self.btn_Fechar.setToolTip(_translate("Principal_Main", "Fechar"))
        self.btn_Fechar.setText(_translate("Principal_Main", "..."))

        '''
        self.btn_Inicio.setToolTip(_translate("Principal_Main", "Inicio"))
        self.btn_Inicio.setText(_translate("Principal_Main", "INICIO"))
        '''

        self.btn_Paciente.setToolTip(_translate("Principal_Main", "Pacientes"))
        self.btn_Paciente.setText(_translate("Principal_Main", "PACIENTE"))
        self.labelPerfilPaciente.setText(
            _translate("Principal_Main", "Nome Paciente"))
        self.btn_NovaConsulta.setText(
            _translate("Principal_Main", "Nova Consulta"))
        '''
        self.label_Calendario.setText(
            _translate("Principal_Main", "CALENDÁRIO"))
        
        self.label_AcessosRecentes.setText(
            _translate("Principal_Main", "ACESSOS RECENTES"))
        
        item = self.tableWidget_AcessosRecentes.horizontalHeaderItem(0)
        item.setText(_translate("Principal_Main", "Nome"))
        item = self.tableWidget_AcessosRecentes.horizontalHeaderItem(1)
        item.setText(_translate("Principal_Main", "N° Prontuário"))
        '''
        self.btn_NovoPaciente.setToolTip(
            _translate("Principal_Main", "Novo Paciente"))
        self.btn_NovoPaciente.setText(
            _translate("Principal_Main", "Novo Paciente"))
        self.lineEdit_PesquisarPaciente.setToolTip(
            _translate("Principal_Main", "Pesquisar Pacientes"))
        self.lineEdit_PesquisarPaciente.setPlaceholderText(
            _translate("Principal_Main", "Pesquisar..."))
        self.tableWidget_ListaPacientes.setSortingEnabled(False)
        item = self.tableWidget_ListaPacientes.horizontalHeaderItem(0)
        item.setText(_translate("Principal_Main", "N° Prontuário"))
        item = self.tableWidget_ListaPacientes.horizontalHeaderItem(1)
        item.setText(_translate("Principal_Main", "CPF"))
        item = self.tableWidget_ListaPacientes.horizontalHeaderItem(2)
        item.setText(_translate("Principal_Main", "Nascimento"))
        item = self.tableWidget_ListaPacientes.horizontalHeaderItem(3)
        self.tableWidget_ListaPacientes.setEditTriggers(QTableWidget.NoEditTriggers)


        item.setText(_translate("Principal_Main", "Nome"))
        self.btn_DadosPrincipais.setText(
            _translate("Principal_Main", "Dados Principais"))
        self.btn_OutrosDados.setText(
            _translate("Principal_Main", "Outros Dados"))
        self.btn_Consultas.setText(_translate("Principal_Main", "Consultas"))
        self.btn_Salvar.setText(_translate("Principal_Main", "Salvar"))
        self.btn_Cancelar.setText(_translate("Principal_Main", "Cancelar"))
        self.btn_Prontuario.setText(_translate(
            "Principal_Main", "   Prontuário"))
        self.label_Identificacao.setText(
            _translate("Principal_Main", "IDENTIFICAÇÃO"))
        self.label_Nome.setText(_translate("Principal_Main", "Nome:"))
        self.label_NomeSocial.setText(
            _translate("Principal_Main", "Nome Social:"))
        self.label_Naturalidade.setText(
            _translate("Principal_Main", "Naturalidade:"))
        self.label_CPF.setText(_translate("Principal_Main", "CPF:"))
        self.label_RG.setText(_translate("Principal_Main", "RG:"))
        self.label_Emissor.setText(_translate("Principal_Main", "Emissor:"))
        self.label_DataNascimento.setText(
            _translate("Principal_Main", "Nascimento:"))
        self.label_Sexo.setText(_translate("Principal_Main", "Sexo:"))
        self.comboBox_Sexo.setItemText(
            1, _translate("Principal_Main", "Masculino"))
        self.comboBox_Sexo.setItemText(
            2, _translate("Principal_Main", "Feminino"))
        self.comboBox_Sexo.setItemText(
            3, _translate("Principal_Main", "Outros"))
        self.label_EstadoCivil.setText(
            _translate("Principal_Main", "Estado Civil:"))
        self.comboBox_EstadoCivil.setItemText(
            1, _translate("Principal_Main", "Solteiro"))
        self.comboBox_EstadoCivil.setItemText(
            2, _translate("Principal_Main", "Casado"))
        self.comboBox_EstadoCivil.setItemText(
            3, _translate("Principal_Main", "Divorciado"))
        self.comboBox_EstadoCivil.setItemText(
            4, _translate("Principal_Main", "Viúvo"))
        self.label_Endereco.setText(_translate("Principal_Main", "ENDEREÇO"))
        self.label_CEP.setText(_translate("Principal_Main", "CEP:"))
        self.label_UF.setText(_translate("Principal_Main", "UF:"))
        self.comboBox_UF.setItemText(1, _translate("Principal_Main", "AC"))
        self.comboBox_UF.setItemText(2, _translate("Principal_Main", "AL"))
        self.comboBox_UF.setItemText(3, _translate("Principal_Main", "AP"))
        self.comboBox_UF.setItemText(4, _translate("Principal_Main", "AM"))
        self.comboBox_UF.setItemText(5, _translate("Principal_Main", "BA"))
        self.comboBox_UF.setItemText(6, _translate("Principal_Main", "CE"))
        self.comboBox_UF.setItemText(7, _translate("Principal_Main", "DF"))
        self.comboBox_UF.setItemText(8, _translate("Principal_Main", "ES"))
        self.comboBox_UF.setItemText(9, _translate("Principal_Main", "GO"))
        self.comboBox_UF.setItemText(10, _translate("Principal_Main", "MA"))
        self.comboBox_UF.setItemText(11, _translate("Principal_Main", "MT"))
        self.comboBox_UF.setItemText(12, _translate("Principal_Main", "MS"))
        self.comboBox_UF.setItemText(13, _translate("Principal_Main", "MG"))
        self.comboBox_UF.setItemText(14, _translate("Principal_Main", "PA"))
        self.comboBox_UF.setItemText(15, _translate("Principal_Main", "PB"))
        self.comboBox_UF.setItemText(16, _translate("Principal_Main", "PR"))
        self.comboBox_UF.setItemText(17, _translate("Principal_Main", "PE"))
        self.comboBox_UF.setItemText(18, _translate("Principal_Main", "PI"))
        self.comboBox_UF.setItemText(19, _translate("Principal_Main", "RJ"))
        self.comboBox_UF.setItemText(20, _translate("Principal_Main", "RN"))
        self.comboBox_UF.setItemText(21, _translate("Principal_Main", "RS"))
        self.comboBox_UF.setItemText(22, _translate("Principal_Main", "RO"))
        self.comboBox_UF.setItemText(23, _translate("Principal_Main", "RR"))
        self.comboBox_UF.setItemText(24, _translate("Principal_Main", "SC"))
        self.comboBox_UF.setItemText(25, _translate("Principal_Main", "SP"))
        self.comboBox_UF.setItemText(26, _translate("Principal_Main", "SE"))
        self.comboBox_UF.setItemText(27, _translate("Principal_Main", "TO"))
        self.label_Cidade.setText(_translate("Principal_Main", "Cidade:"))
        self.label_Bairro.setText(_translate("Principal_Main", "Bairro:"))
        self.label_Numero.setText(_translate("Principal_Main", "Número:"))
        self.label_Logradouro.setText(
            _translate("Principal_Main", "Logradouro:"))
        self.label_Complemento.setText(
            _translate("Principal_Main", "Complemento:"))
        self.label_Contato.setText(_translate("Principal_Main", "CONTATO"))
        self.label_Celular.setText(_translate("Principal_Main", "Celular:"))
        self.label_Telefone.setText(_translate("Principal_Main", "Telefone:"))
        self.label_Email.setText(_translate("Principal_Main", "E-mail:"))
        self.label_Atendimento.setText(
            _translate("Principal_Main", "ATENDIMENTO"))
        self.label_Profissional.setText(
            _translate("Principal_Main", "Profissional:"))
        self.label_Categoria.setText(
            _translate("Principal_Main", "Categoria:"))
        self.comboBox_Categoria.setItemText(
            1, _translate("Principal_Main", "Ativo"))
        self.comboBox_Categoria.setItemText(
            2, _translate("Principal_Main", "Inativo"))
        self.label_Cadastro.setText(_translate("Principal_Main", "CADASTRO"))
        self.label_DataCadastro.setText(_translate(
            "Principal_Main", "Data do Cadastro:"))
        self.label_FatorSanguineo.setText(
            _translate("Principal_Main", "Fator Sanguíneo:"))
        self.comboBox_FatorSanguineo.setItemText(
            1, _translate("Principal_Main", "A+"))
        self.comboBox_FatorSanguineo.setItemText(
            2, _translate("Principal_Main", "B+"))
        self.comboBox_FatorSanguineo.setItemText(
            3, _translate("Principal_Main", "AB+"))
        self.comboBox_FatorSanguineo.setItemText(
            4, _translate("Principal_Main", "O+"))
        self.comboBox_FatorSanguineo.setItemText(
            5, _translate("Principal_Main", "A-"))
        self.comboBox_FatorSanguineo.setItemText(
            6, _translate("Principal_Main", "B-"))
        self.comboBox_FatorSanguineo.setItemText(
            7, _translate("Principal_Main", "AB-"))
        self.comboBox_FatorSanguineo.setItemText(
            8, _translate("Principal_Main", "O-"))
        self.label_CNS.setText(_translate("Principal_Main", "CNS:"))
        self.label_Raca.setText(_translate("Principal_Main", "Raça:"))
        self.comboBox_Raca.setItemText(
            1, _translate("Principal_Main", "Amarelo"))
        self.comboBox_Raca.setItemText(
            2, _translate("Principal_Main", "Branco"))
        self.comboBox_Raca.setItemText(
            3, _translate("Principal_Main", "Indígena"))
        self.comboBox_Raca.setItemText(
            4, _translate("Principal_Main", "Pardo"))
        self.comboBox_Raca.setItemText(
            5, _translate("Principal_Main", "Preto"))
        self.label_DadosFamiliares.setText(
            _translate("Principal_Main", "DADOS FAMILIARES"))
        self.label_NomeMae.setText(_translate(
            "Principal_Main", "Nome da Mãe:"))
        self.label_NomePai.setText(_translate(
            "Principal_Main", "Nome do Pai:"))
        self.label_QuantFilhos.setText(_translate(
            "Principal_Main", "Quantidade de Filhos:"))
        self.label_NomeConjuge.setText(_translate(
            "Principal_Main", "Nome do Conjuge:"))
        self.label_CPFconjuge.setText(_translate(
            "Principal_Main", "CPF do Conjuge:"))
        self.label_NascimentoConjuge.setText(_translate(
            "Principal_Main", "Nascimento do Conjuge:"))
        self.label_NomeResponsavel.setText(_translate(
            "Principal_Main", "Nome do Responsável:"))
        self.label_CPFResponsavel.setText(_translate(
            "Principal_Main", "CPF do Responsável:"))
        self.label_TelefoneResponsavel.setText(_translate(
            "Principal_Main", "Telefone do Responsável:"))
        self.label_DadosEmergencia.setText(
            _translate("Principal_Main", "DADOS DE EMERGÊNCIA"))
        self.label_NomeContatoEmergencia.setText(
            _translate("Principal_Main", "Nome do Contato:"))
        self.label_TelefoneEmergencia.setText(
            _translate("Principal_Main", "Telefone:"))
        self.label_CelularEmergencia.setText(
            _translate("Principal_Main", "Celular:"))
        self.label_EducacaoTrabalho.setText(
            _translate("Principal_Main", "EDUCAÇÃO E TRABALHO"))
        self.label_Empresa.setText(_translate("Principal_Main", "Empresa:"))
        self.label_Profissao.setText(
            _translate("Principal_Main", "Profissão:"))
        self.label_Escolaridade.setText(
            _translate("Principal_Main", "Escolaridade:"))
        self.comboBox_Escolaridade.setItemText(1, _translate(
            "Principal_Main", "Ensino Fundamental Incompleto"))
        self.comboBox_Escolaridade.setItemText(2, _translate(
            "Principal_Main", "Ensino Fundamental Completo"))
        self.comboBox_Escolaridade.setItemText(
            3, _translate("Principal_Main", "Ensino Médio Incompleto"))
        self.comboBox_Escolaridade.setItemText(
            4, _translate("Principal_Main", "Ensino Médio Completo"))
        self.comboBox_Escolaridade.setItemText(5, _translate(
            "Principal_Main", "Ensino Superior Incompleto"))
        self.comboBox_Escolaridade.setItemText(6, _translate(
            "Principal_Main", "Ensino Superior Completo"))
        self.comboBox_Escolaridade.setItemText(
            7, _translate("Principal_Main", "Mestrado"))
        self.comboBox_Escolaridade.setItemText(
            8, _translate("Principal_Main", "Doutorado"))
        self.comboBox_Escolaridade.setItemText(
            9, _translate("Principal_Main", "Sem Escolaridade"))
        self.label_Observacoes.setText(
            _translate("Principal_Main", "OBSERVAÇÕES"))
