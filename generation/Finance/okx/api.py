import requests
from typing import Optional, List

def get_account_balance(currency: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve the account balance for a specified currency.
    Parameters:
     currency [Optional]: string [Description: The currency code (e.g., BTC, ETH) whose balance you want to check.]
    """
    url = "https://www.okx.com/api/v5/account/balance"
    headers = {
        'accept': 'application/json',
        'toolbench-rapidapi-key': toolbench_rapidapi_key
    }
    params = {}
    if currency:
        params['ccy'] = currency
        
    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_market_ticker(inst_id: str = 'BTC-USDT', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Retrieve the market ticker information for a specified instrument.
    Parameters:
     inst_id [Required]: string [Description: The instrument ID (e.g., BTC-USDT) for which ticker information is required.]
    """
    url = "https://www.okx.com/api/v5/market/ticker"
    headers = {
        'accept': 'application/json',
        'toolbench-rapidapi-key': toolbench_rapidapi_key
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
        'toolbench-rapidapi-key': toolbench_rapidapi_key
    }
    params = {
        'instId': inst_id
    }

    response = requests.get(url, headers=headers, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}