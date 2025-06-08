from PyQt5.QtWidgets import QApplication
from input_code import input_handler

app = QApplication([])
window = input_handler()
window.show()
app.exec_()