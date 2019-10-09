import unittest



from Boldyreva import *


class SimpleTestCase(unittest.TestCase):
    generate_key()

    def testConsistency(self):
        plaintext='aravind'
        c = encrypt(plaintext)
        d = decrypt(ciphertext)
        assert d == plaintext




if __name__ == "__main__":
    unittest.main()
