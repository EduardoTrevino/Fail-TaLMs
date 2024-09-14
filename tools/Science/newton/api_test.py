import unittest
from api import newton_calculate

class TestNewtonAPI(unittest.TestCase):

    def test_simplify(self):
        response = newton_calculate("simplify", "2%5E2%2B2%282%29")
        self.assertEqual(response.get("result"), "8", "Test simplify failed.")

    def test_factor(self):
        response = newton_calculate("factor", "x%5E2%2B2x")
        self.assertEqual(response.get("result"), "x (x + 2)", "Test factor failed.")

    def test_derive(self):
        response = newton_calculate("derive", "x%5E2%2B2x")
        self.assertEqual(response.get("result"), "2 x + 2", "Test derive failed.")

    def test_integrate(self):
        response = newton_calculate("integrate", "x%5E2%2B2x")
        self.assertIn("1/3 x^3 + x^2", response.get("result"), "Test integrate failed.")

    def test_zeroes(self):
        response = newton_calculate("zeroes", "x%5E2%2B2x")
        self.assertEqual(response.get("result"), [-2, 0], "Test zeroes failed.")

    def test_area(self):
        response = newton_calculate("area", "2%3A4%7Cx%5E3")
        self.assertEqual(response.get("result"), "60", "Test area failed.")

    def test_cosine(self):
        response = newton_calculate("cos", "pi")
        self.assertEqual(response.get("result"), "-1", "Test cosine failed.")

    def test_sine(self):
        response = newton_calculate("sin", "0")
        self.assertEqual(response.get("result"), "0", "Test sine failed.")

    def test_tangent_angle(self):
        response = newton_calculate("tan", "0")
        self.assertEqual(response.get("result"), "0", "Test tangent failed.")

    def test_arccos(self):
        response = newton_calculate("arccos", "1")
        self.assertEqual(response.get("result"), "0", "Test arccos failed.")

    def test_arcsin(self):
        response = newton_calculate("arcsin", "0")
        self.assertEqual(response.get("result"), "0", "Test arcsin failed.")

    def test_arctan(self):
        response = newton_calculate("arctan", "0")
        self.assertEqual(response.get("result"), "0", "Test arctan failed.")

    def test_absolute(self):
        response = newton_calculate("abs", "-1")
        self.assertEqual(response.get("result"), "1", "Test absolute value failed.")

    def test_logarithm(self):
        response = newton_calculate("log", "2%7C8")
        self.assertEqual(response.get("result"), "3", "Test logarithm failed.")

if __name__ == '__main__':
    unittest.main()