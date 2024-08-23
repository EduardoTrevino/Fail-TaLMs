import unittest
from api import get_product_by_barcode, search_products


class TestOpenFoodFactsAPI(unittest.TestCase):

    def test_get_product_by_barcode(self):
        result = get_product_by_barcode('737628064502')
        self.assertIn('product', result)
        self.assertIn('status', result)
        self.assertEqual(result['status_verbose'], "product found")

    def test_search_products(self):
        result = search_products(nutrition_grades_tags='c', categories_tags_en='Orange Juice')
        self.assertIn('products', result)
        self.assertIn('count', result)

    def test_get_product_by_barcode_with_fields(self):
        result = get_product_by_barcode('737628064502', fields="product_name,nutrition_grades")
        self.assertIn('product', result)
        self.assertIn('status', result)
        self.assertIn('nutrition_grades', result['product'])
        self.assertIn('product_name', result['product'])

    def test_search_products_with_sorting(self):
        result = search_products(categories_tags_en='Orange Juice', nutrition_grades_tags='c', sort_by='last_modified_t')
        self.assertIn('products', result)
        self.assertIn('count', result)
        self.assertGreater(len(result['products']), 0)

if __name__ == '__main__':
    unittest.main()