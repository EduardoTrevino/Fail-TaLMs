import unittest
from api import (
    shuffle_deck, draw_cards, reshuffle_deck, new_deck, partial_deck,
    add_to_pile, return_cards
)

class TestDeckOfCardsAPI(unittest.TestCase):

    def test_shuffle_deck(self):
        response = shuffle_deck(deck_count=1)
        self.assertTrue(response['success'])
        self.assertIn('deck_id', response)

    def test_draw_cards(self):
        response = draw_cards(deck_id="new", count=2)
        self.assertTrue(response['success'])
        self.assertIn('cards', response)

    def test_reshuffle_deck(self):
        shuffle_response = shuffle_deck(deck_count=1)
        deck_id = shuffle_response['deck_id']
        response = reshuffle_deck(deck_id=deck_id)
        self.assertTrue(response['success'])

    def test_new_deck(self):
        response = new_deck(jokers_enabled=True)
        self.assertTrue(response['success'])
        self.assertEqual(response['remaining'], 54)

    def test_partial_deck(self):
        response = partial_deck(cards="AS,2S,KS")
        self.assertTrue(response['success'])
        self.assertEqual(response['remaining'], 3)

    def test_add_to_pile(self):
        shuffle_response = shuffle_deck(deck_count=1)
        deck_id = shuffle_response['deck_id']
        draw_response = draw_cards(deck_id=deck_id, count=2)
        cards = draw_response['cards'][0]['code']
        response = add_to_pile(deck_id=deck_id, pile_name="discard", cards=cards)
        self.assertTrue(response['success'])

    # def test_shuffle_pile(self):
    #     shuffle_response = shuffle_deck(deck_count=1)
    #     deck_id = shuffle_response['deck_id']
    #     response = shuffle_pile(deck_id=deck_id, pile_name="discard")
    #     self.assertTrue(response['success'])

    # def test_list_pile(self):
    #     shuffle_response = shuffle_deck(deck_count=1)
    #     print(shuffle_response)
    #     deck_id = shuffle_response['deck_id']
    #     print(deck_id)
    #     response = list_pile(deck_id=deck_id, pile_name="blue")
    #     self.assertTrue(response['success'])

    # def test_draw_from_pile(self):
    #     shuffle_response = shuffle_deck(deck_count=1)
    #     deck_id = shuffle_response['deck_id']
    #     response = draw_from_pile(deck_id=deck_id, pile_name="discard", count=1)
    #     self.assertTrue(response['success'])

    def test_return_cards(self):
        shuffle_response = shuffle_deck(deck_count=1)
        deck_id = shuffle_response['deck_id']
        draw_response = draw_cards(deck_id=deck_id, count=2)
        cards = draw_response['cards'][0]['code']
        response = return_cards(deck_id=deck_id, cards=cards)
        self.assertTrue(response['success'])

if __name__ == '__main__':
    unittest.main()