import requests
from typing import Optional, List


def get_market_ticker(inst_id: str = 'BTC-USDT', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve the market ticker information for a specified instrument.
    Parameters:
     inst_id [Required]: string [Description: The instrument ID (e.g., BTC-USDT) for which ticker information is required.]
    """
    url = "https://www.okx.com/api/v5/market/ticker"
    headers = {
        'accept': 'application/json',
    }
    params = {
        'instId': inst_id
    }

    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_order_book(inst_id: str = 'BTC-USDT', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve the order book for a specified instrument.
    Parameters:
     inst_id [Required]: string [Description: The instrument ID for which the order book is required (e.g., BTC-USDT).]
    """
    url = "https://www.okx.com/api/v5/market/books"
    headers = {
        'accept': 'application/json',
    }
    params = {
        'instId': inst_id
    }

    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}