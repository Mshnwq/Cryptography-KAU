from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from block import Block
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
    resultSignal = pyqtSignal(str)
    finishedSignal = pyqtSignal(int, QThread)

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
    logsAppendSignal = pyqtSignal(str)
    resultSignal = pyqtSignal(str)
    finishedSignal = pyqtSignal()

    def __init__(self, algo, bit_size):
        super().__init__()
        self.algo = algo
        self.bit_size = bit_size

    def run(self):
        # TODO some kind of progress indicator for long
        i = 0
        while (i != 2):
            self.logsAppendSignal.emit(str(i))
            time.sleep(0.25)
            i += 1
        result = __modules__[self.algo].generateKey(self.bit_size)
        if __modules__[self.algo].isAsymmetric():
            self.resultSignal.emit(str(result[0][0]))
            self.finishedSignal.emit()
        else:
            self.resultSignal.emit(str(result))
            self.finishedSignal.emit()


class Cryptor_Worker(QThread):
    '''Working Crytor Thread Class'''
    logsAppendSignal = pyqtSignal(str)
    resultSignal = pyqtSignal(str)
    finishedSignal = pyqtSignal()


    def __init__(self, size, algo, mode, isEnc, text, key):
        '''
        Cryptor Worker Constructor
        Args:
            size (int): bit size of blocks
            algo (str): encryption or decryption algorithm
            mode (str): mode of block
            isEnc (bool): is Encryption, else Decryption
            text (str): text to encrypt or decrypt
            key (str): algorithm key
        '''
        super().__init__()
        self.block = Block(size, algo, mode, isEnc, text, key)
        # self.crypto.setSignals() #TODO

    def run(self):
        '''The Main Process for the Thread'''
        result = self.block.run()
        # self.finishedSignal.emit()
        self.resultSignal.emit(result)
        self.finishedSignal.emit()


if __name__ == "__main__":
    cryptor = KeyGen_Worker("RSA", 32)
    cryptor.start()
    # rsa = __modules__['RSA'].RSA()
    # rsa.makeKeyFiles('RSA_demo', 32)
    ...
