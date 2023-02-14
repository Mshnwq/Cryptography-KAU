
from pydantic import BaseModel
import importlib
import os
import time
# from multiprocessing import process
import multiprocessing
# import concurrent.futures
from Algorithms.Algorithm import EncModel


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


class Block(BaseModel):
    """
    Block Class
    Args:
        blockSize (int): bit size of blocks
        algo (str): encryption or decryption algorithm
        mode (str): mode of block
        isEnc (bool): is Encryption, else Decryption
        text (str): text to encrypt or decrypt
        key (str): algorithm key
    """
    blockSize: int
    algo: str
    mode: str
    isEnc: bool
    text: str
    key: str
    # other variables
    blockSizeByte = int(0)
    blockSizeHex = int(0)
    algorithm = object()  # TODO type
    textHex = ''
    IV = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blockSizeByte = int(self.blockSize / 8)
        self.blockSizeHex = int(self.blockSize / 4)
        self.algorithm = eval(f"getModules()[self.algo].{self.algo}()")
        if self.isEnc:  # in encrypt it is ascii
            self.textHex = self.text.encode().hex()
        else:  # already encoded hex
            self.textHex = self.text  # in decryption the message is already given in hex

        # the IV key for the enc dec size if the block zise is 64 take the first 64bit
        self.IV = "65787A736F64786B617373746A636164"  # hex format
        self.makeBlocks()

    def makeBlocks(self):
        print("plain before: "+self.textHex)
        textSize = len(self.textHex)
        # textSize is in hex digits
        if textSize < self.blockSizeHex:
            for i in range(textSize, self.blockSizeHex):
                self.textHex += "0"
        elif textSize > self.blockSizeHex and textSize % self.blockSizeHex != 0:
            for i in range(textSize,
                           (textSize + (self.blockSizeHex - textSize % self.blockSizeHex))):
                self.textHex += "0"
        print("plain after: "+self.textHex)

    def run(self):
        if self.mode == 'CBC':
            return self.cbc()
        else:
            return self.ecb()

    def cbc(self):
        cipher = ""
        # take the first block of the array of plaintext
        plain_0 = self.textHex[:self.blockSizeHex]
        #  else it is required to make an if statment for each added encryption
        print(f"IV: {self.IV[:self.blockSizeHex]}")
        # print("IV Size: ", len(self.IV[:self.blockSizeHex]))
        initialBlock = int(self.IV[:self.blockSizeHex], 16) ^ int(plain_0, 16)
        initialBlock = hex(initialBlock)[2:].zfill(self.blockSizeHex)
        if self.isEnc:
            print("initial block:", initialBlock, self.key)
            args = EncModel(**{"plainText": initialBlock,
                            "key": self.key, "isEncrypt": True})
            ciph_0 = self.algorithm.encrypt(args)
            ciph_new = ciph_0
        else:
            args = EncModel(**{"plainText": plain_0,
                            "key": self.key, "isEncrypt": False})
            ciph_0 = self.algorithm.decrypt(args)
            ciph_0 = hex(int(ciph_0, 16) ^ int(self.IV[:self.blockSizeHex], 16))[
                2:].zfill(self.blockSizeHex)
            ciph_new = plain_0
        print(f"initialBlock: {initialBlock}")

        print(f"Cipered: {ciph_0}")
        cipher += ciph_0

        # after the first block every block is xorded with the previous block
        # print("number of blocks: ",
        #   int(len(self.textHex) / self.blockSizeHex))
        for i in range(1, int(len(self.textHex) / self.blockSizeHex)):
            # will slic the array for th required block size
            plain_i = self.textHex[i*self.blockSizeHex: i *
                                   self.blockSizeHex + self.blockSizeHex]
            # print(f"Block#{i}: {plain_i}")
            xored = hex(int(ciph_new, 16) ^ int(plain_i, 16))[
                2:].zfill(self.blockSizeHex)
            # TODO : decide the nu,ber of round
            if self.isEnc:
                args = EncModel(**{"plainText": xored,
                                   "key": self.key, "isEncrypt": True})
                ciph_i = self.algorithm.encrypt(args)
                ciph_new = ciph_i
            else:
                args = EncModel(**{"plainText": plain_i,
                                   "key": self.key, "isEncrypt": False})
                ciph_i = self.algorithm.decrypt(args)
                ciph_i = int(ciph_i, 16) ^ int(ciph_new, 16)
                # print("xored with: " + ciph_new)
                ciph_i = hex(ciph_i)[2:].zfill(self.blockSizeHex)
                ciph_new = plain_i

            # print(f"Cipered: {ciph_i}")
            # xor previous block with current
            # add the blcok to thr array
            print(f"XORED: {xored}\n")
            cipher += ciph_i

            # set the new cipher to xor with plain text
            # ciph_new = ciph_i
        return cipher

    def ecb(self):
        cipher = ""
        start = time.perf_counter()
        for i in range(int(len(self.textHex) / self.blockSizeHex)):
            # will slic the array for th required block size
            plain_i = self.textHex[i*self.blockSizeHex: i *
                                   self.blockSizeHex + self.blockSizeHex]
            if self.isEnc:
                args = EncModel(**{"plainText": plain_i,
                                   "key": self.key, "isEncrypt": True})
                ciph_i = self.algorithm.encrypt(args)
            else:
                args = EncModel(**{"plainText": plain_i,
                                   "key": self.key, "isEncrypt": False})
                ciph_i = self.algorithm.decrypt(args)
            cipher += ciph_i
        finish = time.perf_counter()
        print(f'\nFinished in {round(finish-start, 2)} second(s)\n')
        return cipher

    # def ecb(self):
    #     '''ECB IN PARALLEL'''
    #     start = time.perf_counter()
    #     cipher = ""
    #     num_processes = multiprocessing.cpu_count()
    #     # print('###########')
    #     # print(num_processes)
    #     # print('###########')
    #     with multiprocessing.Pool(processes=num_processes) as pool:
    #         results = []
    #         for i in range(int(len(self.textHex) / self.blockSizeHex)):
    #             plain_i = self.textHex[i*self.blockSizeHex: i *
    #                                         self.blockSizeHex + self.blockSizeHex]
    #             result = pool.apply_async(self.ecb_worker, (plain_i, self.isEnc, self.algorithm, self.key))
    #             results.append(result)

    #         pool.close()
    #         pool.join()

    #     for result in results:
    #         cipher += result.get()

    #     finish = time.perf_counter()
    #     print(f'\nFinished in {round(finish-start, 2)} second(s)\n')
    #     return cipher

    def ecb_worker(self, plain_i, isEnc, algorithm, key):
        # print(f"Process #{plain_i} is running.")
        if isEnc:
            cipher = algorithm.encrypt(plain_i, key)
        else:
            cipher = algorithm.decrypt(plain_i, key)
        return cipher

