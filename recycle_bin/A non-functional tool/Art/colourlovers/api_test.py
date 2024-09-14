import unittest
import json
from api import colors, color, palettes, palette, patterns, pattern, lovers, lover, stats

class TestColourLoversAPI(unittest.TestCase):

    def test_colors(self):
        response = colors(numResults=1, format="json")
        self.assertIsInstance(response, dict)

    def test_color(self):
        hex_value = "6B4106"
        response = color(hex_value, format="json")
        self.assertIsInstance(response, dict)

    def test_palettes(self):
        response = palettes(numResults=1, format="json")
        self.assertIsInstance(response, dict)

    def test_palette(self):
        palette_id = 113451
        response = palette(palette_id, format="json")
        self.assertIsInstance(response, dict)

    def test_patterns(self):
        response = patterns(numResults=1, format="json")
        self.assertIsInstance(response, dict)

    def test_pattern(self):
        pattern_id = 1451
        response = pattern(pattern_id, format="json")
        self.assertIsInstance(response, dict)

    def test_lovers(self):
        response = lovers(numResults=1, format="json")
        self.assertIsInstance(response, dict)

    def test_lover(self):
        username = "COLOURlover"
        response = lover(username, format="json")
        self.assertIsInstance(response, dict)

    def test_stats_colors(self):
        response = stats("colors", format="json")
        self.assertIsInstance(response, dict)

    def test_invalid_stat_resource(self):
        with self.assertRaises(ValueError):
            stats("invalid_resource")



if __name__ == "__main__":
    unittest.main()