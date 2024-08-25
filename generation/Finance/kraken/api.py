import requests
from typing import Optional

def get_server_time(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get the server's time.
    
    Parameters:
    None
    """
    url = "https://api.kraken.com/0/public/Time"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_system_status(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get the current system status or trading mode.
    
    Parameters:
    None
    """
    url = "https://api.kraken.com/0/public/SystemStatus"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_asset_info(asset: Optional[str] = None, aclass: Optional[str] = "currency", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get information about the assets that are available for deposit, withdrawal, trading, and earn.
    
    Parameters:
    asset [Optional]: string - Comma delimited list of assets to get info on (optional, default all available assets)
    aclass [Optional]: string - Asset class (optional, default: currency)
    """
    url = "https://api.kraken.com/0/public/Assets"
    params = {
        'asset': asset,
        'aclass': aclass
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_tradable_asset_pairs(pair: Optional[str] = None, info: Optional[str] = "info", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get tradable asset pairs.
    
    Parameters:
    pair [Optional]: string - Asset pairs to get data for
    info [Optional]: string - Info to retrieve (optional)
    """
    url = "https://api.kraken.com/0/public/AssetPairs"
    params = {
        'pair': pair,
        'info': info
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ticker_information(pair: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get ticker information for all or requested markets.
    
    Parameters:
    pair [Optional]: string - Asset pair to get data for (optional, default: all tradeable exchange pairs)
    """
    url = "https://api.kraken.com/0/public/Ticker"
    params = {
        'pair': pair
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ohlc_data(pair: str, interval: Optional[int] = 1, since: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get OHLC (open/high/low/close) data for a given market.
    
    Parameters:
    pair [Required]: string - Asset pair to get data for
    interval [Optional]: integer - Time frame interval in minutes
    since [Optional]: integer - Return up to 720 OHLC data points since given timestamp
    """
    url = "https://api.kraken.com/0/public/OHLC"
    params = {
        'pair': pair,
        'interval': interval,
        'since': since
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_order_book(pair: str, count: Optional[int] = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get current order book details.
    
    Parameters:
    pair [Required]: string - Asset pair to get data for
    count [Optional]: integer - Maximum number of asks/bids
    """
    url = "https://api.kraken.com/0/public/Depth"
    params = {
        'pair': pair,
        'count': count
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_recent_trades(pair: str, since: Optional[str] = None, count: Optional[int] = 1000, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Returns the last 1000 trades by default.
    
    Parameters:
    pair [Required]: string - Asset pair to get data for
    since [Optional]: string - Return trade data since given timestamp
    count [Optional]: integer - Return specific number of trades, up to 1000
    """
    url = "https://api.kraken.com/0/public/Trades"
    params = {
        'pair': pair,
        'since': since,
        'count': count
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_recent_spreads(pair: str, since: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Returns the last ~200 top-of-book spreads for a given pair.
    
    Parameters:
    pair [Required]: string - Asset pair to get data for
    since [Optional]: integer - Returns spread data since given timestamp.
    """
    url = "https://api.kraken.com/0/public/Spread"
    params = {
        'pair': pair,
        'since': since
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}