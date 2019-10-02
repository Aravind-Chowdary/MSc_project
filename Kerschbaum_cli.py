import struct
from binarytree import tree
import Crypto.Random
from Crypto.Hash import HMAC,SHA256
import math
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

    struct tree()
        tree.left = None
        tree.right =None
        k=None
        l=None
        __root = None


    def enc (x,t,min,max,n ):

        r=math.log(2,n)
        p=2**r
        if (x==t.x):
            k = Crypto.Random.random.randint(0, 1)
        else:
            k=None
        if (x>t.x or k==1):

            if (t.right!= None):
                return enc(x,t,max,min)
            elif (max-t.x<2):
                return rebalance (x,-1,n)
            t.right =HMAC.new(x,t.l,max-t.l/2,digestmod=SHA256)
            return t.right.l
        if (x<t.l or k==0):
            if (t.left!= None):
                return enc(x,t.left,min,t.l)
            elif (t.l-min<2):
                return rebalance(x,-1,p)
            t.left=tree(x,min+(t.l-min/2))


    def rebalance (x,min,max):
        T={t}
        X={t.x}.union({x})
        sorted(X)
        y=T.x
    def dec

