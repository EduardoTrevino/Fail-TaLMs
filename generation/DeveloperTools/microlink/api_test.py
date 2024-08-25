import unittest
from api import retrieve_metadata, take_screenshot, filter_data, execute_custom_query

class TestMicrolinkAPI(unittest.TestCase):

    def test_retrieve_metadata(self):
        response = retrieve_metadata('https://github.com')
        self.assertEqual(response['status'], 'success')
        self.assertIn('data', response)
    
    def test_take_screenshot(self):
        response = take_screenshot('https://github.com')
        self.assertEqual(response['status'], 'success')
        self.assertIn('data', response)
    
    def test_filter_data(self):
        response = filter_data('https://news.ycombinator.com', 'url,title')
        self.assertEqual(response['status'], 'success')
        self.assertIn('data', response)
        self.assertIn('title', response['data'])
    
    def test_execute_custom_query(self):
        custom_params = {'adblock': False, 'audio': True}
        response = execute_custom_query('https://www.youtube.com', custom_params)
        self.assertEqual(response['status'], 'success')
        self.assertIn('data', response)


if __name__ == '__main__':
    unittest.main()