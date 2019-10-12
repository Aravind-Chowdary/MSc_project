import unittest
from random_word import RandomWords


from Popa_cli import enc, dec, key_gen, init_vect
from Popa_ser import OPETree


class SimpleTestCase(unittest.TestCase):
    key = key_gen()
    iv= init_vect()
    OPETree=OPETree.new()

    def testConsistency(self):
        m = RandomWords()
        m.get_random_word()
        c = enc(self.k,self.iv, m)
        d = dec(self.k,self.iv, c)
        assert d == m



if __name__ == "__main__":
    unittest.main()
