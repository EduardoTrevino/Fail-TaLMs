import requests
from typing import Optional, List

BASE_URL = "https://api.binance.com"

def get_agg_trades(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve aggregated trades for a specific symbol.
    """
    url = f"{BASE_URL}/api/v3/aggTrades"
    params = {
        'symbol': symbol
    }
    response = requests.get(url, params=params)
    return response.json()

def get_avg_price(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve current average price for a specific symbol.
    """
    url = f"{BASE_URL}/api/v3/avgPrice"
    params = {
        'symbol': symbol
    }
    response = requests.get(url, params=params)
    return response.json()

def get_exchange_info(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch exchange information.
    """
    url = f"{BASE_URL}/api/v3/exchangeInfo"
    response = requests.get(url)
    return response.json()

def ping(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Ping the server.
    """
    url = f"{BASE_URL}/api/v3/ping"
    response = requests.get(url)
    return response.json()

def get_24hr_ticker_price_change(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch 24hr ticker price change statistics for a specific symbol.
    """
    url = f"{BASE_URL}/api/v3/ticker/24hr"
    params = {
        'symbol': symbol
    }
    response = requests.get(url, params=params)
    return response.json()

def get_all_ticker_prices(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch ticker price for all market symbols.
    """
    url = f"{BASE_URL}/api/v3/ticker/price"
    response = requests.get(url)
    return response.json()

def get_system_status(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get system status.
    """
    url = f"{BASE_URL}/sapi/v1/system/status"
    response = requests.get(url)
    return response.json()

def get_account_status(timestamp: int, recvWindow: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch account status detail.
    """
    url = f"{BASE_URL}/sapi/v1/account/status"
    params = {
        'timestamp': timestamp
    }
    if recvWindow:
        params['recvWindow'] = recvWindow
    response = requests.get(url, params=params)
    return response.json()

def get_api_trading_status(timestamp: int, recvWindow: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch account API trading status detail.
    """
    url = f"{BASE_URL}/sapi/v1/account/apiTradingStatus"
    params = {
        'timestamp': timestamp
    }
    if recvWindow:
        params['recvWindow'] = recvWindow
    response = requests.get(url, params=params)
    return response.json()