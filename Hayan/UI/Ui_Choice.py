from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Ui_Choice(object):
    def setupUi(self, choiceWindow):

        WINDOW_WIDTH = 900
        WINDOW_HEIGHT = 600
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 50
    
        # create components
        choiceWindow.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        stylesheet = """
            QMainWindow {
                background-image: url(:background); 
                background-repeat: no-repeat; 
                background-position: center;
            }
            """
        choiceWindow.setStyleSheet(stylesheet) 
        self.centralwidget = QWidget(choiceWindow)

        font = QFont()
        
        # Create a label to hold the background image
        self.background_label = QLabel(self.centralwidget)
        # self.background_label.setStyleSheet("border :3px solid blue;")
        # self.
        # self.background_label.setStyleSheet(stylesheet) 
        # self.background_label.setStyleSheet( 
                                    # "{"
                                        # "background-image : url(:background.jpg);"
                                        # "border: 2px solid blue;"
                                        # "background-repeat: no-repeat;" 
                                        # "background-position: center;"
                                    # "}"
                                    # )
        # setting label text
        self.background_label.setText("no background image")
        # Create a pixmap from the image file
        # self.pixmap = QPixmap(f"background.jpg")

        # Set the pixmap as the background image
        # self.background_label.setPixmap(self.pixmap)

        self.title_txt = QLabel(self.centralwidget)
        self.title_txt.setGeometry(QRect(int(WINDOW_WIDTH/10), int(WINDOW_HEIGHT/2), 400, 40))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(40)
        self.title_txt.setFont(font)

        self.logout_button = QPushButton("Logout", self.centralwidget)

        # self.button_layout = QVBoxLayout()
        # self.button_layout.addWidget(self.logout_button)

        # Create a layout for the window
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.addWidget(self.background_label)
        # self.layout.addWidget(self.logout_button)
        # self.layout.addLayout(self.button_layout)

        self.BrdMode_btn = QPushButton(self.centralwidget)
        self.BrdMode_btn.setGeometry(QRect(int(WINDOW_WIDTH/16), WINDOW_HEIGHT-int(WINDOW_HEIGHT/4), BUTTON_WIDTH*2, BUTTON_HEIGHT))
        self.BrdMode_btn.setStyleSheet("QPushButton" 
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

        self.RcvMode_btn = QPushButton(self.centralwidget)
        self.RcvMode_btn.setGeometry(QRect(int(WINDOW_WIDTH*8.7/16), WINDOW_HEIGHT-int(WINDOW_HEIGHT/4), BUTTON_WIDTH*2, BUTTON_HEIGHT))
        self.RcvMode_btn.setStyleSheet("QPushButton" 
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

        choiceWindow.setCentralWidget(self.centralwidget)

        # translate text into components
        _translate = QCoreApplication.translate
        choiceWindow.setWindowTitle(_translate("choiceWindow", "Military Cryptology"))
        self.title_txt.setText(_translate("choiceWindow", "     Choose an Operation Mode"))
        self.BrdMode_btn.setText(_translate("choiceWindow", "Broadcast Mode"))
        self.RcvMode_btn.setText(_translate("choiceWindow", "Receive Mode"))

        QMetaObject.connectSlotsByName(choiceWindow)

def construct():
    return Ui_Choice()

def testWindow():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_Choice()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    testWindow()