from algorithims.DES import DES
import binascii

string = "HELdk;tsr".encode("utf-8")
string = string.hex()
enc = DES()
eny = enc.encrypt(string.upper(), "123456ABCD132536", "encrypt")

# decrypt
dec = enc.decrypt(eny, "123456ABCD132536")

print("original: ", string.upper())
print("encrypt : ", enc.bin2hex(eny))
print("decrypt : ", bytearray.fromhex(dec).decode())


