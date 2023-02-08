from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Ui_Fetch(object):
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

        # self.N_label = QLabel(self.frame)
        # self.N_label.setGeometry(QRect(75, 3, 50, 40))
        # self.N_label.setStyleSheet("QFrame" 
        #                             "{"
        #                                 "background-color: rgb(235,235,235);"
        #                                 "border-style: outset;"
        #                                 "border-width: 0.5;"
        #                                 "border-radius: 2;"
        #                                 "border-color: rgb(200,200,200);"
        #                                 "font-size: 24px;"
        #                                 "font-family: Times New Roman;"    
        #                                 "font-weight: bold;"
        #                                 "color: black;"
        #                                 "padding: 1px;"
        #                             "}"
        #                             )
        # self.N_label.setAlignment(Qt.AlignCenter)
        # self.N_label.setFont(font)
        
        self.Cipher_label = QLabel(self.frame)
        self.Cipher_label.setGeometry(QRect(172, 3, int(FETCH_WINDOW_WIDTH/2)-20, 40))
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
        # self.N_label.setText(_translate("Window", "N"))
        self.Cipher_label.setText(_translate("Window", "Cipher"))
        self.OK_btn.setText(_translate("Window", "OK"))
        self.Cancel_btn.setText(_translate("Window", "Cancel"))
        
    def addRow(self, data):
            
        # self.fetched_N = QLabel(data["N"])
        # self.fetched_N.setGeometry(QRect(0, 0, 80, 40))
        # self.fetched_N.setStyleSheet("QFrame" 
        #                                 "{"
        #                                     "background-color: rgb(235,235,235);"
        #                                     "border-style: outset;"
        #                                     "border-width: 0.5px;"
        #                                     "border-radius: 4px;"
        #                                     "border-color: rgb(200,200,200);"
        #                                     "font-size: 24px;"
        #                                     "font-family: Times New Roman;"    
        #                                     "font-weight: bold;"
        #                                     "color: black;"
        #                                     "padding: 1px;"
        #                                 "}"
        #                                 )
        # self.fetched_N.setAlignment(Qt.AlignCenter)
        # self.fetched_N.setObjectName("fetched_N#" + str(1+self.row))
        # self.gridLayout.addWidget(self.fetched_N, self.row, 1, 1, 1)

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
        self.gridLayout.addWidget(self.fetched_Cipher, self.row, 1, 1, 3)

        self.choiceButton = QRadioButton("")
        self.choiceButton.setGeometry(QRect(50, 50, 30, 30))
        self.choiceButton.setObjectName("chosen#" + str(1+self.row))
        self.gridLayout.addWidget(self.choiceButton, self.row, 3, Qt.AlignRight)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.row += 1

    def retranslateFramUi(self, Window):
        _translate = QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Fetched Data"))
        self.OK_btn.setText(_translate("Window", "OK"))
        self.Cancel_btn.setText(_translate("Window", "Cancel"))

def construct():
    return Ui_Fetch()

def testWindow():
    app = QApplication(sys.argv)
    Window = QMainWindow()
    ui = Ui_Fetch()
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
            ,{
                "N":"311",
            "Cipher":"69669663"
            }
            ,{
                "N":"311",
            "Cipher":"69669663"
            }
            ]
    for data in json:
        ui.addRow(data)

    Window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    testWindow()