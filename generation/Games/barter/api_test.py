import unittest
from api import (
    get_app_settings, browse_bundles, browse_cards, browse_dlc, browse_tag,
    get_bundle, get_bundles, get_giveaways, get_item, get_user
)

class TestBarterAPI(unittest.TestCase):

    def test_get_app_settings(self):
        response = get_app_settings(0)
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_browse_bundles(self):
        response = browse_bundles()
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_browse_cards(self):
        response = browse_cards()
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_browse_dlc(self):
        response = browse_dlc()
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_browse_tag(self):
        response = browse_tag(100)
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_get_bundle(self):
        response = get_bundle(1)
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_get_bundles(self):
        response = get_bundles()
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_get_giveaways(self):
        response = get_giveaways()
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_get_item(self):
        response = get_item(1)
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

    def test_get_user(self):
        response = get_user("a0")
        self.assertIsInstance(response, dict)
        self.assertNotIn("error", response)

if __name__ == '__main__':
    unittest.main()