from random import randrange
import pycrypto


def key_gen(p):
    k=randrange()
    return k


def pre(sk, m):
    h=Hmac.new(sk,m,digestmod=SHA256)
    return h.digestmod()


def ore_enc(k, m):
    ab = ""
    ct =()
    for i in m:
        ab += i
        ct += str((f(ab[:-1], k) + int(ab[-1])) % 3)
    return ct


def ore_compare(ct, ct1):
    if  ct!=ct1:
        return 0
    else :
        return 1
