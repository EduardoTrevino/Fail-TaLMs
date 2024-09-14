import requests
from typing import Optional, Dict

def get_country_by_own_ip(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve the country for the requester's own IP address by querying the Country.is API.
    """
    url = "https://api.country.is"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_country_by_ip(ip: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve the country for a specified IP address.

    Parameters:
    ip [Required]: string - The IP address to query.
    """
    url = f"https://api.country.is/{ip}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_data_sources_info(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve information about the data sources used by the Country.is API.
    """
    url = "https://api.country.is/info"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}