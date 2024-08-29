import unittest
from api import get_public_ip_v4, get_public_ip


class TestIpifyAPI(unittest.TestCase):

    def test_get_public_ip_v4_json(self):
        response = get_public_ip_v4()
        self.assertIn('ip', response)

    def test_get_public_ip_v4_text(self):
        response = get_public_ip_v4(format='text')
        self.assertIn('ip', response)

    def test_get_public_ip_json(self):
        response = get_public_ip()
        self.assertIn('ip', response)

    def test_get_public_ip_text(self):
        response = get_public_ip(format='text')
        self.assertIn('ip', response)


if __name__ == '__main__':
    unittest.main()