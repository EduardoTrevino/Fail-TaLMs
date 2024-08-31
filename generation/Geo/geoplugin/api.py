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

def currency_converter(base_currency: str = 'USD', amount: float = 1.0, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Endpoint Description: Convert an amount from a base currency to a target currency using real-time conversion rates.
    Parameters:
    - base_currency [Optional]: string [Description: The currency code of the base currency.]
    - amount [Optional]: float [Description: The amount of base currency to convert.]
    - target_currency [Optional]: string [Description: The currency code into which to convert the base currency.]
    """
    url = f"http://www.geoplugin.net/json.gp?base_currency={base_currency}"
    
    response = requests.get(url)
    try:
        data = response.json()

        # Extract necessary information from the response
        exchange_rate = data.get('geoplugin_currencyConverter', 1)
        local_currency_code = data.get('geoplugin_currencyCode', 'USD')
        local_currency_symbol = data.get('geoplugin_currencySymbol', '$')
        city = data.get('geoplugin_city', 'Unknown city')
        country = data.get('geoplugin_countryName', 'Unknown country')

        # Calculate the converted amount
        converted_amount = exchange_rate * amount

        return {
            "base_currency": base_currency,
            "amount": amount,
            "local_currency": local_currency_code,
            "local_currency_symbol": local_currency_symbol,
            "exchange_rate": exchange_rate,
            "converted_amount": converted_amount,
            "location": {
                "city": city,
                "country": country
            }
        }
    except Exception as e:
        return {"error": str(e), "response": response.text}