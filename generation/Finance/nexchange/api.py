import requests
from typing import Optional

def get_currencies(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all supported currencies.
    """
    url = "https://api.n.exchange/en/api/v1/currency/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_pairs(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get all supported currency pairs.
    """
    url = "https://api.n.exchange/en/api/v1/pair/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_price(pair_name: str, amount_base: Optional[float] = None, amount_quote: Optional[float] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get price quote of a given amount of currency.
    Parameters:
    - pair_name: Name of the exchanged pair, e.g., BTCLTC.
    - amount_base: Amount of base currency which user gets.
    - amount_quote: Amount of base currency which user sends.
    """
    url = f"https://api.n.exchange/en/api/v1/get_price/{pair_name}/"
    params = {
        "amount_base": amount_base,
        "amount_quote": amount_quote
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_rate_info(rate_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Gets price info by rate_id.
    Parameters:
    - rate_id: Unique rate id value of a price.
    """
    url = f"https://api.n.exchange/en/api/v1/rate/{rate_id}/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_latest_price(pair_name: str, market_code: Optional[str] = 'nex', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Gets latest price of the pair.
    Parameters:
    - pair_name: Name of the exchanged pair, e.g., BTCLTC.
    - market_code: Price market code. Default is 'nex'.
    """
    url = f"https://api.n.exchange/en/api/v1/price/{pair_name}/latest/"
    params = {
        "market_code": market_code
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_price_history(pair_name: str, hours: float = 0.1, data_points: int = 3, market_code: str = 'nex', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns price history for selected pair.
    Parameters:
    - pair_name: Name of the exchanged pair, e.g., BTCLTC.
    - hours: How many hours back would you like to get prices for.
    - data_points: Number of data points in the selected hour range.
    - market_code: Price market code. Default market is 'nex'.
    """
    url = f"https://api.n.exchange/en/api/v1/price/{pair_name}/history/"
    params = {
        "hours": hours,
        "data_points": data_points,
        "market_code": market_code
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_prices_info_list(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns list of rates with minimal and maximal amounts.
    """
    url = "https://api.n.exchange/en/api/v1/info/bulk/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_orders(page: int = 1, page_size: int = 3, pair: Optional[str] = "BTCETH", status: Optional[int] = 11, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns orders.
    Parameters:
    - page: Page number.
    - page_size: Number of orders per page.
    - pair: Pair name.
    - status: Order status.
    """
    url = "https://api.n.exchange/en/api/v1/orders/"
    params = {
        "page": page,
        "page_size": page_size,
        "pair": pair,
        "status": status
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_order(unique_reference: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get order data.
    Parameters:
    - unique_reference: Unique reference of the order.
    """
    url = f"https://api.n.exchange/en/api/v1/orders/{unique_reference}/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ticker(hours: float = 24, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get trade Volume.
    Parameters:
    - hours: How many hours back would you like to get trade Volume for.
    """
    url = "https://api.n.exchange/en/api/v1/ticker/"
    params = {
        "hours": hours
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_volume(hours: float = 24, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get trade Volume.
    Parameters:
    - hours: How many hours back would you like to get trade Volume for.
    """
    url = "https://api.n.exchange/en/api/v1/volume/"
    params = {
        "hours": hours
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {toolbench_rapidapi_key}"
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}