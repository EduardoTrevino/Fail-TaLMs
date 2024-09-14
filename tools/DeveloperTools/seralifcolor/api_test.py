import unittest
from api import get_color_info


class TestSeralifColorAPI(unittest.TestCase):

    def test_get_color_info_keyword(self):
        """Test get_color_info with a keyword."""
        result = get_color_info(color='aquamarine')
        self.assertEqual(result['status'], 'success')
        self.assertIn('base', result)

    def test_get_color_info_hex(self):
        """Test get_color_info with a HEX code."""
        result = get_color_info(color='556677')
        self.assertEqual(result['status'], 'success')
        self.assertIn('base', result)

    def test_get_color_info_rgb(self):
        """Test get_color_info with an RGB input."""
        result = get_color_info(color='85,102,119')
        self.assertEqual(result['status'], 'success')
        self.assertIn('base', result)

    def test_get_color_info_invalid(self):
        """Test get_color_info with an invalid color format."""
        result = get_color_info(color='yellou')
        self.assertEqual(result['status'], 'error')
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()