"""
add padding to the plain text
input: plain text in hex
output: plain text with padding in hex
"""


def padding(self, plain):
    pass


class Block:

    def __init__(self, blockSize, algorithm, isEnc, plainText, Key):
        self.blockSize = int(blockSize/8)  # block size in byte
        # self.Enc_Dec = Enc_Dec
        self.algorithm = self.plainText = plainText
        self.Key = Key
        # the IV key for the enc dec size if the block zise is 64 take the first 64bit
        #  else take it all
        self.IV = ("4226452948404D635166546A576E5A72")  # hix formate

    # TODO check the text if it is rquired for it to be coverted
    # to hex befor being xord with the iv key
    def a2Hex(self, text):
        return text.encode().hex()

    def encrypt(self):
        cipher = ""
        plain = self.a2Hex(self.plainText)
        # take the first block of the array of plaintext
        plain_1 = plain[:self.blockSize]

        # TODO : check if the DES and AES have same name of fucntion for encryption,
        #  else it is required to make an if statment for each added encryption
        initialBlock = self.IV[:self.blockSize] ^ plain_1
        initialBlock = hex(initialBlock)[2:].zfill(self.blockSize*2)

        ciph_1 = AES().encrypt(initialBlock, self.Key, None)  # TODO: change it to self.key

        cipher += ciph_1

        ciph_new = ciph_1
        # after the first block every block is xorded with the previous block
        for i in range(1, len(self.plainText) / self.blockSize):

            # will slic the array for th required block size
            plain_i = self.plainText[i *
                                     self.blockSize: (i+1)*self.blockSize]
            # TODO : decide the nu,ber of round
            ciph_i = AES().encrypt(ciph_new, plain_i, None)

            # add the blcok to thr array
            cipher += ciph_i

            # set the new cipher to xor with plain text
            ciph_new = ciph_i

        return cipher

######################################
##########################IF  Encrypt DES ############
        # if (self.Enc_Dec == "DES"):

        #     # take the first block of the array of plaintext
        #     plain_1 = self.palinText[:self.blockSize]

        #     # TODO : check if the DES and AES have same name of fucntion for encryption
        #     #  else it is required to make an if statment for eachadded encryption
        #     # ciph_1 = self.Enc_Dec().encrypt("faisaljabushanab", "abc1234567890123", None)

        #     xor = self.xor(plain_1, self.IV[:self.blockSize])

        #     # TODO : check the function in the des if its the correct formte
        #     ciph_1 = DES().encrypt(xor, self.Key, None)  # TODO: change it to self.key

        #     cipher += ciph_1

        #     ciph_new = ciph_1
        #     # after the first block every block is xorded with the previous block
        #     for i in range(1, len(self.plainText) // self.blockSize):

        #         # will slic the array for th required block size
        #         plain_i = self.plainText[i *
        #                                  self.blockSize: (i+1)*self.blockSize]
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
    def decrypt(self, cipher):
        plainText = []

        if (self.Enc_Dec == "AES"):

            # take the first block of the array of plaintext
            ciph_1 = cipher[:self.blockSize]

            dec_Out = AES().decrypt(ciph_1, self.Key)

            plain_1 = self.xor(dec_Out, self.IV[:self.blockSize])

            plainText += plain_1

            ciph_new = ciph_1
            # after the first block every block is xorded with the previous block
            for i in range(1, len(cipher) // self.blockSize):

                # will slic the array for th required block size
                ciph_i = cipher[i*self.blockSize: (i+1)*self.blockSize]
                dec_Out_i = AES().decrypt(ciph_i, self.Key)  # TODO : decide the nu,ber of round
                plain_i = self.xor(dec_Out_i, ciph_new)

               # add the blcok to thr array
                plainText += plain_i

                ciph_new = ciph_i

            return cipher

        if (self.Enc_Dec == "DES"):

            # take the first block of the array of plaintext
            ciph_1 = cipher[:self.blockSize]

            # TODO : check the method for dec in DES
            dec_Out = DES().decrypt(ciph_1, self.Key)

            plain_1 = self.xor(dec_Out, self.IV[:self.blockSize])

            plainText += plain_1

            ciph_new = ciph_1
            # after the first block every block is xorded with the previous block
            for i in range(1, len(cipher) // self.blockSize):

                # will slic the array for th required block size
                ciph_i = cipher[i*self.blockSize: (i+1)*self.blockSize]
                # TODO : CHECK the name of dec func in DES
                dec_Out_i = DES().decrypt(ciph_i, self.Key)
                plain_i = self.xor(dec_Out_i, ciph_new)

               # add the blcok to thr array
                plainText += plain_i

                # set the new cipher block to be xor with
                ciph_new = ciph_i

            return cipher

        return "error in cbc_Dec func of class Block ,, parameter must be either AES or DES "

    def xor(self, a, b):
        ans = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                ans = ans + "0"
            else:
                ans = ans + "1"
        return ans
