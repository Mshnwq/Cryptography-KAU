

class FPGA:
##### Class Variables
    fOpenComIndex = None

##### Static Values
    ### FROM DATA SHEET
                # address # Baudrate # Scan Time 
    SETTINGS = [0xff,     0x06,      0x50]
    ZERO = 0

    # init method or constructor
    def __init__(self):

        ################################################################# Uncomment when you use the writer
        # self.__setup_dll()
        # self.openPort()
        # print("opened COM ", self.fOpenComIndex.value)
        # self.setDeviceSettings() # use when needed
        # self.getDeviceInfo() # use when needed
        # self.closePort() # use when needed
        ################################################################# Uncomment when you use the writer
        print("constructed FPGA")

    def encrypt_decrypt(self, text, exponant, modulus):
        # text = (text**exponant)%modulus
        #TODO
        if text == 0:
            return 0
        self.out = text
        return 1
    
    def getOut(self):
        return str(self.out)

if __name__ == "__main__":
    # simple text script
    print(__name__)
    
    # fpga = FPGA()
    # E = 13
    # D = 133
    # mod = 169
    # # plainTextString = "haya"
    # cipherTextString = "c"
    # # nchars = len(plainTextString)
    # xchars = len(cipherTextString)

    # # string to int or long. Type depends on nchars
    # # plainTextInt = sum(ord(plainTextString[byte])<<8*(nchars-byte-1) for byte in range(nchars))
    # cipherTextInt = sum(ord(cipherTextString[byte])<<8*(xchars-byte-1) for byte in range(xchars))
    # # print(plainTextInt)
    # print(cipherTextInt)

    # # cipherTextInt = fpga.encrypt_decrypt(plainTextInt, E, mod)
    # # print(cipherTextInt)
    # # cipherTextString = ''.join(chr((cipherTextInt>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))
    # # print(cipherTextString)
    
    # plainTextInt = fpga.encrypt_decrypt(cipherTextInt, D, mod)
    # print(plainTextInt)
    # plainTextString = ''.join(chr((plainTextInt>>8*(xchars-byte-1))&0xFF) for byte in range(xchars))
    # print(plainTextString)
    # print("dd")
