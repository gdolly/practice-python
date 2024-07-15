import unittest

from base64_encoder import Base64Encoder


class TestBase64Encode(unittest.TestCase):
    def test_encode_one(self):
        sut = Base64Encoder()
        self.assertEqual("MQ==", sut.encode("1"))

    def test_encode_two(self):
        sut = Base64Encoder()
        self.assertEqual("Mg==", sut.encode("2"))


if __name__ == '__main__':
    unittest.main()
