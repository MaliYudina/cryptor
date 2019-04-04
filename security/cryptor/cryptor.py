"""
Cryptor module makes all the magic to encrypt & decrypt the data received
from reader results:
string -> to binary string -> to encrypted
encrypted -> binary string -> string
"""
import nacl.secret
import nacl.utils
from reader.reader import Information


class Crypt:
    """
    Crypto process of raw data received from reader's module
    """
    def __init__(self, raw):
        # self.raw = Information.write_result()
        self.raw = raw

    def encrypt(self, raw):  # куда пихать ключ открытый и закрытый??

        key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)  # secret key

        # box to store the encrypt or decrypt messages
        box = nacl.secret.SecretBox(key)

        # Encrypt our message, it will be exactly 40 bytes longer than the
        #   original message as it stores authentication information and the
        #   nonce alongside it.
        encrypted = box.encrypt(raw)
        my_key_as_hex = encrypted.hex()
        my_key = bytes(my_key_as_hex, "utf-8")
        print(my_key)
        print(encrypted)

    def decrypt(self):
        pass

    encrypt(self=None, raw=b'Hello')
    # decrypt()



