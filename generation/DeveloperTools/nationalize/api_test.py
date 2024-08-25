import unittest
from api import predict_nationality

class TestNationalizeAPI(unittest.TestCase):
    
    def test_single_name_prediction(self):
        response = predict_nationality(name="johnson")
        self.assertIn("name", response)
        self.assertEqual(response["name"], "johnson")
        self.assertIn("country", response)
        self.assertIsInstance(response["country"], list)

    def test_batch_name_prediction(self):
        names = ["johnson", "bakshi"]
        response = predict_nationality(names)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        for res in response:
            self.assertIn("name", res)
            self.assertIn("country", res)

    def test_missing_name_parameter(self):
        response = predict_nationality(name="")
        self.assertIn("error", response)

if __name__ == "__main__":
    unittest.main()