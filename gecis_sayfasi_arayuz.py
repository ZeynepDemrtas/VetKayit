# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Zeynep/Desktop/projeVet_calisma/v.0.2/AB/gecis_sayfasi_arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 661)
        MainWindow.setMinimumSize(QtCore.QSize(908, 661))
        MainWindow.setMaximumSize(QtCore.QSize(908, 661))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-color:  qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(129, 179, 178, 152), stop:1 rgba(38, 152, 159, 255));\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buton_vet = QtWidgets.QPushButton(self.centralwidget)
        self.buton_vet.setMinimumSize(QtCore.QSize(500, 50))
        self.buton_vet.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buton_vet.setFont(font)
        self.buton_vet.setObjectName("buton_vet")
        self.gridLayout.addWidget(self.buton_vet, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.buton_coban = QtWidgets.QPushButton(self.centralwidget)
        self.buton_coban.setMinimumSize(QtCore.QSize(500, 50))
        self.buton_coban.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buton_coban.setFont(font)
        self.buton_coban.setObjectName("buton_coban")
        self.gridLayout.addWidget(self.buton_coban, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 26))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        self.menuAyarlar = QtWidgets.QMenu(self.menuYard_m)
        self.menuAyarlar.setObjectName("menuAyarlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_leti_im = QtWidgets.QAction(MainWindow)
        self.action_leti_im.setObjectName("action_leti_im")
        self.actionNas_l_Kullan_l_r = QtWidgets.QAction(MainWindow)
        self.actionNas_l_Kullan_l_r.setObjectName("actionNas_l_Kullan_l_r")
        self.action_sifre_degistir = QtWidgets.QAction(MainWindow)
        self.action_sifre_degistir.setObjectName("action_sifre_degistir")
        self.action_isim_degistir = QtWidgets.QAction(MainWindow)
        self.action_isim_degistir.setObjectName("action_isim_degistir")
        self.menuAyarlar.addAction(self.action_sifre_degistir)
        self.menuAyarlar.addAction(self.action_isim_degistir)
        self.menuYard_m.addAction(self.action_leti_im)
        self.menuYard_m.addAction(self.menuAyarlar.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buton_vet.setText(_translate("MainWindow", "VETERİNER GİRİŞİ"))
        self.buton_coban.setText(_translate("MainWindow", "ÇOBAN GİRİŞİ"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.action_leti_im.setText(_translate("MainWindow", "İletişim"))
        self.actionNas_l_Kullan_l_r.setText(_translate("MainWindow", "Nasıl Kullanılır"))
        self.action_sifre_degistir.setText(_translate("MainWindow", "Şifre Değiştir"))
        self.action_isim_degistir.setText(_translate("MainWindow", "Kullanıcı Adı Değiştir"))
