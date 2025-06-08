from PyQt5.QtWidgets import *
from input_handler import Ui_MainWindow
from bit8_logic import _8bit
from bit16_logic import _16bit
from bit32_logic import _32bit

class input_handler(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.input_handler_ekran = Ui_MainWindow()
        self.input_handler_ekran.setupUi(self)
        self.bit8 = _8bit()
        self.bit16 = _16bit()
        self.bit32 = _32bit()
        self.input_handler_ekran.pushButton_8bit.clicked.connect(self.bit8_islem)
        self.input_handler_ekran.pushButton_16bit.clicked.connect(self.bit16_islem)
        self.input_handler_ekran.pushButton_32bit.clicked.connect(self.bit32_islem)

    def bit8_islem(self):
        self.close()
        self.bit8.show()
    def bit16_islem(self):
        self.close()
        self.bit16.show()
    def bit32_islem(self):
        self.close()
        self.bit32.show()