#!/usr/bin/python
from Window import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from key_gen import RSA
from RFID_Driver import RFID
from FPGA_Driver import FPGA
from firebase_admin import *
from firebase_admin import db
import json
import sys
import os
import platform

class MainWindow(QMainWindow):
      
    rsa  = RSA() # create instance of RSA
    rfid = RFID() # create instance of RFID
    fpga = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dialogType = 0

        # construct choice window
        self.ui = Choice_Window()
        self.ui.setupUi(self)

        # establish FPGA UART comm
        #TODO
        self.ui.FPGA_btn.clicked.connect(self.establishUART)
        
        self.ui.GenMode_btn.clicked.connect(self.generateMode)
        self.ui.AttMode_btn.clicked.connect(self.attemptMode)
        
        # disable buttons
        self.ui.GenMode_btn.setEnabled(False)
        self.ui.AttMode_btn.setEnabled(False)
        
        absolutepath = os.path.abspath(__file__)
        fileDirectory = os.path.dirname(absolutepath)
        if platform.system() == 'Windows':
            # connect to cloud
            cred = credentials.Certificate(fileDirectory + '\\fpga-rfid-rsa-firebase-adminsdk-w7ve4-66256d1a41.json')
            defualt_app = initialize_app(cred, 
                {
                "databaseURL" : "https://fpga-rfid-rsa-default-rtdb.firebaseio.com/"
                }
            )
        elif platform.system() == 'Linux':
                # connect to cloud
            cred = credentials.Certificate(fileDirectory + '/fpga-rfid-rsa-firebase-adminsdk-w7ve4-66256d1a41.json')
            defualt_app = initialize_app(cred, 
                {
                "databaseURL" : "https://fpga-rfid-rsa-default-rtdb.firebaseio.com/"
                }
            )
        else:
            exit(f"{platform.system()} OS is not supported")

    def generateMode(self):

        # construct the window
        self.ui = GenMode_MainWindow()
        self.ui.setupUi(self)
        
        # Generate keys
        self.ui.genKeys_btn.clicked.connect(self.generateKeys)

        # Write Key
        self.ui.writeKey_btn.clicked.connect(self.writeKey)

        # Encrpyt the plaintext
        # TODO
        self.ui.encryptMsg_btn.clicked.connect(self.encrypt)

        # Upload data to backend
        self.ui.uploadData_btn.clicked.connect(self.sendData)

        # Clear logs
        self.ui.clearLogs_btn.clicked.connect(lambda: self.ui.logs_box.setPlainText(""))
        
        # disable buttons
        self.ui.encryptMsg_btn.setEnabled(False)
        self.ui.writeKey_btn.setEnabled(False)
        self.ui.uploadData_btn.setEnabled(False)

    def attemptMode(self):

        # construct the window
        self.ui = AttMode_MainWindow()
        self.ui.setupUi(self)

        # Fetch keys
        self.ui.fetch_btn.clicked.connect(self.fetchData)
        self.fetchStatus = False

        # Read Key
        self.ui.readKey_btn.clicked.connect(self.readKey)
        self.readStatus = False

        # Decrpyt the plaintext
        # TODO
        self.ui.decryptMsg_btn.clicked.connect(self.decrypt)

        # Clear logs
        self.ui.clearLogs_btn.clicked.connect(lambda: self.ui.logs_box.setPlainText(""))
        
        # disable buttons
        self.ui.decryptMsg_btn.setEnabled(False)

    def checkBtns(self):
        if (self.ui.bit16_btn.isChecked()):
            return 16
        elif (self.ui.bit64_btn.isChecked()):
            return 64
        elif (self.ui.bit32_btn.isChecked()):
            return 32
        else:
            return 64
        
    def generateKeys(self):
        # Sorry for no comments
        bitSize = self.checkBtns()
        self.publicKey, self.privateKey = self.rsa.generateKey(
            bitSize, window=self.ui)
        n = self.rsa.getN()
        e = self.rsa.getE()
        d = self.rsa.getD()
        self.ui.N_label_box.setText(n)
        self.ui.E_label_box.setText(e)
        self.ui.D_label_box.setText(d)
    
        privateKey = self.fitNumber(e, 20)
        privateKey += ",\n"
        publicKey = self.fitNumber(d, 20)
        publicKey += ",\n"
        modKey = self.fitNumber(n, 20)
        privateKey += modKey
        publicKey += modKey

        self.ui.Private_box.setText(privateKey)
        self.ui.Public_box.setText(publicKey)
        self.ui.writeKey_btn.setEnabled(True)
        self.ui.encryptMsg_btn.setEnabled(True)
        self.ui.logs_box.append("Key Generation Success")
        self.ui.genKeys_statusText.setText("Keys Generated")
        self.ui.genKeys_statusText.setStyleSheet(
            "color: rgb(0,200,0);\nfont: bold 10px;")

    # helper method for fitting number into a box
    def fitNumber(self, num, width):
        fit = ''
        leng = len(num)
        for i in range(leng):
            fit += num[i]
            if ((i+1)%width == 0):
                fit += "\n"
        return fit

    def readKey(self):
        self.dialogType = 1

        stat = self.rfid.readKey( window=self.ui)
        if (stat == 1):
            self.ui.logs_box.append("Read Key Success")
            self.ui.readKey_statusText.setText("   Success")
            self.ui.readKey_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 14px;")
            self.key = self.rfid.getKey()
            self.ui.logs_box.append(f'(int) read: {self.key}')
            self.ui.logs_box.append(f'(hex) read: {hex(self.key)}')
            self.ui.logs_box.append(f'(bin) read: {bin(self.key)}')
            stringKey = self.fitNumber(str(self.key), 20)
            self.ui.Public_box.setText(stringKey)
            self.readStatus = True
            self.ui.decryptMsg_btn.setEnabled(
                self.readStatus and self.fetchStatus)
        elif stat == 0: 
            self.ui.logs_box.append("Read Key Failed")
            self.ui.readKey_statusText.setText("    Failed")
            self.ui.readKey_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 12px;;")
        else:
            self.ui.readKey_statusText.setText("    Failed")
            self.ui.readKey_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 12px;;")
            dialog = QMessageBox()
            dialog.setText("incorrect amount of keys in front of reader")
            dialog.setWindowTitle("Error!")
            dialog.setIcon(QMessageBox.Critical)
            dialog.setInformativeText("Place only 1 key only infront of reader")
            dialog.setStandardButtons(QMessageBox.Retry|QMessageBox.Cancel)
            dialog.buttonClicked.connect(self.dialogClicked)
            dialog.exec_()

    def writeKey(self):
        self.dialogType = 2

        tagData = bytearray(16)
        keyToWriteInt = self.publicKey[0]
        keyToWrite = keyToWriteInt.to_bytes(16, byteorder = 'big')

        for i in range(0, len(keyToWrite)):  
            tagData[i] = keyToWrite[i]  

        # print(keyToWriteInt)
        # print(keyToWrite)
        # print(tagData)
        stat = self.rfid.writeKey(
            desiredDataToWrite = tagData, window=self.ui)
        if (stat == 1):
            self.ui.logs_box.append("Write Key Success")
            self.ui.writeKey_statusText.setText("Key Issued")
            self.ui.writeKey_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 14px;")
            self.ui.logs_box.append(f'(int) written: {keyToWriteInt}')
            self.ui.logs_box.append(f'(hex) written: {hex(keyToWriteInt)}')
            self.ui.logs_box.append(f'(bin) written: {bin(keyToWriteInt)}')
        elif stat == 0: 
            self.ui.logs_box.append("Write Key Failed")
            self.ui.writeKey_statusText.setText("Issueing Failed")
            self.ui.writeKey_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 12px;;")
        else:
            self.ui.writeKey_statusText.setText("Issueing Failed")
            self.ui.writeKey_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 12px;;")
            dialog = QMessageBox()
            dialog.setText("incorrect amount of keys in front of reader")
            dialog.setWindowTitle("Error!")
            dialog.setIcon(QMessageBox.Critical)
            dialog.setInformativeText("Place only 1 key only infront of reader")
            dialog.setStandardButtons(QMessageBox.Retry|QMessageBox.Cancel)
            dialog.buttonClicked.connect(self.dialogClicked)
            dialog.exec_()

    def dialogClicked(self, btn):
        # print(btn.text())
        if(self.dialogType == 2 and btn.text() == 'Retry'):
            self.writeKey()
        if(self.dialogType == 1 and btn.text() == 'Retry'):
            self.readKey()

    def establishUART(self):
        #TODO ABDULLAH HELP
        print("kaka")
        
        self.fpga = FPGA() # create instance of RFID

        stat = 1

        if stat == 1:
            # self.ui.logs_box.append("FPGA UART Success")
            self.ui.FPGA_statusText.setText("  Success")
            self.ui.FPGA_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 16px;")
            self.ui.GenMode_btn.setEnabled(True)
            self.ui.AttMode_btn.setEnabled(True)
        else: 
            # self.ui.logs_box.append("FPGA UART Failed")
            self.ui.FPGA_statusText.setText("Failed")
            self.ui.FPGA_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 16px;;")

    def encrypt(self):
    
        plainTextString = self.ui.plaintext_box.text()
        nchars = len(plainTextString)
        # string to int or long. Type depends on nchars
        plainTextInt = sum(ord(plainTextString[byte])<<8*(nchars-byte-1) for byte in range(nchars))
        print(plainTextInt)
        # plainTextHex = hex(plainTextInt)[2::]
        # print(plainTextHex)

        #encrypting # TODO
        stat = self.fpga.encrypt_decrypt(plainTextInt, self.rsa.getE(), self.rsa.getN())
        # self.cipherTextInt = cipherTextInt

        # cipherTextString = ''.join(chr((cipherTextInt>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))
        # int or long to string
        # self.ui.ciphertext_text.setText(cipherTextString)
        # self.ui.ciphertext_text.setText(str(cipherTextInt))

        if stat == 1:
            self.ui.logs_box.append("Encryption Success")
            self.ui.encryptMsg_statusText.setText("Success")
            self.ui.encryptMsg_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 16px;")
            out = self.fpga.getOut() 
            pln = self.fitNumber(out, 20)
            self.ui.ciphertext_text.setText(pln)
            self.ui.uploadData_btn.setEnabled(True)
        else: 
            self.ui.logs_box.append("Encryption Failed")
            self.ui.encryptMsg_statusText.setText("Failed")
            self.ui.encryptMsg_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 16px;;")
    
    def decrypt(self):
    
        # cipherTextString = self.ui.ciphertext_text.text()
        # nchars = len(cipherTextString)
        # string to int or long. Type depends on nchars
        # cipherTextInt = sum(ord(cipherTextString[byte])<<8*(nchars-byte-1) for byte in range(nchars))
        cipherTextInt = int(self.ui.ciphertext_text.text())
        # print(cipherTextInt)
        # # plainTextHex = hex(plainTextInt)[2::]
        # # print(plainTextHex)

        # decrypting # TODO
        stat = self.fpga.encrypt_decrypt(cipherTextInt, self.key, self.n)
        # self.plainTextInt = plainTextInt

        # plainTextString = ''.join(chr((plainTextInt>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))
        # # int or long to string
        # self.ui.plaintext_text.setText(plainTextString)

        if stat == 1:
            self.ui.logs_box.append("Decryption Success")
            self.ui.decryptMsg_statusText.setText("Success")
            self.ui.decryptMsg_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 16px;")
            out = self.fpga.getOut() 
            pln = self.fitNumber(out, 50)
            self.ui.plaintext_text.setText(pln)
        else: 
            self.ui.logs_box.append("Decryption Failed")
            self.ui.decryptMsg_statusText.setText("Failed")
            self.ui.decryptMsg_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 16px;;")

    def fetchData(self):
        
        try:
            get_app()
            ref = db.reference("/storage/")
            json_dict = ref.get()
            stat = 1
        except:
            stat = 0   

        self.dataFetched = []
        # self.dataFetched = ['{\n    "Modulus": "3842753039",\n    "Cipher": 10012\n}', '{\n    "Modulus": "2978427307",\n    "Cipher": 10012\n}'
        #                    ,'{\n    "Modulus": "3842753039",\n    "Cipher": 10012\n}', '{\n    "Modulus": "2978427307",\n    "Cipher": 10012\n}'
        #                    ,'{\n    "Modulus": "3842753039",\n    "Cipher": 10012\n}', '{\n    "Modulus": "2978427307",\n    "Cipher": 10012\n}'
        #                    ,'{\n    "Modulus": "3842753039",\n    "Cipher": 10012\n}', '{\n    "Modulus": "2978427307",\n    "Cipher": 10012\n}'
        #                    ,'{\n    "Modulus": "3842753039",\n    "Cipher": 10012\n}', '{\n    "Modulus": "2927307",\n    "Cipher": 112\n}']

        for i in json_dict.keys():
            self.dataFetched.append(json_dict[i])

        if stat == 1:
            self.chosenFetched = None
            self.showFetched(self.dataFetched)

        else: 
            self.ui.logs_box.append("Fetch Failed")
            self.ui.fetch_statusText.setText("Failed")
            self.ui.fetch_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 16px;;")

    def sendData(self):

        pair = {}
        pair["Modulus"] = self.rsa.getN()
        pair["Cipher"] = 10012

        json_object = json.dumps(pair, indent = 4) 

        try:
            get_app()
            ref = db.reference("/storage/")
            ref.push(json_object)
            stat = 1
        except:
            stat = 0


        if stat == 1:
            self.ui.logs_box.append("Upload Success")
            self.ui.uploadData_statusText.setText("Success")
            self.ui.uploadData_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 16px;")
        else: 
            self.ui.logs_box.append("Upload Failed")
            self.ui.uploadData_statusText.setText("Failed")
            self.ui.uploadData_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 16px;;")

    # display a new window containing the fetched info from DB
    def showFetched(self, fetched):
        #construct it
        self.fetchedWindow = QMainWindow()
        self.fetchedUI = fetchedData_Window()
        self.fetchedUI.setupUi(self.fetchedWindow)

        # Add rows
        for data0 in fetched:
            #format it to be able to convert to dict
            data1 = data0.replace("\n","")
            data2 = data1.replace(":"," :")
            data3 = data2.replace("    ","")

            data_dict = json.loads(data3)
            self.fetchedUI.addRow(data_dict)

        # Buttons    
        self.fetchedUI.OK_btn.clicked.connect(self.checkChosen)
        self.fetchedUI.Cancel_btn.clicked.connect(lambda: self.checkChosen(isCancel=True))

        # display it
        self.fetchedWindow.show()

    def checkChosen(self, isCancel):

        if isCancel:
            self.fetchedWindow.close()
            return
        
        # loop through to find chosen row contents
        collectChosen = {}
        for obj in self.fetchedUI.scrollArea.children():
            if (obj.objectName() == 'qt_scrollarea_viewport'):
                rows = obj.children()[0].children()
                for i in range(1, len(rows)):
                    if rows[i].objectName().startswith("chosen#"):
                        if rows[i].isChecked():
                            arr = rows[i].objectName().split("#")
                            index = int(arr[len(arr)-1])
                            collectChosen["Modulus"] = rows[i-2].text()
                            collectChosen["Cipher"] = rows[i-1].text()
   
        # display the chosen
        self.chosenFetched = collectChosen
        if (self.chosenFetched != {}):

            self.N = self.chosenFetched["Modulus"]
            self.cipherText = self.chosenFetched["Cipher"]

            self.ui.ciphertext_text.setText(self.cipherText)
    
            self.ui.logs_box.append("Fetch Success")
            self.ui.fetch_statusText.setText("  Success")
            self.ui.fetch_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 14px;")
            
            self.fetchStatus = True
            self.ui.decryptMsg_btn.setEnabled(
                self.readStatus and self.fetchStatus)

        self.fetchedWindow.close()


if __name__ == '__main__':
    app = QApplication(sys.argv) 
    display = MainWindow()
    display.show()
    sys.exit(app.exec_())
