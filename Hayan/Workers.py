from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Key_Gen import *
import time
import os
import importlib
import sys


# import all Algorithms
package = 'Algorithms'
fileDirectory = os.path.dirname(__file__)
__modules__ = dict()
for file_name in os.listdir(f"{fileDirectory}\\{package}"):
    if file_name.endswith('.py') and file_name != '__init__.py':
        module_name = file_name[:-3]
        __modules__[module_name] = importlib.import_module(
            f"{package}.{module_name}", '.')


def getModules():
    return __modules__


class Fetch_Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        ...


class Upload_Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        ...


class RFID_Worker(QThread):
    '''RFID Working Thread Class'''
    ##### Signal for GUI Slots #####
    logsAppendSignal = pyqtSignal(str)
    finishedSignal = pyqtSignal(int, QThread)
    resultSignal = pyqtSignal(str)

    def __init__(self, rfid, tagData=None, op='Read'):
        super().__init__()

        self.rfid = rfid
        self.tagData = tagData
        self.op = op
        # set the signals for GUI communication
        self.rfid.setSignals(self.logsAppendSignal)

    @pyqtSlot()
    def run(self):
        '''The Main Process for the Thread'''
        if self.op == 'Read':
            stat = self.rfid.readKey()
            key = str(self.rfid.getKey())
            # print(f"THE KEY #{key}")
            # print(type(key))
            self.resultSignal.emit(key)
            self.finishedSignal.emit(stat, self)
        else:
            stat = self.rfid.writeKey(self.tagData)
            self.finishedSignal.emit(stat, self)


class KeyGen_Worker(QThread):
    '''Key Generator Worker Thread Class'''
    progressSignal = pyqtSignal(str)
    finishedSignal = pyqtSignal()
    resultSignal = pyqtSignal(int)

    def __init__(self, algo, bit_size):
        super().__init__()
        self.algo = algo
        self.bit_size = bit_size

    def run(self):
        # TODO some kind of progress indicator for long
        i = 0
        while (i != 2):
            self.progressSignal.emit(str(i))
            time.sleep(0.25)
            i += 1
        result = __modules__[self.algo].generateKey(self.bit_size)
        if __modules__[self.algo].isAsymmetric():
            self.resultSignal.emit(str(result[0][0]))
            self.finishedSignal.emit()
        else:
            self.resultSignal.emit(result)
            self.finishedSignal.emit()


class Cryptor_Worker(QThread):
    '''Working Thread Class'''
    progressSignal = pyqtSignal(int)
    finishedSignal = pyqtSignal()
    resultSignal = pyqtSignal(str)
    '''BLOCK MODE should be'''

    def __init__(self, block, algo, key):
        super().__init__()
        self.key = key
        # self.block = block(ECB, DES, Text)
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
                self.__modules__[module_name] = (
                    importlib.import_module(f"{self.package}.{module_name}", '.'))

    def setupAlgo(self, algo):
        '''Import Algorithm Modules'''
        self.algo = (importlib.import_module(f"{self.package}.{algo}", '.'))

    def run(self):
        '''The Main Process for the Thread'''
        result = self.crypto.encrypt_decrypt(self.block, self.key)
        self.finishedSignal.emit()
        self.resultSignal.emit(result)


if __name__ == "__main__":
    cryptor = KeyGen_Worker("RSA", 32)
    cryptor.start()
    # rsa = __modules__['RSA'].RSA()
    # rsa.makeKeyFiles('RSA_demo', 32)
    ...
