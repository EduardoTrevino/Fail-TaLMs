import unittest
from api import *

class TestColourLoversAPI(unittest.TestCase):
    
    def test_colors(self):
        response = colors()
        self.assertIn('colors', response, msg="Error fetching colors")

    def test_colors_new(self):
        response = colors_new()
        self.assertIn('colors', response, msg="Error fetching new colors")

    def test_colors_top(self):
        response = colors_top()
        self.assertIn('colors', response, msg="Error fetching top colors")

    def test_colors_random(self):
        response = colors_random()
        self.assertIn('colors', response, msg="Error fetching random color")

    def test_color(self):
        response = color(hex_value="6B4106")
        self.assertIn('colors', response, msg="Error fetching specific color")

    def test_palettes(self):
        response = palettes()
        self.assertIn('palettes', response, msg="Error fetching palettes")

    def test_palettes_new(self):
        response = palettes_new()
        self.assertIn('palettes', response, msg="Error fetching new palettes")

    def test_palettes_top(self):
        response = palettes_top()
        self.assertIn('palettes', response, msg="Error fetching top palettes")

    def test_palettes_random(self):
        response = palettes_random()
        self.assertIn('palettes', response, msg="Error fetching random palette")

    def test_palette(self):
        response = palette(palette_id=113451)
        self.assertIn('palettes', response, msg="Error fetching specific palette")

    def test_patterns(self):
        response = patterns()
        self.assertIn('patterns', response, msg="Error fetching patterns")

    def test_patterns_new(self):
        response = patterns_new()
        self.assertIn('patterns', response, msg="Error fetching new patterns")

    def test_patterns_top(self):
        response = patterns_top()
        self.assertIn('patterns', response, msg="Error fetching top patterns")

    def test_patterns_random(self):
        response = patterns_random()
        self.assertIn('patterns', response, msg="Error fetching random pattern")

    def test_pattern(self):
        response = pattern(pattern_id=1451)
        self.assertIn('patterns', response, msg="Error fetching specific pattern")

    def test_lovers(self):
        response = lovers()
        self.assertIn('lovers', response, msg="Error fetching lovers")

    def test_lovers_new(self):
        response = lovers_new()
        self.assertIn('lovers', response, msg="Error fetching new lovers")

    def test_lovers_top(self):
        response = lovers_top()
        self.assertIn('lovers', response, msg="Error fetching top lovers")

    def test_lover(self):
        response = lover(username="COLOURlover")
        self.assertIn('lovers', response, msg="Error fetching specific lover")

    def test_stats_colors(self):
        response = stats_colors()
        self.assertIn('stats', response, msg="Error fetching stats colors")

    def test_stats_palettes(self):
        response = stats_palettes()
        self.assertIn('stats', response, msg="Error fetching stats palettes")

    def test_stats_patterns(self):
        response = stats_patterns()
        self.assertIn('stats', response, msg="Error fetching stats patterns")

    def test_stats_lovers(self):
        response = stats_lovers()
        self.assertIn('stats', response, msg="Error fetching stats lovers")


if __name__ == '__