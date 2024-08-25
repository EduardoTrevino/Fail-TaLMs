import requests
from typing import Optional, Dict

def get_location_by_ip(ip: str = 'auto', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint Description: Get geolocation information based on a given IP address.
    Parameters:
    - ip [Optional]: string [Description: The IPv4 or IPv6 address to look up. Use 'auto' to automatically determine client's IP address.]
    """
    url = f"http://www.geoplugin.net/json.gp?ip={ip}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def currency_converter(base_currency: str = 'USD', amount: float = 1.0, target_currency: str = 'EUR', toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint Description: Convert an amount from a base currency to a target currency using real-time conversion rates.
    Parameters:
    - base_currency [Optional]: string [Description: The currency code of the base currency.]
    - amount [Optional]: float [Description: The amount of base currency to convert.]
    - target_currency [Optional]: string [Description: The currency code into which to convert the base currency.]
    """
    url = f"http://www.geoplugin.net/convert?from={base_currency}&to={target_currency}&amount={amount}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}