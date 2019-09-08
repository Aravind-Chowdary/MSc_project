import unittest
import random

from My_CLWW import *


class SimpleTestCase(unittest.TestCase):
    k = key_gen()

    def testOrderPreserving(self):
        m1 = random.randint(1, 65535)
        m2 = random.randint(1, 65535)
        c1 = ore_enc(self.k, m1)
        c2 = ore_enc(self.k, m2)
        if m1 < m2:
            assert ore_compare(ct1,ct2)==-1
        if m1 > m2:
            assert ore_compare(ct1,ct2)==1
        if m1==m2:
            assert ore_compare(ct1,ct2)==0



if __name__ == "__main__":
    unittest.main()
