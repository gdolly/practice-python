import base64

class Base64Encoder:
    def encode(self, value):
        sample_string = value
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string
