import requests
from typing import Optional, Dict, List, Union


def current_exchange_rate(code: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the current exchange rate for a specified currency from table A.
    """
    url = f"https://api.nbp.pl/api/exchangerates/rates/A/{code}/"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def gold_price_history(start_date: str, end_date: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get historical gold prices for a specified date range.
    """
    url = f"https://api.nbp.pl/api/cenyzlota/"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def current_gold_price(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get the current price of gold per gram.
    """
    url = f"https://api.nbp.pl/api/cenyzlota/"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
