import unittest
from api import (
    get_token_price, 
    get_supported_networks,
    get_supported_dexes,
    get_trending_pools_all,
    get_trending_pools
)

API_KEY = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'

class TestGeckoTerminalAPI(unittest.TestCase):

    def test_get_token_price(self):
        response = get_token_price(network="eth", addresses="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", toolbench_rapidapi_key=API_KEY)
        self.assertIn("data", response)

    def test_get_supported_networks(self):
        response = get_supported_networks(toolbench_rapidapi_key=API_KEY)
        self.assertIn("data", response)

    def test_get_supported_dexes(self):
        response = get_supported_dexes(network="eth", toolbench_rapidapi_key=API_KEY)
        self.assertIn("data", response)

    def test_get_trending_pools_all(self):
        response = get_trending_pools_all(toolbench_rapidapi_key=API_KEY)
        self.assertIn("data", response)

    def test_get_trending_pools(self):
        response = get_trending_pools(network="eth", toolbench_rapidapi_key=API_KEY)
        self.assertIn("data", response)

if __name__ == "__main__":
    unittest.main()