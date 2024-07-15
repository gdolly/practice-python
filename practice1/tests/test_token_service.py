import unittest

from token_service import TokenService


class TestTokenService(unittest.TestCase):
    def test_get_unique_token(self):
        sut = TokenService()
        self.assertEqual(sut.get_unique_token(), 1)
        self.assertEqual(sut.get_unique_token(), 2)
        self.assertEqual(sut.get_unique_token(), 3)

if __name__ == '__main__':
    unittest.main()