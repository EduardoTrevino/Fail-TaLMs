import unittest
import json
from api import colors, color, palettes, palette, patterns, pattern, lovers, lover, stats

class TestColourLoversAPI(unittest.TestCase):

    def test_colors(self):
        response = colors()
        self.assertIsInstance(response, (dict, str))  # Depending on format, it can be a dict (JSON) or str (XML)

    def test_color(self):
        hex_value = "6B4106"
        response = color(hex_value)
        self.assertIsInstance(response, (dict, str))

    def test_palettes(self):
        response = palettes()
        self.assertIsInstance(response, (dict, str))

    def test_palette(self):
        palette_id = 113451
        response = palette(palette_id)
        self.assertIsInstance(response, (dict, str))

    def test_patterns(self):
        response = patterns()
        self.assertIsInstance(response, (dict, str))

    def test_pattern(self):
        pattern_id = 1451
        response = pattern(pattern_id)
        self.assertIsInstance(response, (dict, str))

    def test_lovers(self):
        response = lovers()
        self.assertIsInstance(response, (dict, str))

    def test_lover(self):
        username = "COLOURlover"
        response = lover(username)
        self.assertIsInstance(response, (dict, str))
    
    def test_stats_colors(self):
        response = stats("colors")
        self.assertIsInstance(response, (dict, str))

    def test_invalid_stat_resource(self):
        with self.assertRaises(ValueError):
            stats("invalid_resource")


if __name__ == "__main__":
    unittest.main()