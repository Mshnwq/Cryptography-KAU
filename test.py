from algorithims.DES import DES
import binascii

string = "Faisal Abushanab"
enc = DES()
eny = enc.encrypt(string, "123456ABCD132536", "encrypt")
print("eny ", bytearray.fromhex(dec).decode())
# decrypt
# dec = enc.decrypt(eny, "123456ABCD132536")

# print("original: ", string.upper())
# print("encrypt : ", enc.bin2hex(eny))
# print("decrypt : ", bytearray.fromhex(dec).decode())
