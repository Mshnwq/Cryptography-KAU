from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import Workers

class Ui_Receive(object):
    def setupUi(self, MainWindow):
        
        WINDOW_WIDTH = 1200
        WINDOW_HEIGHT = 800
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 36
        font = QFont()
    
        # create components
        MainWindow.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        stylesheet = """
            QMainWindow {
                background-repeat: no-repeat; 
                background-position: center;
            }
            """
        MainWindow.setStyleSheet(stylesheet)
        MainWindow.setWindowTitle("Receive Mode")
        self.centralwidget = QWidget(MainWindow)

        fetchBox_Xaxis = int(WINDOW_WIDTH/24)
        fetchBox_Yaxis = int(WINDOW_HEIGHT/24)

        self.fetch_groupBox = QGroupBox("Fetch Data", self.centralwidget)
        self.fetch_groupBox.setGeometry(QRect(fetchBox_Xaxis, fetchBox_Yaxis, 
                                int(WINDOW_WIDTH/4), int(WINDOW_HEIGHT/2)+36))
        self.fetch_groupBox.setAutoFillBackground(False)
        self.fetch_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.fetch_groupBox.setFont(font)
        
        self.fetch_btn = QPushButton("Fetch", self.fetch_groupBox)
        self.fetch_btn.setIcon(QIcon(":radar"))
        self.fetch_btn.setStyleSheet("QPushButton" 
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
        self.fetch_btn.setGeometry(QRect(36, int(36*1.5), BUTTON_WIDTH+6, BUTTON_HEIGHT))
        self.fetch_statusBox = QGroupBox("Status", self.fetch_groupBox)
        self.fetch_statusBox.setGeometry(QRect(int(36*4.8), int(36*1.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.fetch_statusBox.setFont(font)
        self.fetch_statusText = QLabel("-------------", self.fetch_statusBox)
        self.fetch_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        
        self.readKey_btn = QPushButton("Scan Key", self.fetch_groupBox)
        self.readKey_btn.setIcon(QIcon(":scan"))
        self.readKey_btn.setStyleSheet("QPushButton" 
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
        self.readKey_btn.setGeometry(QRect(36, int(36*3), BUTTON_WIDTH+6, BUTTON_HEIGHT))
        self.readKey_statusBox = QGroupBox("Status", self.fetch_groupBox)
        self.readKey_statusBox.setStyleSheet("font-weight: bold")
        self.readKey_statusBox.setGeometry(QRect(int(36*4.8), int(36*3), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.readKey_statusBox.setFont(font)
        self.readKey_statusText = QLabel("-------------", self.readKey_statusBox)
        self.readKey_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

        self.scanned_label = QLabel("Scanned Key", self.fetch_groupBox)
        self.scanned_label.setGeometry(QRect(36, int(36*5), BUTTON_WIDTH+46, BUTTON_HEIGHT))
        self.scanned_groupBox = QGroupBox(self.fetch_groupBox)
        self.scanned_groupBox.setGeometry(QRect(36, int(36*6), int(36*6.5), (36*5)+4))
        self.scanned_box = QLabel(self.scanned_groupBox)
        self.scanned_box.setGeometry(QRect(6, 2, int(36*8), 36*5))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(10)
        self.scanned_box.setFont(font)
        self.scanned_label.setFont(font)

        self.message_groupBox = QGroupBox("The Message", self.centralwidget)
        self.message_groupBox.setGeometry(QRect(int(2*WINDOW_WIDTH/24)+int(WINDOW_WIDTH/4), 
                                                int(WINDOW_HEIGHT/24), 
                                                WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)), 
                                                int(WINDOW_HEIGHT/2)+36))
        self.message_groupBox.setAutoFillBackground(False)
        self.message_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.message_groupBox.setFont(font)

        self.encrypt_groupBox = QGroupBox(self.message_groupBox)
        self.encrypt_groupBox.setGeometry(QRect(int(1.5*WINDOW_WIDTH/24), int(6.5*WINDOW_HEIGHT/24),
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

        self.decryptMsg_btn = QPushButton("Decrypt Message", self.message_groupBox)
        self.decryptMsg_btn.setIcon(QIcon(":unlock"))
        self.decryptMsg_btn.setStyleSheet("QPushButton" 
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
        self.decryptMsg_btn.setGeometry(QRect(40*6, int(40*6.5), BUTTON_WIDTH+30, BUTTON_HEIGHT))
        self.gridLayout.addWidget(self.decryptMsg_btn, 0, 2, 2, 1)
        self.decryptMsg_statusBox = QGroupBox("Status", self.message_groupBox)
        self.decryptMsg_statusBox.setStyleSheet("font-weight: bold")
        self.decryptMsg_statusBox.setGeometry(QRect(40*10, int(40*6.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.decryptMsg_statusBox.setFont(font)
        self.decryptMsg_statusText = QLabel("-------------", self.decryptMsg_statusBox)
        self.decryptMsg_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.gridLayout.addWidget(self.decryptMsg_statusBox, 0, 3, 2, 1)

        self.ciphertext_label = QLabel("CipherText", self.message_groupBox)
        self.ciphertext_label.setGeometry(QRect(40*3, 40, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.ciphertext_label.setFont(font)
        self.ciphertext_box = QGroupBox(self.message_groupBox)
        self.ciphertext_box.setGeometry(QRect(40, 40*2, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40*3))
        self.ciphertext_text = QLabel(self.message_groupBox)
        self.ciphertext_text.setGeometry(QRect(40, 40*2, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40))

        self.plaintext_label = QLabel("PlainText", self.message_groupBox)
        self.plaintext_label.setGeometry(QRect(40*3, int(40*7.5), 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.plaintext_label.setFont(font)
        self.plaintext_box = QGroupBox(self.message_groupBox)
        self.plaintext_box.setGeometry(QRect(40, int(40*8.5), 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40*2))
        self.plaintext_text = QLabel(self.plaintext_box)
        self.plaintext_text.setGeometry(QRect(12, -45, BUTTON_WIDTH*6, BUTTON_HEIGHT*4))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(10)
        self.plaintext_text.setFont(font)

        self.logs_box = QTextEdit(self.centralwidget)
        self.logs_box.setGeometry(QRect(fetchBox_Xaxis + BUTTON_WIDTH + 36, 
                                        int(2.5*WINDOW_HEIGHT/24)+int(WINDOW_HEIGHT/2), 
                                        WINDOW_WIDTH-(fetchBox_Xaxis + BUTTON_WIDTH + 4)*2, 
                                        int(WINDOW_HEIGHT/2)-int(4.5*WINDOW_HEIGHT/24)))

        self.logs_label = QLabel("Logs", self.centralwidget)
        self.logs_label.setGeometry(QRect(fetchBox_Xaxis+10*6,       
                                            int(2.5*WINDOW_HEIGHT/24)+int(WINDOW_HEIGHT/2), 
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
        self.clearLogs_btn.setGeometry(QRect(int(fetchBox_Xaxis*1.5), int(WINDOW_HEIGHT)-102, 
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
        settingsMenu.addAction(self.exitAction)
        # Help menu
        helpMenu = self.menuBar.addMenu(QIcon(":info"), "&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

        MainWindow.setMenuBar(self.menuBar)

    def _createActions(self, MainWindow):
        self.appConfigAction = QAction("&App Configurations", MainWindow)
        self.appConfigAction.triggered.connect(self.appConfigActionButtonClick)
        self.FPGAConfigAction = QAction("&FPGA Configurations", MainWindow)
        self.exitAction = QAction("&Exit", MainWindow)
        self.exitAction.triggered.connect(qApp.quit) # TODO logout handle
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