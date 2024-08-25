import requests
from typing import Optional, List

def ping(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Test connectivity to the Rest API.
    """
    url = "https://api.wazirx.com/sapi/v1/ping"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def system_status(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetch system status.
    """
    url = "https://api.wazirx.com/sapi/v1/systemStatus"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def server_time(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Test connectivity to the Rest API and get the current server time.
    """
    url = "https://api.wazirx.com/sapi/v1/time"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def exchange_info(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Fetch all exchange information.
    """
    url = "https://api.wazirx.com/sapi/v1/exchangeInfo"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def tickers_24hr(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: 24 hour rolling window price change statistics for all symbols.
    """
    url = "https://api.wazirx.com/sapi/v1/tickers/24hr"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def ticker_24hr(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: 24 hour rolling window price change statistics for a single symbol.
    Parameters:
    symbol [Required]: string [The trading pair symbol]
    """
    url = "https://api.wazirx.com/sapi/v1/ticker/24hr"
    params = {
        'symbol': symbol
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def klines(symbol: str, interval: str = '1m', limit: int = 500, start_time: Optional[int] = None, end_time: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get Kline/candlestick data of the specified symbol.
    Parameters:
    symbol [Required]: string [The trading pair symbol]
    interval [Optional]: string [Time interval, default 1m]
    limit [Optional]: int [Number of klines to return, default 500]
    start_time [Optional]: int [Start time in milliseconds]
    end_time [Optional]: int [End time in milliseconds]
    """
    url = "https://api.wazirx.com/sapi/v1/klines"
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def depth(symbol: str, limit: Optional[int] = 20, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get Order book depth.
    Parameters:
    symbol [Required]: string [The trading pair symbol]
    limit [Optional]: int [Number of orders to return, default 20]
    """
    url = "https://api.wazirx.com/sapi/v1/depth"
    params = {
        'symbol': symbol,
        'limit': limit
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def recent_trades(symbol: str, limit: Optional[int] = 500, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get recent trades.
    Parameters:
    symbol [Required]: string [The trading pair symbol]
    limit [Optional]: int [Number of trades to return, default 500]
    """
    url = "https://api.wazirx.com/sapi/v1/trades"
    params = {
        'symbol': symbol,
        'limit': limit
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}