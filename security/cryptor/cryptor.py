"""
Cryptor module makes all the magic to encrypt & decrypt the data received
from reader results:
string -> to binary string -> to encrypted
encrypted -> binary string -> string
"""
from cryptography.fernet import Fernet
from reader.reader import Reader




class Crypt:
    """
    Crypto process of raw data received from reader's module
    """

    def __init__(self, raw):
        self.raw = Reader.write_result()

    def encrypt(self, raw):
        key = Fernet.generate_key()
        f = Fernet(key)
        token = f.encrypt(b"A really secret message. Not for prying eyes.")
        print(token)
        pass

    def decrypt(self):
        f.decrypt(token)
