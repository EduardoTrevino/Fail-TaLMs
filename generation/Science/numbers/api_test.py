import unittest
from api import get_number_fact, get_batch_number_facts

class TestNumbersAPI(unittest.TestCase):

    def test_get_number_fact(self):
        response = get_number_fact(number='42', type='trivia', json=True)
        self.assertIn('text', response)
        self.assertEqual(response['number'], 42)
        self.assertEqual(response['type'], 'trivia')

    def test_get_random_number_fact(self):
        response = get_number_fact(number='random', json=True)
        self.assertIn('text', response)

    def test_get_year_fact(self):
        response = get_number_fact(number='1969', type='year', json=True)
        self.assertIn('text', response)
        self.assertEqual(response['number'], 1969)
        self.assertEqual(response['type'], 'year')

    def test_get_date_fact(self):
        response = get_number_fact(number='2/29', type='date', json=True)
        self.assertIn('text', response)
        self.assertEqual(response['type'], 'date')

    def test_get_batch_number_facts(self):
        response = get_batch_number_facts(numbers='1..3', json=True)
        self.assertEqual(len(response), 3)
        self.assertIn('1', response)
        self.assertIn('2', response)
        self.assertIn('3', response)

if __name__ == '__main__':
    unittest.main()