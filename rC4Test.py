    
def swap(S, i, j):
    """Swap the values at the specified indices in the given list."""
    S[i], S[j] = S[j], S[i]
    
def encrypt(plaintext, key):
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
        swap(S, i, j)
    
    # Pseudo-Random Generation Algorithm (PRGA) Phase
    i = j = 0
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        swap(S, i, j)
        # XOR the current character with the next keystream byte
        out.append(char ^ S[(S[i] + S[j]) % 256])
    
    text = ''.join('{:02x}'.format(x) for x in bytes(out))
    return text


def decrypt(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)
    plaintext = encrypt(ciphertext, key)
    plaintext = bytes.fromhex(plaintext)
    plaintext = plaintext.decode()
    return plaintext


# Example data and key (as strings)
data = 'Test me please'
key = 'Key'


# Encrypt the data using RC4
ciphertext = encrypt(data, key)

# Decrypt the ciphertext using RC4
plaintext = decrypt(ciphertext, key)


# Check that the original data and the decrypted plaintext match
if data == plaintext:
    print('Original = ', data, '| Decrypted = ', plaintext)

print('Encrypted ciphertext:', ciphertext)
print('Decrypted plaintext:', plaintext)
print('Test passed.')

