from random import randrange

t=''
p=1**t
f=k*(n*{0,1}**n-1)


def key_gen(p):
    k=randrange(f)
    return k


def ore_enc(k, m):
    tmp_m = ""
    tmpres = ""
    for i in m:
        tmp_m += i
        tmpres += str((f(tmp_m[:-1], k) + int(tmp_m[-1])) % 3)
    return tmpres
