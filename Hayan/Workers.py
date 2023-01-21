from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import os
import importlib
import sys

package = 'Algorithms'
fileDirectory = os.path.dirname(__file__)
__modules__ = dict()
for file_name in os.listdir(f"{fileDirectory}\\{package}"):
    if file_name.endswith('.py') and file_name != '__init__.py':
        module_name = file_name[:-3]
        __modules__[module_name] = importlib.import_module(f"{package}.{module_name}", '.')

class Cloud_Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        ...


class RFID_Worker(QThread):
    '''RFID Working Thread Class'''
    ##### Signal for GUI Slots #####
    insertSignal = pyqtSignal(object)
    sendingRequestSignal = pyqtSignal(int)
    gateStatusSignal = pyqtSignal(int)
    logsAppendSignal = pyqtSignal(str)
    clearSignal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        # create instance of checkpoint gate
        # self.checkPointGate = CheckPoint(GATE_ID, BUFFER_SIZE, TIMEOUT, TIME_WINDOW, POLLING_CONTROL_TIME)
        # set the signals for GUI communication
        self.checkPointGate.setSignals (self.insertSignal,
                                        self.sendingRequestSignal,
                                        self.gateStatusSignal,
                                        self.logsAppendSignal,
                                        self.clearSignal)

    @pyqtSlot()
    def run(self):
        '''The Main Process for the Thread'''
        while self.checkPointGate.getGateStatus() != 0:
            time.sleep(0.2)
            self.checkPointGate.process_RFID_batch()


class Key_Worker(QThread):
    progressSignal = pyqtSignal(int)
    finishedSignal = pyqtSignal()
    resultSignal = pyqtSignal(str)

    def __init__(self, algo, size):
        super().__init__()
        self.size = size
        self.constructCrypto(algo)

    def constructCrypto(self, algo):
        self.crypto = __modules__[algo].construct()

    def run(self):
        print("ssssss")
        result = self.crypto.generateKey(self.size)
        print(result)
        self.finishedSignal.emit()
        self.resultSignal.emit(result)


class Cryptor_Worker(QThread):
    '''Working Thread Class'''
    progressSignal = pyqtSignal(int)
    finishedSignal = pyqtSignal()
    resultSignal = pyqtSignal(str)

    def __init__(self, block, algo, key):
        super().__init__()
        self.key = key
        self.block = block
        # self.package = 'Algorithms'
        # self.fileDirectory = os.path.dirname(__file__)
        # if algo == None:
        #     self.setupAllAlgos()
        # else:
        #     self.setupAlgo(algo)
        self.constructCrypto(algo)
        # self.crypto.setSignals() #TODO
    

    def constructCrypto(self, algo):
        self.crypto = __modules__[algo].construct()
        # match(algo):
            # case algo == "RSA":
                # self.crypto = 

    def setupAllAlgos(self):
        '''Import All Algorithms Modules'''
        self.__modules__ = dict()
        for file_name in os.listdir(f"{self.fileDirectory}\\{self.package}"):
            if file_name.endswith('.py') and file_name != '__init__.py':
                module_name = file_name[:-3]
                self.__modules__[module_name] = (importlib.import_module(f"{self.package}.{module_name}", '.'))

    def setupAlgo(self, algo):
        '''Import Algorithm Modules'''
        self.algo = (importlib.import_module(f"{self.package}.{algo}", '.'))

    def run(self):
        '''The Main Process for the Thread'''
        result = self.crypto.encrypt_decrypt(self.block, self.key)
        self.finishedSignal.emit()
        self.resultSignal.emit(result)


if __name__ == "__main__":
    cryptor = Key_Worker("RSA", 32)
    cryptor.start()
    # rsa = __modules__['RSA'].RSA()
    # rsa.makeKeyFiles('RSA_demo', 32)
    ...
