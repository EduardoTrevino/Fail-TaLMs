import unittest
from api import forward_geocode, reverse_geocode, geoparse

class TestGeocodeAPI(unittest.TestCase):

    def test_forward_geocode(self):
        result = forward_geocode("Hauptstr., 57632 Berzhausen")
        self.assertIn('latt', result)
        self.assertIn('longt', result)

    def test_reverse_geocode(self):
        result = reverse_geocode(51.50354, -0.12768)
        self.assertIn('standard', result)
        self.assertIn('latt', result)
        self.assertIn('longt', result)

    def test_geoparse(self):
        result = geoparse("The most important museums of Amsterdam are located on the Museumplein.")
        self.assertIsInstance(result, dict)
        self.assertIn('matches', result)

    def test_forward_geocode_with_output_format(self):
        result = forward_geocode("Hauptstr., 57632 Berzhausen", "xml")
        self.assertIsInstance(result, str)  # XML response is a string and not a dictionary

    def test_reverse_geocode_with_output_format(self):
        result = reverse_geocode(51.50354, -0.12768, "csv")
        self.assertIsInstance(result, str)  # CSV response is a string

    def test_geoparse_with_sentiment_analysis(self):
        result = geoparse("The most important museums of Amsterdam are located on the Museumplein.", sentiment=True)
        self.assertIn('matches', result)
        self.assertIn('sentiment', result)

if __name__ == '__main__':
    unittest.main()