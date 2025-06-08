from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 503)
        MainWindow.setStyleSheet("background-color: #f9f9f9;")  

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Başlık
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 481, 41))
        font = QtGui.QFont("Arial", 20, QtGui.QFont.Bold)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #2c3e50;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # Data Etiketi
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 121, 21))
        font = QtGui.QFont("Arial", 11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #34495e;")
        self.label_2.setObjectName("label_2")
        # Data Giriş Kutus
        self.lineEdit_data = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_data.setGeometry(QtCore.QRect(20, 130, 451, 41))
        font = QtGui.QFont("Consolas", 17)
        self.lineEdit_data.setFont(font)
        self.lineEdit_data.setStyleSheet("background-color: white; border-radius: 6px; padding: 5px;")
        self.lineEdit_data.setObjectName("lineEdit_data")

        # Check Bits Etiketi
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 110, 91, 21))
        font = QtGui.QFont("Arial", 11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #34495e;")
        self.label_3.setObjectName("label_3")

        # Check Bit Girişi
        self.lineEdit_check_bit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_check_bit.setGeometry(QtCore.QRect(640, 130, 101, 51))
        font = QtGui.QFont("Consolas", 17)
        self.lineEdit_check_bit.setFont(font)
        self.lineEdit_check_bit.setStyleSheet("background-color: white; border-radius: 6px; padding: 5px;")
        self.lineEdit_check_bit.setObjectName("lineEdit_check_bit")

        # Check Bit Hesapla Butonu
        self.pushButton_check_bits = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_check_bits.setGeometry(QtCore.QRect(510, 140, 111, 31))
        font = QtGui.QFont("Arial", 9, QtGui.QFont.Bold)
        self.pushButton_check_bits.setFont(font)
        self.pushButton_check_bits.setStyleSheet("background-color: #2980b9; color: white; border-radius: 5px;")
        self.pushButton_check_bits.setObjectName("pushButton_check_bits")

        # Memory Butonu
        self.pushButton_memory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_memory.setGeometry(QtCore.QRect(30, 230, 101, 31))
        font = QtGui.QFont("Arial", 9, QtGui.QFont.Bold)
        self.pushButton_memory.setFont(font)
        self.pushButton_memory.setStyleSheet("background-color: #27ae60; color: white; border-radius: 5px;")
        self.pushButton_memory.setObjectName("pushButton_memory")

        # Control Butonu
        self.pushButton_control = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_control.setGeometry(QtCore.QRect(30, 270, 101, 31))
        font = QtGui.QFont("Arial", 9, QtGui.QFont.Bold)
        self.pushButton_control.setFont(font)
        self.pushButton_control.setStyleSheet("background-color: #e67e22; color: white; border-radius: 5px;")
        self.pushButton_control.setObjectName("pushButton_control")

        # Memory Giriş Kutusu
        self.lineEdit_memory = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_memory.setGeometry(QtCore.QRect(150, 250, 581, 31))
        font = QtGui.QFont("Consolas", 15)
        self.lineEdit_memory.setFont(font)
        self.lineEdit_memory.setStyleSheet("background-color: white; border-radius: 6px; padding: 5px;")
        self.lineEdit_memory.setObjectName("lineEdit_memory")

        # Çıktı Alanı
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 330, 721, 131))
        font = QtGui.QFont("Courier New", 12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: #ecf0f1; border-radius: 6px; padding: 8px;")
        self.textEdit.setObjectName("textEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hamming Code Simulator"))
        self.label.setText(_translate("MainWindow", "Hamming Code Simulator for 32 Bit Data's"))
        self.pushButton_memory.setText(_translate("MainWindow", "Bring Memory"))
        self.label_2.setText(_translate("MainWindow", "Data"))
        self.label_3.setText(_translate("MainWindow", "Check Bits"))
        self.pushButton_control.setText(_translate("MainWindow", "Control"))
        self.textEdit.setHtml(_translate("MainWindow", """
        <html><body style='font-family:Courier New; font-size:12pt;'>
        <p></p></body></html>
        """))
        self.pushButton_check_bits.setText(_translate("MainWindow", "Find Check Bits"))
