from base64_encoder import Base64Encoder
from token_service import TokenService


class UrlShortener:
    def __init__(self):
        self.x = "something"
        self.token_service = TokenService()
        self.encoder = Base64Encoder()
        self.db = {}

    def get_short_url(self, long_url):
        token = self.token_service.get_unique_token()
        short_url = self.encoder.encode(str(token))
        self.db[short_url] = long_url
        return short_url
