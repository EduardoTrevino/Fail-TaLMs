import unittest
from api import application_json, application_wadl, catalogs, contributors, count, query, version
import json
class TestUSGSApi(unittest.TestCase):

    def test_application_json(self):
        response = application_json()

    def test_application_wadl(self):
        response = application_wadl()
        self.assertIsInstance(response, str)
        self.assertIn("wadl", response)

    def test_catalogs(self):
        response = catalogs()

    def test_contributors(self):
        response = contributors()

    def test_count(self):
        response = count(starttime="2023-01-01", endtime="2023-01-02", minmagnitude=5)

    def test_query(self):
        response = query(starttime="2023-01-01", endtime="2023-01-02", minmagnitude=5)
        self.assertIn("metadata", str(json.dumps(response)))

    def test_version(self):
        response = version()
        self.assertIsInstance(response, str)
        self.assertRegex(response, r'^\d+\.\d+\.\d+')

if __name__ == '__main__':
    unittest.main()