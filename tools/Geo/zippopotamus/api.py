import requests
from typing import Optional, Dict, Any


def get_zip_info_by_postal_code(country: str, postal_code: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Get information for a specific postal code in a given country.
    
    :param country: The country code (e.g., "US" for the United States).
    :param postal_code: The postal code to lookup (e.g., "90210").
    :param toolbench_rapidapi_key: API key for authentication (default provided).
    :return: JSON response from the API or error information.
    """
    url = f"http://api.zippopotam.us/{country}/{postal_code}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def get_zip_info_by_city(country: str, state: str, city: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict[str, Any]:
    """
    Get information about all postal codes for a given city in a given country and state.
    
    :param country: The country code (e.g., "US").
    :param state: The state code (e.g., "MA" for Massachusetts).
    :param city: The city name (e.g., "Belmont").
    :param toolbench_rapidapi_key: API key for authentication (default provided).
    :return: JSON response from the API or error information.
    """
    url = f"http://api.zippopotam.us/{country}/{state}/{city}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}