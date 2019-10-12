import unittest



from Kerschbaum import calc_max,  n, T, encrypt, reencrypt


class SimpleTestCase(unittest.TestCase):
    n==13
    T=={}
    max=calc_max(10)

    def testConsistency(self):
        x='sunil'
        c = encrypt(x,'gary',6,max)
        d = reencrypt(None,x,-1,calc_max(10))
        assert d ==x




if __name__ == "__main__":
    unittest.main()
