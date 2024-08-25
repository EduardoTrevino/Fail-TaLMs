import unittest
from api import query_by_catnr, query_by_intdes, query_by_group, query_by_name, query_by_special

class TestCelestrakAPI(unittest.TestCase):

    def test_query_by_catnr(self):
        result = query_by_catnr(catnr="25544", format="JSON")
        self.assertIsInstance(result, dict)

    def test_query_by_intdes(self):
        result = query_by_intdes(intdes="2020-025", format="JSON")
        self.assertIsInstance(result, dict)

    def test_query_by_group(self):
        result = query_by_group(group="STATIONS", format="XML")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('<?xml'))

    def test_query_by_name(self):
        result = query_by_name(name="MICROSAT-R", format="JSON")
        self.assertIsInstance(result, dict)

    def test_query_by_special(self):
        result = query_by_special(special="gpz", format="CSV")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('OMM,OBJECT_NAME'))

if __name__ == '__main__':
    unittest.main()