from PyQt5 import QtCore, QtGui, QtWidgets

from interface.mainWindow import Ui_MainWindow

from algorithims.DES import DES
from solider import Solider
from battalion import Battalion

import random
import string

class mainWindow(QtWidgets.QMainWindow):
    des = DES()
    # aes = AES()
    key = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(self.encrypt)
        self.ui.pushButton_2.clicked.connect(self.decrypt)
        self.ui.pushButton_3.clicked.connect(self.generateKey)
    
    def login(self):
        battalion = Battalion(self.ui.comboBox.currentData(), "test123")
        self.currentSolider = Solider(self.ui.lineEdit.text(), battalion)
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()
        MainWindow.close()
        # self.ui.label_2.setText(self.currentSolider.name)

    def encrypt(self):
        algorithim = self.ui.comboBox.currentText()
        message = self.ui.textEdit_2.toPlainText()
        print(message)
        if algorithim == "DES":
            hexMessage = message.encode("utf-8").hex().upper()
            print(hexMessage)
            hexKey = self.key.encode("utf-8").hex().upper()
            print(hexKey)
            sipher_text = self.des.encrypt(hexMessage, hexKey, "encrypt")
            bin_sipher = self.des.bin2hex(sipher_text)
            self.ui.textEdit.setText("0x"+bin_sipher)
    
    def decrypt(self):
        algorithim = self.ui.comboBox.currentText()
        message = self.ui.textEdit_2.toPlainText()
        print(message)
        if algorithim == "DES":
            binMessage = self.des.hex2bin(message)
            print(binMessage)
            hexKey = self.key.encode("utf-8").hex().upper()
            print(hexKey)
            sipher_text = self.des.decrypt(binMessage, hexKey)
            text = bytearray.fromhex(sipher_text).decode("utf-8")
            self.ui.textEdit.setText(text)

    def generateKey(self):
        key = ''.join(random.choice(string.ascii_letters+ string.punctuation) for i in range(8))
        # key = "".join(key.split())
        print(key)
        self.ui.lineEdit.setText(key)
        self.key = key


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = mainWindow()
    MainWindow.show()
    sys.exit(app.exec_())