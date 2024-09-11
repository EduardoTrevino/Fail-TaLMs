import unittest
from api import get_cat_facts

class TestCatFactsAPI(unittest.TestCase):
    
    def test_get_cat_facts(self):
        response = get_cat_facts()
        self.assertIsInstance(response, list)
        if response:
            for fact in response:
                self.assertIn('text', fact)

if __name__ == '__main__':
    unittest.main()