from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Principal_Login(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(640, 480)
        self.centralwidget_Login = QtWidgets.QWidget(Principal)
        self.centralwidget_Login.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget_Login.setAutoFillBackground(False)
        self.centralwidget_Login.setStyleSheet("#centralwidget_Login{\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.497522, y1:1, x2:0.581697, y2:0, stop:0 rgba(21, 178, 255, 255), stop:1 rgba(0, 30, 255, 255))\n"
                                               "}\n"
                                               "\n"
                                               "#label_Topo{\n"
                                               "color: white;\n"
                                               "}\n"
                                               "\n"
                                               "#label_CRM{\n"
                                               "color: white;\n"
                                               "}\n"
                                               "\n"
                                               "#lineEdit_CRM{\n"
                                               "padding: 5px;\n"
                                               "border-radius: 12px;\n"
                                               "color: blue;\n"
                                               "}\n"
                                               "\n"
                                               "#label_Senha{\n"
                                               "color: white;\n"
                                               "}\n"
                                               "\n"
                                               "#lineEdit_Senha{\n"
                                               "padding: 5px;\n"
                                               "border-radius: 12px;\n"
                                               "color: blue;\n"
                                               "}\n"
                                               "\n"
                                               "#btn_Entrar{\n"
                                               "background-color: #5688E1;\n"
                                               "color: white;\n"
                                               "}")
        self.centralwidget_Login.setObjectName("centralwidget_Login")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget_Login)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_Topo = QtWidgets.QFrame(self.centralwidget_Login)
        self.frame_Topo.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_Topo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Topo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Topo.setObjectName("frame_Topo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_Topo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Topo = QtWidgets.QLabel(self.frame_Topo)
        self.label_Topo.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Topo.setFont(font)
        self.label_Topo.setObjectName("label_Topo")
        self.horizontalLayout.addWidget(self.label_Topo)
        self.verticalLayout.addWidget(self.frame_Topo)
        self.frame_Itens = QtWidgets.QFrame(self.centralwidget_Login)
        self.frame_Itens.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_Itens.setStyleSheet("")
        self.frame_Itens.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Itens.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Itens.setObjectName("frame_Itens")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_Itens)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.frame_Itens2 = QtWidgets.QFrame(self.frame_Itens)
        self.frame_Itens2.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_Itens2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_Itens2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Itens2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Itens2.setObjectName("frame_Itens2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_Itens2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_CRM = QtWidgets.QLabel(self.frame_Itens2)
        self.label_CRM.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CRM.setFont(font)
        self.label_CRM.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_CRM.setWordWrap(False)
        self.label_CRM.setObjectName("label_CRM")
        self.verticalLayout_3.addWidget(self.label_CRM)
        self.lineEdit_CRM = QtWidgets.QLineEdit(self.frame_Itens2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.lineEdit_CRM.setFont(font)
        self.lineEdit_CRM.setDragEnabled(False)
        self.lineEdit_CRM.setClearButtonEnabled(True)
        self.lineEdit_CRM.setObjectName("lineEdit_CRM")
        self.verticalLayout_3.addWidget(self.lineEdit_CRM)
        self.label_Senha = QtWidgets.QLabel(self.frame_Itens2)
        self.label_Senha.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Senha.setFont(font)
        self.label_Senha.setObjectName("label_Senha")
        self.verticalLayout_3.addWidget(self.label_Senha)

        
        self.lineEdit_Senha = QtWidgets.QLineEdit(self.frame_Itens2)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.lineEdit_Senha.setFont(font)
        self.lineEdit_Senha.setClearButtonEnabled(True)
        self.lineEdit_Senha.setObjectName("lineEdit_Senha")
        self.lineEdit_Senha.setEchoMode(QtWidgets.QLineEdit.Password) #Senha em formato de Ponto
        self.verticalLayout_3.addWidget(self.lineEdit_Senha)
        self.btn_Entrar = QtWidgets.QToolButton(self.frame_Itens2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Entrar.sizePolicy().hasHeightForWidth())
        self.btn_Entrar.setSizePolicy(sizePolicy)
        self.btn_Entrar.setMinimumSize(QtCore.QSize(190, 0))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Entrar.setFont(font)
        self.btn_Entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Entrar.setIconSize(QtCore.QSize(50, 50))
        self.btn_Entrar.setAutoRepeat(False)
        self.btn_Entrar.setAutoExclusive(False)
        self.btn_Entrar.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_Entrar.setAutoRaise(False)
        self.btn_Entrar.setArrowType(QtCore.Qt.NoArrow)
        self.btn_Entrar.setObjectName("btn_Entrar")
        self.verticalLayout_3.addWidget(self.btn_Entrar)
        self.horizontalLayout_2.addWidget(self.frame_Itens2)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_Itens)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.frame_Rodape = QtWidgets.QFrame(self.centralwidget_Login)
        self.frame_Rodape.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_Rodape.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Rodape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Rodape.setObjectName("frame_Rodape")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_Rodape)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_IconAtencao = QtWidgets.QFrame(self.frame_Rodape)
        self.frame_IconAtencao.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_IconAtencao.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_IconAtencao.setStyleSheet(
            "border-image: url(:/Icons/icon_Atencao.png);")
        self.frame_IconAtencao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_IconAtencao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_IconAtencao.setObjectName("frame_IconAtencao")
        self.horizontalLayout_3.addWidget(self.frame_IconAtencao)
        self.label_LinkAtencao = QtWidgets.QLabel(self.frame_Rodape)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_LinkAtencao.setFont(font)
        self.label_LinkAtencao.setStyleSheet(
            "#label_LinkAtencao{color: white;}")
        self.label_LinkAtencao.setObjectName("label_LinkAtencao")
        self.horizontalLayout_3.addWidget(self.label_LinkAtencao)
        self.verticalLayout.addWidget(self.frame_Rodape)
        Principal.setCentralWidget(self.centralwidget_Login)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "MainWindow"))
        self.label_Topo.setText(_translate("Principal", "BEM-VINDO!"))
        self.label_CRM.setText(_translate("Principal", "CRM"))
        self.label_Senha.setText(_translate("Principal", "SENHA"))
        self.btn_Entrar.setText(_translate("Principal", "Entrar"))
        self.label_LinkAtencao.setText(_translate(
            "Principal", " www.projepis.com/support"))

from Img.Img_Login_ import Icons_Login_rc
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
'''
