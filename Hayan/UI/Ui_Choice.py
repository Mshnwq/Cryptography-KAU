from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Ui_Choice(object):
    def setupUi(self, choiceWindow):

        WINDOW_WIDTH = 1200
        WINDOW_HEIGHT = 900
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 50
    
        # create components
        choiceWindow.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        stylesheet = """
            QMainWindow {
                background-image: url(:background_blur); 
                background-repeat: no-repeat; 
                background-position: center;
            }
            """
        choiceWindow.setStyleSheet(stylesheet)
        choiceWindow.setWindowTitle("Military Cryptology") 
        self.centralwidget = QWidget(choiceWindow)

        self.title_txt = QLabel("Choose an Operation Mode", self.centralwidget)
        self.title_txt.setGeometry(QRect(int(12*WINDOW_WIDTH/24)-300, int(2*WINDOW_HEIGHT/24), 600, 60))
        self.title_txt.setStyleSheet("QFrame" 
                                        "{"
                                            "background-color: rgb(100,20,200);"
                                            "border-style: outset;"
                                            "border-width: 3px;"
                                            "border-radius: 4px;"
                                            "border-color: black;"
                                            "font-size: 36px;"
                                            "font-family: Times New Roman;"    
                                            "font-weight: bold;"
                                            "color: white;"
                                            "padding: 1px;"
                                        "}"
                                        )
        self.title_txt.setAlignment(Qt.AlignCenter)

        self.BrdMode_btn = QPushButton(self.centralwidget)
        self.BrdMode_btn.setGeometry(QRect(int(3*WINDOW_WIDTH/24), int(6*WINDOW_HEIGHT/24), 
                                BUTTON_WIDTH*4, BUTTON_HEIGHT*10))
        self.BrdMode_btn.setStyleSheet("QPushButton" 
                                        "{"
                                            "background-image: url(:broadcast_image);"
                                            "background-position: center;"
                                            "background-color: rgb(0, 250, 0);"
                                            "border-style: outset;"
                                            "border-width: 2px;"
                                            "border-radius: 10px;"
                                            "border-color: black;"
                                            "padding: 1px;"
                                        "}"
                                        "QPushButton::pressed" 
                                        "{"
                                            "background-color: rgb(0, 150, 0);"
                                            "border-style: inset;"
                                        "}"
                                        )
        self.BrdMode_txt = ClickableLabel("Broadcast Mode", self.centralwidget)
        self.BrdMode_txt.setGeometry(QRect(int((3*WINDOW_WIDTH/24)+BUTTON_WIDTH/2), 
                                            int(6*WINDOW_HEIGHT/24)+BUTTON_HEIGHT*5-30, 
                                            BUTTON_WIDTH*3, 60))
        self.BrdMode_txt.setStyleSheet("QFrame" 
                                        "{"
                                            "background-color: rgb(100,20,200);"
                                            "border-style: outset;"
                                            "border-width: 3px;"
                                            "border-radius: 4px;"
                                            "border-color: black;"
                                            "font-size: 32px;"
                                            "font-family: Times New Roman;"    
                                            "font-weight: bold;"
                                            "color: white;"
                                            "padding: 1px;"
                                        "}"
                                        )
        self.BrdMode_txt.setAlignment(Qt.AlignCenter)

        self.RcvMode_btn = QPushButton(self.centralwidget)
        self.RcvMode_btn.setGeometry(QRect(int(21*WINDOW_WIDTH/24)-BUTTON_WIDTH*4, int(6*WINDOW_HEIGHT/24), 
                                        BUTTON_WIDTH*4, BUTTON_HEIGHT*10))
        self.RcvMode_btn.setStyleSheet("QPushButton" 
                                        "{" 
                                            "background-image: url(:mobileradar_image);"
                                            "background-position: center;"
                                            "background-color: rgb(250, 0, 0);"
                                            "border-style: outset;"
                                            "border-width: 2px;"
                                            "border-radius: 10px;"
                                            "border-color: black;"
                                            "color: black;"
                                            "padding: 1px;"
                                        "}"
                                        "QPushButton::pressed" 
                                        "{"
                                            "background-color: rgb(150, 0, 0);"
                                            "border-style: inset;"
                                        "}"
                                        )
        self.RcvMode_txt = ClickableLabel("Receive Mode", self.centralwidget)
        self.RcvMode_txt.setGeometry(QRect(int((21*WINDOW_WIDTH/24)-(BUTTON_WIDTH*3.5)), 
                                            int(6*WINDOW_HEIGHT/24)+BUTTON_HEIGHT*5-30, 
                                            BUTTON_WIDTH*3, 60))
        self.RcvMode_txt.setStyleSheet("QFrame" 
                                        "{"
                                            "background-color: rgb(100,20,200);"
                                            "border-style: outset;"
                                            "border-width: 3px;"
                                            "border-radius: 4px;"
                                            "border-color: black;"
                                            "font-size: 32px;"
                                            "font-family: Times New Roman;"    
                                            "font-weight: bold;"
                                            "color: white;"
                                            "padding: 1px;"
                                        "}"
                                        )
        self.RcvMode_txt.setAlignment(Qt.AlignCenter)

        choiceWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(choiceWindow)

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

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