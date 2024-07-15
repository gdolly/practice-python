class TokenService:
    def __init__(self):
        self.start = 0
        self.end = 1000
        self.last_token = self.start

    def get_unique_token(self):
        self.last_token += 1
        return self.last_token
