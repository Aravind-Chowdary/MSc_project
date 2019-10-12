from Crypto.Random import random
from Crypto.Cipher import AES
from Popa_ser import OPETree


def key_gen():
    key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))


def init_vect():
    iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])  # This needs to be involved in enc function(doubt)


def enc(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    # data = 'hello world 1234'   <- 16 bytes
    encd = aes.encrypt(data)
    OPETree.insert_in_tree.enc_val=encd
    return encd


def dec(key,encd, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    decd = aes.decrypt(encd)
    return decd