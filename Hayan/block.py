"""
add padding to the plain text
input: plain text in hex
output: plain text with padding in hex
"""
# import all Algorithms
import importlib
import os
import time


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


class Block:
    '''
    Block Class
    '''
    def __init__(self, blockSize, algo, mode, isEnc, text, key):
        '''
        Block Constructor
        Args:
            blockSize (int): bit size of blocks
            algo (str): encryption or decryption algorithm
            mode (str): mode of block
            isEnc (bool): is Encryption, else Decryption
            text (str): text to encrypt or decrypt
            key (str): algorithm key
        '''
        self.blockSizeByte = int(blockSize/8)  # block size in Bytes
        self.blockSizeHex = int(blockSize/4)  # block size in Bytes
        self.isEnc = isEnc
        self.isAsymmetric = getModules()[algo].isAsymmetric()
        self.algorithm = getModules()[algo].construct()
        self.key = key
        self.mode = mode            
        if isEnc: # in encrypt it is ascii
            self.textHex = text.encode().hex()
        else: # already encoded hex
            self.textHex = text  # in decryption the message is already given in hex

        # the IV key for the enc dec size if the block zise is 64 take the first 64bit
        self.IV = "65787A736F64786B617373746A636164"  # hix formate
        self.makeBlocks()

    def makeBlocks(self):
        # print("plain before: "+self.textHex)
        textSize = len(self.textHex)
        # textSize is in hex digits
        if textSize < self.blockSizeHex:
            for i in range(textSize, self.blockSizeHex):
                self.textHex += "0"
        elif textSize > self.blockSizeHex and textSize % self.blockSizeHex != 0:
            for i in range(textSize,
                        (textSize + (self.blockSizeHex - textSize % self.blockSizeHex))):
                self.textHex += "0"
        # print("plain after: "+self.textHex)

    def run(self):
        if self.mode == 'CBC':
            return self.cbc()
        else:
            return self.ecb()

    def cbc(self):
        cipher = ""
        # take the first block of the array of plaintext
        plain_0 = self.textHex[:self.blockSizeHex]
        # print("plain0 size: ", plain_0)
        # TODO : check if the DES and AES have same name of fucntion for encryption,
        #  else it is required to make an if statment for each added encryption
        # print(f"IV: {self.IV[:self.blockSizeHex]}")
        # print("IV Size: ", len(self.IV[:self.blockSizeHex]))
        initialBlock = int(self.IV[:self.blockSizeHex], 16) ^ int(plain_0, 16)
        initialBlock = hex(initialBlock)[2:].zfill(self.blockSizeHex)
        if self.isEnc:
            if self.isAsymmetric:
                ciph_0 = self.algorithm.encrypt(
                    initialBlock, self.key[0], self.key[0])
            else:
                ciph_0 = self.algorithm.encrypt(initialBlock, self.key)
            ciph_new = ciph_0
        else:
            if self.isAsymmetric:
                ciph_0 = self.algorithm.decrypt(
                    plain_0, self.key[0], self.key[0])
            else:
                ciph_0 = self.algorithm.decrypt(plain_0, self.key)
            ciph_0 = hex(int(ciph_0, 16) ^ int(self.IV[:self.blockSizeHex], 16))[
                2:].zfill(self.blockSizeHex)
            ciph_new = plain_0
        # print(f"initialBlock: {initialBlock}")

        # print(f"Cipered: {ciph_0}")
        cipher += ciph_0

        # after the first block every block is xorded with the previous block
        # print("number of blocks: ",
                # int(len(self.textHex) / self.blockSizeHex))
        for i in range(1, int(len(self.textHex) / self.blockSizeHex)):
            # will slic the array for th required block size
            plain_i = self.textHex[i*self.blockSizeHex: i *
                                        self.blockSizeHex + self.blockSizeHex]
            # print(f"Block#{i}: {plain_i}")
            xored = hex(int(ciph_new, 16) ^ int(plain_i, 16))[
                2:].zfill(self.blockSizeHex)
            # TODO : decide the nu,ber of round
            if self.isEnc:
                if self.isAsymmetric:
                    ciph_i = self.algorithm.encrypt(
                    xored, self.key[0], self.key[0])
                else:
                    ciph_i = self.algorithm.encrypt(xored, self.key)
                ciph_new = ciph_i
            else:
                if self.isAsymmetric:
                    ciph_0 = self.algorithm.decrypt(
                        plain_i, self.key[0], self.key[0])
                else:
                    ciph_0 = self.algorithm.decrypt(plain_i, self.key)
                ciph_i = int(ciph_i, 16) ^ int(ciph_new, 16)
                # print("xored with: " + ciph_new)
                ciph_i = hex(ciph_i)[2:].zfill(self.blockSizeHex)
                ciph_new = plain_i

            # print(f"Cipered: {ciph_i}")
            # xor previous block with current
            # add the blcok to thr array
            # print(f"XORED: {xored}\n")
            cipher += ciph_i

            # set the new cipher to xor with plain text
            # ciph_new = ciph_i
        return cipher

    def ecb(self):
        cipher = ""
        for i in range(int(len(self.textHex) / self.blockSizeHex)):
            # will slice the array for th required block size
            plain_i = self.textHex[i*self.blockSizeHex : 
                                    i*self.blockSizeHex + self.blockSizeHex]
            print(f"PLAIN{i} is {plain_i}")
            print(f"PLAIN{i} type {type(plain_i)}")
            if self.isEnc:
                if self.isAsymmetric:
                    ciph_i = self.algorithm.encrypt(
                        plain_i, self.key[0], self.key[0])
                else:
                    ciph_i = self.algorithm.encrypt(plain_i, self.key)
            else:
                if self.isAsymmetric:
                    ciph_i = self.algorithm.decrypt(
                        plain_i, self.key[0], self.key[0])
                else:
                    ciph_i = self.algorithm.decrypt(plain_i, self.key)
            print(f"adding {ciph_i}")
            cipher += ciph_i
        return cipher


