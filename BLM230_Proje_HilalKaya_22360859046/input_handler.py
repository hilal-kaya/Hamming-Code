from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 538)
        MainWindow.setStyleSheet("background-color: #f0f3f4;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Başlık
        self.label_baslik = QtWidgets.QLabel(self.centralwidget)
        self.label_baslik.setGeometry(QtCore.QRect(60, 20, 521, 51))
        font = QtGui.QFont("Arial", 20, QtGui.QFont.Bold)
        self.label_baslik.setFont(font)
        self.label_baslik.setStyleSheet("color: #2c3e50;")
        self.label_baslik.setAlignment(QtCore.Qt.AlignCenter)
        self.label_baslik.setObjectName("label_baslik")

        # Açıklama
        self.label_aciklama = QtWidgets.QLabel(self.centralwidget)
        self.label_aciklama.setGeometry(QtCore.QRect(100, 90, 441, 41))
        font = QtGui.QFont("Arial", 12)
        self.label_aciklama.setFont(font)
        self.label_aciklama.setStyleSheet("color: #34495e;")
        self.label_aciklama.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aciklama.setObjectName("label_aciklama")


        # Ortak stil: butonlar için
        button_style = """
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """

        # 8 Bit Butonu
        self.pushButton_8bit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8bit.setGeometry(QtCore.QRect(230, 170, 171, 51))
        font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold)
        self.pushButton_8bit.setFont(font)
        self.pushButton_8bit.setStyleSheet(button_style)
        self.pushButton_8bit.setObjectName("pushButton_8bit")

        # 16 Bit Butonu
        self.pushButton_16bit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16bit.setGeometry(QtCore.QRect(230, 250, 171, 51))
        font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold)
        self.pushButton_16bit.setFont(font)
        self.pushButton_16bit.setStyleSheet(button_style)
        self.pushButton_16bit.setObjectName("pushButton_16bit")

        # 32 Bit Butonu
        self.pushButton_32bit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32bit.setGeometry(QtCore.QRect(230, 330, 171, 51))
        font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold)
        self.pushButton_32bit.setFont(font)
        self.pushButton_32bit.setStyleSheet(button_style)
        self.pushButton_32bit.setObjectName("pushButton_32bit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hamming SEC-DED Code Simulator"))
        self.label_baslik.setText(_translate("MainWindow", "Hamming SEC-DED Code Simulator"))
        self.pushButton_8bit.setText(_translate("MainWindow", "8 BIT"))
        self.pushButton_16bit.setText(_translate("MainWindow", "16 BIT"))
        self.pushButton_32bit.setText(_translate("MainWindow", "32 BIT"))
        self.label_aciklama.setText(_translate("MainWindow", "İşlem yapmak istediğiniz bit sayısını seçiniz"))
