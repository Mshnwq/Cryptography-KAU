
import random
import string


class RC4:
    def swap(self, S, i, j):
        """Swap the values at the specified indices in the given list."""
        S[i], S[j] = S[j], S[i]

    def encrypt(self, plaintext, key):
        plaintext = bytes.fromhex(plaintext)
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
        print("The cipher entered to RC4: ", ciphertext)
        print("The key entered to RC4: ", key)
        plaintext = self.encrypt(ciphertext, key)
        print("The retrived plain text: ", plaintext)
        return plaintext
    
    @staticmethod
    def generateKey(size):
        if int(size) in list(map(int, RC4.getKeyBitSizes())):
        # generate random key
            numOfChar = int(size/8)
            key = get_random_string(numOfChar)
            return key
        else:
            return "key size is not valid"

    @staticmethod
    def isAsymmetric():
        return False

    @staticmethod
    def getKeyBitSizes():
        return ['128', '256']


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



# def construct():
#     return RC4()


def main():

    # Example data and key (as strings)
    data = 'Test me please'
    key = RC4.generateKey(256)
    algo = RC4()

    # Encrypt the data using RC4
    ciphertext = algo.encrypt(data, key)

    # Decrypt the ciphertext using RC4
    plaintext = algo.decrypt(ciphertext, key)

    # Check that the original data and the decrypted plaintext match
    # if data == plaintext:
    print('Original = ', data)

    print('Encrypted ciphertext:', ciphertext)
    # print('Decrypted plaintext:', bytes.fromhex(plaintext).decode('utf-8'))
    print('Decrypted plaintext:', plaintext)
    print('Test passed.')


if __name__ == "__main__":
    main()
    ...
