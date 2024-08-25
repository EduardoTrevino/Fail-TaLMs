import unittest
from api import (
    list_datasets,
    search_datasets,
    get_dataset_details,
    list_organizations,
    get_organization_details,
    list_nodes,
    get_node_details,
)

class TestGBIFAPI(unittest.TestCase):

    def test_list_datasets(self):
        response = list_datasets(limit=2)
        self.assertIn('results', response)

    def test_search_datasets(self):
        response = search_datasets(q="plants", limit=2)
        self.assertIn('results', response)

    def test_get_dataset_details(self):
        response = get_dataset_details(key="3fa85f64-5717-4562-b3fc-2c963f66afa6") # Example key
        self.assertIn('key', response)

    def test_list_organizations(self):
        response = list_organizations(limit=2)
        self.assertIn('results', response)

    def test_get_organization_details(self):
        response = get_organization_details(key="3fa85f64-5717-4562-b3fc-2c963f66afa6") # Example key
        self.assertIn('key', response)

    def test_list_nodes(self):
        response = list_nodes(limit=2)
        self.assertIn('results', response)

    def test_get_node_details(self):
        response = get_node_details(key="3fa85f64-5717-4562-b3fc-2c963f66afa6") # Example key
        self.assertIn('key', response)

if __name__ == '__main__':
    unittest.main()