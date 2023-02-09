
from pydantic import BaseModel
import importlib
import os
import time
# from multiprocessing import process
import multiprocessing
# import concurrent.futures


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
    algorithm = object()
    textHex = ''
    IV = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.blockSizeByte = int(self.blockSize / 8)
        self.blockSizeHex = int(self.blockSize / 4)
        self.algorithm = getModules()[self.algo].construct()
        if self.isEnc:  # in encrypt it is ascii
            self.textHex = self.text.encode().hex()
        else:  # already encoded hex
            self.textHex = self.text  # in decryption the message is already given in hex

        # the IV key for the enc dec size if the block zise is 64 take the first 64bit
        self.IV = "65787A736F64786B617373746A636164"  # hex format
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
        print(f"IV: {self.IV[:self.blockSizeHex]}")
        # print("IV Size: ", len(self.IV[:self.blockSizeHex]))
        initialBlock = int(self.IV[:self.blockSizeHex], 16) ^ int(plain_0, 16)
        initialBlock = hex(initialBlock)[2:].zfill(self.blockSizeHex)
        if self.isEnc:
            # TODO: change it to self.key
            ciph_0 = self.algorithm.encrypt(initialBlock, self.key)
            ciph_new = ciph_0
        else:
            # TODO: change it to self.key
            ciph_0 = self.algorithm.decrypt(plain_0, self.key)
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
                ciph_i = self.algorithm.encrypt(xored, self.key)
                ciph_new = ciph_i
            else:
                ciph_i = self.algorithm.decrypt(plain_i, self.key)
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

    # def do_act(self, blockStart):
    #     print(f"Thread #{blockStart} is running.")
    #     cipher = None
    #     plain_i = self.textHex[blockStart*self.blockSizeHex: blockStart *
    #                             self.blockSizeHex + self.blockSizeHex]
    #     if self.isEnc:
    #         cipher = self.algorithm.encrypt(plain_i, self.key)
    #     else:
    #         cipher = self.algorithm.decrypt(plain_i, self.key)
    #     return cipher

    # def ecb(self):

    #     cipher = ""
    #     numOfBlocks = int(len(self.textHex) / self.blockSizeHex)
    #     blockStart = [_ for _ in range(numOfBlocks)]
    #     start = time.perf_counter()
    #     with concurrent.futures.ThreadPoolExecutor() as executer:
    #         results = executer.map(self.do_act, blockStart)
    #     for result in results:
    #         cipher += result
    #     finish = time.perf_counter()
    #     print(f'Finished in {round(finish-start, 2)} second(s)')
    #     return cipher

    def ecb(self):
        cipher = ""
        start = time.perf_counter()
        for i in range(int(len(self.textHex) / self.blockSizeHex)):
            # will slic the array for th required block size
            plain_i = self.textHex[i*self.blockSizeHex: i *
                                   self.blockSizeHex + self.blockSizeHex]
            if self.isEnc:
                ciph_i = self.algorithm.encrypt(plain_i, self.key)
            else:
                ciph_i = self.algorithm.decrypt(plain_i, self.key)
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
    algo = 'RC4'
    key = getModules()[algo].generateKey(256)  # ascii string
    # message = "Cybersecurity is a critical issue in today's world, with more and more personal and business activities moving online. It refers to the protection of computer systems, networks, and data from unauthorized access, theft, damage, or destruction. The goal of cybersecurity is to ensure the confidentiality, integrity, and availability of sensitive information and systems. One of the most common forms of cyber attacks is hacking, where an attacker gains unauthorized access to a computer system or network. Another type of attack is phishing, where an attacker tricks a user into revealing sensitive information through emails or websites that appear to be from legitimate sources. Another common form of attack is malware, which is a type of software specifically designed to cause harm to a computer system. To prevent cyber attacks, it is important to adopt best practices such as keeping software and systems up-to-date, using strong passwords and multi-factor authentication, and being vigilant about email and website phishing scams. Additionally, organizations should implement firewalls, intrusion detection systems, and antivirus software to protect their networks and systems from cyber attacks. It is also important for individuals to take responsibility for their own cybersecurity. This includes being careful about what information they share online and being aware of the security of their personal. This progress report provides a summary of the Car-Park simulation project that has been underway since 2023/1/26. The goal of this project is to create and synchronize multi-threaded programs in Linux.. Over the past week, our team has made significant progress towards achieving this goal. This report will highlight our accomplishments, discuss any challenges we have faced, and outline our plans for the next stage of the project.devices, such as laptops and smartphones. Additionally, individuals should use encryption and virtual private networks(VPNs) when accessing sensitive information over public Wi-Fi networks. In conclusion, cybersecurity is a crucial aspect of our digital lives and requires a collective effort from individuals, organizations, and governments to ensure the protection of sensitive information and systems. Adopting best practices and being vigilant can help prevent cyber attacks and keep personal and business information secure. cybersecurity is a crucial aspect of our digital lives and requires a collective effort from individuals, organizations, and governments to ensure the protection of sensitive information and systems. Adopting best practices and being vigilant can help prevent cyber attacks and keep personal and business information secure. cybersecurity is a crucial aspect of our digital lives and requires a collective effort from individuals, organizations, and governments to ensure the protection of sensitive information and systems. Adopting best practices and being vigilant can help prevent cyber attacks and keep personal and business information secure."
    # message = "Cybersecurity is a critical issue in today's world, with more and more personal and business activities moving online. It refers to the protection of computer systems, networks, and data from unauthorized access, theft, damage, or destruction. The goal of cybersecurity is to ensure the confidentiality, integrity, and availability of sensitive information and systems. One of the most common forms of cyber attacks is hacking, where an attacker gains unauthorized access to a computer system or network. Another type of attack is phishing, where an attacker tricks a user into revealing sensitive information through emails or websites that appear to be from legitimate sources. Another common form of attack is malware, which is a type of software specifically designed to cause harm to a computer system. To prevent cyber attacks, it is important to adopt best practices such as keeping software and systems up-to-date, using strong passwords and multi-factor authentication, and being vigilant about email and website phishing scams. Additionally, organizations should implement firewalls, intrusion detection systems, and antivirus software to protect their networks and systems from cyber attacks. It is also important for individuals to take responsibility for their own cybersecurity. This includes being careful about what information they share online and being aware of the security of their personal. This progress report provides a summary of the Car-Park simulation project that has been underway since 2023/1/26. The goal of this project is to create and synchronize multi-threaded programs in Linux.. Over the past week, our team has made significant progress towards achieving this goal. This report will highlight our accomplishments, discuss any challenges we have faced, and outline our plans for the next stage of the project.devices, such as laptops and smartphones. Additionally, individuals should use encryption and virtual private networks(VPNs) when accessing sensitive information over public Wi-Fi networks. In conclusion, cybersecurity is a crucial aspect of our digital lives and requires a collective effort from individuals, organizations, and governments to ensure the protection of sensitive information and systems. Adopting best practices and being vigilant can help prevent cyber attacks and keep personal and business information secure. cybersecurity is a crucial aspect of our digital lives and requires a collective effort from individuals, organizations, and governments to ensure the protection of sensitive information and systems. Adopting best practices and being vigilant can help prevent cyber attacks and keep personal and business information secure. cybersecurity is a crucial aspect of our digital lives and requires a collective effort from individuals, organizations, and governments to ensure the protection of sensitive information and systems. Adopting best practices and being vigilant can help prevent cyber attacks and keep personal and business information secure."
    message = "ffffffffffffffffff"
    print("\n-------------(RC4 - Enc - ECB)----------------")
    # block = Block(blockSize=128, algo='RC4', mode='ECB', isEnc=True, text=message, key=key)
    block = Block(blockSize=256, algo=algo, mode='CBC',
                  isEnc=True, text=message, key=key)
    cipher = block.run()
    print("key is: " + key)
    print("cipher is: " + cipher)

    print("\n-------------(Decryption)----------------")
    # block2 = Block(blockSize=128, algo='RC4', mode='ECB', isEnc=False, text=cipher, key=key)
    block2 = Block(blockSize=256, algo=algo, mode='CBC',
                   isEnc=False, text=cipher, key=key)
    orig = block2.run()
    print("key is: " + key)
    print("originalis: " + orig)
    # b = bytes.fromhex(orig)
    # print(b.decode("utf-8"))

    # # print("\n-------------(AES - Enc - CBC)----------------")
    # block = Block(128, 'AES', 'CBC', True, message, key)
    # cipher = block.run()
    # # print("key is: " + key)
    # # print("cipher is: " + cipher)

    # # print("-------------(Decryption)----------------")
    # block2 = Block(128, 'AES', 'CBC', False, cipher, key)
    # orig = block2.run()
    # # print("key is: " + key)
    # # print("originalis: " + orig)

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
