from interface.login import Ui_LoginWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from algorithims.DES import DES
import random
import string

class mainWindow(QtWidgets.QMainWindow):
    des = DES()
    key = ''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = mainWindow()
    MainWindow.show()
    sys.exit(app.exec_())