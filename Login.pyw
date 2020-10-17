
from PyQt5 import QtCore, QtGui, QtWidgets
from PDV import Ui_PDV

class Ui_TelaLogin(object):

    def LoginOK(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PDV()
        self.ui.setupUi(self.window)
        TelaLogin.hide()
        self.window.show()


    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName("TelaLogin")
        TelaLogin.resize(424, 202)
        self.centralwidget = QtWidgets.QWidget(TelaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.CancelarButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarButton.setGeometry(QtCore.QRect(241, 135, 91, 31))
        self.CancelarButton.setObjectName("CancelarButton")
        self.LabelSenha = QtWidgets.QLabel(self.centralwidget)
        self.LabelSenha.setGeometry(QtCore.QRect(69, 36, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.LabelSenha.setFont(font)
        self.LabelSenha.setObjectName("LabelSenha")
        self.OkButton = QtWidgets.QPushButton(self.centralwidget)
        self.OkButton.setGeometry(QtCore.QRect(134, 135, 91, 31))
        self.OkButton.setObjectName("OkButton")
        self.OkButton.clicked.connect(self.LoginOK)

        self.EntrySenha = QtWidgets.QLineEdit(self.centralwidget)
        self.EntrySenha.setGeometry(QtCore.QRect(139, 39, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EntrySenha.setFont(font)
        self.EntrySenha.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.EntrySenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EntrySenha.setAlignment(QtCore.Qt.AlignCenter)
        self.EntrySenha.setObjectName("EntrySenha")
        TelaLogin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TelaLogin)
        self.statusbar.setObjectName("statusbar")
        TelaLogin.setStatusBar(self.statusbar)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

    def retranslateUi(self, TelaLogin):
        _translate = QtCore.QCoreApplication.translate
        TelaLogin.setWindowTitle(_translate("TelaLogin", "Super Market PDV"))
        self.CancelarButton.setText(_translate("TelaLogin", "Cancelar"))
        self.LabelSenha.setText(_translate("TelaLogin", "Senha:"))
        self.OkButton.setText(_translate("TelaLogin", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLogin = QtWidgets.QMainWindow()
    ui = Ui_TelaLogin()
    ui.setupUi(TelaLogin)
    TelaLogin.show()
    sys.exit(app.exec_())

