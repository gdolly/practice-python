import hashlib
import unittest

from base64_encoder import Base64Encoder
from url_shortener import UrlShortener


class TestUrlShortner(unittest.TestCase):
    def test_url_shortener(self):
        sut = UrlShortener()
        actual = sut.get_short_url("hackerrank.com/blah")
        expected = "MQ=="
        
        url = 'http://xyz'
        md5_hash = hashlib.md5()
        md5_hash.update(url.encode('utf-8'))
        hexdigest = md5_hash.hexdigest()
        print(len(list(hexdigest)))
        digest = "".join(list(hexdigest)[0:43])
        print(digest)
        print(Base64Encoder().encode(digest))
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
