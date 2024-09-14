import requests
from typing import Optional

def get_networks(fields: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve a list of all available networks.
    
    Parameters:
    fields [Optional]: A comma-separated list of fields to include in the response.
    """
    url = "http://api.citybik.es/v2/networks"
    params = {}
    if fields:
        params['fields'] = fields

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_network_details(network_id: str, fields: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Retrieve details of a specific network.

    Parameters:
    network_id [Required]: The ID of the network.
    fields [Optional]: A comma-separated list of fields to include in the response.
    """
    url = f"http://api.citybik.es/v2/networks/{network_id}"
    params = {}
    if fields:
        params['fields'] = fields

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}