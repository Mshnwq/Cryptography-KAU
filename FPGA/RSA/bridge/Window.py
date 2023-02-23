from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class GenMode_MainWindow(object):
    def setupUi(self, MainWindow):
        
        FETCH_WINDOW_WIDTH = 1200
        FETCH_WINDOW_HEIGHT = 800
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 36
        font = QFont()
    
        # create components
        MainWindow.resize(FETCH_WINDOW_WIDTH, FETCH_WINDOW_HEIGHT)
        self.centralwidget = QWidget(MainWindow)

        keyGenBox_Xaxis = int(FETCH_WINDOW_WIDTH/24)
        keyGenBox_Yaxis = int(FETCH_WINDOW_HEIGHT/24)

        self.keyGen_groupBox = QGroupBox(self.centralwidget)
        self.keyGen_groupBox.setGeometry(QRect(keyGenBox_Xaxis, keyGenBox_Yaxis, 
                                int(FETCH_WINDOW_WIDTH/4), FETCH_WINDOW_HEIGHT-int(2*FETCH_WINDOW_HEIGHT/24)))
        self.keyGen_groupBox.setAutoFillBackground(False)
        self.keyGen_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.keyGen_groupBox.setFont(font)
        
        self.bitSize_groupBox = QGroupBox(self.keyGen_groupBox)
        self.bitSize_groupBox.setGeometry(QRect(10, 30,
                                int(FETCH_WINDOW_WIDTH/4)-20, 10+int(FETCH_WINDOW_HEIGHT/24)))
        self.horizontalLayout = QHBoxLayout(self.bitSize_groupBox)

        self.bit64_btn = QRadioButton(self.bitSize_groupBox)
        self.bit64_btn.setGeometry(QRect(0, 0, 18, 18))
        self.bit64_btn.setChecked(True)
        self.horizontalLayout.addWidget(self.bit64_btn)
        self.bit32_btn = QRadioButton(self.bitSize_groupBox)
        self.bit32_btn.setGeometry(QRect(0, 0, 18, 18))
        self.horizontalLayout.addWidget(self.bit32_btn)
        self.bit16_btn = QRadioButton(self.bitSize_groupBox)
        self.bit16_btn.setGeometry(QRect(0, 0, 18, 18))
        self.horizontalLayout.addWidget(self.bit16_btn)

        self.genKeys_btn = QPushButton(self.keyGen_groupBox)
        self.genKeys_btn.setGeometry(QRect(36, int(36*2.5), BUTTON_WIDTH+6, BUTTON_HEIGHT))
        self.genKeys_statusBox = QGroupBox(self.keyGen_groupBox)
        self.genKeys_statusBox.setGeometry(QRect(int(36*4.8), int(36*2.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.genKeys_statusBox.setFont(font)
        self.genKeys_statusText = QLabel(self.genKeys_statusBox)
        self.genKeys_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        
        self.N_label = QLabel(self.keyGen_groupBox)
        self.N_label.setGeometry(QRect(36, 36*4, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.N_label_box = QLabel(self.keyGen_groupBox)
        self.N_label_box.setGeometry(QRect(36+18, 36*4, BUTTON_WIDTH*2, BUTTON_HEIGHT)) 
        self.E_label = QLabel(self.keyGen_groupBox)
        self.E_label.setGeometry(QRect(36, 36*5, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.E_label_box = QLabel(self.keyGen_groupBox)
        self.E_label_box.setGeometry(QRect(36+18, 36*5, BUTTON_WIDTH*2, BUTTON_HEIGHT))
        self.D_label = QLabel(self.keyGen_groupBox)
        self.D_label.setGeometry(QRect(36, 36*6, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.D_label_box = QLabel(self.keyGen_groupBox)
        self.D_label_box.setGeometry(QRect(36+18, 36*6, BUTTON_WIDTH*2, BUTTON_HEIGHT))
        self.Private_label = QLabel(self.keyGen_groupBox)
        self.Private_label.setGeometry(QRect(36, 36*7, BUTTON_WIDTH+42, BUTTON_HEIGHT))
        self.Private_groupBox = QGroupBox(self.keyGen_groupBox)
        self.Private_groupBox.setGeometry(QRect(36, 36*8, int(36*6.5), 36*4))
        self.Private_box = QLabel(self.Private_groupBox)
        self.Private_box.setGeometry(QRect(6, 2, int(36*6.5), 36*4))
        self.Public_label = QLabel(self.keyGen_groupBox)
        self.Public_label.setGeometry(QRect(36, int(36*12.5), BUTTON_WIDTH+36, BUTTON_HEIGHT))
        self.Public_groupBox = QGroupBox(self.keyGen_groupBox)
        self.Public_groupBox.setGeometry(QRect(36, int(36*13.5), int(36*6.5), (36*5)+4))
        self.Public_box = QLabel(self.Public_groupBox)
        self.Public_box.setGeometry(QRect(6, 2, int(36*6.5), 36*5))
        font.setPointSize(5)
        font.setBold(False)
        font.setWeight(4)
        self.N_label_box.setFont(font)
        self.E_label_box.setFont(font)
        self.D_label_box.setFont(font)
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(10)
        self.Private_box.setFont(font)
        self.Public_box.setFont(font)

        self.writeKey_btn = QPushButton(self.centralwidget)
        self.writeKey_btn.setStyleSheet("font-weight: bold")
        self.writeKey_btn.setGeometry(QRect(keyGenBox_Xaxis+36, int(FETCH_WINDOW_HEIGHT)-40*2, 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        self.writeKey_statusBox = QGroupBox(self.centralwidget)
        self.writeKey_statusBox.setStyleSheet("font-weight: bold")
        self.writeKey_statusBox.setGeometry(QRect(int(keyGenBox_Xaxis+36*4.8), int(FETCH_WINDOW_HEIGHT)-40*2, 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.writeKey_statusBox.setFont(font)
        self.writeKey_statusText = QLabel(self.writeKey_statusBox)
        self.writeKey_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

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

        self.plaintext_label = QLabel(self.message_groupBox)
        self.plaintext_label.setGeometry(QRect(40*3, 40, 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.plaintext_label.setFont(font)
        self.plaintext_box = QLineEdit(self.message_groupBox)
        self.plaintext_box.setGeometry(QRect(40, 40*2, 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40))
        self.ciphertext_label = QLabel(self.message_groupBox)
        self.ciphertext_label.setGeometry(QRect(40*3, 40*5, 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.ciphertext_label.setFont(font)
        self.ciphertext_box = QGroupBox(self.message_groupBox)
        self.ciphertext_box.setGeometry(QRect(40, 40*6, 
        FETCH_WINDOW_WIDTH-(int(3*FETCH_WINDOW_WIDTH/24)+ int(FETCH_WINDOW_WIDTH/4)) - 40*2, 40*4))
        self.ciphertext_text = QLabel(self.ciphertext_box)
        self.ciphertext_text.setGeometry(QRect(12, 5, BUTTON_WIDTH*6, BUTTON_HEIGHT*4))

        self.encryptMsg_btn = QPushButton(self.message_groupBox)
        self.encryptMsg_btn.setStyleSheet("font-weight: bold")
        self.encryptMsg_btn.setGeometry(QRect(40*6, int(40*3.5), BUTTON_WIDTH+30, BUTTON_HEIGHT))
        self.encryptMsg_statusBox = QGroupBox(self.message_groupBox)
        self.encryptMsg_statusBox.setStyleSheet("font-weight: bold")
        self.encryptMsg_statusBox.setGeometry(QRect(40*10, int(40*3.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.encryptMsg_statusBox.setFont(font)
        self.encryptMsg_statusText = QLabel(self.encryptMsg_statusBox)
        self.encryptMsg_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        

        self.logs_box = QTextEdit(self.centralwidget)
        self.logs_box.setGeometry(QRect(int(3.8*FETCH_WINDOW_WIDTH/24)+int(FETCH_WINDOW_WIDTH/4), 
                                          int(2.5*FETCH_WINDOW_HEIGHT/24)+int(FETCH_WINDOW_HEIGHT/2), 
                                          FETCH_WINDOW_WIDTH-(int(4.8*FETCH_WINDOW_WIDTH/24)+int(FETCH_WINDOW_WIDTH/4)), 
                                          int(FETCH_WINDOW_HEIGHT/2)-int(3.5*FETCH_WINDOW_HEIGHT/24)))

        self.logs_label = QLabel(self.centralwidget)
        self.logs_label.setGeometry(QRect(int(2*FETCH_WINDOW_WIDTH/24)+int(FETCH_WINDOW_WIDTH/4),       
                                          int(2.5*FETCH_WINDOW_HEIGHT/24)+int(FETCH_WINDOW_HEIGHT/2), 
                                          BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(60)
        self.logs_label.setFont(font)

        self.uploadData_btn = QPushButton(self.centralwidget)
        self.uploadData_btn.setStyleSheet("font-weight: bold")
        self.uploadData_btn.setGeometry(QRect(int(1.4*FETCH_WINDOW_WIDTH/24)+int(FETCH_WINDOW_WIDTH/4),       
                                          int(4*FETCH_WINDOW_HEIGHT/24)+int(FETCH_WINDOW_HEIGHT/2),
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        self.uploadData_statusBox = QGroupBox(self.centralwidget)
        self.uploadData_statusBox.setStyleSheet("font-weight: bold")
        self.uploadData_statusBox.setGeometry(QRect(int(1.4*FETCH_WINDOW_WIDTH/24)+int(FETCH_WINDOW_WIDTH/4),       
                                          int(6*FETCH_WINDOW_HEIGHT/24)+int(FETCH_WINDOW_HEIGHT/2),
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.uploadData_statusBox.setFont(font)
        self.uploadData_statusText = QLabel(self.uploadData_statusBox)
        self.uploadData_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

        self.clearLogs_btn = QPushButton(self.centralwidget)
        self.clearLogs_btn.setStyleSheet("font-weight: bold")
        self.clearLogs_btn.setGeometry(QRect(int(1.4*FETCH_WINDOW_WIDTH/24)+int(FETCH_WINDOW_WIDTH/4),       
                                        int(FETCH_WINDOW_HEIGHT)-40*2, BUTTON_WIDTH, BUTTON_HEIGHT))

        MainWindow.setCentralWidget(self.centralwidget)

        # translate text into components
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generate Mode"))
        self.keyGen_groupBox.setTitle(_translate("MainWindow", "Generation"))
        self.bit64_btn.setText(_translate("MainWindow", "64 bit"))
        self.bit32_btn.setText(_translate("MainWindow", "32 bit"))
        self.bit16_btn.setText(_translate("MainWindow", "16 bit"))
        self.N_label.setText(_translate("MainWindow", "N:"))
        self.N_label_box.setText(_translate("MainWindow", "---"))
        self.E_label.setText(_translate("MainWindow", "E:"))
        self.E_label_box.setText(_translate("MainWindow", "---"))
        self.D_label.setText(_translate("MainWindow", "D:"))
        self.D_label_box.setText(_translate("MainWindow", "---"))
        self.Private_label.setText(_translate("MainWindow", "Private Key Pair {E,N}"))
        self.Public_label.setText(_translate("MainWindow", "Public Key Pair {D,N}"))
        self.message_groupBox.setTitle(_translate("MainWindow", "Enter a message"))
        self.plaintext_label.setText(_translate("MainWindow", "PlainText"))
        self.ciphertext_label.setText(_translate("MainWindow", "CipherText"))
        self.logs_label.setText(_translate("MainWindow", "Logs"))
        self.genKeys_btn.setText(_translate("MainWindow", "Generate Keys"))
        self.genKeys_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.genKeys_statusText.setText(_translate("MainWindow", "-------------"))
        self.writeKey_btn.setText(_translate("MainWindow", "Write Key"))
        self.writeKey_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.writeKey_statusText.setText(_translate("MainWindow", "-------------"))
        self.encryptMsg_btn.setText(_translate("MainWindow", "Encrypt Message"))
        self.encryptMsg_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.encryptMsg_statusText.setText(_translate("MainWindow", "-------------"))
        self.uploadData_btn.setText(_translate("MainWindow", "Upload Data"))
        self.uploadData_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.uploadData_statusText.setText(_translate("MainWindow", "-------------"))
        self.clearLogs_btn.setText(_translate("MainWindow", "Clear"))

        self.logs_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        QMetaObject.connectSlotsByName(MainWindow)

class AttMode_MainWindow(object):
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

class Choice_Window(object):
    def setupUi(self, ChoiceWindow):
       
        FETCH_WINDOW_WIDTH = 500
        FETCH_WINDOW_HEIGHT = 250
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 50
    
        # create components
        ChoiceWindow.resize(FETCH_WINDOW_WIDTH, FETCH_WINDOW_HEIGHT)
        self.centralwidget = QWidget(ChoiceWindow)

        font = QFont()
        
        self.FPGA_btn = QPushButton(self.centralwidget)
        self.FPGA_btn.setGeometry(QRect(int((FETCH_WINDOW_WIDTH/5)), int(FETCH_WINDOW_HEIGHT/4), 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        self.FPGA_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(0, 0, 250);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 10px;"
                                        "border-color: black;"
                                        "font: bold 14px;"
                                        "color: white;"
                                        "padding: 1px;"
                                    "}"
                                    "QPushButton::pressed" 
                                    "{"
                                        "background-color: rgb(0, 0, 150);"
                                        "border-style: inset;"
                                    "}"
                                    )
        self.FPGA_statusBox = QGroupBox(self.centralwidget)
        self.FPGA_statusBox.setStyleSheet("color: rgb(0, 0, 250);\nfont-weight: bold;")
        self.FPGA_statusBox.setGeometry(QRect(int((FETCH_WINDOW_WIDTH*3/5)), int(FETCH_WINDOW_HEIGHT/4), 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.FPGA_statusBox.setFont(font)
        self.FPGA_statusText = QLabel(self.FPGA_statusBox)
        self.FPGA_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

        self.title_txt = QLabel(self.centralwidget)
        self.title_txt.setGeometry(QRect(int(FETCH_WINDOW_WIDTH/10), int(FETCH_WINDOW_HEIGHT/2), 400, 40))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(40)
        self.title_txt.setFont(font)

        self.FPGA_txt = QLabel(self.centralwidget)
        self.FPGA_txt.setGeometry(QRect(int(FETCH_WINDOW_WIDTH/10), int(FETCH_WINDOW_HEIGHT/24), 400, 40))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(40)
        self.FPGA_txt.setFont(font)

        self.GenMode_btn = QPushButton(self.centralwidget)
        self.GenMode_btn.setGeometry(QRect(int(FETCH_WINDOW_WIDTH/16), FETCH_WINDOW_HEIGHT-int(FETCH_WINDOW_HEIGHT/4), BUTTON_WIDTH*2, BUTTON_HEIGHT))
        self.GenMode_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(0, 250, 0);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 10px;"
                                        "border-color: black;"
                                        "font: bold 14px;"
                                        "color: white;"
                                        "padding: 1px;"
                                    "}"
                                    "QPushButton::pressed" 
                                    "{"
                                        "background-color: rgb(0, 150, 0);"
                                        "border-style: inset;"
                                    "}"
                                    "QPushButton::disabled" 
                                    "{"
                                        "background-color: rgb(0, 50, 0);"
                                        "border-style: inset;"
                                    "}"
                                    )
        self.AttMode_btn = QPushButton(self.centralwidget)
        self.AttMode_btn.setGeometry(QRect(int(FETCH_WINDOW_WIDTH*8.7/16), FETCH_WINDOW_HEIGHT-int(FETCH_WINDOW_HEIGHT/4), BUTTON_WIDTH*2, BUTTON_HEIGHT))
        self.AttMode_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(250, 0, 0);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 10px;"
                                        "border-color: black;"
                                        "font: bold 14px;"
                                        "color: white;"
                                        "padding: 1px;"
                                    "}"
                                    "QPushButton::pressed" 
                                    "{"
                                        "background-color: rgb(150, 0, 0);"
                                        "border-style: inset;"
                                    "}"
                                    "QPushButton::disabled" 
                                    "{"
                                        "background-color: rgb(50, 0, 0);"
                                        "border-style: inset;"
                                    "}"
                                    )

        ChoiceWindow.setCentralWidget(self.centralwidget)

        # translate text into components
        _translate = QCoreApplication.translate
        ChoiceWindow.setWindowTitle(_translate("ChoiceWindow", "RSA Encryption/Decryption"))
        self.title_txt.setText(_translate("ChoiceWindow", "     Choose an Operation Mode"))
        self.FPGA_txt.setText(_translate("ChoiceWindow", "Establish FPGA UART Connection"))
        self.FPGA_btn.setText(_translate("ChoiceWindow", "Connect"))
        self.FPGA_statusBox.setTitle(_translate("ChoiceWindow", "     Status"))
        self.FPGA_statusText.setText(_translate("ChoiceWindow", "-------------"))
        self.GenMode_btn.setText(_translate("ChoiceWindow", "Generate Mode"))
        self.AttMode_btn.setText(_translate("ChoiceWindow", "Attempt Mode"))

        QMetaObject.connectSlotsByName(ChoiceWindow)
        
class fetchedData_Window(object):
    row = 0
    def setupUi(self, Window):

        FETCH_WINDOW_WIDTH = 900
        FETCH_WINDOW_HEIGHT = 600
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 36
        font = QFont()

        # create components
        Window.resize(FETCH_WINDOW_WIDTH, FETCH_WINDOW_HEIGHT)
        self.centralwidget = QWidget(Window)

        self.Window_label = QLabel(self.centralwidget)
        self.Window_label.setGeometry(QRect(0, 0, FETCH_WINDOW_WIDTH, 40))
        self.Window_label.setAlignment(Qt.AlignCenter)
        self.Window_label.setStyleSheet("QFrame" 
                                        "{"
                                            "font-size: 34px;"
                                            "font-family: Times New Roman;"    
                                            "font-weight: bold;"
                                            "color: black;"
                                        "}"
                                        )

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QRect(40, 100, FETCH_WINDOW_WIDTH-80, int(FETCH_WINDOW_HEIGHT/1.75)))
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidgetResizable(True)

        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(51, 45, FETCH_WINDOW_WIDTH-125, 45))
        self.frame.setStyleSheet("QFrame" 
                                    "{"
                                        "background-color: rgb(230,230,230);"
                                        "border-style: outset;"
                                        "border-width: 0.5px;"
                                        "border-radius: 4px;"
                                        "border-color: white;"
                                        "padding: 1px;"
                                    "}"
                                    )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.N_label = QLabel(self.frame)
        self.N_label.setGeometry(QRect(75, 3, 50, 40))
        self.N_label.setStyleSheet("QFrame" 
                                    "{"
                                        "background-color: rgb(235,235,235);"
                                        "border-style: outset;"
                                        "border-width: 0.5;"
                                        "border-radius: 2;"
                                        "border-color: rgb(200,200,200);"
                                        "font-size: 24px;"
                                        "font-family: Times New Roman;"    
                                        "font-weight: bold;"
                                        "color: black;"
                                        "padding: 1px;"
                                    "}"
                                    )
        self.N_label.setAlignment(Qt.AlignCenter)
        self.N_label.setFont(font)
        
        self.Cipher_label = QLabel(self.frame)
        self.Cipher_label.setGeometry(QRect(275, 3, int(FETCH_WINDOW_WIDTH/2)-20, 40))
        self.Cipher_label.setStyleSheet("QFrame" 
                                        "{"
                                            "background-color: rgb(235,235,235);"
                                            "border-style: outset;"
                                            "border-width: 0.5px;"
                                            "border-radius: 4px;"
                                            "border-color: rgb(200,200,200);"
                                            "font-size: 24px;"
                                            "font-family: Times New Roman;"    
                                            "font-weight: bold;"
                                            "color: black;"
                                            "padding: 1px;"
                                        "}"
                                        )
        self.Cipher_label.setAlignment(Qt.AlignCenter)
        self.Cipher_label.setFont(font)
    
        self.decide_groupBox = QGroupBox(self.centralwidget)
        self.decide_groupBox.setGeometry(QRect(50, int(FETCH_WINDOW_HEIGHT/1.25), FETCH_WINDOW_WIDTH-100, 95))

        self.Cancel_btn = QPushButton(self.centralwidget)
        self.Cancel_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(200,200,200);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 18px;"
                                        "border-color: grey;"
                                        "font-size: 36px;"
                                        "font-family: Times New Roman;"    
                                        "font-weight: bold;"
                                        "color: black;"
                                        "padding: 1px;"
                                    "}"
                                    "QPushButton::pressed" 
                                    "{"
                                        "background-color: rgb(150, 150, 150);"
                                        "border-style: inset;"
                                    "}"
                                    )
        self.Cancel_btn.setGeometry(QRect(50+10, int(FETCH_WINDOW_HEIGHT/1.25)+11, 
                                        (BUTTON_WIDTH*4)-20, BUTTON_HEIGHT*2))

        self.OK_btn = QPushButton(self.centralwidget)
        self.OK_btn.setStyleSheet("QPushButton" 
                                        "{"
                                            "background-color: rgb(200,200,200);"
                                            "border-style: outset;"
                                            "border-width: 2px;"
                                            "border-radius: 18px;"
                                            "border-color: grey;"
                                            "font-size: 36px;"
                                            "font-family: Times New Roman;"    
                                            "font-weight: bold;"
                                            "color: black;"
                                            "padding: 1px;"
                                        "}"
                                      "QPushButton::pressed" 
                                        "{"
                                            "background-color: rgb(150, 150, 150);"
                                            "border-style: inset;"
                                        "}"
                                        )
        self.OK_btn.setGeometry(QRect(int(FETCH_WINDOW_WIDTH/2)+10, int(FETCH_WINDOW_HEIGHT/1.25)+11, 
                                        (BUTTON_WIDTH*4)-20, BUTTON_HEIGHT*2))

        Window.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Fetched Data"))
        self.Window_label.setText(_translate("Window", "Choose from Fetched"))
        self.N_label.setText(_translate("Window", "N"))
        self.Cipher_label.setText(_translate("Window", "Cipher"))
        self.OK_btn.setText(_translate("Window", "OK"))
        self.Cancel_btn.setText(_translate("Window", "Cancel"))
        
    def addRow(self, data):
            
        self.fetched_N = QLabel(data["Modulus"])
        self.fetched_N.setGeometry(QRect(0, 0, 80, 40))
        self.fetched_N.setStyleSheet("QFrame" 
                                        "{"
                                            "background-color: rgb(235,235,235);"
                                            "border-style: outset;"
                                            "border-width: 0.5px;"
                                            "border-radius: 4px;"
                                            "border-color: rgb(200,200,200);"
                                            "font-size: 24px;"
                                            "font-family: Times New Roman;"    
                                            "font-weight: bold;"
                                            "color: black;"
                                            "padding: 1px;"
                                        "}"
                                        )
        self.fetched_N.setAlignment(Qt.AlignCenter)
        self.fetched_N.setObjectName("fetched_N#" + str(1+self.row))
        self.gridLayout.addWidget(self.fetched_N, self.row, 1, 1, 1)

        self.fetched_Cipher = QLabel(str(data["Cipher"]))
        self.fetched_Cipher.setGeometry(QRect(0, 0, 80, 40))
        self.fetched_Cipher.setStyleSheet("QFrame" 
                                            "{"
                                                "background-color: rgb(235,235,235);"
                                                "border-style: outset;"
                                                "border-width: 0.5px;"
                                                "border-radius: 4px;"
                                                "border-color: rgb(200,200,200);"
                                                "font-size: 24px;"
                                                "font-family: Times New Roman;"    
                                                "font-weight: bold;"
                                                "color: black;"
                                                "padding: 1px;"
                                            "}"
                                            )
        self.fetched_Cipher.setAlignment(Qt.AlignCenter)
        self.fetched_Cipher.setObjectName("fetched_Cipher#" + str(1+self.row))
        self.gridLayout.addWidget(self.fetched_Cipher, self.row, 2, 1, 3)

        self.choiceButton = QRadioButton("")
        self.choiceButton.setGeometry(QRect(50, 50, 30, 30))
        self.choiceButton.setObjectName("chosen#" + str(1+self.row))
        self.gridLayout.addWidget(self.choiceButton, self.row, 4, Qt.AlignRight)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.row += 1

    def retranslateFramUi(self, Window):
        _translate = QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Fetched Data"))
        self.OK_btn.setText(_translate("Window", "OK"))
        self.Cancel_btn.setText(_translate("Window", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Window = QMainWindow()
    ui = fetchedData_Window()
    ui.setupUi(Window)
    json = [
            {
                "N":"3333",
             "Cipher":"151151"
             }
            ,{
                "N":"311",
             "Cipher":"69669663"
             }
             ,{
                "N":"311",
             "Cipher":"69669663"
             }
             ,{
                "N":"311",
             "Cipher":"69669663"
             }
             ,{
                "N":"311",
             "Cipher":"69669663"
             }
             ,{
                "N":"311",
             "Cipher":"696vebr55555569ffffff663"
             }
             ,{
                "N":"311",
             "Cipher":"69669663"
             }
             ,{
                "N":"001",
             "Cipher":"77777"
             }
             ,{
                "N":"311",
             "Cipher":"69669663"
             }
            #  ,{
            #     "N":"311",
            #  "Cipher":"69669663"
            #  }
            #  ,{
            #     "N":"311",
            #  "Cipher":"69669663"
            #  }
            ]
    for data in json:
        ui.addRow(data)

    Window.show()
    sys.exit(app.exec_())
