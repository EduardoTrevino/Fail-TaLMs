import unittest
from api import (
    get_version, 
    get_fields, 
    get_all_characters, 
    get_characters_by_radical,
    get_strokes,
    get_sounds_mandarin
)

class TestChineseCharacterWebAPI(unittest.TestCase):

    def test_get_version(self):
        result = get_version()
        self.assertIsInstance(result, dict)
        self.assertIn('phpVersion', result)

    def test_get_fields(self):
        result = get_fields()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_get_all_characters(self):
        result = get_all_characters(filter='gb', fields='kDefinition,kMandarin', count=False)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_get_all_characters_count(self):
        result = get_all_characters(filter='gb', count=True)
        self.assertIsInstance(result, dict)
        self.assertIn('count', result)

    def test_get_characters_by_radical(self):
        result = get_characters_by_radical(85, strokes=10)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_get_strokes(self):
        result = get_strokes()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_get_sounds_mandarin(self):
        result = get_sounds_mandarin(with_pitch=True)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()