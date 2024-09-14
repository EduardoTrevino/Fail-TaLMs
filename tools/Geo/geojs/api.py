import requests
from typing import Optional, List

def get_ip(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> str:
    """
    Endpoint description: Returns the requesting IP address.
    """
    url = "https://get.geojs.io/v1/ip.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_country(ip: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> str:
    """
    Endpoint description: Returns the country information about an IP.
    
    Parameters:
    ip [Optional]: string [Description: Allows searching for a specific IP address; if None, uses the requester's IP]
    """
    url = f"https://get.geojs.io/v1/ip/country.json" if ip is None else f"https://get.geojs.io/v1/ip/country/{ip}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_geo_info(ip: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> str:
    """
    Endpoint description: Contains all available geographical information about an IP.
    
    Parameters:
    ip [Optional]: string [Description: Allows searching for a specific IP address; if None, uses the requester's IP]
    """
    url = f"https://get.geojs.io/v1/ip/geo.json" if ip is None else f"https://get.geojs.io/v1/ip/geo/{ip}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_ptr_record(ip: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> str:
    """
    Endpoint description: Returns PTR (pointer record) information about an IP.
    
    Parameters:
    ip [Required]: string [Description: The IP address to lookup]
    """
    url = f"https://get.geojs.io/v1/dns/ptr/{ip}.json"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}