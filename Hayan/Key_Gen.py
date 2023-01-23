import random
import string

class Key_Gen:
    def __init__(self, bit_size):
        self.bit_size = bit_size

    def mix_key(self):
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=self.bit_size))
        return key

    def ltr_key(self):
        key = ''.join(random.choices(string.ascii_letters, k=self.bit_size))
        return key

    def num_key(self):
        key = ''.join(random.choices(string.digits, k=self.bit_size))
        return key

    def RSA_key(self):
        # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
        # window.logs_box.append('Generating p prime...')
        print('Generating p prime...')
        p = self.generateLargePrime()
        # window.logs_box.append('Generating q prime...')
        print('Generating q prime...')
        q = self.generateLargePrime()
        n = p * q
        # n = str(n)
        
        # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
        # window.logs_box.append('Generating e that is relatively prime to (p-1)*(q-1)...')
        print('Generating e that is relatively prime to (p-1)*(q-1)...')
        while True:
            e = random.randrange(2 ** (self.bit_size - 1), 2 ** (self.bit_size))
            if self.gcd(e, (p - 1) * (q - 1)) == 1:
                # e = str(e)
                break
        
        # Step 3: Calculate d, the mod inverse of e.
        # window.logs_box.append('Calculating d that is mod inverse of e...')
        print('Calculating d that is mod inverse of e...')
        d = self.findModInverse(e, (p - 1) * (q - 1))
        # d = str(d)
        privateKey = (e, n)
        publicKey = (d, n)
        # window.logs_box.append(f'Private key: {privateKey}')
        print('Private key:', privateKey)
        # window.logs_box.append(f'Public key:  {publicKey}')
        print('Public key:', publicKey)
        return (publicKey, privateKey)

    ####### HELPER METHODS FOR RSA ########
    def generateLargePrime(self):
        while True:
            num = random.randrange(2**(self.bit_size-1), 2**(self.bit_size))
            if self.isPrime(num):
                return num

    def gcd(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b

    def findModInverse(self, a, m):
        if self.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m

    def rabinMiller(self, num):
        s = num - 1
        t = 0
        
        while s % 2 == 0:
            s = s // 2
            t += 1
        for trials in range(5):
            a = random.randrange(2, num - 1)
            v = pow(a, s, num)
            if v != 1:
                i = 0
                while v != (num - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % num
            return True

    def isPrime(self, num):
        if (num < 2):
            return False
        lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
        67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
        251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349, 
        353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 
        457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
        571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 
        673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
        797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 
        911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        
        if num in lowPrimes:
            return True
        for prime in lowPrimes:
            if (num % prime == 0):
                return False
        return self.rabinMiller(num)

def test():
    keygen = Key_Gen(16)
    print(keygen.mix_key())
    print(keygen.num_key())
    print(keygen.ltr_key())
    print(keygen.RSA_key())

if __name__ == "__main__":
    test()