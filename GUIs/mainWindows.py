# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        self.menuCLIENTES = QtWidgets.QMenu(self.menubar)
        self.menuCLIENTES.setObjectName("menuCLIENTES")
        self.menuPRODUCTOS = QtWidgets.QMenu(self.menubar)
        self.menuPRODUCTOS.setObjectName("menuPRODUCTOS")
        self.menuVENTAS = QtWidgets.QMenu(self.menubar)
        self.menuVENTAS.setObjectName("menuVENTAS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAgregar_Clientes = QtWidgets.QAction(MainWindow)
        self.actionAgregar_Clientes.setObjectName("actionAgregar_Clientes")
        self.actionVer_Clientes = QtWidgets.QAction(MainWindow)
        self.actionVer_Clientes.setObjectName("actionVer_Clientes")
        self.actionActualizar_CLientes = QtWidgets.QAction(MainWindow)
        self.actionActualizar_CLientes.setObjectName("actionActualizar_CLientes")
        self.actionEliminar_Clientes = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Clientes.setObjectName("actionEliminar_Clientes")
        self.actionAgregar_Productos = QtWidgets.QAction(MainWindow)
        self.actionAgregar_Productos.setObjectName("actionAgregar_Productos")
        self.actionVer_Productos = QtWidgets.QAction(MainWindow)
        self.actionVer_Productos.setObjectName("actionVer_Productos")
        self.actionActualizar_Productos = QtWidgets.QAction(MainWindow)
        self.actionActualizar_Productos.setObjectName("actionActualizar_Productos")
        self.actionEliminar_Productos = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Productos.setObjectName("actionEliminar_Productos")
        self.actionAgregar_Venta = QtWidgets.QAction(MainWindow)
        self.actionAgregar_Venta.setObjectName("actionAgregar_Venta")
        self.actionLeer_Ventas = QtWidgets.QAction(MainWindow)
        self.actionLeer_Ventas.setObjectName("actionLeer_Ventas")
        self.actionActualizar_Ventas = QtWidgets.QAction(MainWindow)
        self.actionActualizar_Ventas.setObjectName("actionActualizar_Ventas")
        self.actionEliminar_Ventas = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Ventas.setObjectName("actionEliminar_Ventas")
        self.menuCLIENTES.addAction(self.actionAgregar_Clientes)
        self.menuCLIENTES.addAction(self.actionVer_Clientes)
        self.menuCLIENTES.addAction(self.actionActualizar_CLientes)
        self.menuCLIENTES.addAction(self.actionEliminar_Clientes)
        self.menuPRODUCTOS.addAction(self.actionAgregar_Productos)
        self.menuPRODUCTOS.addAction(self.actionVer_Productos)
        self.menuPRODUCTOS.addAction(self.actionActualizar_Productos)
        self.menuPRODUCTOS.addAction(self.actionEliminar_Productos)
        self.menuVENTAS.addAction(self.actionAgregar_Venta)
        self.menuVENTAS.addAction(self.actionLeer_Ventas)
        self.menuVENTAS.addAction(self.actionActualizar_Ventas)
        self.menuVENTAS.addAction(self.actionEliminar_Ventas)
        self.menubar.addAction(self.menuCLIENTES.menuAction())
        self.menubar.addAction(self.menuPRODUCTOS.menuAction())
        self.menubar.addAction(self.menuVENTAS.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuCLIENTES.setTitle(_translate("MainWindow", "CLIENTES"))
        self.menuPRODUCTOS.setTitle(_translate("MainWindow", "PRODUCTOS"))
        self.menuVENTAS.setTitle(_translate("MainWindow", "VENTAS"))
        self.actionAgregar_Clientes.setText(_translate("MainWindow", "Agregar Clientes"))
        self.actionVer_Clientes.setText(_translate("MainWindow", "Ver Clientes"))
        self.actionActualizar_CLientes.setText(_translate("MainWindow", "Actualizar CLientes"))
        self.actionEliminar_Clientes.setText(_translate("MainWindow", "Eliminar Clientes"))
        self.actionAgregar_Productos.setText(_translate("MainWindow", "Agregar Productos"))
        self.actionVer_Productos.setText(_translate("MainWindow", "Ver Productos"))
        self.actionActualizar_Productos.setText(_translate("MainWindow", "Actualizar Productos"))
        self.actionEliminar_Productos.setText(_translate("MainWindow", "Eliminar Productos "))
        self.actionAgregar_Venta.setText(_translate("MainWindow", "Agregar Venta"))
        self.actionLeer_Ventas.setText(_translate("MainWindow", "Leer Ventas"))
        self.actionActualizar_Ventas.setText(_translate("MainWindow", "Actualizar Ventas"))
        self.actionEliminar_Ventas.setText(_translate("MainWindow", "Eliminar Ventas"))
