import requests

def getfiatcurrencies(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Lists known fiat currencies. Currency codes conform to the ISO 4217 standard where possible.
    """
    url = "https://api.coinbase.com/v2/currencies"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getexchangerates(currency: str = 'USD', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get current exchange rates. Default base currency is USD but it can be defined as any supported currency.
    """
    url = f"https://api.coinbase.com/v2/exchange-rates"
    querystring = {'currency': currency}
    
    response = requests.get(url, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
