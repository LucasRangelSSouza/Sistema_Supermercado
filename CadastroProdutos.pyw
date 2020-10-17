
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_CadastroDeProdutos(object):
    def Salvar(self):
        conexao = sqlite3.connect("SuperMarket.db")
        banco = conexao.cursor()
        print("aqui")
        CODIGO = "'"+str(self.EntryCodigo.text())+"'"
        DESCRICAO = "'"+str(self.EntryDescricao.text())+"'"
        PRECOVENDA = "'"+str(self.EntryPrecoVenda.text())+"'"
        PRECOCUSTO="'"+str(self.EntryPrecoCusto.text())+"'"
        print(CODIGO,DESCRICAO)
        sql = "INSERT INTO Produto (CODIGO,DESCRICAO,PRECO_VENDA,PRECO_CUSTO)VALUES ("+CODIGO+","+DESCRICAO+","+PRECOVENDA+","+PRECOCUSTO+");"
        banco.execute(sql)
        conexao.commit()
        self.EntryCodigo.setText("")
        self.EntryDescricao.setText("")
        self.EntryPrecoVenda.setText("")
        self.EntryPrecoCusto.setText("")

    def Cancelar(self):
        CadastroDeProdutos.hide()

    def setupUi(self, CadastroDeProdutos):
        CadastroDeProdutos.setObjectName("CadastroDeProdutos")
        CadastroDeProdutos.resize(727, 345)
        CadastroDeProdutos.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.centralwidget = QtWidgets.QWidget(CadastroDeProdutos)
        self.centralwidget.setObjectName("centralwidget")
        self.EntryCodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.EntryCodigo.setGeometry(QtCore.QRect(220, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.EntryCodigo.setFont(font)
        self.EntryCodigo.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(147, 147, 147);")
        self.EntryCodigo.setText("")
        self.EntryCodigo.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryCodigo.setObjectName("EntryCodigo")
        self.EntryDescricao = QtWidgets.QLineEdit(self.centralwidget)
        self.EntryDescricao.setGeometry(QtCore.QRect(220, 85, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.EntryDescricao.setFont(font)
        self.EntryDescricao.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(147, 147, 147);")
        self.EntryDescricao.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryDescricao.setObjectName("EntryDescricao")
        self.EntryPrecoVenda = QtWidgets.QLineEdit(self.centralwidget)
        self.EntryPrecoVenda.setGeometry(QtCore.QRect(220, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.EntryPrecoVenda.setFont(font)
        self.EntryPrecoVenda.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(147, 147, 147);")
        self.EntryPrecoVenda.setText("")
        self.EntryPrecoVenda.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryPrecoVenda.setObjectName("EntryPrecoVenda")
        self.EntryPrecoCusto = QtWidgets.QLineEdit(self.centralwidget)
        self.EntryPrecoCusto.setGeometry(QtCore.QRect(220, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.EntryPrecoCusto.setFont(font)
        self.EntryPrecoCusto.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(147, 147, 147);")
        self.EntryPrecoCusto.setText("")
        self.EntryPrecoCusto.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryPrecoCusto.setObjectName("EntryPrecoCusto")
        self.ButtonSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSalvar.setGeometry(QtCore.QRect(190, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ButtonSalvar.setFont(font)
        self.ButtonSalvar.setStyleSheet("background-color: #25ecd3;\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);")
        self.ButtonSalvar.setObjectName("ButtonSalvar")
        self.ButtonSalvar.clicked.connect(self.Salvar)

        self.LabelCodigo = QtWidgets.QLabel(self.centralwidget)
        self.LabelCodigo.setGeometry(QtCore.QRect(100, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.LabelCodigo.setFont(font)
        self.LabelCodigo.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelCodigo.setObjectName("LabelCodigo")
        self.LabelDescricao = QtWidgets.QLabel(self.centralwidget)
        self.LabelDescricao.setGeometry(QtCore.QRect(84, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.LabelDescricao.setFont(font)
        self.LabelDescricao.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelDescricao.setObjectName("LabelDescricao")
        self.LabelPecoVenda = QtWidgets.QLabel(self.centralwidget)
        self.LabelPecoVenda.setGeometry(QtCore.QRect(40, 130, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.LabelPecoVenda.setFont(font)
        self.LabelPecoVenda.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelPecoVenda.setObjectName("LabelPecoVenda")
        self.LabelPrecoCusto = QtWidgets.QLabel(self.centralwidget)
        self.LabelPrecoCusto.setGeometry(QtCore.QRect(40, 180, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.LabelPrecoCusto.setFont(font)
        self.LabelPrecoCusto.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelPrecoCusto.setObjectName("LabelPrecoCusto")
        self.ButtonCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonCancelar.setGeometry(QtCore.QRect(330, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ButtonCancelar.setFont(font)
        self.ButtonCancelar.setStyleSheet("background-color: #25ecd3;\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);")
        self.ButtonCancelar.setObjectName("ButtonCancelar")
        self.ButtonExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExcluir.setGeometry(QtCore.QRect(470, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ButtonExcluir.setFont(font)
        self.ButtonExcluir.setStyleSheet("background-color: #25ecd3;\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);")
        self.ButtonExcluir.setObjectName("ButtonExcluir")
        CadastroDeProdutos.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadastroDeProdutos)
        QtCore.QMetaObject.connectSlotsByName(CadastroDeProdutos)

    def retranslateUi(self, CadastroDeProdutos):
        _translate = QtCore.QCoreApplication.translate
        CadastroDeProdutos.setWindowTitle(_translate("CadastroDeProdutos", "Cadastro de Produtos"))
        self.ButtonSalvar.setText(_translate("CadastroDeProdutos", "SALVAR"))
        self.LabelCodigo.setText(_translate("CadastroDeProdutos", "CODIGO"))
        self.LabelDescricao.setText(_translate("CadastroDeProdutos", "DESCRIÇÃO"))
        self.LabelPecoVenda.setText(_translate("CadastroDeProdutos", "PREÇO DE VENDA"))
        self.LabelPrecoCusto.setText(_translate("CadastroDeProdutos", "PREÇO DE CUSTO"))
        self.ButtonCancelar.setText(_translate("CadastroDeProdutos", "CANCELAR"))
        self.ButtonExcluir.setText(_translate("CadastroDeProdutos", "EXCLUIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadastroDeProdutos = QtWidgets.QMainWindow()
    ui = Ui_CadastroDeProdutos()
    ui.setupUi(CadastroDeProdutos)
    CadastroDeProdutos.show()
    sys.exit(app.exec_())

