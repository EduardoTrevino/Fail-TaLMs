import requests
from typing import Optional, Dict

def get_currencies(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get a list of all supported currencies and their details.
    """
    url = "https://api.n.exchange/en/api/v1/currency/"
    
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def get_price(pair_name: str, amount_base: Optional[float] = None, amount_quote: Optional[float] = None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the price quote of a given amount of currency, or determine how much currency you would get for a specified amount of currency.
    """
    url = f"https://api.n.exchange/en/api/v1/get_price/{pair_name}/"
    querystring = {}
    
    if amount_base:
        querystring['amount_base'] = amount_base
    if amount_quote:
        querystring['amount_quote'] = amount_quote

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def get_price_history(pair_name: str, hours: Optional[float] = None, data_points: Optional[int] = None, market_code: Optional[str] = 'nex', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Returns the price history for a selected pair over a specified period of time.
    """
    url = f"https://api.n.exchange/en/api/v1/price/{pair_name}/history/"
    querystring = {}

    if hours:
        querystring['hours'] = hours
    if data_points:
        querystring['data_points'] = data_points
    if market_code:
        querystring['market_code'] = market_code

    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
