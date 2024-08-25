import requests
from typing import Optional, List

BASE_URL = "https://api.gemini.com"


def get_symbols(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve all available symbols for trading.
    """
    url = f"{BASE_URL}/v1/symbols"
    response = requests.get(url)
    return response.json()

def get_symbol_details(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve extra details about a supported symbol.
    """
    url = f"{BASE_URL}/v1/symbols/details/{symbol}"
    response = requests.get(url)
    return response.json()

def get_network(token: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve the associated network for a requested token.
    """
    url = f"{BASE_URL}/v1/network/{token}"
    response = requests.get(url)
    return response.json()

def get_ticker(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about recent trading activity for the symbol.
    """
    url = f"{BASE_URL}/v1/pubticker/{symbol}"
    response = requests.get(url)
    return response.json()

def get_ticker_v2(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve information about recent trading activity for the provided symbol.
    """
    url = f"{BASE_URL}/v2/ticker/{symbol}"
    response = requests.get(url)
    return response.json()

def get_candles(symbol: str, time_frame: str = "15m", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve time-intervaled data for the provided symbol.
    """
    url = f"{BASE_URL}/v2/candles/{symbol}/{time_frame}"
    response = requests.get(url)
    return response.json()

def get_derivatives_candles(symbol: str, time_frame: str = "1m", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve time-intervaled data for the provided derivatives symbol.
    """
    url = f"{BASE_URL}/v2/derivatives/candles/{symbol}/{time_frame}"
    response = requests.get(url)
    return response.json()

def get_fee_promos(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve symbols that currently have fee promos.
    """
    url = f"{BASE_URL}/v1/feepromos"
    response = requests.get(url)
    return response.json()

def get_current_order_book(symbol: str, limit_bids: Optional[int] = 50, limit_asks: Optional[int] = 50, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Return the current order book as two arrays (bids / asks).
    """
    params = {
        'limit_bids': limit_bids,
        'limit_asks': limit_asks,
    }
    url = f"{BASE_URL}/v1/book/{symbol}"
    response = requests.get(url, params=params)
    return response.json()

def get_trade_history(symbol: str, timestamp: Optional[int] = None, since_tid: Optional[int] = None, limit_trades: Optional[int] = 50, include_breaks: Optional[bool] = False, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Return the trades that have executed since the specified timestamp.
    """
    params = {
        'timestamp': timestamp,
        'since_tid': since_tid,
        'limit_trades': limit_trades,
        'include_breaks': '1' if include_breaks else '0',
    }
    url = f"{BASE_URL}/v1/trades/{symbol}"
    response = requests.get(url, params=params)
    return response.json()

def get_price_feed(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve price feed for all trading pairs.
    """
    url = f"{BASE_URL}/v1/pricefeed"
    response = requests.get(url)
    return response.json()

def get_funding_amount(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve extra detail on supported symbols, such as minimum order size, tick size, quote increment and more.
    """
    url = f"{BASE_URL}/v1/fundingamount/{symbol}"
    response = requests.get(url)
    return response.json()