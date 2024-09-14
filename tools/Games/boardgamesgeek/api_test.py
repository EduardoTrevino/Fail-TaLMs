import unittest
from api import (get_thing_items, get_family_items, get_forum_list, get_user_info, get_guild_info, 
                 get_plays, get_collection, get_hot_items, search_items, get_thread, get_forum)


class TestBoardGamesGeekAPI(unittest.TestCase):

    def test_get_thing_items(self):
        response = get_thing_items(ids="174430")
        self.assertIn("<name", response.decode('utf-8'))

    def test_get_family_items(self):
        response = get_family_items(ids="1234")
        self.assertIn("<item", response.decode('utf-8'))

    def test_get_forum_list(self):
        response = get_forum_list(id=174430, type='thing')
        self.assertIn("<forum", response.decode('utf-8'))

    def test_get_forum(self):
        response = get_forum(id=123)
        self.assertIn("<threads", response.decode('utf-8'))

    def test_get_thread(self):
        response = get_thread(id=123)
        self.assertIn("<thread", response.decode('utf-8'))

    def test_get_user_info(self):
        response = get_user_info(name="eekspider")
        self.assertIn("<user", response.decode('utf-8'))

    def test_get_guild_info(self):
        response = get_guild_info(id=1229)
        self.assertIn("<guild", response.decode('utf-8'))

    def test_get_plays(self):
        response = get_plays(username="eekspider")
        self.assertIn("<plays", response.decode('utf-8'))

    def test_get_collection(self):
        response = get_collection(username="eekspider")
        self.assertIn("<item", response.decode('utf-8'))

    def test_get_hot_items(self):
        response = get_hot_items(type="boardgame")
        self.assertIn("<item", response.decode('utf-8'))

    def test_search_items(self):
        response = search_items(query="Catan")
        self.assertIn("<item", response.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()