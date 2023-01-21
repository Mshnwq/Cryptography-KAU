from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Ui_Receive(object):
    def setupUi(self, MainWindow):
        
        FETCH_WINDOW_WIDTH = 1200
        FETCH_WINDOW_HEIGHT = 800
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 36
        font = QFont()
    
        # create components
        MainWindow.resize(FETCH_WINDOW_WIDTH, FETCH_WINDOW_HEIGHT)
        self.centralwidget = QWidget(MainWindow)

        fetchBox_Xaxis = int(FETCH_WINDOW_WIDTH/24)
        fetchBox_Yaxis = int(FETCH_WINDOW_HEIGHT/24)

        self.fetch_groupBox = QGroupBox(self.centralwidget)
        self.fetch_groupBox.setGeometry(QRect(fetchBox_Xaxis, fetchBox_Yaxis, 
                                int(FETCH_WINDOW_WIDTH/4), int(FETCH_WINDOW_HEIGHT/2)+36))
        self.fetch_groupBox.setAutoFillBackground(False)
        self.fetch_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.fetch_groupBox.setFont(font)
        
        self.fetch_btn = QPushButton(self.fetch_groupBox)
        self.fetch_btn.setGeometry(QRect(36, int(36*1.5), BUTTON_WIDTH+6, BUTTON_HEIGHT))
        self.fetch_statusBox = QGroupBox(self.fetch_groupBox)
        self.fetch_statusBox.setGeometry(QRect(int(36*4.8), int(36*1.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.fetch_statusBox.setFont(font)
        self.fetch_statusText = QLabel(self.fetch_statusBox)
        self.fetch_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        
        self.readKey_btn = QPushButton(self.fetch_groupBox)
        self.readKey_btn.setStyleSheet("font-weight: bold")
        self.readKey_btn.setGeometry(QRect(36, int(36*3), BUTTON_WIDTH+6, BUTTON_HEIGHT))
        self.readKey_statusBox = QGroupBox(self.fetch_groupBox)
        self.readKey_statusBox.setStyleSheet("font-weight: bold")
        self.readKey_statusBox.setGeometry(QRect(int(36*4.8), int(36*3), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.readKey_statusBox.setFont(font)
        self.readKey_statusText = QLabel(self.readKey_statusBox)
        self.readKey_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

        self.Public_label = QLabel(self.fetch_groupBox)
        self.Public_label.setGeometry(QRect(36, int(36*5), BUTTON_WIDTH+46, BUTTON_HEIGHT))
        self.Public_groupBox = QGroupBox(self.fetch_groupBox)
        self.Public_groupBox.setGeometry(QRect(36, int(36*6), int(36*6.5), (36*5)+4))
        self.Public_box = QLabel(self.Public_groupBox)
        self.Public_box.setGeometry(QRect(6, 2, int(36*8), 36*5))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(10)
        self.Public_box.setFont(font)
        self.Public_label.setFont(font)

        self.message_groupBox = QGroupBox(self.centralwidget)
        self.message_groupBox.setGeometry(QRect(int(2*FETCH_WINDOW_WIDTH/24)+int(FETCH_WINDOW_WIDTH/4), 
                                                int(FETCH_WINDOW_HEIGHT/24), 
                                                FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)), 
                                                int(FETCH_WINDOW_HEIGHT/2)+36))
        self.message_groupBox.setAutoFillBackground(False)
        self.message_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.message_groupBox.setFont(font)

        self.ciphertext_label = QLabel(self.message_groupBox)
        self.ciphertext_label.setGeometry(QRect(40*3, 40, 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.ciphertext_label.setFont(font)
        self.ciphertext_box = QGroupBox(self.message_groupBox)
        self.ciphertext_box.setGeometry(QRect(40, 40*2, 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40*4))
        self.ciphertext_text = QLabel(self.message_groupBox)
        self.ciphertext_text.setGeometry(QRect(40, 40*2, 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40))

        self.plaintext_label = QLabel(self.message_groupBox)
        self.plaintext_label.setGeometry(QRect(40*3, int(40*7.5), 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.plaintext_label.setFont(font)
        self.plaintext_box = QGroupBox(self.message_groupBox)
        self.plaintext_box.setGeometry(QRect(40, int(40*8.5), 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40*2))
        self.plaintext_text = QLabel(self.plaintext_box)
        self.plaintext_text.setGeometry(QRect(12, -45, BUTTON_WIDTH*6, BUTTON_HEIGHT*4))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(10)
        self.plaintext_text.setFont(font)

        self.decryptMsg_btn = QPushButton(self.message_groupBox)
        self.decryptMsg_btn.setStyleSheet("font-weight: bold")
        self.decryptMsg_btn.setGeometry(QRect(40*6, int(40*6.5), BUTTON_WIDTH+30, BUTTON_HEIGHT))
        self.decryptMsg_statusBox = QGroupBox(self.message_groupBox)
        self.decryptMsg_statusBox.setStyleSheet("font-weight: bold")
        self.decryptMsg_statusBox.setGeometry(QRect(40*10, int(40*6.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.decryptMsg_statusBox.setFont(font)
        self.decryptMsg_statusText = QLabel(self.decryptMsg_statusBox)
        self.decryptMsg_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        

        self.logs_box = QTextEdit(self.centralwidget)
        self.logs_box.setGeometry(QRect(fetchBox_Xaxis + BUTTON_WIDTH + 36, 
                                          int(2.5*FETCH_WINDOW_HEIGHT/24)+int(FETCH_WINDOW_HEIGHT/2), 
                                          FETCH_WINDOW_WIDTH-(fetchBox_Xaxis + BUTTON_WIDTH + 4)*2, 
                                          int(FETCH_WINDOW_HEIGHT/2)-int(3.5*FETCH_WINDOW_HEIGHT/24)))

        self.logs_label = QLabel(self.centralwidget)
        self.logs_label.setGeometry(QRect(fetchBox_Xaxis+10*6,       
                                          int(2.5*FETCH_WINDOW_HEIGHT/24)+int(FETCH_WINDOW_HEIGHT/2), 
                                          BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(60)
        self.logs_label.setFont(font)

        self.clearLogs_btn = QPushButton(self.centralwidget)
        self.clearLogs_btn.setStyleSheet("font-weight: bold")
        self.clearLogs_btn.setGeometry(QRect(int(fetchBox_Xaxis*1.5), 11+ int(FETCH_WINDOW_HEIGHT)-40*2, 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))

        MainWindow.setCentralWidget(self.centralwidget)

        # translate text into components
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attempt Mode"))
        self.fetch_groupBox.setTitle(_translate("MainWindow", "Fetch Data"))
        self.Public_label.setText(_translate("MainWindow", "Public Key Read"))
        self.message_groupBox.setTitle(_translate("MainWindow", "The Message"))
        self.ciphertext_label.setText(_translate("MainWindow", "CipherText"))
        self.plaintext_label.setText(_translate("MainWindow", "PlainText"))
        self.logs_label.setText(_translate("MainWindow", "Logs"))
        self.fetch_btn.setText(_translate("MainWindow", "Fetch"))
        self.fetch_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.fetch_statusText.setText(_translate("MainWindow", "-------------"))
        self.readKey_btn.setText(_translate("MainWindow", "Read Key"))
        self.readKey_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.readKey_statusText.setText(_translate("MainWindow", "-------------"))
        self.decryptMsg_btn.setText(_translate("MainWindow", "Decrypt Message"))
        self.decryptMsg_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.decryptMsg_statusText.setText(_translate("MainWindow", "-------------"))
        self.clearLogs_btn.setText(_translate("MainWindow", "Clear"))

        self.logs_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        QMetaObject.connectSlotsByName(MainWindow)


def construct():
    return Ui_Receive()

def testWindow():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_Receive()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    testWindow()