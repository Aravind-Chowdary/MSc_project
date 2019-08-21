from random import randrange

t=''
p=1**t
f=k*(n*{0,1}**n-1)


def key_gen(p):
    k=randrange(f)
    return k


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
