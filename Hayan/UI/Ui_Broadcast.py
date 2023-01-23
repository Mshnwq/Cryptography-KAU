from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import importlib
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import Workers
class Ui_Broadcast(object):
    def setupUi(self, MainWindow):
        
        WINDOW_WIDTH = 1200
        WINDOW_HEIGHT = 800
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 36
        font = QFont()
    
        # create components
        MainWindow.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
                # background-color: rgb(220, 220, 220); 
        stylesheet = """
            QMainWindow {
                background-repeat: no-repeat; 
                background-position: center;
            }
            """
        MainWindow.setStyleSheet(stylesheet)
        MainWindow.setWindowTitle("Broadcast Mode")
        self.centralwidget = QWidget(MainWindow)

        keyGenBox_Xaxis = int(WINDOW_WIDTH/24)
        keyGenBox_Yaxis = int(WINDOW_HEIGHT/24)

        self.keyGen_groupBox = QGroupBox("Generation", self.centralwidget)
        self.keyGen_groupBox.setGeometry(QRect(keyGenBox_Xaxis, keyGenBox_Yaxis, 
                                int(WINDOW_WIDTH/4), int(WINDOW_HEIGHT/1.5)))
        self.keyGen_groupBox.setAutoFillBackground(False)
        self.keyGen_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.keyGen_groupBox.setFont(font)
        
        # TODO depend on what algos
        # self.algoType_groupBox = QGroupBox(self.keyGen_groupBox)
        # self.algoType_groupBox.setGeometry(QRect(10, 40,
        #                         int(WINDOW_WIDTH/4)-20, 10+int(WINDOW_HEIGHT/12)))
        # self.gridLayout = QGridLayout(self.algoType_groupBox)

        # self.bitSize_label = QLabel("Bit Size")
        # self.gridLayout.addWidget(self.bitSize_label, 0, 1, 1, 1)
        # self.bitSize_combo = QComboBox(self.algoType_groupBox)
        # self.bitSize_combo.setGeometry(QRect(0, 0, 18, 18))
        # self.updateBitCombo()
        # self.gridLayout.addWidget(self.bitSize_combo, 1, 1, 1, 1)

        self.bitSize_groupBox = QGroupBox(self.keyGen_groupBox)
        self.bitSize_groupBox.setGeometry(QRect(10, 30,
                                int(WINDOW_WIDTH/4)-20, 10+int(WINDOW_HEIGHT/24)))
        self.horizontalLayout = QHBoxLayout(self.bitSize_groupBox)

        self.bit128_btn = QRadioButton("128 bit", self.bitSize_groupBox)
        self.bit128_btn.setGeometry(QRect(0, 0, 18, 18))
        self.horizontalLayout.addWidget(self.bit128_btn)
        self.bit64_btn = QRadioButton("64 bit", self.bitSize_groupBox)
        self.bit64_btn.setGeometry(QRect(0, 0, 18, 18))
        self.bit64_btn.setChecked(True)
        self.horizontalLayout.addWidget(self.bit64_btn)
        # self.bit32_btn = QRadioButton("32 bit", self.bitSize_groupBox)
        # self.bit32_btn.setGeometry(QRect(0, 0, 18, 18))
        # self.horizontalLayout.addWidget(self.bit32_btn)
        # self.bit16_btn = QRadioButton("16 bit", self.bitSize_groupBox)
        # self.bit16_btn.setGeometry(QRect(0, 0, 18, 18))
        # self.horizontalLayout.addWidget(self.bit16_btn)


        self.genKeys_btn = QPushButton("Generate Key", self.keyGen_groupBox)
        self.genKeys_btn.setIcon(QIcon(":key"))
        self.genKeys_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(200,250,200);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 10px;"
                                        "border-color: grey;"
                                        "font-size: 16px;"
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
                                    "QPushButton::disabled" 
                                    "{"
                                        "background-color: rgb(150, 150, 150);"
                                        "border-style: inset;"
                                    "}"
                                    )
        self.genKeys_btn.setGeometry(QRect(36, int(36*4.5), BUTTON_WIDTH+25, BUTTON_HEIGHT))
        self.genKeys_statusBox = QGroupBox("Status", self.keyGen_groupBox)
        self.genKeys_statusBox.setGeometry(QRect(int(36*4.8), int(36*4.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.genKeys_statusBox.setFont(font)
        self.genKeys_statusText = QLabel("-------------", self.genKeys_statusBox)
        self.genKeys_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        
        self.Public_label = QLabel("Key Generated", self.keyGen_groupBox)
        self.Public_label.setGeometry(QRect(36, int(36*6.5), BUTTON_WIDTH+36, BUTTON_HEIGHT))
        self.Public_groupBox = QGroupBox(self.keyGen_groupBox)
        self.Public_groupBox.setGeometry(QRect(36, int(36*7.5), int(36*6.5), (36*5)+4))
        self.Public_box = QLabel(self.Public_groupBox)
        self.Public_box.setGeometry(QRect(6, 2, int(36*6), 36*5))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(10)
        self.Public_box.setFont(font)

        self.writeKey_btn = QPushButton("Print Key", self.centralwidget)
        self.writeKey_btn.setIcon(QIcon(":barcode"))
        self.writeKey_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(200,250,200);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 10px;"
                                        "border-color: grey;"
                                        "font-size: 16px;"
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
                                    "QPushButton::disabled" 
                                    "{"
                                        "background-color: rgb(150, 150, 150);"
                                        "border-style: inset;"
                                    "}"
                                    )
        self.writeKey_btn.setGeometry(QRect(keyGenBox_Xaxis+36, 
                    int(WINDOW_HEIGHT/1.575), BUTTON_WIDTH+15, BUTTON_HEIGHT))
        self.writeKey_statusBox = QGroupBox("Status", self.centralwidget)
        self.writeKey_statusBox.setStyleSheet("font-weight: bold")
        self.writeKey_statusBox.setGeometry(QRect(int(keyGenBox_Xaxis+36*4.8), 
                    int(WINDOW_HEIGHT/1.575), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.writeKey_statusBox.setFont(font)
        self.writeKey_statusText = QLabel("-------------", self.writeKey_statusBox)
        self.writeKey_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

        self.message_groupBox = QGroupBox("Enter a message", self.centralwidget)
        self.message_groupBox.setGeometry(QRect(int(8*WINDOW_WIDTH/24), keyGenBox_Yaxis, 
                                                int(15*WINDOW_WIDTH/24), int(WINDOW_HEIGHT/1.5)))
        self.message_groupBox.setAutoFillBackground(False)
        self.message_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.message_groupBox.setFont(font)

        self.encrypt_groupBox = QGroupBox(self.message_groupBox)
        self.encrypt_groupBox.setGeometry(QRect(int(1.5*WINDOW_WIDTH/24), int(4.5*WINDOW_HEIGHT/24),
                                int(12*WINDOW_WIDTH/24), 10+int(WINDOW_HEIGHT/12)))
        self.gridLayout = QGridLayout(self.encrypt_groupBox)

        self.blockMode_label = QLabel("Block Mode")
        self.gridLayout.addWidget(self.blockMode_label, 0, 0, 1, 1)
        self.blockMode_combo = QComboBox(self.encrypt_groupBox)
        self.blockMode_combo.setGeometry(QRect(0, 0, 18, 18))
        # populate with current available block modes
        self.blockMode_combo.addItems(["ECB", "CBC"]) # TODO
        self.gridLayout.addWidget(self.blockMode_combo, 1, 0, 1, 1)

        self.algoType_label = QLabel(" Algorithm")
        self.gridLayout.addWidget(self.algoType_label, 0, 1, 1, 1)
        self.algoType_combo = QComboBox(self.encrypt_groupBox)
        self.algoType_combo.setGeometry(QRect(0, 0, 18, 18))
        # populate with current available algorithms
        for algo in Workers.getModules().keys():
            self.algoType_combo.addItem(algo)
        self.gridLayout.addWidget(self.algoType_combo, 1, 1, 1, 1)

        self.encryptMsg_btn = QPushButton("Encrypt Message", self.encrypt_groupBox)
        self.encryptMsg_btn.setIcon(QIcon(":key_lock"))
        self.encryptMsg_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(20, 200, 20);"
                                        "border-width: 2px;"
                                        "border-color: black;"
                                        "font: bold 14px;"
                                        "color: white;"
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
        self.encryptMsg_btn.setGeometry(QRect(0, 0, BUTTON_WIDTH+40, BUTTON_HEIGHT+10))
        self.gridLayout.addWidget(self.encryptMsg_btn, 0, 2, 3, 1)
        self.encryptMsg_statusBox = QGroupBox("Status", self.encrypt_groupBox)
        self.encryptMsg_statusBox.setStyleSheet("font-weight: bold")
        self.encryptMsg_statusBox.setGeometry(QRect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.encryptMsg_statusBox.setFont(font)
        self.encryptMsg_statusText = QLabel("   -------------", self.encryptMsg_statusBox)
        self.encryptMsg_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.gridLayout.addWidget(self.encryptMsg_statusBox, 0, 3, 2, 1)

        self.plaintext_label = QLabel("Plaintext", self.message_groupBox)
        self.plaintext_label.setGeometry(QRect(40*3, 40, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.plaintext_label.setFont(font)
        self.plaintext_box = QTextEdit(self.message_groupBox)
        self.plaintext_box.setGeometry(QRect(40, 40*2, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 60))
        self.ciphertext_label = QLabel("Ciphertext", self.message_groupBox)
        self.ciphertext_label.setGeometry(QRect(40*3, 250, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.ciphertext_label.setFont(font)
        self.ciphertext_box = QGroupBox(self.message_groupBox)
        self.ciphertext_box.setGeometry(QRect(40, 295, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40*4))
        self.ciphertext_text = QLabel(self.ciphertext_box)
        self.ciphertext_text.setGeometry(QRect(12, 5, BUTTON_WIDTH*6, BUTTON_HEIGHT*4))


        self.uploadData_btn = QPushButton("Broadcast Data", self.centralwidget)
        self.uploadData_btn.setIcon(QIcon(":broadcast_tower"))
        self.uploadData_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(200,250,200);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 18px;"
                                        "border-color: grey;"
                                        "font-size: 16px;"
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
                                    "QPushButton::disabled" 
                                    "{"
                                        "background-color: rgb(150, 150, 150);"
                                        "border-style: inset;"
                                    "}"
                                    )
        self.uploadData_btn.setGeometry(QRect(int(12*WINDOW_WIDTH/24)-20, int(15*WINDOW_HEIGHT/24),       
                                            BUTTON_WIDTH+40, BUTTON_HEIGHT))
        self.uploadData_statusBox = QGroupBox("Status", self.centralwidget)
        self.uploadData_statusBox.setStyleSheet("font-weight: bold")
        self.uploadData_statusBox.setGeometry(QRect(int(15*WINDOW_WIDTH/24), int(15*WINDOW_HEIGHT/24),       
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.uploadData_statusBox.setFont(font)
        self.uploadData_statusText = QLabel("-------------", self.uploadData_statusBox)
        self.uploadData_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        

        self.logs_box = QTextEdit(self.centralwidget)
        self.logs_box.setGeometry(QRect(keyGenBox_Xaxis, int(WINDOW_HEIGHT/1.35), 
                                        int(WINDOW_WIDTH/1.25), int(WINDOW_HEIGHT/5.6)))

        self.logs_label = QLabel("Logs", self.centralwidget)
        self.logs_label.setGeometry(QRect(int(21*WINDOW_WIDTH/24), int(18*WINDOW_HEIGHT/24), 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(60)
        self.logs_label.setFont(font)

        self.clearLogs_btn = QPushButton("Clear", self.centralwidget)
        self.clearLogs_btn.setIcon(QIcon(":clear"))
        self.clearLogs_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(200,250,200);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 18px;"
                                        "border-color: grey;"
                                        "font-size: 16px;"
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
                                    "QPushButton::disabled" 
                                    "{"
                                        "background-color: rgb(150, 150, 150);"
                                        "border-style: inset;"
                                    "}"
                                    )
        self.clearLogs_btn.setGeometry(QRect(int(21*WINDOW_WIDTH/24), int(21*WINDOW_HEIGHT/24), 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))

        # Create actions to attach to menu bar
        self._createActions(MainWindow)
        # Create menu bar and populate with actions
        self._createMenuBar(MainWindow)
        
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)

        # translate text into components
        _translate = QCoreApplication.translate
        self.logs_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        QMetaObject.connectSlotsByName(MainWindow)

    def _createMenuBar(self, MainWindow):
        self.menuBar = QMenuBar(MainWindow)
        # File menu
        settingsMenu = self.menuBar.addMenu(QIcon(":settings"), "&Settings")
        configMenu = settingsMenu.addMenu("&Configurations")
        configMenu.addAction(self.appConfigAction)
        configMenu.addAction(self.FPGAConfigAction)
        settingsMenu.addSeparator()
        settingsMenu.addAction(self.logoutAction)
        # Help menu
        helpMenu = self.menuBar.addMenu(QIcon(":info"), "&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

        MainWindow.setMenuBar(self.menuBar)

    def _createActions(self, MainWindow):
        self.appConfigAction = QAction("&App Configurations", MainWindow)
        self.appConfigAction.triggered.connect(self.appConfigActionButtonClick)
        self.FPGAConfigAction = QAction("&FPGA Configurations", MainWindow)
        self.logoutAction = QAction("&Logout", MainWindow)
        self.helpContentAction = QAction("&Help Content", MainWindow)
        self.helpContentAction.triggered.connect(lambda: self.logs_box.append("Help Later"))
        self.aboutAction = QAction("&About", MainWindow)
        self.aboutAction.triggered.connect(self.aboutActionButtonClick)

    def appConfigActionButtonClick(self):
        # self.settingWindow = Ui_SettingsWindow(self.isAdmin)
        # self.settingWindow.show()
        ...

    def aboutActionButtonClick(self):
        dlg = AboutDialog()
        dlg.exec_()

    def updateBitCombo(self, sizes = ["16", "32", "64", "128"]):
        self.bitSize_combo.clear()
        self.bitSize_combo.addItems(sizes)

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.buttonBox = QDialogButtonBox()
        self.setWindowIcon(QIcon(":seal"))
        self.layout = QGridLayout()
        message = QLabel("Licensed by SCFS")
        self.layout.addWidget(message, 0, 0)
        version = QLabel("Version: {\"Beta\"}")
        self.layout.addWidget(version, 2, 0)
        icon = QPixmap(":SCFS")
        image = QLabel()
        image.setPixmap(icon.scaled(100, 100))
        self.layout.addWidget(image, 1, 1)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

def construct():
    return Ui_Broadcast()

def testWindow():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_Broadcast()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    testWindow()