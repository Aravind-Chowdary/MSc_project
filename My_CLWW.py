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
    ct1 =()
    for i in m:
        ab += i
        ct1 += str((f(ab[:-1], k) + int(ab[-1])) % 3)
    return ct1


def ore_compare(ct1, ct2, st):
    if  ct1!=ct2:
        return 0
    else :
        return 1
