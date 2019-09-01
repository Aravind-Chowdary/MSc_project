from Crypto.Random import random
from Crypto.Cipher import AES


def key_gen():
    key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))


def init_vect():
    iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])


def enc(key, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = 'hello world 1234'  # <- 16 bytes
    encd = aes.encrypt(data)


def dec(key,encd, adec, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    decd = adec.decrypt(encd)