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
        response = get_dataset_details(key="6d52d3ee-d375-4daa-8c3b-c94e0ef4eb76") # Example key
        self.assertIn('key', response)

    def test_list_organizations(self):
        response = list_organizations(limit=2)
        self.assertIn('results', response)

    def test_get_organization_details(self):
        response = get_organization_details(key="eae15943-0c7d-4312-9d2f-22b7944c9502") # Example key
        self.assertIn('key', response)

    def test_list_nodes(self):
        response = list_nodes(limit=2)
        self.assertIn('results', response)

    def test_get_node_details(self):
        response = get_node_details(key="18aacf1e-738e-4172-a28d-15b639abb1a8") # Example key
        self.assertIn('key', response)

if __name__ == '__main__':
    unittest.main()