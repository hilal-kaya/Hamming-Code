from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 530)
        MainWindow.setStyleSheet("background-color: #f4f6f7;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Title Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 511, 41))
        font = QtGui.QFont("Arial", 20, QtGui.QFont.Bold)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: #2c3e50;")
        self.label.setObjectName("label")
        # Data Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 171, 21))
        font = QtGui.QFont("Arial", 11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # Data Input
        self.lineEdit_data = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_data.setGeometry(QtCore.QRect(20, 110, 200, 41))
        font = QtGui.QFont("Consolas", 17)
        self.lineEdit_data.setFont(font)
        self.lineEdit_data.setStyleSheet("background-color: #fff; padding: 5px;")
        self.lineEdit_data.setObjectName("lineEdit_data")

        # Check Bits Label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 90, 100, 21))
        font = QtGui.QFont("Arial", 11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Check Bits Input
        self.lineEdit_check_bit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_check_bit.setGeometry(QtCore.QRect(380, 110, 100, 41))
        font = QtGui.QFont("Consolas", 17)
        self.lineEdit_check_bit.setFont(font)
        self.lineEdit_check_bit.setStyleSheet("background-color: #ffffff; padding: 5px;")
        self.lineEdit_check_bit.setObjectName("lineEdit_check_bit")

        # Find Check Bits Button
        self.pushButton_check_bits = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_check_bits.setGeometry(QtCore.QRect(240, 115, 120, 31))
        font = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
        self.pushButton_check_bits.setFont(font)

        self.pushButton_check_bits.setStyleSheet("background-color: #3498db; color: white; border-radius: 5px;")
        self.pushButton_check_bits.setObjectName("pushButton_check_bits")

        # Memory Input
        self.lineEdit_memory = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_memory.setGeometry(QtCore.QRect(150, 200, 200, 35))
        font = QtGui.QFont("Consolas", 14)
        self.lineEdit_memory.setFont(font)
        self.lineEdit_memory.setStyleSheet("background-color: #ffffff; padding: 5px;")
        self.lineEdit_memory.setObjectName("lineEdit_memory")

        # Bring Memory Button
        self.pushButton_memory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_memory.setGeometry(QtCore.QRect(30, 200, 110, 35))
        font = QtGui.QFont("Arial", 9, QtGui.QFont.Bold)
        self.pushButton_memory.setFont(font)
        self.pushButton_memory.setStyleSheet("background-color: #2ecc71; color: white; border-radius: 5px;")
        self.pushButton_memory.setObjectName("pushButton_memory")

        # Control Button
        self.pushButton_control = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_control.setGeometry(QtCore.QRect(370, 200, 110, 35))
        font = QtGui.QFont("Arial", 9, QtGui.QFont.Bold)
        self.pushButton_control.setFont(font)
        self.pushButton_control.setStyleSheet("background-color: #e67e22; color: white; border-radius: 5px;")
        self.pushButton_control.setObjectName("pushButton_control")

        # Output Text Area
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 270, 511, 181))
        font = QtGui.QFont("Courier New", 12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: #ecf0f1; padding: 10px;")
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
        self.label.setText(_translate("MainWindow", "Hamming Code Simulator for 8-Bit Data"))
        self.label_2.setText(_translate("MainWindow", "Enter 8-Bit Data"))
        self.label_3.setText(_translate("MainWindow", "Check Bits"))
        self.pushButton_check_bits.setText(_translate("MainWindow", "Find Check Bits"))
        self.pushButton_memory.setText(_translate("MainWindow", "Bring Memory"))
        self.pushButton_control.setText(_translate("MainWindow", "Control"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<html><body style='font-family:Courier New; font-size:12pt;'>"
                                         "<p></p></body></html>"))
