import Crypto.Random
from Kerschbaum_ser import *

class Node:
    __left=None
    __right=None
    __val=None

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert a new node with the given key


class Tree:
    __root = None


def key_gen():
    k=Crypto.Random.random.randint(0, 1)
    return k

def enc (x,t,min,max):
    if (t.right!= None):
        return enc(x,t,max,min)
    elif (max-t.x<2):
        return rebalance (x,-1,n)
        t.right =HMAC.new(x,t.l,)

def rebalance (x,min,max):


