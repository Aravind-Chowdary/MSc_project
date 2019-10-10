import unittest



from Boldyreva import *


class SimpleTestCase(unittest.TestCase):
    OPE=OPE.new()
    OPE.generate_key()

    def testConsistency(self):
        plaintext=4916684
        c = OPE.encrypt(plaintext)
        d = OPE.decrypt(c)
        assert d == plaintext




if __name__ == "__main__":
    unittest.main()
