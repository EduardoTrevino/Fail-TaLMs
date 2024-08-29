# Your existing code
from api import *
import unittest  # Change from pytest to unittest

class TestAPI(unittest.TestCase):  # Wrap tests in a unittest class

    def setUp(self):
        self.toolbench_rapidapi_key = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

    def test_get_global_market_overview(self):
        response = get_global_market_overview(self.toolbench_rapidapi_key)
        self.assertIn('market_cap_usd', response)

    def test_list_coins(self):
        response = list_coins(self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

    def test_get_coin_by_id(self):
        coin_id = "btc-bitcoin"
        response = get_coin_by_id(coin_id, self.toolbench_rapidapi_key)
        self.assertEqual(response['id'], coin_id)

    def test_get_coin_twitter(self):
        coin_id = "btc-bitcoin"
        response = get_coin_twitter(coin_id, self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

    def test_get_coin_events(self):
        coin_id = "btc-bitcoin"
        response = get_coin_events(coin_id, self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

    def test_get_exchanges_by_coin_id(self):
        coin_id = "btc-bitcoin"
        response = get_exchanges_by_coin_id(coin_id, self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

    def test_get_markets_by_coin_id(self):
        coin_id = "btc-bitcoin"
        response = get_markets_by_coin_id(coin_id, self.toolbench_rapidapi_key)
        self.assertIsInstance(response, dict)

    def test_get_ohlc_last_day(self):
        coin_id = "btc-bitcoin"
        response = get_ohlc_last_day(coin_id, self.toolbench_rapidapi_key)
        self.assertIsInstance(response, dict)

    def test_get_ohlc_today(self):
        coin_id = "btc-bitcoin"
        response = get_ohlc_today(coin_id, self.toolbench_rapidapi_key)
        self.assertIsInstance(response, dict)

    def test_list_people(self):
        response = list_people(self.toolbench_rapidapi_key)
        self.assertIsInstance(response, dict)

    def test_list_tags(self):
        response = list_tags(self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

    def test_get_tag_by_id(self):
        tag_id = "blockchain-service"
        response = get_tag_by_id(tag_id)
        self.assertEqual(response['id'], tag_id)

    def test_get_tickers(self):
        response = get_tickers(self.toolbench_rapidapi_key)
        self.assertIsInstance(response, dict)

    def test_get_ticker_by_id(self):
        coin_id = "btc-bitcoin"
        
        # Test without quotes (default behavior)
        response = get_ticker_by_id(coin_id)
        self.assertIn('id', response)
        self.assertEqual(response['id'], coin_id)
        
        # Test with valid quotes
        response = get_ticker_by_id(coin_id, quotes="USD,EUR")
        self.assertIn('id', response)
        self.assertIn('quotes', response)
        self.assertIn('USD', response['quotes'])
        self.assertIn('EUR', response['quotes'])
        
        # Test with an invalid quote
        response = get_ticker_by_id(coin_id, quotes="INVALID")
        self.assertIn('error', response)
        self.assertEqual(response['error'], "Invalid quote(s) provided: INVALID. Allowed values are: ARS, AUD, BOB, BRL, BTC, CAD, CHF, CLP, CNY, COP, CZK, DKK, ETH, EUR, GBP, HKD, HUF, IDR, ILS, INR, ISK, JPY, KRW, MXN, MYR, NGN, NOK, NZD, PEN, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD, UAH, USD, VND, ZAR.")
        
        # Test with a non-existing coin ID
        response = get_ticker_by_id("non-existing-coin")
        self.assertIn('error', response)
        self.assertEqual(response['error'], "Coin with ID 'non-existing-coin' not found.")


    def test_list_exchanges(self):
        response = list_exchanges(self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

    def test_get_exchange_by_id(self):
        exchange_id = "binance"
        response = get_exchange_by_id(exchange_id, self.toolbench_rapidapi_key)
        self.assertEqual(response['id'], exchange_id)

    def test_list_exchange_markets(self):
        exchange_id = "binance"
        response = list_exchange_markets(exchange_id, self.toolbench_rapidapi_key)
        self.assertIsInstance(response, dict)

    def test_search(self):
        query = "btc"
        
        # Test with no categories (should return search results based on the query alone)
        response = search(query)
        self.assertTrue(any(response.values()), "Expected search results for the query only.")
        
        # Test with specific categories
        response = search(query, categories="currencies,exchanges")
        self.assertIn('currencies', response)
        self.assertIn('exchanges', response)
        
        # Test with an invalid category
        response = search(query, categories="invalid_category")
        self.assertIn('error', response)
        self.assertEqual(response['error'], "Invalid category: invalid_category. Supported categories are 'currencies', 'exchanges', 'icos', 'people', 'tags'.")

    def test_price_converter(self):
        response = price_converter("btc-bitcoin", "eth-ethereum", 1, self.toolbench_rapidapi_key)
        self.assertEqual(response['base_currency_id'], "btc-bitcoin")

    def test_list_contracts(self):
        response = list_contracts(self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

    def test_get_contracts_by_platform(self):
        platform_id = "eth-ethereum"
        response = get_contracts_by_platform(platform_id, self.toolbench_rapidapi_key)
        self.assertIsInstance(response, list)

if __name__ == '__main__':
    unittest.main()
