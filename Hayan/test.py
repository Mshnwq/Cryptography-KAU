hexStr = '686920686179616e0000000000000000'
b = bytes.fromhex(hexStr)
s = b.decode("utf-8")
print(s)
s = s.replace("\x00", "")
b = s.encode("utf-8")
print(b)