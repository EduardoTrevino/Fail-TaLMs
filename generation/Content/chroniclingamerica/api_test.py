import unittest
from api import (
    search_titles,
    search_pages,
    suggest_titles,
    get_newspapers_json,
    get_all_batches_json,
    get_specific_batch_json,
    get_awardees_json,
    get_specific_awardee_json
)

class TestChroniclingAmericaAPI(unittest.TestCase):
    def test_search_titles(self):
        response = search_titles('michigan', format='json', page=1)
        # print(response)  # Debugging line
        self.assertIn('items', response, f"'items' key not found in response: {response}")
        self.assertIsInstance(response['items'], list, "Expected 'items' to be a list.")

    def test_search_pages(self):
        response = search_pages('thomas', format='json', page=1)
        # print(response)  # Debugging line
        self.assertIn('items', response, f"'items' key not found in response: {response}")
        self.assertIsInstance(response['items'], list, "Expected 'items' to be a list.")

    def test_suggest_titles(self):
        response = suggest_titles('Florida')
        assert isinstance(response, list)

    def test_get_newspapers_json(self):
        response = get_newspapers_json()
        assert isinstance(response, dict)

    def test_get_all_batches_json(self):
        response = get_all_batches_json()
        assert isinstance(response, dict)

    def test_get_specific_batch_json(self):
        response = get_specific_batch_json('dlc_jamaica_ver01')
        assert 'name' in response and 'url' in response

    def test_get_awardees_json(self):
        response = get_awardees_json()
        assert isinstance(response, dict)

    def test_get_specific_awardee_json(self):
        response = get_specific_awardee_json('dlc')
        assert 'name' in response and 'url' in response

if __name__ == "__main__":
    unittest.main()