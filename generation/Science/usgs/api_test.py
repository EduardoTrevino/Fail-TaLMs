import unittest
from api import application_json, application_wadl, catalogs, contributors, count, query, version

class TestUSGSApi(unittest.TestCase):

    def test_application_json(self):
        response = application_json()
        self.assertIsInstance(response, dict)
        self.assertIn("parameters", response.keys())

    def test_application_wadl(self):
        response = application_wadl()
        self.assertIsInstance(response, str)
        self.assertIn("<wadl", response)

    def test_catalogs(self):
        response = catalogs()
        self.assertIsInstance(response, list)

    def test_contributors(self):
        response = contributors()
        self.assertIsInstance(response, list)

    def test_count(self):
        response = count(starttime="2023-01-01", endtime="2023-01-02", minmagnitude=5)
        self.assertIsInstance(response, dict)
        self.assertIn("metadata", response.keys())

    def test_query(self):
        response = query(starttime="2023-01-01", endtime="2023-01-02", minmagnitude=5)
        self.assertIsInstance(response, dict)
        self.assertIn("metadata", response.keys())

    def test_version(self):
        response = version()
        self.assertIsInstance(response, str)
        self.assertRegex(response, r'^\d+\.\d+\.\d+')

if __name__ == '__main__':
    unittest.main()