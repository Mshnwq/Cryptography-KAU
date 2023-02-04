import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.browse_button = QPushButton('Browse', self)
        self.browse_button.clicked.connect(self.show_file_dialog)
        self.setCentralWidget(self.line_edit)
        # self.addToolBar(self.browse_button)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as f:
                contents = f.read()
            self.line_edit.setText(contents)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())