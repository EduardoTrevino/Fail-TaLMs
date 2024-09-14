import unittest
from api import get_brands, get_models, get_years, get_value

class TestFipeAPI(unittest.TestCase):

    def test_get_brands(self):
        response = get_brands()
        self.assertIsInstance(response, list, "Expected a list of brands.")
        self.assertGreater(len(response), 0, "Expected at least one brand returned.")

    def test_get_models(self):
        response = get_models("59")  # Example using brand code for VW - VolksWagen
        self.assertIn("modelos", response, "Expected 'modelos' key in response.")
        self.assertIn("anos", response, "Expected 'anos' key in response.")

    def test_get_years(self):
        response = get_years("59", "5940")  # Example using brand code and model code
        self.assertIsInstance(response, list, "Expected a list of years.")
        self.assertGreater(len(response), 0, "Expected at least one year returned.")

    def test_get_value(self):
        response = get_value("59", "5940", "2014-3")  # Example using VW year code
        self.assertIsInstance(response, dict, "Expected a dictionary with price details.")
        self.assertIn("Valor", response, "Expected 'Valor' key in response.")

if __name__ == "__main__":
    unittest.main()