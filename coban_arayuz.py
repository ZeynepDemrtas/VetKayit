from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Degisim(object):
    def setupUi(self, Degisim):
        Degisim.setObjectName("Degisim")
        Degisim.resize(1104, 803)
        font = QtGui.QFont()
        font.setPointSize(10)
        Degisim.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ikon/ikon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Degisim.setWindowIcon(icon)
        Degisim.setAutoFillBackground(False)
        Degisim.setIconSize(QtCore.QSize(239, 30))
        self.centralwidget = QtWidgets.QWidget(Degisim)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(129, 179, 178, 152), stop:1 rgba(38, 152, 159, 255));\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tablo_degisim = QtWidgets.QTableWidget(self.groupBox)
        self.tablo_degisim.setMinimumSize(QtCore.QSize(791, 188))
        self.tablo_degisim.setMaximumSize(QtCore.QSize(986, 351))
        font = QtGui.QFont()
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tablo_degisim.setFont(font)
        self.tablo_degisim.setAcceptDrops(False)
        self.tablo_degisim.setAutoFillBackground(False)
        self.tablo_degisim.setStyleSheet("background-color: rgb(242,242,242);\n"
"selection-color: rgb(142, 113, 107);\n"
"color: rgb(63, 63, 65);\n"
"alternate-background-color: rgb(222, 221, 217);\n"
"selection-background-color: rgb(222, 222, 222);\n"
"gridline-color: rgb(201, 195,rgb(201, 195, 183) 183);")
        self.tablo_degisim.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.tablo_degisim.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tablo_degisim.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tablo_degisim.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tablo_degisim.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tablo_degisim.setAutoScroll(True)
        self.tablo_degisim.setAutoScrollMargin(16)
        self.tablo_degisim.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablo_degisim.setTabKeyNavigation(True)
        self.tablo_degisim.setProperty("showDropIndicator", True)
        self.tablo_degisim.setDragEnabled(True)
        self.tablo_degisim.setDragDropOverwriteMode(True)
        self.tablo_degisim.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tablo_degisim.setAlternatingRowColors(False)
        self.tablo_degisim.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablo_degisim.setShowGrid(False)
        self.tablo_degisim.setRowCount(1000)
        self.tablo_degisim.setColumnCount(30)
        self.tablo_degisim.setObjectName("tablo_degisim")
        self.verticalLayout.addWidget(self.tablo_degisim)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.girdi_tarih = QtWidgets.QCalendarWidget(self.groupBox)
        self.girdi_tarih.setMinimumSize(QtCore.QSize(300, 0))
        self.girdi_tarih.setMaximumSize(QtCore.QSize(500, 16777215))
        self.girdi_tarih.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.girdi_tarih.setStyleSheet("selection-background-color: rgb(167, 167, 167);")
        self.girdi_tarih.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.girdi_tarih.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.girdi_tarih.setDateEditEnabled(True)
        self.girdi_tarih.setObjectName("girdi_tarih")
        self.gridLayout_4.addWidget(self.girdi_tarih, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)
        self.girdi_ozellik4 = QtWidgets.QComboBox(self.groupBox)
        self.girdi_ozellik4.setMinimumSize(QtCore.QSize(100, 50))
        self.girdi_ozellik4.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.girdi_ozellik4.setFont(font)
        self.girdi_ozellik4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.girdi_ozellik4.setCurrentText("")
        self.girdi_ozellik4.setObjectName("girdi_ozellik4")
        self.girdi_ozellik4.addItem("")
        self.girdi_ozellik4.addItem("")
        self.girdi_ozellik4.addItem("")
        self.girdi_ozellik4.addItem("")
        self.gridLayout_4.addWidget(self.girdi_ozellik4, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)
        self.girdi_ozellik1 = QtWidgets.QLineEdit(self.groupBox)
        self.girdi_ozellik1.setMinimumSize(QtCore.QSize(200, 0))
        self.girdi_ozellik1.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.girdi_ozellik1.setFont(font)
        self.girdi_ozellik1.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.girdi_ozellik1.setFrame(False)
        self.girdi_ozellik1.setClearButtonEnabled(True)
        self.girdi_ozellik1.setObjectName("girdi_ozellik1")
        self.gridLayout_4.addWidget(self.girdi_ozellik1, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)
        self.girdi_kupeNum = QtWidgets.QLineEdit(self.groupBox)
        self.girdi_kupeNum.setMinimumSize(QtCore.QSize(200, 0))
        self.girdi_kupeNum.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.girdi_kupeNum.setFont(font)
        self.girdi_kupeNum.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.girdi_kupeNum.setFrame(False)
        self.girdi_kupeNum.setClearButtonEnabled(True)
        self.girdi_kupeNum.setObjectName("girdi_kupeNum")
        self.gridLayout_4.addWidget(self.girdi_kupeNum, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.girdi_ozellik3 = QtWidgets.QSpinBox(self.groupBox)
        self.girdi_ozellik3.setMinimumSize(QtCore.QSize(80, 0))
        self.girdi_ozellik3.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.girdi_ozellik3.setFont(font)
        self.girdi_ozellik3.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.girdi_ozellik3.setMaximum(1000)
        self.girdi_ozellik3.setObjectName("girdi_ozellik3")
        self.gridLayout_4.addWidget(self.girdi_ozellik3, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.cikti_kayit_sayisi = QtWidgets.QLabel(self.groupBox)
        self.cikti_kayit_sayisi.setMinimumSize(QtCore.QSize(50, 0))
        self.cikti_kayit_sayisi.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cikti_kayit_sayisi.setText("")
        self.cikti_kayit_sayisi.setTextFormat(QtCore.Qt.PlainText)
        self.cikti_kayit_sayisi.setObjectName("cikti_kayit_sayisi")
        self.gridLayout_3.addWidget(self.cikti_kayit_sayisi, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(85, 30))
        self.label.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.buton_geri = QtWidgets.QPushButton(self.groupBox)
        self.buton_geri.setMinimumSize(QtCore.QSize(60, 50))
        self.buton_geri.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buton_geri.setFont(font)
        self.buton_geri.setObjectName("buton_geri")
        self.verticalLayout.addWidget(self.buton_geri)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buton_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.buton_ekle.setMinimumSize(QtCore.QSize(131, 101))
        self.buton_ekle.setMaximumSize(QtCore.QSize(131, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buton_ekle.setFont(font)
        self.buton_ekle.setObjectName("buton_ekle")
        self.gridLayout.addWidget(self.buton_ekle, 6, 0, 1, 1)
        self.buton_sil = QtWidgets.QPushButton(self.centralwidget)
        self.buton_sil.setMinimumSize(QtCore.QSize(131, 101))
        self.buton_sil.setMaximumSize(QtCore.QSize(131, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buton_sil.setFont(font)
        self.buton_sil.setObjectName("buton_sil")
        self.gridLayout.addWidget(self.buton_sil, 5, 0, 1, 1)
        self.buton_guncelle = QtWidgets.QPushButton(self.centralwidget)
        self.buton_guncelle.setMinimumSize(QtCore.QSize(131, 101))
        self.buton_guncelle.setMaximumSize(QtCore.QSize(131, 101))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buton_guncelle.setFont(font)
        self.buton_guncelle.setObjectName("buton_guncelle")
        self.gridLayout.addWidget(self.buton_guncelle, 3, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.girdi_aranacak = QtWidgets.QLineEdit(self.centralwidget)
        self.girdi_aranacak.setMinimumSize(QtCore.QSize(199, 30))
        self.girdi_aranacak.setMaximumSize(QtCore.QSize(199, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.girdi_aranacak.setFont(font)
        self.girdi_aranacak.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.girdi_aranacak.setFrame(False)
        self.girdi_aranacak.setClearButtonEnabled(True)
        self.girdi_aranacak.setObjectName("girdi_aranacak")
        self.gridLayout_2.addWidget(self.girdi_aranacak, 2, 0, 1, 1)
        self.buton_bul = QtWidgets.QPushButton(self.centralwidget)
        self.buton_bul.setMinimumSize(QtCore.QSize(50, 30))
        self.buton_bul.setMaximumSize(QtCore.QSize(50, 30))
        self.buton_bul.setObjectName("buton_bul")
        self.gridLayout_2.addWidget(self.buton_bul, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.buton_listele = QtWidgets.QPushButton(self.centralwidget)
        self.buton_listele.setMinimumSize(QtCore.QSize(131, 101))
        self.buton_listele.setMaximumSize(QtCore.QSize(131, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buton_listele.setFont(font)
        self.buton_listele.setStyleSheet("selection-color: rgb(255, 170, 255);")
        self.buton_listele.setObjectName("buton_listele")
        self.gridLayout.addWidget(self.buton_listele, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        Degisim.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Degisim)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 26))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        self.menuAyarlar = QtWidgets.QMenu(self.menuYard_m)
        self.menuAyarlar.setObjectName("menuAyarlar")
        Degisim.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Degisim)
        self.statusbar.setObjectName("statusbar")
        Degisim.setStatusBar(self.statusbar)
        self.action_iletisim = QtWidgets.QAction(Degisim)
        self.action_iletisim.setObjectName("action_iletisim")
        self.action_kullanim = QtWidgets.QAction(Degisim)
        self.action_kullanim.setObjectName("action_kullanim")
        self.action_sifre_degistir = QtWidgets.QAction(Degisim)
        self.action_sifre_degistir.setObjectName("action_sifre_degistir")
        self.actionKullan_c_Ad_De_i_tir = QtWidgets.QAction(Degisim)
        self.actionKullan_c_Ad_De_i_tir.setObjectName("actionKullan_c_Ad_De_i_tir")
        self.menuAyarlar.addAction(self.action_sifre_degistir)
        self.menuAyarlar.addAction(self.actionKullan_c_Ad_De_i_tir)
        self.menuYard_m.addAction(self.action_iletisim)
        self.menuYard_m.addAction(self.menuAyarlar.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(Degisim)
        self.girdi_ozellik4.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Degisim)

    def retranslateUi(self, Degisim):
        _translate = QtCore.QCoreApplication.translate
        Degisim.setWindowTitle(_translate("Degisim", "VetKayıt"))
        self.groupBox.setTitle(_translate("Degisim", "KAYITLI HAYVAN LİSTESİ"))
        self.label_5.setText(_translate("Degisim", "ozellik4(hayvan turu)"))
        self.girdi_ozellik4.setItemText(0, _translate("Degisim", "Manda"))
        self.girdi_ozellik4.setItemText(1, _translate("Degisim", "Koyun"))
        self.girdi_ozellik4.setItemText(2, _translate("Degisim", "İnek"))
        self.girdi_ozellik4.setItemText(3, _translate("Degisim", "Tavuk"))
        self.label_2.setText(_translate("Degisim", "Küpe Numarası:"))
        self.label_4.setText(_translate("Degisim", "ozellik3"))
        self.label_6.setText(_translate("Degisim", "ozellik2(kilo mesela)"))
        self.label_3.setText(_translate("Degisim", "ozellik1"))
        self.label.setText(_translate("Degisim", "KAYIT SAYISI:"))
        self.buton_geri.setText(_translate("Degisim", "<--"))
        self.buton_ekle.setText(_translate("Degisim", "KAYIT EKLE"))
        self.buton_sil.setText(_translate("Degisim", "KAYIT SİL"))
        self.buton_guncelle.setText(_translate("Degisim", "KAYIT GÜNCELLE"))
        self.buton_bul.setText(_translate("Degisim", "BUL"))
        self.buton_listele.setText(_translate("Degisim", "LİSTEYE DÖN"))
        self.menuYard_m.setTitle(_translate("Degisim", "Yardım"))
        self.menuAyarlar.setTitle(_translate("Degisim", "Ayarlar"))
        self.action_iletisim.setText(_translate("Degisim", "İletişim"))
        self.action_kullanim.setText(_translate("Degisim", "Nasıl kullanılır?"))
        self.action_sifre_degistir.setText(_translate("Degisim", "Şifre Değiştir"))
        self.actionKullan_c_Ad_De_i_tir.setText(_translate("Degisim", "Kullanıcı Adı Değiştir"))

