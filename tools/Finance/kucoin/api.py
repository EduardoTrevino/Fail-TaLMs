import requests
from typing import Optional

def get_currency_list(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the currency list.

    This function retrieves the list of available currencies, including detailed information
    such as the currency's name, precision, and supported chains.

    Parameters: None

    Returns:
    - JSON response from the API or an error message.
    """
    url = "https://api.kucoin.com/api/v3/currencies"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_currency_detail(currency: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the details of a specified currency.

    This function retrieves detailed information about a specified currency, including its supported chains, 
    minimum deposit/withdrawal amounts, and contract address.

    Parameters:
    - currency (Required): str - Currency code (e.g., "BTC").

    Returns:
    - JSON response from the API or an error message.
    """
    url = f"https://api.kucoin.com/api/v3/currencies/{currency}"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_symbols_list(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the list of available currency pairs for trading.

    This function retrieves a list of available trading pairs, including base and quote currencies,
    minimum and maximum order sizes, and whether trading is enabled for the pair.

    Parameters: None

    Returns:
    - JSON response from the API or an error message.
    """
    url = "https://api.kucoin.com/api/v2/symbols"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}
    
def get_ticker(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Level 1 Market Data for a specific trading pair.

    This function retrieves the best bid/ask prices and sizes, last traded price and size, and other market data
    for a specified trading pair.

    Parameters:
    - symbol (Required): str - Trading pair symbol (e.g., "BTC-USDT").

    Returns:
    - JSON response from the API or an error message.
    """
    url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}
    
def get_all_tickers(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get market tickers for all trading pairs.

    This function retrieves Level 1 Market Data for all trading pairs, including the best bid/ask prices,
    last traded price, 24-hour volume, and more.

    Parameters: None

    Returns:
    - JSON response from the API or an error message.
    """
    url = "https://api.kucoin.com/api/v1/market/allTickers"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_24hr_stats(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the 24-hour statistics for a specified trading pair.

    This function retrieves statistics for the last 24 hours, including the highest and lowest prices, 
    24-hour volume, and price changes for a specified trading pair.

    Parameters:
    - symbol (Required): str - Trading pair symbol (e.g., "BTC-USDT").

    Returns:
    - JSON response from the API or an error message.
    """
    url = f"https://api.kucoin.com/api/v1/market/stats?symbol={symbol}"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_market_list(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the list of trading markets.

    This function retrieves the list of available trading markets, including USDS, BTC, KCS, and others.

    Parameters: None

    Returns:
    - JSON response from the API or an error message.
    """
    url = "https://api.kucoin.com/api/v1/markets"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_part_order_book(symbol: str, level: str = "level2_20", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of open orders for a symbol (aggregated).

    This function retrieves part of the order book (level 2) for a specific trading pair.

    Parameters:
    - symbol (Required): str - Trading pair symbol (e.g., "BTC-USDT").
    - level (Optional): str - Level of order book (e.g., "level2_20" or "level2_100"). Defaults to "level2_20".

    Returns:
    - JSON response from the API or an error message.
    """
    url = f"https://api.kucoin.com/api/v1/market/orderbook/{level}?symbol={symbol}"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_trade_histories(symbol: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the trade history of the specified symbol.

    This function retrieves the last 100 transaction records for a specific trading pair.

    Parameters:
    - symbol (Required): str - Trading pair symbol (e.g., "BTC-USDT").

    Returns:
    - JSON response from the API or an error message.
    """
    url = f"https://api.kucoin.com/api/v1/market/histories?symbol={symbol}"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_klines(symbol: str, type: str, startAt: Optional[int] = None, endAt: Optional[int] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get Kline data for the specified symbol.

    This function retrieves candlestick (Kline) data for a specific trading pair.

    Parameters:
    - symbol (Required): str - Trading pair symbol (e.g., "BTC-USDT").
    - type (Required): str - Type of candlestick patterns (e.g., "1min", "1day").
    - startAt (Optional): int - Start time in seconds (default is 0).
    - endAt (Optional): int - End time in seconds (default is 0).

    Returns:
    - JSON response from the API or an error message.
    """
    url = f"https://api.kucoin.com/api/v1/market/candles?symbol={symbol}&type={type}"
    
    if startAt:
        url += f"&startAt={startAt}"
    if endAt:
        url += f"&endAt={endAt}"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_fiat_price(base: Optional[str] = "USD", currencies: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the fiat price of the currencies for the available trading pairs.

    This function retrieves the fiat prices of cryptocurrencies for the specified base currency.

    Parameters:
    - base (Optional): str - Ticker symbol of a base currency (default is "USD").
    - currencies (Optional): str - Comma-separated cryptocurrencies to be converted into fiat (e.g., "BTC,ETH").

    Returns:
    - JSON response from the API or an error message.
    """
    url = f"https://api.kucoin.com/api/v1/prices?base={base}"
    
    if currencies:
        url += f"&currencies={currencies}"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_server_time(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the server time.

    This function retrieves the current server time.

    Parameters: None

    Returns:
    - JSON response from the API or an error message.
    """
    url = "https://api.kucoin.com/api/v1/timestamp"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_service_status(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the service status.

    This function retrieves the current service status of the API.

    Parameters: None

    Returns:
    - JSON response from the API or an error message.
    """
    url = "https://api.kucoin.com/api/v1/status"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unexpected error: HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e), "response": response.text}
