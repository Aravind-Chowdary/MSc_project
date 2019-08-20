
from random import randrange


def key_gen(l):
    k=randrange(2**l,2**(l+1))
    return k


def enc(k, m):
    r=randrange(k**0.75,k-k**0.75)
    c=m*k+r
    return c


def dec(k, c):
    return c/k


