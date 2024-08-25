import unittest
from api import search_makeup_products


class TestMakeupAPI(unittest.TestCase):

    def test_search_by_brand_only(self):
        result = search_makeup_products(brand="maybelline")
        self.assertIsInstance(result, list)
        for product in result:
            self.assertEqual(product.get('brand').lower(), "maybelline")

    def test_search_by_product_type(self):
        result = search_makeup_products(product_type="lipstick")
        self.assertIsInstance(result, list)
        for product in result:
            self.assertEqual(product.get('product_type'), "lipstick")

    def test_search_by_brand_and_type(self):
        result = search_makeup_products(brand="maybelline", product_type="eyeliner")
        self.assertIsInstance(result, list)
        for product in result:
            self.assertEqual(product.get('brand').lower(), "maybelline")
            self.assertEqual(product.get('product_type'), "eyeliner")

    def test_search_by_tags(self):
        result = search_makeup_products(product_tags=["vegan", "cruelty free"])
        self.assertIsInstance(result, list)
        for product in result:
            self.assertTrue(set(["vegan", "cruelty free"]).issubset(set(product.get('tag_list', []))))

    def test_price_filtering(self):
        result = search_makeup_products(price_greater_than=10.0, price_less_than=20.0)
        self.assertIsInstance(result, list)
        for product in result:
            price = float(product.get('price', 0))
            self.assertGreater(price, 10.0)
            self.assertLess(price, 20.0)

    def test_rating_filtering(self):
        result = search_makeup_products(rating_greater_than=4.0, rating_less_than=5.0)
        self.assertIsInstance(result, list)
        for product in result:
            rating = product.get('rating', 0)
            self.assertGreater(rating, 4.0)
            self.assertLess(rating, 5.0)


if __name__ == '__main__':
    unittest.main()