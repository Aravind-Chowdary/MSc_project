import unittest
import random

from My_CLWW import *


class SimpleTestCase(unittest.TestCase):
    k = key_gen(48)

    def testConsistency(self):
        m = random.randint(1, 65535)
        c = ore_enc(self.k, m)
        d = ore_compare(self.k, c)
        assert d == m

    def testOrderPreserving(self):
        m1 = random.randint(1, 65535)
        m2 = random.randint(1, 65535)
        c1 = ore_enc(self.k, m1)
        c2 = ore_compare(self.k, m2)
        if m1 < m2:
            assert c1 < c2
        if m1 > m2:
            assert c1 > c2
        assert True


if __name__ == "__main__":
    unittest.main()
