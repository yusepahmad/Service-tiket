from ..core.s3 import S3

class Parsing(S3):
    def __init__(self):
        super().__init__()

    def convert_cookies(self, cookies):
        converted_cookies = []
        for name, value in cookies.items():
            converted_cookie = {
                'name': name,
                'value': value,
                'domain': '.tiket.com',
                'path': '/',
                'httpOnly': False,
                'secure': False
            }
            converted_cookies.append(converted_cookie)
        return converted_cookies