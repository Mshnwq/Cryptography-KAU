
import random
import string


class RC4:
    def swap(S, i, j):
        """Swap the values at the specified indices in the given list."""
        S[i], S[j] = S[j], S[i]
        
    def encrypt(self, plaintext, key):
        if isinstance(plaintext, str):
            plaintext = plaintext.encode()
        key = key.encode()
        """Encrypt the input `data` using the key `key` using the RC4 algorithm."""
        # Initialize the state list
        S = list(range(256))
        j = 0
        out = bytearray()
        
        # Key-scheduling Algorithm (KSA) Phase
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256
            self.swap(S, i, j)
        
        # Pseudo-Random Generation Algorithm (PRGA) Phase
        i = j = 0
        for char in plaintext:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            self.swap(S, i, j)
            # XOR the current character with the next keystream byte
            out.append(char ^ S[(S[i] + S[j]) % 256])
        
        text = ''.join('{:02x}'.format(x) for x in bytes(out))
        return text
    def decrypt(self, ciphertext, key):
        ciphertext = bytes.fromhex(ciphertext)
        plaintext = self.encrypt(ciphertext, key)
        plaintext = bytes.fromhex(plaintext)
        plaintext = plaintext.decode()
        return plaintext



    


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
def generateKey(size):
    if int(size) in list(map(int, getKeyBitSizes())):
        # generate random key
        numOfChar = int(size/8)
        key = get_random_string(numOfChar)
        return key
    else:
        return "key size is not valid"


def getKeyBitSizes():
    return ["128", "256"]


def isAsymmetric():
    return False


def construct():
    return RC4()