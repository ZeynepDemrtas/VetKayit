# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Zeynep/Desktop/projeVet_calisma/AB/kullanici_isim_degistir_arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 241)
        Form.setMinimumSize(QtCore.QSize(500, 241))
        Form.setMaximumSize(QtCore.QSize(500, 241))
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        Form.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.005, y1:0, x2:1, y2:0.636, stop:0.621891 rgba(0, 0, 0, 255), stop:1 rgba(38, 152, 159, 255));")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(170, 30))
        self.label.setMaximumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.girdi_eski_isim = QtWidgets.QLineEdit(Form)
        self.girdi_eski_isim.setMinimumSize(QtCore.QSize(210, 30))
        self.girdi_eski_isim.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.girdi_eski_isim.setFont(font)
        self.girdi_eski_isim.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.girdi_eski_isim.setFrame(False)
        self.girdi_eski_isim.setClearButtonEnabled(True)
        self.girdi_eski_isim.setObjectName("girdi_eski_isim")
        self.gridLayout.addWidget(self.girdi_eski_isim, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(170, 30))
        self.label_2.setMaximumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.girdi_yeni_isim = QtWidgets.QLineEdit(Form)
        self.girdi_yeni_isim.setMinimumSize(QtCore.QSize(210, 30))
        self.girdi_yeni_isim.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.girdi_yeni_isim.setFont(font)
        self.girdi_yeni_isim.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.girdi_yeni_isim.setFrame(False)
        self.girdi_yeni_isim.setClearButtonEnabled(True)
        self.girdi_yeni_isim.setObjectName("girdi_yeni_isim")
        self.gridLayout.addWidget(self.girdi_yeni_isim, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buton_iptal = QtWidgets.QPushButton(Form)
        self.buton_iptal.setMinimumSize(QtCore.QSize(100, 55))
        self.buton_iptal.setMaximumSize(QtCore.QSize(100, 55))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buton_iptal.setFont(font)
        self.buton_iptal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_iptal.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.buton_iptal.setObjectName("buton_iptal")
        self.horizontalLayout.addWidget(self.buton_iptal)
        self.buton_isim_degistir = QtWidgets.QPushButton(Form)
        self.buton_isim_degistir.setMinimumSize(QtCore.QSize(270, 55))
        self.buton_isim_degistir.setMaximumSize(QtCore.QSize(270, 55))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buton_isim_degistir.setFont(font)
        self.buton_isim_degistir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_isim_degistir.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.buton_isim_degistir.setObjectName("buton_isim_degistir")
        self.horizontalLayout.addWidget(self.buton_isim_degistir)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Eski Kullanıcı Adı:"))
        self.girdi_eski_isim.setPlaceholderText(_translate("Form", "Yoksa boş bırakınız!"))
        self.label_2.setText(_translate("Form", "Yeni Kullanıcı Adı:"))
        self.buton_iptal.setText(_translate("Form", "İPTAL"))
        self.buton_isim_degistir.setText(_translate("Form", "Kulanıcı Adımı Değiştir"))

