import requests
from typing import Optional

def get_standard_exchange_rates(base_currency: str = "USD", toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetch all supported currency exchange rates for a given base currency."""
    url = f"https://v6.exchangerate-api.com/v6/{toolbench_rapidapi_key}/latest/{base_currency}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def pair_conversion(base_currency: str, target_currency: str, amount: Optional[float] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Convert a specific amount from a base currency to a target currency.
    If amount is None, only the conversion rate is returned.
    """
    if amount is None:
        url = f"https://v6.exchangerate-api.com/v6/{toolbench_rapidapi_key}/pair/{base_currency}/{target_currency}"
    else:
        url = f"https://v6.exchangerate-api.com/v6/{toolbench_rapidapi_key}/pair/{base_currency}/{target_currency}/{amount}"
    
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_historical_data(base_currency: str, year: int, month: int, day: int, amount: Optional[float] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Fetch historical exchange rate data for a specific date.
    If amount is provided, returns amount conversion as well.
    """
    if amount is None:
        url = f"https://v6.exchangerate-api.com/v6/{toolbench_rapidapi_key}/history/{base_currency}/{year}/{month}/{day}"
    else:
        url = f"https://v6.exchangerate-api.com/v6/{toolbench_rapidapi_key}/history/{base_currency}/{year}/{month}/{day}/{amount}"
    
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_supported_codes(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """Fetches all the supported currency codes and their names."""
    url = f"https://v6.exchangerate-api.com/v6/{toolbench_rapidapi_key}/codes"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}