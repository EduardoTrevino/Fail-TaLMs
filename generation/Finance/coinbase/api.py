import requests
from typing import Optional


def show_current_user(token: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get current user's public information. To get user's email or private information, use permissions wallet:user:email and wallet:user:read.
    """
    url = "https://api.coinbase.com/v2/user"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def show_authorization_information(token: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get current user's authorization information including granted scopes and send limits.
    """
    url = "https://api.coinbase.com/v2/user/auth"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_fiat_currencies(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Lists known fiat currencies.
    """
    url = "https://api.coinbase.com/v2/currencies"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_cryptocurrencies(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Lists known cryptocurrencies.
    """
    url = "https://api.coinbase.com/v2/currencies/crypto"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_exchange_rates(currency: Optional[str] = "USD", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get current exchange rates. Default base currency is USD.
    Parameters:
      currency [Optional]: string [Description: Base currency]
    """
    url = f"https://api.coinbase.com/v2/exchange-rates"
    params = {'currency': currency}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_buy_price(currency_pair: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get the total price to buy one bitcoin or ether.
    Parameters:
      currency_pair [Required]: string [Description: Currency pair e.g. 'BTC-USD']
    """
    url = f"https://api.coinbase.com/v2/prices/{currency_pair}/buy"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_sell_price(currency_pair: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get the total price to sell one bitcoin or ether.
    Parameters:
      currency_pair [Required]: string [Description: Currency pair e.g. 'BTC-USD']
    """
    url = f"https://api.coinbase.com/v2/prices/{currency_pair}/sell"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_spot_price(currency_pair: str, date: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get the current market price for bitcoin or other cryptocurrencies.
    Parameters:
      currency_pair [Required]: string [Description: Currency pair e.g. 'BTC-USD']
      date [Optional]: string [Description: For historic spot price, use format YYYY-MM-DD (UTC)]
    """
    url = f"https://api.coinbase.com/v2/prices/{currency_pair}/spot"
    params = {}
    if date:
        params['date'] = date
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_current_time(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Get the API server time.
    """
    url = "https://api.coinbase.com/v2/time"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}