def main():

    key = getModules()['RSA'].generateKey(16)  # ascii string
    # key = 'ozuqhdqvyveogvddaiwpwaoummcoxalx'  # ascii string
    message = "RSAA"
    print("\n-------------(RSA - Enc - ECB)----------------")
    block = Block(16, 'RSA', 'ECB', True, message, key[0])
    cipher = block.run()
    print(f"key is: {key[0]}")
    print("cipher is: " + cipher)

    print("-------------(Decryption)----------------")
    block2 = Block(16, 'RSA', 'ECB', False, cipher, key[1])
    print(f"key is: {key[1]}")
    orig = block2.run()
    print("originalis: " + orig)
    b = bytes.fromhex(orig)
    s = b.decode("utf-8")
    print(s)


    # print("\n-------------(AES - Enc - ECB)----------------")
    # block = Block(128, 'AES', 'ECB', True, message, key)
    # cipher = block.run()
    # print("key is: " + key)
    # print("cipher is: " + cipher)

    # print("-------------(Decryption)----------------")
    # block2 = Block(128, 'AES', 'ECB', False, cipher, key)
    # orig = block2.run()
    # print("key is: " + key)
    # print("originalis: " + orig)

    # print("\n-------------(AES - Enc - CBC)----------------")
    # block = Block(256, 'AES', 'CBC', True, message, key)
    # cipher = block.run()
    # print("key is: " + key)
    # print("cipher is: " + cipher)

    # print("-------------(Decryption)----------------")
    # block2 = Block(256, 'AES', 'CBC', False, cipher, key)
    # orig = block2.run()
    # print("key is: " + key)
    # print("originalis: " + orig)

    # key = getModules()['DES'].generateKey(64)  # ascii string

    # key = getModules()['DES'].generateKey(64)  # ascii string
    # message = "hi hayan DES"

    # print("\n-------------(DES - Enc - ECB)----------------")
    # block = Block(64, 'DES', 'ECB', True, message, key)
    # cipher = block.run()
    # print("key is: " + str(type(key)))
    # print("cipher is: " + cipher)

    # print("-------------(Decryption)----------------")
    # block2 = Block(64, 'DES', 'ECB', False, cipher, key)
    # orig = block2.run()
    # print("key is: " + key)
    # print("originalis: " + orig)

    # b = bytes.fromhex(orig)
    # s = b.decode("utf-8")
    # print(s)

    # key = getModules()['AES'].generateKey(256)
    # print("\n-------------(DES - Enc - CBC)----------------")
    # block = Block(256, 'DES', 'CBC', True, message, key)
    # cipher = block.run()
    # print("key is: " + key)
    # print("cipher is: " + cipher)

    # print("-------------(Decryption)----------------")
    # block2 = Block(256, 'DES', 'CBC', False, cipher, key)
    # orig = block2.run()
    # print("key is: " + key)
    # print("originalis: " + orig)
    
    ...


if __name__ == '__main__':
    main()
