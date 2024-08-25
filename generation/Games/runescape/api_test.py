import unittest
from api import (
    grand_exchange_info, 
    grand_exchange_category, 
    grand_exchange_items, 
    grand_exchange_detail, 
    grand_exchange_graph, 
    hiscores_ranking, 
    runemetrics_profile, 
    player_count
)

class TestRunescapeAPI(unittest.TestCase):
    
    def test_grand_exchange_info(self):
        result = grand_exchange_info()
        self.assertIn("lastConfigUpdateRuneday", result)  # or another key

    def test_grand_exchange_category(self):
        result = grand_exchange_category(category=9)
        self.assertIn("types", result)

    def test_grand_exchange_items(self):
        result = grand_exchange_items(category=9, alpha='c', page=1)
        self.assertIn("items", result)

    def test_grand_exchange_detail(self):
        result = grand_exchange_detail(item_id=21787)
        self.assertIn("item", result)

    def test_grand_exchange_graph(self):
        result = grand_exchange_graph(item_id=21787)
        self.assertIn("daily", result)

    def test_hiscores_ranking(self):
        result = hiscores_ranking(table=9, category=0, size=2)
        self.assertIsInstance(result, list)

    def test_runemetrics_profile(self):
        result = runemetrics_profile(user="SomePlayer")
        self.assertIn("name", result)
        
    def test_player_count(self):
        result = player_count()
        self.assertIn("iPlayerCount", result)

if __name__ == '__main__':
    unittest.main()