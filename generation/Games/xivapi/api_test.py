import unittest
from api import *

class TestXivApi(unittest.TestCase):
    def setUp(self):
        self.api_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

    def test_search(self):
        response = search(string="aiming", toolbench_rapidapi_key=self.api_key)
        self.assertIn('Results', response)

    def test_get_content(self):
        response = get_content(toolbench_rapidapi_key=self.api_key)
        self.assertIn('content', response)

    def test_get_item(self):
        response = get_item(item_id=1675, toolbench_rapidapi_key=self.api_key)
        self.assertIn('ID', response)
        self.assertEqual(response['ID'], 1675)

    def test_list_servers(self):
        response = list_servers(toolbench_rapidapi_key=self.api_key)
        self.assertIsInstance(response, list)

    def test_list_servers_data_centers(self):
        response = list_servers_data_centers(toolbench_rapidapi_key=self.api_key)
        self.assertIsInstance(response, dict)

    def test_character_search(self):
        response = character_search(name="Sora Amity", server="Adamantoise", toolbench_rapidapi_key=self.api_key)
        self.assertIn('Results', response)

    def test_get_character(self):
        response = get_character(lodestone_id=730968, toolbench_rapidapi_key=self.api_key)
        self.assertIn('Character', response)

    def test_freecompany_search(self):
        response = freecompany_search(name="Knights of the Round", toolbench_rapidapi_key=self.api_key)
        self.assertIn('Results', response)

    def test_get_freecompany(self):
        response = get_freecompany(lodestone_id=9231253336202687179, toolbench_rapidapi_key=self.api_key)
        self.assertIn('FreeCompany', response)

    def test_linkshell_search(self):
        response = linkshell_search(name="Echo", toolbench_rapidapi_key=self.api_key)
        self.assertIn('Results', response)

    def test_linkshell_crossworld_search(self):
        response = linkshell_crossworld_search(name="Echo", toolbench_rapidapi_key=self.api_key)
        self.assertIn('Results', response)

if __name__ == '__main__':
    unittest.main()