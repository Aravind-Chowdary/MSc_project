import unittest



from Kerschbaum import calc_max, MAX, n, T, encrypt, reencrypt


class SimpleTestCase(unittest.TestCase):
    MAX==60
    n==13
    T=={}
    r=calc_max(10)

    def testConsistency(self):
        x='sunil'
        c = encrypt(x,'gary',6,MAX)
        d = reencrypt(None,x,-1,calc_max(10))
        assert d ==x




if __name__ == "__main__":
    unittest.main()
