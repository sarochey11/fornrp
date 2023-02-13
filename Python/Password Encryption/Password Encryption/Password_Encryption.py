
from Crypto.Cipher import AES
import os

key = b'Sixteen byte key'

def encrypt_file(in_file, out_file, key):
    # create a new AES cipher
    cipher = AES.new(key, AES.MODE_EAX)

    # encrypt the plaintext
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(in_file.read())

    # write the ciphertext and the nonce to the output file
    [ out_file.write(x) for x in (nonce, ciphertext, tag) ]

with open('plaintext.txt', 'rb') as in_file, open('ciphertext.bin', 'wb') as out_file:
    encrypt_file(in_file, out_file, key)
