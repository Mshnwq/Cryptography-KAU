import json
import platform
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Workers import *
from RFID_Driver import RFID
from firebase_admin import *
from firebase_admin import db
import assets.qrc
import importlib
import ctypes
import sys
import os
from functools import partial

# import all UI
package = 'UI'
fileDirectory = os.path.dirname(__file__)
__ui__ = dict()
for file_name in os.listdir(f"{fileDirectory}\\{package}"):
    if file_name.endswith('.py') and file_name.startswith('Ui_') and file_name != '__init__.py':
        module_name = file_name[:-3]
        print(f"{module_name[3:]}")
        __ui__[module_name[3:]] = importlib.import_module(
            f"{package}.{module_name}", '.')


class MainWindow(QMainWindow):
    '''GUI Class'''

    def __init__(self):
        '''MainWindow constructor'''
        super().__init__()

        # Window Setup
        self.setWindowIcon(QIcon(":seal"))

        self.rfid = None
        self._threads = []
        self.dialogType = 0

        # show choice window
        self.choiceWindow()

    def logout(self):
        self.choiceWindow()
        # self.clear() # TODO clear any data

    def choiceWindow(self):
        self.ui = __ui__['Choice'].construct()
        self.ui.setupUi(self)

        self.ui.BrdMode_btn.clicked.connect(self.broadcastMode)
        self.ui.BrdMode_txt.clicked.connect(self.broadcastMode)
        self.ui.RcvMode_btn.clicked.connect(self.receiveMode)
        self.ui.RcvMode_txt.clicked.connect(self.receiveMode)

    def broadcastMode(self):
        # construct the window
        self.ui = __ui__['Broadcast'].construct()
        with open(fileDirectory+'\\Broadcast'+'_config.json', 'r') as file:
            config = json.load(file)
        self.ui.setupUi(self, config)

        # Generate keys
        self.ui.genKeys_btn.clicked.connect(self.generateKeys)

        # Write Key
        if (self.ui.keyWrAction.isChecked() and self.checkRFID()):  # onto RFID
            self.ui.writeKey_btn.clicked.connect(self.writeKey)
        else:  # onto .txt
            self.ui.writeKey_btn.clicked.connect(self.saveKey)

        # Encrpyt the plaintext
        # if self.ui.encrypSrcAction.isChecked():
        if False:  # Hardware Encrypt
            # TODO an fpga encrypt
            ...
        else:  # Software Encrypt
            self.ui.encryptMsg_btn.clicked.connect(self.encrypt)

        # Upload data to backend
        if self.ui.broadcastSrcAction.isChecked() and self.checkCloud():  # use cloud
            self.ui.uploadData_btn.clicked.connect(self.sendData)
        else:  # use .txt
            self.ui.uploadData_btn.clicked.connect(self.saveData)

        # Clear logs
        self.ui.clearLogs_btn.clicked.connect(
            lambda: self.ui.logs_box.setPlainText(""))

        # disable buttons
        self.ui.encryptMsg_btn.setEnabled(False)
        self.ui.writeKey_btn.setEnabled(False)
        self.ui.uploadData_btn.setEnabled(False)

        # Key Generation Source action
        self.ui.keyGenAction.triggered.connect(
            lambda: self.ui.logs_box.append("Key Gen on FPGA Later"))
        # Key Write action
        self.ui.keyWrAction.triggered.connect(lambda: self.toggle_rfid('Wr'))
        # Encryption Source action
        self.ui.encrypSrcAction.triggered.connect(
            lambda: self.logs_box.append("Encryption on FPGA Later"))
        # Broadcast Source action
        self.ui.broadcastSrcAction.triggered.connect(
            lambda: self.toggle_Cloud('Up'))
        # Save Broadcast Configuration action
        self.ui.saveConfigAction.triggered.connect(self.saveBroadcastConfig)
        # logout action
        self.ui.logoutAction.triggered.connect(self.logout)

    def receiveMode(self):
        # construct the window
        self.ui = __ui__['Receive'].construct()
        with open(fileDirectory+'\\Receive'+'_config.json', 'r') as file:
            config = json.load(file)
        self.ui.setupUi(self, config)

        # Fetch keys
        self.fetchStatus = False
        if (self.ui.fetchSrcAction.isChecked() and self.checkCloud()):  # from Cloud
            self.ui.fetch_btn.clicked.connect(self.fetchData)
        else:  # from .txt
            self.ui.fetch_btn.clicked.connect(self.txtRdHelper)

        # Read Key
        self.readStatus = False
        if (self.ui.keyRdAction.isChecked() and self.checkRFID()):  # from RFID
            self.ui.readKey_btn.clicked.connect(self.readKey)
        else:  # from.txt
            self.ui.readKey_btn.clicked.connect(self.readKeyTxt)

        # Decrpyt the plaintext
        self.ui.decryptMsg_btn.clicked.connect(self.decrypt)

        # Clear logs
        self.ui.clearLogs_btn.clicked.connect(
            lambda: self.ui.logs_box.setPlainText(""))

        # disable buttons
        self.ui.decryptMsg_btn.setEnabled(False)

        # Fetch Source action
        self.ui.fetchSrcAction.triggered.connect(
            lambda: self.toggle_Cloud('Ft'))
        # Key Read action
        self.ui.keyRdAction.triggered.connect(lambda: self.toggle_rfid('Rd'))
        # Decryption Source action
        self.ui.decrypSrcAction.triggered.connect(
            lambda: self.ui.logs_box.append("Decryption on FPGA Later"))
        # Save Broadcast Configuration action
        self.ui.saveConfigAction.triggered.connect(self.saveReceiveConfig)
        # logout action
        self.ui.logoutAction.triggered.connect(self.logout)

    def logsAppend(self, data):
        '''Append a text to the logs box'''
        self.ui.logs_box.append(data)

    def checkRFID(self, mode):
        try:  # connect RFID
            self.rfid = RFID()
            return True
        except Exception as e:
            self.rfid = None
            dialog = QMessageBox()
            dialog.setWindowTitle(f"Error Occured with RFID")
            dialog.setText(f"Details: {e}")
            dialog.setIcon(QMessageBox.Critical)
            dialog.setInformativeText(f"Make sure RFID is connected")
            dialog.setStandardButtons(QMessageBox.Ok)
            dialog.exec_()
            if mode == 'Wr':
                self.ui.keyWrAction.setChecked(False)
            else:
                self.ui.keyRdAction.setChecked(False)
            return False

    def checkCloud(self, mode):
        try:  # connect to cloud
            cred = credentials.Certificate(
                fileDirectory + '\\ee495-military-cryptology-firebase-adminsdk-b4q79-7de77dd092.json')
            self.default_app = initialize_app(cred,
                                                {
                                                "databaseURL": "https://ee495-military-cryptology-default-rtdb.firebaseio.com/"
                                                }
                                                )
            get_app()
            self.ref = db.reference("/storage/")
            print("Cloud Connected ")
            return True
        except Exception as e:
            self.ref = None
            dialog = QMessageBox()
            dialog.setWindowTitle(f"Error Occured with Cloud")
            dialog.setText(f"Details: {e}")
            dialog.setIcon(QMessageBox.Critical)
            dialog.setInformativeText(f"Make sure Internet is connected")
            dialog.setStandardButtons(QMessageBox.Ok)
            dialog.exec_()
            if mode == 'Up':
                self.ui.broadcastSrcAction.setChecked(False)
            else:
                self.ui.fetchSrcAction.setChecked(False)
            return False

    def toggle_rfid(self, mode):
        # Connect the button to the appropriate function based on the toggle state
        if mode == 'Wr':
            if self.ui.keyWrAction.isChecked() and self.checkRFID(mode):
                self.ui.writeKey_btn.clicked.disconnect()
                self.ui.writeKey_btn.clicked.connect(self.writeKey)
            else:
                self.ui.writeKey_btn.clicked.disconnect()
                self.ui.writeKey_btn.clicked.connect(self.saveKey)
        else:
            if self.ui.keyRdAction.isChecked() and self.checkRFID(mode):
                self.ui.readKey_btn.clicked.disconnect()
                self.ui.readKey_btn.clicked.connect(self.readKey)
            else:
                self.ui.readKey_btn.clicked.disconnect()
                self.ui.readKey_btn.clicked.connect(self.readKeyTxt)

    def toggle_Cloud(self, mode):
        # Connect the button to the appropriate function based on the toggle state
        if mode == 'Up':
            if self.ui.broadcastSrcAction.isChecked() and self.checkCloud(mode):
                self.ui.uploadData_btn.clicked.disconnect()
                self.ui.uploadData_btn.clicked.connect(self.sendData)
            else:
                delete_app(self.default_app)
                self.ui.uploadData_btn.clicked.disconnect()
                self.ui.uploadData_btn.clicked.connect(self.saveData)
        else:
            if self.ui.fetchSrcAction.isChecked() and self.checkCloud(mode):
                self.ui.fetch_btn.clicked.disconnect()
                self.ui.fetch_btn.clicked.connect(self.fetchData)
            else:
                delete_app(self.default_app)
                self.ui.fetch_btn.clicked.disconnect()
                self.ui.fetch_btn.clicked.connect(self.txtRdHelper)

    def saveData(self):
        name = fileDirectory+'\\Data\\'+str(self.__key__)+"_cipher.txt"
        content = self.ui.plaintext_box.toPlainText()
        self.txtWrHelper(name, content)

        self.ui.logs_box.append("Save Success")
        self.ui.uploadData_statusText.setText("Success")
        self.ui.uploadData_statusText.setStyleSheet(
            "color: rgb(0,200,0);\nfont: bold 16px;")

    def saveKey(self):
        name = fileDirectory+'\\Key\\'+str(self.__key__)+'.txt'
        content = str(self.__key__)
        self.txtWrHelper(name, content)
        print(type(self.__key__))
        self.ui.logs_box.append("Save Key Success")
        self.ui.writeKey_statusText.setText("Key Saved")
        self.ui.writeKey_statusText.setStyleSheet(
            "color: rgb(0,200,0);\nfont: bold 14px;")
        self.ui.logs_box.append(f'(int) saved: {self.__key__}')
        self.ui.logs_box.append(f'(hex) saved: {hex(self.__key__)}')
        self.ui.logs_box.append(f'(bin) saved: {bin(self.__key__)}')

    def saveBroadcastConfig(self):
        data = {
            "FPGA_gen": self.ui.keyGenAction.isChecked(),
            "RFID_wr": self.ui.keyWrAction.isChecked(),
            "FPGA_crypt": self.ui.encrypSrcAction.isChecked(),
            "Cloud": self.ui.broadcastSrcAction.isChecked()
        }
        try:
            with open(fileDirectory+'\\Broadcast_config.json', 'w') as file:
                json.dump(data, file, indent=4)
            self.ui.logs_box.append("Settings updated successfully")
        except Exception as e:
            print(f"An error occurred while saving config file: {e}")

    def saveReceiveConfig(self):
        data = {
            "Cloud": self.ui.fetchSrcAction.isChecked(),
            "RFID_rd": self.ui.keyRdAction.isChecked(),
            "FPGA_crypt": self.ui.decrypSrcAction.isChecked()
        }
        try:
            with open(fileDirectory+'\\Receive_config.json', 'w') as file:
                json.dump(data, file, indent=4)
            self.ui.logs_box.append("Settings updated successfully")
        except Exception as e:
            print(f"An error occurred while saving config file: {e}")

    def generateKeys(self):

        # Create a worker thread
        bitSize = self.getBitSizeChosen()
        key_worker = KeyGen_Worker(self.getAlgoChosen(), bit_size=bitSize)

        # Connect signals & slots
        key_worker.resultSignal.connect(self.storeKey)
        key_worker.progressSignal.connect(self.logsAppend)
        key_worker.finishedSignal.connect(lambda:
                                          self.finishedKeyGen(key_worker))

        # Start the worker
        key_worker.start()
        self._threads.append(key_worker)
        self.update_threads()

    def update_threads(self):
        # self.logsAppend(f"threads now {self._threads}")
        active_threads = len(
            [thread for thread in self._threads if thread.isRunning()])
        self.ui.statusbar.showMessage(f"Active Threads: {active_threads}")

    def storeKey(self, __key__):
        # print(f"STORING {__key__}")
        self.__key__ = __key__

    def finishedKeyGen(self, key_worker):
        key_worker.terminate()
        self._threads.remove(key_worker)
        self.update_threads()
        self.logsAppend("Key Generated: " + str(self.__key__))
        self.ui.key_box.setText(self.fitNumber(
            str(self.__key__), 20))
        self.ui.writeKey_btn.setEnabled(True)
        self.ui.encryptMsg_btn.setEnabled(True)
        self.logsAppend("Key Generation Success")
        self.ui.genKeys_statusText.setText("Keys Generated")
        self.ui.genKeys_statusText.setStyleSheet(
            "color: rgb(0,200,0);\nfont: bold 10px;")

    def fitNumber(self, num, width):
        # helper method for fitting number into a box
        fit = ''
        leng = len(num)
        for i in range(leng):
            fit += num[i]
            if ((i+1) % width == 0):
                fit += "\n"
        return fit

    def getBitSizeChosen(self):
        return int(self.ui.bitSize_combo.currentText())

    def getAlgoChosen(self):
        return self.ui.algoType_combo.currentText()

    def readKey(self):

        # if self.getBitSizeChosen() > 64:
        #     dialog = QMessageBox()
        #     dialog.setText(f"Cannot Read {self.getBitSizeChosen()} bit key on tag")
        #     dialog.setWindowTitle("Invalid Key Bit Size!")
        #     dialog.setIcon(QMessageBox.Critical)
        #     dialog.setInformativeText(f"Choose a Key Bit Size of 128 or lower")
        #     dialog.setStandardButtons(QMessageBox.Ok)
        #     dialog.exec_()
        #     return None

        self.ui.readKey_btn.setEnabled(False)
        self.dialogType = 1

        # Create a worker thread
        rfid_worker = RFID_Worker(self.rfid, op='Read')

        # Connect signals & slots
        rfid_worker.resultSignal.connect(self.storeKey)
        rfid_worker.logsAppendSignal.connect(self.logsAppend)
        rfid_worker.finishedSignal.connect(partial(self.readKeyStatus))

        # Start the worker
        rfid_worker.start()
        self._threads.append(rfid_worker)
        self.update_threads()

    def readKeyStatus(self, stat, rfid_worker):
        rfid_worker.terminate()
        self._threads.remove(rfid_worker)
        self.update_threads()
        self.ui.readKey_btn.setEnabled(True)
        if (stat == 1):
            self.ui.logs_box.append("Read Key Success")
            self.ui.readKey_statusText.setText("   Success")
            self.ui.readKey_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 14px;")
            # self.key = self.rfid.getKey()
            self.ui.logs_box.append(f'(int) read: {int(self.__key__)}')
            self.ui.logs_box.append(f'(hex) read: {hex(int(self.__key__))}')
            self.ui.logs_box.append(f'(bin) read: {bin(int(self.__key__))}')
            stringKey = self.fitNumber(str(self.__key__), 20)
            self.ui.scanned_box.setText(stringKey)
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
            dialog.setInformativeText(
                "Place only 1 key only infront of reader")
            dialog.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
            dialog.buttonClicked.connect(self.dialogClicked)
            dialog.exec_()

    def writeKey(self):

        if self.getBitSizeChosen() > 128:
            dialog = QMessageBox()
            dialog.setWindowTitle("Invalid Key Bit Size!")
            dialog.setText(
                f"Cannot Write {self.getBitSizeChosen()} bit key on tag")
            dialog.setIcon(QMessageBox.Critical)
            dialog.setInformativeText(f"Choose 128 bit or lower")
            dialog.setStandardButtons(QMessageBox.Ok)
            dialog.exec_()
            return None

        self.ui.writeKey_btn.setEnabled(False)
        self.dialogType = 2

        # TODO FAISAL initialize data
        tagData = bytearray(16)
        self.keyToWriteInt = int(self.__key__)
        # self.keyToWriteInt = 1945954
        keyToWrite = self.keyToWriteInt.to_bytes(16, byteorder='big')

        for i in range(0, len(keyToWrite)):
            tagData[i] = keyToWrite[i]

        # Create a worker thread
        rfid_worker = RFID_Worker(self.rfid, tagData, op='Write')

        # Connect signals & slots
        rfid_worker.logsAppendSignal.connect(self.logsAppend)
        rfid_worker.finishedSignal.connect(partial(self.writeKeyStatus))

        # Start the worker
        rfid_worker.start()
        self._threads.append(rfid_worker)
        self.update_threads()

    def writeKeyStatus(self, stat, rfid_worker):
        rfid_worker.terminate()
        self._threads.remove(rfid_worker)
        self.update_threads()
        self.ui.writeKey_btn.setEnabled(True)
        if (stat == 1):
            self.ui.logs_box.append("Write Key Success")
            self.ui.writeKey_statusText.setText("Key Issued")
            self.ui.writeKey_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 14px;")
            self.ui.logs_box.append(f'(int) written: {self.__key__}')
            self.ui.logs_box.append(f'(hex) written: {hex(self.__key__)}')
            self.ui.logs_box.append(f'(bin) written: {bin(self.__key__)}')
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
            dialog.setInformativeText(
                "Place only 1 key only infront of reader")
            dialog.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
            dialog.buttonClicked.connect(self.dialogClicked)
            dialog.exec_()

    def dialogClicked(self, btn):
        if(self.dialogType == 2 and btn.text() == 'Retry'):
            self.writeKey()
        if(self.dialogType == 1 and btn.text() == 'Retry'):
            self.readKey()

    def encrypt(self):

        plainTextString = self.ui.plaintext_box.toPlainText()
        nchars = len(plainTextString)
        # string to int or long. Type depends on nchars
        plainTextInt = sum(
            ord(plainTextString[byte]) << 8*(nchars-byte-1) for byte in range(nchars))
        print(plainTextInt)
        # plainTextHex = hex(plainTextInt)[2::]
        # print(plainTextHex)

        # encrypting # TODO
        # stat = self.fpga.encrypt_decrypt(plainTextInt, self.rsa.getE(), self.rsa.getN())
        # self.cipherTextInt = cipherTextInt

        # cipherTextString = ''.join(chr((cipherTextInt>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))
        # int or long to string
        # self.ui.ciphertext_text.setText(cipherTextString)
        # self.ui.ciphertext_text.setText(str(cipherTextInt))
        stat = 1
        if stat == 1:
            self.ui.logs_box.append("Encryption Success")
            self.ui.encryptMsg_statusText.setText("Success")
            self.ui.encryptMsg_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 16px;")
            # out = self.fpga.getOut()
            # pln = self.fitNumber(out, 20)
            self.ui.ciphertext_text.setText("edvrvrbvewb")
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
        cipherTextInt = int(self.ui.ciphertext_text.toPlainText())
        # print(cipherTextInt)
        # # plainTextHex = hex(plainTextInt)[2::]
        # # print(plainTextHex)

        # decrypting # TODO
        # stat = self.fpga.encrypt_decrypt(cipherTextInt, self.key, self.n)
        # self.plainTextInt = plainTextInt

        # plainTextString = ''.join(chr((plainTextInt>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))
        # # int or long to string
        # self.ui.plaintext_text.setText(plainTextString)
        stat = 1
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
        # pair["Modulus"] = self.rsa.getN()
        pair["Cipher"] = 66661211

        json_object = json.dumps(pair, indent=4)

        try:
            self.ref.push(json_object)
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

    def showFetched(self, fetched):
        '''display a new window containing the fetched info from DB'''
        # construct it
        self.fetchedWindow = QMainWindow()
        self.fetchedUI = __ui__["Fetch"].construct()
        self.fetchedUI.setupUi(self.fetchedWindow)

        # Add rows
        for data0 in fetched:
            # format it to be able to convert to dict
            data1 = data0.replace("\n", "")
            data2 = data1.replace(":", " :")
            data3 = data2.replace("    ", "")

            data_dict = json.loads(data3)
            self.fetchedUI.addRow(data_dict)

        # Buttons
        self.fetchedUI.OK_btn.clicked.connect(self.checkChosen)
        self.fetchedUI.Cancel_btn.clicked.connect(
            lambda: self.checkChosen(isCancel=True))

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

    def txtWrHelper(self, file_name, text):
        try:
            with open(file_name, "w") as file:
                file.write(text)
            print(f"Successfully wrote {file_name}")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    def txtRdHelper(self):
        # TODO
        print("FILLLL")
        ...

    def readKeyTxt(self):
        # TODO
        print("TODODOODO")
        ...

    def establishUART(self):
        # TODO ABDULLAH HELP
        print("kaka")
        ...

        # self.fpga = FPGA() # create instance of RFID

        # stat = 1

        # if stat == 1:
        #     # self.ui.logs_box.append("FPGA UART Success")
        #     self.ui.FPGA_statusText.setText("  Success")
        #     self.ui.FPGA_statusText.setStyleSheet(
        #         "color: rgb(0,200,0);\nfont: bold 16px;")
        #     self.ui.GenMode_btn.setEnabled(True)
        #     self.ui.AttMode_btn.setEnabled(True)
        # else:
        #     # self.ui.logs_box.append("FPGA UART Failed")
        #     self.ui.FPGA_statusText.setText("Failed")
        #     self.ui.FPGA_statusText.setStyleSheet(
        #         "color: rgb(250,0,0);\nfont: bold 16px;;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
