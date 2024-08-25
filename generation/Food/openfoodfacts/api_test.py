import unittest
from api import get_product_by_barcode, search_products

class OpenFoodFactsAPITest(unittest.TestCase):
    
    def test_get_product_by_barcode(self):
        response = get_product_by_barcode('3017624010701', fields='product_name,nutrition_grades')
        self.assertEqual(response.get('status'), 1)
        self.assertIn('product', response)
        self.assertEqual(response['product']['product_name'], 'Nutella')
        self.assertEqual(response['product']['nutrition_grades'], 'e')

    def test_search_products(self):
        response = search_products(categories='Orange Juice', nutrition_grades='c', fields='code,nutrition_grades')
        self.assertIsInstance(response, dict)
        self.assertIn('products', response)
        self.assertGreater(len(response['products']), 0)
        for product in response['products']:
            self.assertEqual(product['nutrition_grades'], 'c')


if __name__ == '__main__':
    unittest.main()