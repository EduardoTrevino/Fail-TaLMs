import requests

def get_ip_address_text(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Returns your IP address in text format.
    Parameters: None
    """
    url = "https://api.aruljohn.com/ip"
    response = requests.get(url)
    return response.text.strip()

def get_ip_address_json(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: Returns your IP address in JSON format.
    Parameters: None
    """
    url = "https://api.aruljohn.com/ip/json"
    response = requests.get(url)
    return response.json()