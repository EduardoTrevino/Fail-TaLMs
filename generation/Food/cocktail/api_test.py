import unittest
from api import *

class TestCocktailAPI(unittest.TestCase):

    def test_search_cocktail_by_name(self):
        response = search_cocktail_by_name(s="margarita")
        self.assertIn("drinks", response)
    
    def test_list_all_cocktails_by_first_letter(self):
        response = list_all_cocktails_by_first_letter(f="a")
        self.assertIn("drinks", response)
    
    def test_search_ingredient_by_name(self):
        response = search_ingredient_by_name(i="vodka")
        self.assertIn("ingredients", response)
    
    def test_lookup_full_cocktail_details_by_id(self):
        response = lookup_full_cocktail_details_by_id(i=11007)
        self.assertIn("drinks", response)
        
    def test_lookup_ingredient_by_id(self):
        response = lookup_ingredient_by_id(iid=552)
        self.assertIn("ingredients", response)
        
    def test_lookup_random_cocktail(self):
        response = lookup_random_cocktail()
        self.assertIn("drinks", response)
    
    def test_search_by_ingredient(self):
        response = search_by_ingredient(i="Gin")
        self.assertIn("drinks", response)
        
    def test_filter_by_alcoholic(self):
        response = filter_by_alcoholic(a="Alcoholic")
        self.assertIn("drinks", response)
        
    def test_filter_by_category(self):
        response = filter_by_category(c="Ordinary_Drink")
        self.assertIn("drinks", response)
        
    def test_filter_by_glass(self):
        response = filter_by_glass(g="Cocktail_glass")
        self.assertIn("drinks", response)
        
    def test_list_categories(self):
        response = list_categories()
        self.assertIn("drinks", response)
        
    def test_list_glasses(self):
        response = list_glasses()
        self.assertIn("drinks", response)
        
    def test_list_ingredients(self):
        response = list_ingredients()
        self.assertIn("drinks", response)
        
    def test_list_alcoholic(self):
        response = list_alcoholic()
        self.assertIn("drinks", response)

if __name__ == '__main__':
    unittest.main()