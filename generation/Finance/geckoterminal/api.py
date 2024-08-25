import requests

BASE_URL = "https://api.geckoterminal.com/api/v2"
DEFAULT_ACCEPT_HEADER = "application/json;version=20230302"

def get_headers(rapidapi_key):
    return {
        "Accept": DEFAULT_ACCEPT_HEADER,
        "X-RapidAPI-Key": rapidapi_key
    }

def get_token_price(network: str, addresses: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get current USD prices of multiple tokens on a network.
    """
    url = f"{BASE_URL}/simple/networks/{network}/token_price/{addresses}"
    headers = get_headers(toolbench_rapidapi_key)
    response = requests.get(url, headers=headers)
    return response.json()

def get_supported_networks(page: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get list of supported networks.
    """
    url = f"{BASE_URL}/networks"
    params = {'page': page}
    headers = get_headers(toolbench_rapidapi_key)
    response = requests.get(url, params=params, headers=headers)
    return response.json()

def get_supported_dexes(network: str, page: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get list of supported dexes on a network.
    """
    url = f"{BASE_URL}/networks/{network}/dexes"
    params = {'page': page}
    headers = get_headers(toolbench_rapidapi_key)
    response = requests.get(url, params=params, headers=headers)
    return response.json()

def get_trending_pools_all(include: str = None, page: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get trending pools across all networks.
    """
    url = f"{BASE_URL}/networks/trending_pools"
    params = {'include': include, 'page': page}
    headers = get_headers(toolbench_rapidapi_key)
    response = requests.get(url, params=params, headers=headers)
    return response.json()

def get_trending_pools(network: str, include: str = None, page: int = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Get trending pools on a network.
    """
    url = f"{BASE_URL}/networks/{network}/trending_pools"
    params = {'include': include, 'page': page}
    headers = get_headers(toolbench_rapidapi_key)
    response = requests.get(url, params=params, headers=headers)
    return response.json()

# Additional methods for other endpoints can be implemented in a similar manner following the API documentation