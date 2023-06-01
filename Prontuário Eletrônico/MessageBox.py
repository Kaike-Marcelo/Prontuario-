from PyQt5.QtWidgets import QMessageBox


def showInfoMessage(message):

    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("Sucesso")
    msg_box.setText(message)
    msg_box.exec_()


def showErrorMessage(message):
        
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle("Erro")
    msg.exec_()