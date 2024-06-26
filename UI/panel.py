# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtHost = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txtHost.setObjectName("txtHost")
        self.horizontalLayout.addWidget(self.txtHost)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtAdmin = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txtAdmin.setObjectName("txtAdmin")
        self.horizontalLayout_2.addWidget(self.txtAdmin)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.txtPaswword = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txtPaswword.setObjectName("txtPaswword")
        self.horizontalLayout_3.addWidget(self.txtPaswword)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnTest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnTest.setObjectName("btnTest")
        self.horizontalLayout_5.addWidget(self.btnTest)
        self.btnInternetTest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnInternetTest.setObjectName("btnInternetTest")
        self.horizontalLayout_5.addWidget(self.btnInternetTest)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuHola = QtWidgets.QMenu(self.menubar)
        self.menuHola.setObjectName("menuHola")
        self.menuPagos = QtWidgets.QMenu(self.menubar)
        self.menuPagos.setObjectName("menuPagos")
        self.menuCortes = QtWidgets.QMenu(self.menubar)
        self.menuCortes.setObjectName("menuCortes")
        self.menuVer_Clientes = QtWidgets.QMenu(self.menubar)
        self.menuVer_Clientes.setObjectName("menuVer_Clientes")
        self.menuVer_Pagos = QtWidgets.QMenu(self.menubar)
        self.menuVer_Pagos.setObjectName("menuVer_Pagos")
        self.menuGestion = QtWidgets.QMenu(self.menubar)
        self.menuGestion.setObjectName("menuGestion")
        self.menuMicrotik = QtWidgets.QMenu(self.menubar)
        self.menuMicrotik.setObjectName("menuMicrotik")
        self.menuHerramientas_Net = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas_Net.setObjectName("menuHerramientas_Net")
        self.menuA_cerda = QtWidgets.QMenu(self.menubar)
        self.menuA_cerda.setObjectName("menuA_cerda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHola = QtWidgets.QAction(MainWindow)
        self.actionHola.setObjectName("actionHola")
        self.actionRed_Cliente = QtWidgets.QAction(MainWindow)
        self.actionRed_Cliente.setObjectName("actionRed_Cliente")
        self.actionUpdate_Cliente = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Cliente.setObjectName("actionUpdate_Cliente")
        self.actionDelete_Cliente = QtWidgets.QAction(MainWindow)
        self.actionDelete_Cliente.setObjectName("actionDelete_Cliente")
        self.actionCreate_Pago = QtWidgets.QAction(MainWindow)
        self.actionCreate_Pago.setObjectName("actionCreate_Pago")
        self.actionRead_Pagos = QtWidgets.QAction(MainWindow)
        self.actionRead_Pagos.setObjectName("actionRead_Pagos")
        self.actionSearch_Pagos = QtWidgets.QAction(MainWindow)
        self.actionSearch_Pagos.setObjectName("actionSearch_Pagos")
        self.actionCreate_Comprobante = QtWidgets.QAction(MainWindow)
        self.actionCreate_Comprobante.setObjectName("actionCreate_Comprobante")
        self.actionCorte_x_Hora = QtWidgets.QAction(MainWindow)
        self.actionCorte_x_Hora.setObjectName("actionCorte_x_Hora")
        self.actionCorte_x_Dias = QtWidgets.QAction(MainWindow)
        self.actionCorte_x_Dias.setObjectName("actionCorte_x_Dias")
        self.actionCorte_x_Marguen = QtWidgets.QAction(MainWindow)
        self.actionCorte_x_Marguen.setObjectName("actionCorte_x_Marguen")
        self.actionCorte_Automatico = QtWidgets.QAction(MainWindow)
        self.actionCorte_Automatico.setObjectName("actionCorte_Automatico")
        self.actionClientes_sin_pagar = QtWidgets.QAction(MainWindow)
        self.actionClientes_sin_pagar.setObjectName("actionClientes_sin_pagar")
        self.actionRecaudacion_x_Marguen = QtWidgets.QAction(MainWindow)
        self.actionRecaudacion_x_Marguen.setObjectName("actionRecaudacion_x_Marguen")
        self.actionDeudas_x_Marguen = QtWidgets.QAction(MainWindow)
        self.actionDeudas_x_Marguen.setObjectName("actionDeudas_x_Marguen")
        self.actionReiniciar = QtWidgets.QAction(MainWindow)
        self.actionReiniciar.setObjectName("actionReiniciar")
        self.actionPing = QtWidgets.QAction(MainWindow)
        self.actionPing.setObjectName("actionPing")
        self.actionPing_2 = QtWidgets.QAction(MainWindow)
        self.actionPing_2.setObjectName("actionPing_2")
        self.actionARP = QtWidgets.QAction(MainWindow)
        self.actionARP.setObjectName("actionARP")
        self.actionIpTrafft = QtWidgets.QAction(MainWindow)
        self.actionIpTrafft.setObjectName("actionIpTrafft")
        self.actionNMap = QtWidgets.QAction(MainWindow)
        self.actionNMap.setObjectName("actionNMap")
        self.actionScaneo_de_IP = QtWidgets.QAction(MainWindow)
        self.actionScaneo_de_IP.setObjectName("actionScaneo_de_IP")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuHola.addAction(self.actionHola)
        self.menuHola.addAction(self.actionRed_Cliente)
        self.menuHola.addAction(self.actionUpdate_Cliente)
        self.menuHola.addAction(self.actionDelete_Cliente)
        self.menuPagos.addAction(self.actionCreate_Pago)
        self.menuPagos.addAction(self.actionRead_Pagos)
        self.menuPagos.addAction(self.actionSearch_Pagos)
        self.menuPagos.addAction(self.actionCreate_Comprobante)
        self.menuCortes.addAction(self.actionCorte_x_Hora)
        self.menuCortes.addAction(self.actionCorte_x_Dias)
        self.menuCortes.addAction(self.actionCorte_x_Marguen)
        self.menuCortes.addAction(self.actionCorte_Automatico)
        self.menuGestion.addAction(self.actionClientes_sin_pagar)
        self.menuGestion.addAction(self.actionRecaudacion_x_Marguen)
        self.menuGestion.addAction(self.actionDeudas_x_Marguen)
        self.menuMicrotik.addAction(self.actionReiniciar)
        self.menuMicrotik.addAction(self.actionPing)
        self.menuHerramientas_Net.addAction(self.actionPing_2)
        self.menuHerramientas_Net.addAction(self.actionARP)
        self.menuHerramientas_Net.addAction(self.actionIpTrafft)
        self.menuHerramientas_Net.addAction(self.actionNMap)
        self.menuHerramientas_Net.addAction(self.actionScaneo_de_IP)
        self.menuA_cerda.addAction(self.actionInfo)
        self.menubar.addAction(self.menuHola.menuAction())
        self.menubar.addAction(self.menuPagos.menuAction())
        self.menubar.addAction(self.menuCortes.menuAction())
        self.menubar.addAction(self.menuVer_Clientes.menuAction())
        self.menubar.addAction(self.menuVer_Pagos.menuAction())
        self.menubar.addAction(self.menuGestion.menuAction())
        self.menubar.addAction(self.menuMicrotik.menuAction())
        self.menubar.addAction(self.menuHerramientas_Net.menuAction())
        self.menubar.addAction(self.menuA_cerda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Panel Wisplus Server"))
        self.label_4.setText(_translate("MainWindow", "Credenciales - IMPORTANTES"))
        self.label.setText(_translate("MainWindow", "Host"))
        self.label_2.setText(_translate("MainWindow", "Usuario"))
        self.label_3.setText(_translate("MainWindow", "Psssword"))
        self.btnTest.setText(_translate("MainWindow", "Test Conexion"))
        self.btnInternetTest.setText(_translate("MainWindow", "Test Internet"))
        self.menuHola.setTitle(_translate("MainWindow", "Clienes"))
        self.menuPagos.setTitle(_translate("MainWindow", "Pagos"))
        self.menuCortes.setTitle(_translate("MainWindow", "Cortes"))
        self.menuVer_Clientes.setTitle(_translate("MainWindow", "Ver Clientes"))
        self.menuVer_Pagos.setTitle(_translate("MainWindow", "Ver Pagos"))
        self.menuGestion.setTitle(_translate("MainWindow", "Gestion"))
        self.menuMicrotik.setTitle(_translate("MainWindow", "Microtik"))
        self.menuHerramientas_Net.setTitle(_translate("MainWindow", "Herramientas Net"))
        self.menuA_cerda.setTitle(_translate("MainWindow", "About"))
        self.actionHola.setText(_translate("MainWindow", "Create Cliente"))
        self.actionRed_Cliente.setText(_translate("MainWindow", "Red Cliente"))
        self.actionUpdate_Cliente.setText(_translate("MainWindow", "Update Cliente"))
        self.actionDelete_Cliente.setText(_translate("MainWindow", "Delete Cliente"))
        self.actionCreate_Pago.setText(_translate("MainWindow", "Create Pago"))
        self.actionRead_Pagos.setText(_translate("MainWindow", "Read Pagos"))
        self.actionSearch_Pagos.setText(_translate("MainWindow", "Search Pagos"))
        self.actionCreate_Comprobante.setText(_translate("MainWindow", "Create Comprobante"))
        self.actionCorte_x_Hora.setText(_translate("MainWindow", "Corte x Hora"))
        self.actionCorte_x_Dias.setText(_translate("MainWindow", "Corte x Dias"))
        self.actionCorte_x_Marguen.setText(_translate("MainWindow", "Corte x Marguen"))
        self.actionCorte_Automatico.setText(_translate("MainWindow", "Corte Automatico"))
        self.actionClientes_sin_pagar.setText(_translate("MainWindow", "Clientes sin pagar"))
        self.actionRecaudacion_x_Marguen.setText(_translate("MainWindow", "Recaudacion x Marguen"))
        self.actionDeudas_x_Marguen.setText(_translate("MainWindow", "Deudas x Marguen"))
        self.actionReiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.actionPing.setText(_translate("MainWindow", "Queue"))
        self.actionPing_2.setText(_translate("MainWindow", "Ping"))
        self.actionARP.setText(_translate("MainWindow", "ARP"))
        self.actionIpTrafft.setText(_translate("MainWindow", "IpTrafft"))
        self.actionNMap.setText(_translate("MainWindow", "NMap"))
        self.actionScaneo_de_IP.setText(_translate("MainWindow", "Scaneo de IP"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
