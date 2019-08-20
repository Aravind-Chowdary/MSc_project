import unittest
import random


from Dyer import key_gen, enc, dec


class SimpleTestCase(unittest.TestCase):
    k = key_gen(48)

    def testConsistency(self):
        m = random.randint(1, 65535)
        c = enc(self.k, m)
        d = dec(self.k, c)
        assert d == m

    def testOrderPreserving(self):
        m1 = random.randint(1, 65535)
        m2 = random.randint(1, 65535)
        c1 = enc(self.k, m1)
        c2 = enc(self.k, m2)
        if m1 < m2:
            assert c1 < c2
        if m1 > m2:
            assert c1 > c2
        assert True


if __name__ == "__main__":
    unittest.main()
