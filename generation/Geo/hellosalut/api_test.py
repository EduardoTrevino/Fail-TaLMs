import unittest
from api import say_hello

class TestHelloSalutAPI(unittest.TestCase):
    
    def test_hello_with_language(self):
        response = say_hello(lang='ja')
        self.assertIn('hello', response)
    
    def test_hello_with_ip(self):
        response = say_hello(ip='89.120.120.120')
        self.assertIn('hello', response)
    
    def test_hello_with_country_code(self):
        response = say_hello(cc='nl')
        self.assertIn('hello', response)
    
    def test_hello_auto_mode(self):
        response = say_hello(mode='auto')
        self.assertIn('hello', response)

    def test_hello_with_no_params(self):
        response = say_hello()
        self.assertIn('hello', response)

if __name__ == '__main__':
    unittest.main()