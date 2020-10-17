# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PDV.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from CadastroProdutos import Ui_CadastroDeProdutos
import sqlite3
class Ui_PDV(object):

    def AumentaQuantidade(self):
        self.EditQuantidade.setText(str(int(self.EditQuantidade.text())+1))

    def DiminuiQuantidade(self):
        self.EditQuantidade.setText(str(int(self.EditQuantidade.text()) - 1))
    def VendeProduto(self):
        EAN=self.EntryEAN.text()

    def AbrirCadastroProdutos(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CadastroDeProdutos()
        self.ui.setupUi(self.window)
        self.window.show()


    Total = float(0)
    def VendeProduto(self):
        print("hihihi")
        conexao = sqlite3.connect("SuperMarket.db")
        banco = conexao.cursor()
        CODIGO= "'"+self.EntryEAN.text()+"'"
        sql="select * from PRODUTO where codigo like "+CODIGO
        banco.execute(sql)
        Result = banco.fetchall()
        rowPosition = self.TableProdutos.rowCount()
        self.TableProdutos.insertRow(rowPosition)
        print(str(self.EditQuantidade.text()))
        Quantidade = float(self.EditQuantidade.text())
        Valor = float((Result[0][3]))
        self.TableProdutos.setItem(rowPosition, 0,QTableWidgetItem(str(self.EditQuantidade.text())))
        self.TableProdutos.setItem(rowPosition, 1,QTableWidgetItem(str(Result[0][1])))
        self.TableProdutos.setItem(rowPosition, 2,QTableWidgetItem(str(Result[0][2])))
        self.TableProdutos.setItem(rowPosition, 3,QTableWidgetItem(str(Result[0][3])))
        self.TableProdutos.setItem(rowPosition, 4,QTableWidgetItem(str(Quantidade*Valor)))
        self.EntryEAN.setText("")
        self.Total=(Quantidade*Valor)+self.Total
        self.LabelSubtotalValor.setText(str(self.Total))
        self.LabelTotalValor.setText(str(self.Total).replace(".",","))

    def FecharConta(self):
        self.LabelSubtotalValor.setText("0,00")
        self.LabelTotalValor.setText(str("0,0"))
        rowPosition = self.TableProdutos.rowCount()
        while (rowPosition != 0):
            rowPosition = self.TableProdutos.rowCount()-1
            self.TableProdutos.removeRow(rowPosition)
        self.TableProdutos.removeRow(rowPosition)
        self.Total=0



    def setupUi(self, PDV):
        PDV.setObjectName("PDV")
        PDV.resize(1366, 767)
        self.centralwidget = QtWidgets.QWidget(PDV)
        self.centralwidget.setObjectName("centralwidget")

        #Frame com os valores
        self.ContainerValores = QtWidgets.QFrame(self.centralwidget)
        self.ContainerValores.setGeometry(QtCore.QRect(930, 0, 441, 771))
        self.ContainerValores.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.ContainerValores.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContainerValores.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContainerValores.setObjectName("ContainerValores")

        #Label Com o total da venda
        self.LabelTotal = QtWidgets.QLabel(self.ContainerValores)
        self.LabelTotal.setGeometry(QtCore.QRect(0, 540, 431, 51))

        #Label Valor Total
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTotal.setFont(font)
        self.LabelTotal.setStyleSheet("color: rgb(212, 212, 212);")
        self.LabelTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelTotal.setObjectName("LabelTotal")
        self.LabelTotalValor = QtWidgets.QLabel(self.ContainerValores)
        self.LabelTotalValor.setGeometry(QtCore.QRect(0, 590, 431, 61))

        font = QtGui.QFont()
        font.setPointSize(38)
        font.setBold(False)
        font.setWeight(50)
        self.LabelTotalValor.setFont(font)
        self.LabelTotalValor.setStyleSheet("color: rgb(255, 255, 255);\n""")
        self.LabelTotalValor.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelTotalValor.setObjectName("LabelTotalValor")
        self.LabelSubtotal = QtWidgets.QLabel(self.ContainerValores)
        self.LabelSubtotal.setGeometry(QtCore.QRect(30, 390, 91, 21))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSubtotal.setFont(font)
        self.LabelSubtotal.setStyleSheet("color: rgb(212, 212, 212);")
        self.LabelSubtotal.setObjectName("LabelSubtotal")
        self.LabelDesconto = QtWidgets.QLabel(self.ContainerValores)
        self.LabelDesconto.setGeometry(QtCore.QRect(30, 440, 111, 21))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelDesconto.setFont(font)
        self.LabelDesconto.setStyleSheet("color: rgb(212, 212, 212);")
        self.LabelDesconto.setObjectName("LabelDesconto")

        self.LabelAcrescimo = QtWidgets.QLabel(self.ContainerValores)
        self.LabelAcrescimo.setGeometry(QtCore.QRect(30, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelAcrescimo.setFont(font)
        self.LabelAcrescimo.setStyleSheet("color: rgb(212, 212, 212);")
        self.LabelAcrescimo.setObjectName("LabelAcrescimo")

        self.LabelSubtotalValor = QtWidgets.QLabel(self.ContainerValores)
        self.LabelSubtotalValor.setGeometry(QtCore.QRect(170, 390, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LabelSubtotalValor.setFont(font)
        self.LabelSubtotalValor.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelSubtotalValor.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelSubtotalValor.setObjectName("LabelSubtotalValor")

        self.EntryDescontoValor = QtWidgets.QLineEdit(self.ContainerValores)
        self.EntryDescontoValor.setGeometry(QtCore.QRect(168, 434, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EntryDescontoValor.setFont(font)
        self.EntryDescontoValor.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(97, 97, 97);\n"
"border-top-right-radius: 1px;\n"
"border-bottom-right-radius: 1px;")

        self.EntryDescontoValor.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryDescontoValor.setObjectName("EntryDescontoValor")

        self.EntryAcrescimoValor = QtWidgets.QLineEdit(self.ContainerValores)
        self.EntryAcrescimoValor.setGeometry(QtCore.QRect(168, 480, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EntryAcrescimoValor.setFont(font)
        self.EntryAcrescimoValor.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(97, 97, 97);\n"
"border-top-right-radius: 1px;\n"
"border-bottom-right-radius: 1px;")
        self.EntryAcrescimoValor.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryAcrescimoValor.setObjectName("EntryAcrescimoValor")

        self.ButtonReceber = QtWidgets.QPushButton(self.ContainerValores)
        self.ButtonReceber.setGeometry(QtCore.QRect(0, 690, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonReceber.setFont(font)
        self.ButtonReceber.setStyleSheet("background-color: #25ecd3;\n"
"border-top-right-radius: 1px;\n"
"border-bottom-right-radius: 1px;\n"
"color: rgb(255, 255, 255);")
        self.ButtonReceber.setObjectName("ButtonReceber")
        self.ButtonReceber.clicked.connect(self.FecharConta)
        self.LabelEANLogo = QtWidgets.QLabel(self.centralwidget)
        self.LabelEANLogo.setGeometry(QtCore.QRect(377, 20, 71, 61))
        self.LabelEANLogo.setStyleSheet("border-top:0px solid #25ecd3;\n"
"border-right:0px solid #25ecd3;\n"
"border-bottom:0px solid #25ecd3;\n"
"border-left:0px solid #25ecd3;\n"
"background-color: #25ecd3;")
        self.LabelEANLogo.setText("")
        self.LabelEANLogo.setPixmap(QtGui.QPixmap("Imagens/Icones/EAN.png"))
        self.LabelEANLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelEANLogo.setObjectName("LabelEANLogo")
        self.EntryEAN = QtWidgets.QLineEdit(self.centralwidget)
        self.EntryEAN.setGeometry(QtCore.QRect(447, 20, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EntryEAN.setFont(font)
        self.EntryEAN.setStyleSheet("background-color: #25ecd3;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"")
        self.EntryEAN.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryEAN.setObjectName("EntryEAN")
        self.EntryEAN.returnPressed.connect(self.VendeProduto)

        self.EditQuantidade = QtWidgets.QLineEdit(self.centralwidget)
        self.EditQuantidade.setGeometry(QtCore.QRect(317, 20, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.EditQuantidade.setFont(font)
        self.EditQuantidade.setStyleSheet("background-color: #25ecd3;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.EditQuantidade.setAlignment(QtCore.Qt.AlignCenter)
        self.EditQuantidade.setObjectName("EditQuantidade")
        self.ContainerDados = QtWidgets.QFrame(self.centralwidget)
        self.ContainerDados.setGeometry(QtCore.QRect(-1, -1, 241, 771))
        self.ContainerDados.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.ContainerDados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContainerDados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContainerDados.setObjectName("ContainerDados")
        self.LabelDiaSemana = QtWidgets.QLabel(self.ContainerDados)
        self.LabelDiaSemana.setGeometry(QtCore.QRect(0, 179, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LabelDiaSemana.setFont(font)
        self.LabelDiaSemana.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelDiaSemana.setObjectName("LabelDiaSemana")
        self.LabelData = QtWidgets.QLabel(self.ContainerDados)
        self.LabelData.setGeometry(QtCore.QRect(0, 212, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LabelData.setFont(font)
        self.LabelData.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelData.setObjectName("LabelData")
        self.LabelPerfil = QtWidgets.QLabel(self.ContainerDados)
        self.LabelPerfil.setGeometry(QtCore.QRect(0, 302, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelPerfil.setFont(font)
        self.LabelPerfil.setStyleSheet("color: rgb(147, 147, 147);")
        self.LabelPerfil.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelPerfil.setObjectName("LabelPerfil")
        self.LabelOperador = QtWidgets.QLabel(self.ContainerDados)
        self.LabelOperador.setGeometry(QtCore.QRect(0, 332, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.LabelOperador.setFont(font)
        self.LabelOperador.setStyleSheet("color: rgb(252, 252, 252);")
        self.LabelOperador.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelOperador.setObjectName("LabelOperador")
        self.LabelLogo = QtWidgets.QLabel(self.ContainerDados)
        self.LabelLogo.setGeometry(QtCore.QRect(10, 6, 231, 151))
        self.LabelLogo.setText("")
        self.LabelLogo.setPixmap(QtGui.QPixmap("Imagens/Icones/SuperMarket-Logo-Color.png"))
        self.LabelLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelLogo.setObjectName("LabelLogo")
        self.ButtonCadastroProdutos = QtWidgets.QPushButton(self.ContainerDados)
        self.ButtonCadastroProdutos.setGeometry(QtCore.QRect(10, 439, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonCadastroProdutos.setFont(font)
        self.ButtonCadastroProdutos.setStyleSheet("background-color: #25ecd3;\n"
                                                  "border-radius: 8px;\n"
                                                  "color: rgb(255, 255, 255);")
        self.ButtonCadastroProdutos.setObjectName("ButtonCadastroProdutos")
        self.ButtonCadastroProdutos.clicked.connect(self.AbrirCadastroProdutos)

        self.ButtonCadastroUsuario = QtWidgets.QPushButton(self.ContainerDados)
        self.ButtonCadastroUsuario.setGeometry(QtCore.QRect(10, 519, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonCadastroUsuario.setFont(font)
        self.ButtonCadastroUsuario.setStyleSheet("background-color: #25ecd3;\n"
                                                 "border-radius: 8px;\n"
                                                 "color: rgb(255, 255, 255);")
        self.ButtonCadastroUsuario.setObjectName("ButtonCadastroUsuario")
        self.ButtonOpcao = QtWidgets.QPushButton(self.ContainerDados)
        self.ButtonOpcao.setGeometry(QtCore.QRect(10, 599, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonOpcao.setFont(font)
        self.ButtonOpcao.setStyleSheet("background-color: #25ecd3;\n"
                                       "border-radius: 8px;\n"
                                       "color: rgb(255, 255, 255);")
        self.ButtonOpcao.setObjectName("ButtonOpcao")
        self.ButtonSair = QtWidgets.QPushButton(self.ContainerDados)
        self.ButtonSair.setGeometry(QtCore.QRect(10, 679, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonSair.setFont(font)
        self.ButtonSair.setStyleSheet("background-color: #25ecd3;\n"
                                      "border-radius: 8px;\n"
                                      "color: rgb(255, 255, 255);")
        self.ButtonSair.setObjectName("ButtonSair")
        self.ButtonMenosQuantidade = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonMenosQuantidade.setGeometry(QtCore.QRect(277, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        #Botao diminuir quantidade
        self.ButtonMenosQuantidade.setFont(font)
        self.ButtonMenosQuantidade.setStyleSheet("background-color: #25ecd3;\n"
                                                 "border-bottom-left-radius: 15px;")
        self.ButtonMenosQuantidade.setObjectName("ButtonMenosQuantidade")
        self.ButtonMenosQuantidade.clicked.connect(self.DiminuiQuantidade)

       #Botao aumentar quantidade
        self.ButtonMaisQuantidade = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonMaisQuantidade.setGeometry(QtCore.QRect(277, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonMaisQuantidade.setFont(font)
        self.ButtonMaisQuantidade.setStyleSheet("background-color: #25ecd3;\n"
                                                "border-top-left-radius: 15px;")
        self.ButtonMaisQuantidade.setObjectName("ButtonMaisQuantidade")
        self.ButtonMaisQuantidade.clicked.connect(self.AumentaQuantidade)



        self.TableProdutos = QtWidgets.QTableWidget(self.centralwidget)
        self.TableProdutos.setGeometry(QtCore.QRect(280, 90, 541, 581))
        self.TableProdutos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.TableProdutos.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.TableProdutos.setWordWrap(True)
        self.TableProdutos.setRowCount(0)
        self.TableProdutos.setColumnCount(5)
        self.TableProdutos.setObjectName("TableProdutos")
        item = QtWidgets.QTableWidgetItem()
        self.TableProdutos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdutos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdutos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdutos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdutos.setHorizontalHeaderItem(4, item)
        self.TableProdutos.horizontalHeader().setCascadingSectionResizes(False)
        PDV.setCentralWidget(self.centralwidget)

        self.EntryEAN.setFocus()

        self.retranslateUi(PDV)
        QtCore.QMetaObject.connectSlotsByName(PDV)

    def retranslateUi(self, PDV):
        _translate = QtCore.QCoreApplication.translate
        PDV.setWindowTitle(_translate("PDV", "Super Market PDV"))
        self.LabelTotal.setText(_translate("PDV", "TOTAL  A PAGAR"))
        self.LabelTotalValor.setText(_translate("PDV", "0,00"))
        self.LabelSubtotal.setText(_translate("PDV", "SUBTOTAL"))
        self.LabelDesconto.setText(_translate("PDV", "DESCONTOS"))
        self.LabelAcrescimo.setText(_translate("PDV", "ACRESCIMOS"))
        self.LabelSubtotalValor.setText(_translate("PDV", "0,00"))
        self.EntryDescontoValor.setText(_translate("PDV", "0,00"))
        self.EntryAcrescimoValor.setText(_translate("PDV", "0,00"))
        self.ButtonReceber.setText(_translate("PDV", "RECEBER  CONTA"))
        self.EntryEAN.setPlaceholderText(_translate("PDV", "ADICIONAR PRODUTO"))
        self.EditQuantidade.setText(_translate("PDV", "1"))
        self.LabelDiaSemana.setText(_translate("PDV", "Quinta-Feira"))
        self.LabelData.setText(_translate("PDV", "25/04/2019"))
        self.LabelPerfil.setText(_translate("PDV", "ADM"))
        self.LabelOperador.setText(_translate("PDV", "OPERADOR"))
        self.ButtonCadastroProdutos.setText(_translate("PDV", "CADASTRAR PRODUTOS"))
        self.ButtonCadastroUsuario.setText(_translate("PDV", "CADASTRAR USUARIOS"))
        self.ButtonOpcao.setText(_translate("PDV", "OPÇOES"))
        self.ButtonSair.setText(_translate("PDV", "SAIR"))
        self.ButtonMenosQuantidade.setText(_translate("PDV", "-"))
        self.ButtonMaisQuantidade.setText(_translate("PDV", "+"))
        item = self.TableProdutos.horizontalHeaderItem(0)
        item.setText(_translate("PDV", "QTD"))
        item = self.TableProdutos.horizontalHeaderItem(1)
        item.setText(_translate("PDV", "Codigo"))
        item = self.TableProdutos.horizontalHeaderItem(2)
        item.setText(_translate("PDV", "Produto"))
        item = self.TableProdutos.horizontalHeaderItem(3)
        item.setText(_translate("PDV", "Valor Unitario"))
        item = self.TableProdutos.horizontalHeaderItem(4)
        item.setText(_translate("PDV", "Valor Total"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PDV = QtWidgets.QMainWindow()
    ui = Ui_PDV()
    ui.setupUi(PDV)
    PDV.show()
    sys.exit(app.exec_())

