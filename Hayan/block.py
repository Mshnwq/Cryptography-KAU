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


def padding(self, plain):
    pass


class Block:

    def __init__(self, blockSize, algorithm, isEnc, plainText, Key):
        self.blockSizeHex = int(blockSize/4)  # block size in hex digot
        self.isEnc = isEnc
        self.algorithm = getModules()[algorithm].construct()
        self.KeyHex = hex(Key)[2:]
        print("keyhex :", self.KeyHex)
        self.plainTextHex = plainText.encode().hex()
        # the IV key for the enc dec size if the block zise is 64 take the first 64bit
        #  else take it all
        self.IV = "4226452948404D635166546A576E5A72"  # hix formate
        self.makeBlocks()

    def makeBlocks(self):
        textSize = len(self.plainTextHex)
        print(f"plain text size: {textSize}")
        print(f"block size: {self.blockSizeHex}")
        if textSize < self.blockSizeHex :
            for i in range(textSize, self.blockSizeHex ):
                self.plainTextHex += "0"
        elif textSize > self.blockSizeHex  and textSize % self.blockSizeHex  != 0:
            for i in range(textSize, 
                        (textSize + (self.blockSizeHex  - textSize % self.blockSizeHex ))):
                self.plainTextHex += "0"

    # TODO check the text if it is rquired for it to be coverted
    # to hex befor being xord with the iv key
    def a2Hex(self, text):
        return text.encode().hex()

    def run(self):
        cipher = ""
        # take the first block of the array of plaintext
        plain_0 = self.plainTextHex[:self.blockSizeHex]

        # TODO : check if the DES and AES have same name of fucntion for encryption,
        #  else it is required to make an if statment for each added encryption
        print(f"plain_0: {plain_0}")
        print(f"IV: {self.IV[:self.blockSizeHex]}")
        initialBlock = int(self.IV[:self.blockSizeHex], 16) ^ int(plain_0, 16)
        initialBlock = hex(initialBlock)[2:].zfill(self.blockSizeHex)
        print(f"initialBlock: {initialBlock}")
        if self.isEnc:
            ciph_0 = self.algorithm.encrypt(initialBlock, self.KeyHex)  # TODO: change it to self.key
        else:
            ciph_0 = self.algorithm.decrypt(initialBlock, self.KeyHex)  # TODO: change it to self.key
            
        print(f"Cipered: {ciph_0}")
        # cipher += ciph_0

        # ciph_new = ciph_0
        # after the first block every block is xorded with the previous block
        # for i in range(1, int(len(self.plainTextHex) / self.blockSizeHex)):
        #     # will slic the array for th required block size
        #     plain_i = self.plainTextHex[i*self.blockSizeHex: i*self.blockSizeHex + self.blockSizeHex]
        #     print(f"Block#{i}: {plain_i}")
        #     # TODO : decide the nu,ber of round
        #     if self.isEnc:
        #         ciph_i = self.algorithm.encrypt(plain_i, self.KeyHex)
        #     else:
        #         ciph_i = self.algorithm.decrypt(plain_i, self.KeyHex)

        #     print(f"Cipered: {ciph_i}")
        #     #xor previous block with current
        #     xored = hex(int(ciph_new, 16) ^ int(ciph_i, 16))
        #     # add the blcok to thr array
        #     print(f"XORED: {xored}\n")
        #     cipher += xored

        #     # set the new cipher to xor with plain text
        #     ciph_new = xored

        return cipher

