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


def calc_max(l):

