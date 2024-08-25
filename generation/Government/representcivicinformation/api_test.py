import unittest
from api import *


class TestApi(unittest.TestCase):

    def test_get_representatives_by_postal_code(self):
        response = get_representatives_by_postal_code("L5G4L3")
        self.assertIn("boundaries_centroid", response)

    def test_get_boundary_sets(self):
        response = get_boundary_sets(limit=2)
        self.assertIn("objects", response)
        self.assertTrue(len(response["objects"]) > 0)

    def test_get_boundaries(self):
        response = get_boundaries(name="Niagara Falls")
        self.assertIn("objects", response)
        self.assertTrue(len(response["objects"]) > 0)

    def test_get_representative_sets(self):
        response = get_representative_sets(limit=2)
        self.assertIn("objects", response)
        self.assertTrue(len(response["objects"]) > 0)

    def test_get_representatives(self):
        response = get_representatives(last_name="Trudeau")
        self.assertIn("objects", response)
        self.assertTrue(len(response["objects"]) > 0)

    def test_get_elections(self):
        response = get_elections(limit=1)
        self.assertIn("objects", response)
        self.assertTrue(len(response["objects"]) > 0)

    def test_get_candidates(self):
        response = get_candidates(limit=1)
        self.assertIn("objects", response)
        self.assertTrue(len(response["objects"]) > 0)


if __name__ == '__main__':
    unittest.main()