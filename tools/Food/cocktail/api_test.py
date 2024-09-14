import unittest
from api import search_cocktail_by_name, list_cocktails_by_first_letter, search_ingredient_by_name, lookup_cocktail_by_id, lookup_ingredient_by_id, lookup_random_cocktail, search_by_ingredient, filter_by_alcoholic, filter_by_category, filter_by_glass, list_categories, list_glasses, list_ingredients, list_alcoholic_filters


class TestCocktailAPI(unittest.TestCase):
    def test_search_cocktail_by_name(self):
        result = search_cocktail_by_name("margarita")
        self.assertIn("drinks", result)

    def test_list_cocktails_by_first_letter(self):
        result = list_cocktails_by_first_letter("a")
        self.assertIn("drinks", result)

    def test_search_ingredient_by_name(self):
        result = search_ingredient_by_name("vodka")
        self.assertIn("ingredients", result)

    def test_lookup_cocktail_by_id(self):
        result = lookup_cocktail_by_id(11007)
        self.assertIn("drinks", result)

    def test_lookup_ingredient_by_id(self):
        result = lookup_ingredient_by_id(552)
        self.assertIn("ingredients", result)

    def test_lookup_random_cocktail(self):
        result = lookup_random_cocktail()
        self.assertIn("drinks", result)

    def test_search_by_ingredient(self):
        result = search_by_ingredient("Gin")
        self.assertIn("drinks", result)

    def test_filter_by_alcoholic(self):
        result = filter_by_alcoholic("Alcoholic")
        self.assertIn("drinks", result)

    def test_filter_by_category(self):
        result = filter_by_category("Ordinary_Drink")
        self.assertIn("drinks", result)

    def test_filter_by_glass(self):
        result = filter_by_glass("Cocktail_glass")
        self.assertIn("drinks", result)

    def test_list_categories(self):
        result = list_categories()
        self.assertIn("drinks", result)

    def test_list_glasses(self):
        result = list_glasses()
        self.assertIn("drinks", result)

    def test_list_ingredients(self):
        result = list_ingredients()
        self.assertIn("drinks", result)

    def test_list_alcoholic_filters(self):
        result = list_alcoholic_filters()
        self.assertIn("drinks", result)


if __name__ == '__main__':
    unittest.main()