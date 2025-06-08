from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import *
from bit8_operations import Ui_MainWindow
                                       
class _8bit(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.syndrome = None
        self.xor_after_control = None       
        self.code_control = None
        self.code_string = None
        self.xor_arr = None
        self.xor = None
        self.data = None
        self.code = None
        self.bit_position = None
        self.memory = None
        self._8bit_ekran = Ui_MainWindow()
        self._8bit_ekran.setupUi(self)
        self._8bit_ekran.pushButton_check_bits.clicked.connect(self.Find_Check_Bits)       
        self._8bit_ekran.pushButton_memory.clicked.connect(self.Bring_Memory)
        self._8bit_ekran.pushButton_control.clicked.connect(self.Control)
        self._8bit_ekran.lineEdit_data.setMaxLength(8)     
        self._8bit_ekran.lineEdit_memory.setMaxLength(12)   
        self._8bit_ekran.lineEdit_check_bit.setReadOnly(True) 
        self._8bit_ekran.textEdit.setReadOnly(True)
        self._8bit_ekran.lineEdit_data.setValidator(QRegExpValidator(QRegExp("[01]+")))   
        self._8bit_ekran.lineEdit_memory.setValidator(QRegExpValidator(QRegExp("[01]+")))
        self._8bit_ekran.lineEdit_data.textChanged.connect(self.check_data_length)     
        self._8bit_ekran.lineEdit_memory.textChanged.connect(self.check_data_length)
        self._8bit_ekran.lineEdit_check_bit.textChanged.connect(self.check_data_length)
        self._8bit_ekran.pushButton_check_bits.setEnabled(False)  
        self._8bit_ekran.pushButton_control.setEnabled(False)
        self._8bit_ekran.pushButton_memory.setEnabled(False)
    def check_data_length(self):
        if len(self._8bit_ekran.lineEdit_data.text()) == 8:            
            self._8bit_ekran.pushButton_check_bits.setEnabled(True)
        else :
            self._8bit_ekran.pushButton_check_bits.setEnabled(False)
        if len(self._8bit_ekran.lineEdit_memory.text()) == 12:
            self._8bit_ekran.pushButton_control.setEnabled(True)
        else :
            self._8bit_ekran.pushButton_control.setEnabled(False)
        if len(self._8bit_ekran.lineEdit_check_bit.text()) == 4:
            self._8bit_ekran.pushButton_memory.setEnabled(True)
    def Find_Check_Bits(self):
        self.code = [None]*12         
        text = self._8bit_ekran.lineEdit_data.text()    
        self.data = [int(ch) for ch in text]  

        j = 0
        for i in range(12):        
            if i == 4 or i == 8 or i == 10 or i == 11 :
                continue
            else:
                self.code[11 - i] = self.data[j]
            j += 1

        self.bit_position = []    
        for i in range(12):
            if self.code[i] == 1:
                eleman = bin(i+1)[2:]
                eleman = eleman.zfill(4)
                self.bit_position.append(eleman)

        self.xor = int(self.bit_position[len(self.bit_position)-1], 2)
        for i in range(len(self.bit_position)-1):
            self.xor = self.xor ^ int(self.bit_position[i], 2)  

        self.xor = bin(self.xor)[2:].zfill(4)  
        self._8bit_ekran.lineEdit_check_bit.setText(self.xor)  
        self.xor_arr = [int(ch) for ch in self.xor]  

        x=1
        for i in range(12):       
            if i == 0 or i == 1 or i == 3 or i == 7 :
                self.code[i] = self.xor_arr[len(self.xor_arr)-x]
                x += 1
            else:
                continue

    def Bring_Memory(self):    
        self.code.reverse()
        self.code_string = ''.join(str(bit) for bit in self.code)
        self._8bit_ekran.lineEdit_memory.setText(self.code_string)

    def Control(self):
        raw = self._8bit_ekran.lineEdit_memory.text()   
        self.code_control = [int(ch) for ch in raw]    
        ded = 0
        for i in range(12):          
            if raw[i] != self.code_string[i]: 
                ded += 1

        bit_position_after_control = []
        for i in range(12):
            if self.code_control[i] == 1 and i != 4 and i != 8 and i != 10 and i != 11 :  
                eleman = bin(12-i)[2:]          
                eleman = eleman.zfill(4)
                bit_position_after_control.append(eleman)

        self.xor_after_control = int(bit_position_after_control[len(bit_position_after_control)-1], 2)
        for i in range(len(bit_position_after_control)-1):
            self.xor_after_control = self.xor_after_control ^ int(bit_position_after_control[i], 2) 

        control_bits = raw[4] + raw[8] + raw[10] + raw[11]  
        control_bits = int(control_bits, 2)
        self.syndrome = control_bits ^ self.xor_after_control   
        temporary = self.syndrome                       
        self.syndrome = bin(self.syndrome)[2:].zfill(4)
        if ded == 2:
            message = "Double Error Detected"
            self._8bit_ekran.textEdit.setText(message)
        elif ded > 2:
            self._8bit_ekran.textEdit.setText("Error! \nSomething went wrong!")
        elif temporary == 1 or temporary == 2 or temporary == 4 or temporary == 8: 
            raw2 = []
            for i in range(len(raw)):
                if i == 12-temporary:
                    raw2.append('[')
                    raw2.append(raw[i])     
                    raw2.append(']')
                else:
                    raw2.append(raw[i])
            raw2_str = ''.join(raw2)
            message = "Before: " + self.xor + "\n" + "After: " + bin(control_bits)[2:].zfill(4) + "\n" + "Syndrome: " + self.syndrome + "\n" + "Data has not changed" + "\n" + raw2_str
            self._8bit_ekran.textEdit.setText(message)  
        elif temporary <= 12 and temporary != 1 and temporary != 2 and temporary != 4 and temporary != 8 and temporary != 0: #diğer bitlerdeki hata durumu
            raw2 = []
            for i in range(len(raw)):
                if i == 12-temporary:
                    raw2.append('[')
                    raw2.append(raw[i])         
                    raw2.append(']')
                else:
                    raw2.append(raw[i])
            raw2_str = ''.join(raw2)
            control_bits = int(self.xor, 2) ^ int(self.syndrome, 2)
            message = "Before: " + self.xor + "\n" + "After: " + bin(control_bits)[2:].zfill(4) + "\n" + "Syndrome: " + self.syndrome + "\n" + "Data has changed" + "\n" + raw2_str
            self._8bit_ekran.textEdit.setText(message)
        elif temporary == 0: 
            message = "Before: " + self.xor + "\n" + "After: " + bin(control_bits)[2:].zfill(
                4) + "\n" + "Syndrome: " + self.syndrome + "\n" + "Nothing has changed" + "\n" + raw
            self._8bit_ekran.textEdit.setText(message)
        else:
            self._8bit_ekran.textEdit.setText("Error! \nSomething went wrong!")  