######################################
##########################IF  Encrypt DES ############
        # if (self.Enc_Dec == "DES"):

        #     # take the first block of the array of plaintext
        #     plain_1 = self.palinText[:self.blockSizeHex]

        #     # TODO : check if the DES and AES have same name of fucntion for encryption
        #     #  else it is required to make an if statment for eachadded encryption
        #     # ciph_1 = self.Enc_Dec().encrypt("faisaljabushanab", "abc1234567890123", None)

        #     xor = self.xor(plain_1, self.IV[:self.blockSizeHex])

        #     # TODO : check the function in the des if its the correct formte
        #     ciph_1 = DES().encrypt(xor, self.Key, None)  # TODO: change it to self.key

        #     cipher += ciph_1

        #     ciph_new = ciph_1
        #     # after the first block every block is xorded with the previous block
        #     for i in range(1, len(self.plainText) // self.blockSizeHex):

        #         # will slic the array for th required block size
        #         plain_i = self.plainText[i *
        #                                  self.blockSizeHex: (i+1)*self.blockSizeHex]
        #         # TODO : decide the nu,ber of round
        #         ciph_i = DES().encrypt(ciph_new, plain_i, None)

        #         # add the blcok to thr array
        #         cipher += ciph_i

        #         # set the new cipher to xor with
        #         ciph_new = ciph_i

        #     return cipher

        return "error in cbc_Enc func of class Block ,, parameter must be either AES or DES "

#######################################################
#######################DECRYTION#######################
#######################################################
    # def decrypt(self, cipher):
    #     plainText = []

    #     if (self.Enc_Dec == "AES"):

    #         # take the first block of the array of plaintext
    #         ciph_1 = cipher[:self.blockSizeHex]

    #         dec_Out = self.algorithm.decrypt(ciph_1, self.Key)

    #         plain_1 = self.xor(dec_Out, self.IV[:self.blockSizeHex])

    #         plainText += plain_1

    #         ciph_new = ciph_1
    #         # after the first block every block is xorded with the previous block
    #         for i in range(1, len(cipher) // self.blockSizeHex):

    #             # will slic the array for th required block size
    #             ciph_i = cipher[i*self.blockSizeHex: (i+1)*self.blockSizeHex]
    #             dec_Out_i = self.algorithm.decrypt(ciph_i, self.Key)  # TODO : decide the nu,ber of round
    #             plain_i = self.xor(dec_Out_i, ciph_new)

    #             # add the blcok to thr array
    #             plainText += plain_i

    #             ciph_new = ciph_i

    #         return cipher

    #     if (self.Enc_Dec == "DES"):

    #         # take the first block of the array of plaintext
    #         ciph_1 = cipher[:self.blockSizeHex]

    #         # TODO : check the method for dec in DES
    #         dec_Out = DES().decrypt(ciph_1, self.Key)

    #         plain_1 = self.xor(dec_Out, self.IV[:self.blockSizeHex])

    #         plainText += plain_1

    #         ciph_new = ciph_1
    #         # after the first block every block is xorded with the previous block
    #         for i in range(1, len(cipher) // self.blockSizeHex):

    #             # will slic the array for th required block size
    #             ciph_i = cipher[i*self.blockSizeHex: (i+1)*self.blockSizeHex]
    #             # TODO : CHECK the name of dec func in DES
    #             dec_Out_i = DES().decrypt(ciph_i, self.Key)
    #             plain_i = self.xor(dec_Out_i, ciph_new)

    #             # add the blcok to thr array
    #             plainText += plain_i

    #             # set the new cipher block to be xor with
    #             ciph_new = ciph_i

    #         return cipher

    #     return "error in cbc_Dec func of class Block ,, parameter must be either AES or DES "
            
    def xor(self, a, b):
        ans = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                ans = ans + "0"
            else:
                ans = ans + "1"
        return ans


def main():
    keyInt = getModules()['AES'].generateKey(128)
    # key = "abc1234567890123"
    # keyInt = int(key, 16)
    block = Block(64, 'AES', True, "HEllo0 FAISAL", keyInt)
    print(block.KeyHex, " ", block.plainTextHex) 
    print(type(block.KeyHex), " ", type(block.plainTextHex))
    cipher = block.run()
    print(f"THE CIPHEEEEER {type(cipher)}")
    print(f"THE CIPHEEEEER {cipher}")


    # time.sleep(4)
    # plainBlock = Block(64, 'AES', False, cipher, keyInt)
    # palin = plainBlock.run()
    # print(f"THE PLAIN {palin}")
    # print(type(block.run()))
    # block.makeBlocks()
    # print("after")
    # print(block.KeyHex, " ", block.plainTextHex) 
    # print(type(block.KeyHex), " ", type(block.plainTextHex))
    

if __name__ == '__main__':
    main()