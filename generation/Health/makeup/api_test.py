# import unittest
# from api import search_makeup_products

# class TestMakeupAPI(unittest.TestCase):
#     def test_search_makeup_products_without_params(self):
#         response = search_makeup_products()
#         self.assertIsInstance(response, list, "Expected response to be a list")

#     def test_search_makeup_products_with_brand(self):
#         response = search_makeup_products(brand="maybelline")
#         self.assertIsInstance(response, list, "Expected response to be a list")
#         for product in response:
#             if "brand" in product:
#                 self.assertEqual(product['brand'], "maybelline")

#     def test_search_makeup_products_with_product_type(self):
#         response = search_makeup_products(product_type="lipstick")
#         self.assertIsInstance(response, list, "Expected response to be a list")
#         for product in response:
#             if "product_type" in product:
#                 self.assertEqual(product['product_type'], "lipstick")

#     def test_search_makeup_products_with_brand_and_product_type(self):
#         response = search_makeup_products(brand="covergirl", product_type="lipstick")
#         self.assertIsInstance(response, list, "Expected response to be a list")
#         for product in response:
#             if "brand" in product:
#                 self.assertEqual(product['brand'], "covergirl")
#             if "product_type" in product:
#                 self.assertEqual(product['product_type'], "lipstick")

# if __name__ == '__main__':
#     unittest.main()
import unittest
from api import search_makeup_products

class TestMakeupAPI(unittest.TestCase):
    def print_summary(self, response):
        if isinstance(response, list) and response:
            # Print only the first item and its keys
            print("Sample Response (first item):", response[0])
            print("Available keys:", response[0].keys())
        else:
            print("Response is empty or not a list:", response)

    def test_search_makeup_products_without_params(self):
        response = search_makeup_products()
        self.print_summary(response)
        self.assertIsInstance(response, list, "Expected response to be a list")

    def test_search_makeup_products_with_brand(self):
        response = search_makeup_products(brand="maybelline")
        self.print_summary(response)
        self.assertIsInstance(response, list, "Expected response to be a list")
        for product in response:
            if "brand" in product:
                self.assertEqual(product['brand'], "maybelline")

    def test_search_makeup_products_with_product_type(self):
        response = search_makeup_products(product_type="lipstick")
        self.print_summary(response)
        self.assertIsInstance(response, list, "Expected response to be a list")
        for product in response:
            if "product_type" in product:
                self.assertEqual(product['product_type'], "lipstick")

    def test_search_makeup_products_with_brand_and_product_type(self):
        response = search_makeup_products(brand="covergirl", product_type="lipstick")
        self.print_summary(response)
        self.assertIsInstance(response, list, "Expected response to be a list")
        for product in response:
            if "brand" in product:
                self.assertEqual(product['brand'], "covergirl")
            if "product_type" in product:
                self.assertEqual(product['product_type'], "lipstick")

if __name__ == '__main__':
    unittest.main()