import Crypto.Random
import math

MAX = None
n = None
T = None


class Tree:
    left = None
    right = None
    plain = None
    cipher = None

    def __init__(self, plain, cipher):
        self.left = None
        self.right = None
        self.plain = plain
        self.cipher = cipher


def get(t, plain):
    if t.plain == plain:
        return t
    else:
        l = None
        r = None
        if t.left is not None:
            l = t.get(t.left, plain)
        if t.right is not None:
            r = t.get(t.right, plain)
        if l is not None and r is not None:
            coin = Crypto.Random.random.randint(0, 1)
            if coin == 0:
                return l
            else:
                return r
        if l is not None:
            return l
        if r is not None:
            return r
        return None


def get_all_plaintexts(l, t):
    l.append(t.plain)
    if t.left is not None:
        get_all_plaintexts(l, t.left)
    if t.right is not None:
        get_all_plaintexts(l, t.right)
    return l


def calc_max(l):

    r = l * math.log(2, n)
    return 2**r

def encrypt(x, t, min, max):
    global MAX
    if x == t.plain:
        coin = Crypto.Random.random.randint(0, 1)
    else:
        coin = None
    if x > t.plain or coin == 1:
        if t.right is not None:
            return encrypt(x, t.right, t.cipher, max)
        else:
            if max - t.plain < 2:
                return rebalance(x, -1, n)
            t.right = Tree.new(x, t.cipher + math.ceil((max - t.cipher)/2.0))
            return t.right.cipher
    if x < t.plain or coin == 0:
        if t.left is not None:
            return encrypt(x, t.left, min, t.cipher)
        else:
            if t.cipher - min < 2:
                return rebalance(x, -1, MAX)
            t.left = Tree.new(x, min + math.ceil((t.cipher - min)/2.0))
            return t.left.cipher

def rebalance(x, min, max):
    global T
    X = get_all_plaintexts(T).append(x)
    X.sort()
    median = X[math.ceil(len(X)/2.0)]
    t = Tree.new(median, min + math.ceil((max-min)/2.0))
    reencrypt(t, X, min, max)
    T = t
    return get(t, x).cipher


def reencrypt(t, X, min, max):
    medianXidx = math.ceil(len(X)/2.0)
    X1 = X[0:medianXidx-1]
    X2 = X[medianXidx+1:]
    medianX1 = X[math.ceil(len(X1)/2.0)]
    medianX2 = X[math.ceil(len(X2)/2.0)]
    encrypt(medianX1, t, min, max)
    encrypt(medianX2, t, min, max)
    reencrypt(t, X1, min, max)
    reencrypt(t, X2, min, max)

def decrypt(median,t):
    if median>t.cipher:
        return decrypt(median,t.right)
    elif median<t.cipher:
        return decrypt(median.t.left)
    else :
        return t.plain