# 4c


def main():
    # algo = 'RSA'
    # # key = getModules()[algo].RSA.generateKey(16)  # ascii string
    # key = ('43123$48443', '187$48443')
    message = "Faisal Jehad Abushanab"
    # # message = "Hi"
    # print("\n-------------(RSA - Enc - ECB)----------------")
    # # block = Block(blockSize=128, algo='RC4', mode='ECB', isEnc=True, text=message, key=key)
    # block = Block(blockSize=16, algo=algo, mode='CBC',
    #                 isEnc=True, text=message, key=key[0])
    # cipher = block.run()
    # print("plainHex is: " + message.encode().hex())
    # print("key is: " + key[0])
    # print("cipher is: " + cipher)
    # print("\n-------------(Decryption)----------------")
    # # block2 = Block(blockSize=128, algo='RC4', mode='ECB', isEnc=False, text=cipher, key=key)
    # block2 = Block(blockSize=16, algo=algo, mode='CBC',
    #                 isEnc=False, text=cipher, key=key[1])
    # orig = block2.run()
    # print("key is: " + key[1])
    # print("originalis: " + orig)
    # b = bytes.fromhex(orig)
    # s = b.decode("utf-8")
    # print(s)
    key = getModules()["RC4"].RC4.generateKey(64)
    print("\n-------------(AES - Enc - CBC)----------------")
    block = Block(blockSize=64, algo='DES', mode='ECB',
                  isEnc=True, text=message, key=key)
    cipher = block.run()
    print("key is: " + key)
    print("cipher is: " + cipher)

    print("-------------(Decryption)----------------")
    block2 = Block(blockSize=64, algo='DES', mode='ECB',
                   isEnc=False, text=cipher, key=key)
    orig = block2.run()
    print("key is: " + key)
    print("originalis: " + orig)

    # key = getModules()['DES'].generateKey(64)  # ascii string

    # # print("\n-------------(DES - Enc - ECB)----------------")
    # block = Block(64, 'DES', 'ECB', True, message, key)
    # cipher = block.run()
    # # print("key is: " + key)
    # # print("cipher is: " + cipher)

    # # print("-------------(Decryption)----------------")
    # block2 = Block(64, 'DES', 'ECB', False, cipher, key)
    # orig = block2.run()
    # # print("key is: " + key)
    # # print("originalis: " + orig)

    # # print("\n-------------(DES - Enc - CBC)----------------")
    # block = Block(64, 'DES', 'CBC', True, message, key)
    # cipher = block.run()
    # # print("key is: " + key)
    # # print("cipher is: " + cipher)

    # # print("-------------(Decryption)----------------")
    # block2 = Block(64, 'DES', 'CBC', False, cipher, key)
    # orig = block2.run()
    # # print("key is: " + key)
    # # print("originalis: " + orig)


if __name__ == '__main__':
    main()
