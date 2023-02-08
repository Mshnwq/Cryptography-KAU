import random, sys, os

class RSA:

   def __init__(self):
      print("constrcuted RSA")

   def decrypt(self, text, exponant, modulus):
      exponant = int(exponant)
      modulus = int(modulus)
      # print(f"TEXT before decode {text}")
      text = int(text)
      # print(f"TEXT after decode {text}")
      result = (text**exponant)%modulus
      resultHex = hex(result)
      resultStr = bytes.fromhex(resultHex[2:]).decode()
      return resultStr
   
   def encrypt(self, text, exponant, modulus):
      exponant = int(exponant)
      modulus = int(modulus)
      print(f"TEXT before encode {text}")
      text = int(text.encode().hex(),16)
      print(f"TEXT after encode {text}")
      result = (text**exponant)%modulus
      # print(f"TEXT after code {text}")
      return str(result)

def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

def findModInverse(a, m):
   if gcd(a, m) != 1:
      return None
   u1, u2, u3 = 1, 0, a
   v1, v2, v3 = 0, 1, m
   
   while v3 != 0:
      q = u3 // v3
      v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
   return u1 % m

def rabinMiller(num):
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

def isPrime(num):
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
   return rabinMiller(num)

def generateLargePrime(keysize):
   while True:
      num = random.randrange(2**(keysize-1), 2**(keysize))
      if isPrime(num):
         return num

##################### for GUI FAISAL

def getKeyBitSizes():
   return ["16", "32", "64", "128"]

def generateKey(keySize = 64):
   keySize = keySize/2
   # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
   print('Generating p prime...')
   p = generateLargePrime(keySize)
   print('Generating q prime...')
   q = generateLargePrime(keySize)
   n = p * q
   phi = (p-1) * (q-1)
   
   # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
   print('Generating e that is relatively prime to (p-1)*(q-1)...')
   while True:
      e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
      if gcd(e, phi) == 1:
         # e = str(e)
         break
   
   # Step 3: Calculate d, the mod inverse of e.
   print('Calculating d that is mod inverse of e...')
   d = findModInverse(e, phi)
   privateKey = (d, n)
   publicKey = (e, n)
   # window.logs_box.append(f'Private key: {privateKey}')
   print('Private key:', privateKey)
   # window.logs_box.append(f'Public key:  {publicKey}')
   print('Public key:', publicKey)
   return (privateKey, publicKey)

def makeKeyFiles(name, keySize):
   # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' 
   #(where x is the value in name) with the the n,e and d,e integers written in them,
   # delimited by a comma.
   if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
      sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))
   privateKey, publicKey  = generateKey(keySize)
   
   print('The private key is a %s and a %s digit number.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
   print('Writing private key to file %s_privkey.txt...' % (name))
   
   fo = open('%s_privkey.txt' % (name), 'w')
   fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
   fo.close()
   
   print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1])))) 
   print('Writing public key to file %s_pubkey.txt...' % (name))
   
   fo = open('%s_pubkey.txt' % (name), 'w')
   fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
   fo.close()

def isAsymmetric():
   return True

def construct():
   return RSA()

def main():
   key = generateKey(16)
   message = "Hi"
   rsa = RSA()

   ciph = rsa.encrypt(message, key[0][0], key[0][1])
   print(f"CIPH is {ciph}")
   # ciph = ciph.encode('utf-8').decode('utf-8')
   # print(f"CIPH is {ciph}")
   plain = rsa.decrypt(ciph, key[1][0], key[1][1])
   print(f"Plain is {plain}")
   # print(f"Plain decode {plain}")

   # makeKeyFiles('RSA_demo', 64)

if __name__ == '__main__':
   main()