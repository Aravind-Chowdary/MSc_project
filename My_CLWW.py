from Crypto.Random import random
from Crypto.Hash import HMAC,SHA256


def key_gen():
    k=random.get_random_bytes(64)
    return k


def pre(k, m):
    h=HMAC.new(k,m,digestmod=SHA256)
    return h.digestmod()


def ore_enc(k, m, h):
    ab = ""
    ct1 =()
    for i in m:
        ab += i
        ct1 += str((h(ab[:-1], k) + int(ab[-1])) % 3)
    return ct1


def ore_compare(ct1, ct2, st):
    if  ct1<ct2:
        return 0
    else :
        return 1
