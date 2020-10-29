#from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery,QSqlDriver


from GUIs.mainWindows import *  
from GUIs.agregarCliente import *
from GUIs.agregarProducto import *

import sys


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self,*args,**kwards):
        super(MainWindow,self).__init__(*args,**kwards)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionAgregar_Clientes.triggered.connect(self.mostrarAgrClient)
        self.ui.actionAgregar_Productos.triggered.connect(self.mostrarAgrProducto)
    
    def mostrarAgrClient(self):
        ventanaAgrClient = agregarCliente(self)
        ventanaAgrClient.show()

    def mostrarAgrProducto(self):
        ventanaAgrProd = agregarProducto(self)
        ventanaAgrProd.show()


class agregarCliente(QtWidgets.QDialog):
    def __init__(self):
        super(agregarCliente,self).__init__()
        self.ui = Ui_agregarCliente()
        self.ui.setupUi(self)


class agregarProducto(QtWidgets.QDialog):
    def __init__(self):
        super(agregarProducto,self).__init__()
        self.ui = Ui_agregarProducto()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])

application = MainWindow()

application.show()

sys.exit(app.exec())

