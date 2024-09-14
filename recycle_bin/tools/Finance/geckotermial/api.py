import requests
from typing import Optional, Dict

def token_price(network: str, addresses: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get current USD prices of multiple tokens on a network.
    
    :param network: Network ID from the /networks list (e.g., eth for Ethereum).
    :param addresses: Comma-separated list of token addresses (up to 30 addresses).
    :param toolbench_rapidapi_key: API key for Toolbench RapidAPI (not used in this function).
    :return: A dictionary containing token prices.
    """
    url = f"https://api.geckoterminal.com/api/v2/simple/networks/{network}/token_price/{addresses}"
    response = requests.get(url)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def networks(page: Optional[int] = 1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get list of supported networks.
    
    :param page: Page through results (default: 1).
    :param toolbench_rapidapi_key: API key for Toolbench RapidAPI (not used in this function).
    :return: A dictionary containing the list of supported networks.
    """
    url = "https://api.geckoterminal.com/api/v2/networks"
    params = {'page': page}
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def trending_pools(include: Optional[str] = None, page: Optional[int] = 1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get trending pools across all networks.
    
    :param include: Attributes for related resources to include (e.g., base_token, quote_token, dex, network).
    :param page: Page through results (default: 1).
    :param toolbench_rapidapi_key: API key for Toolbench RapidAPI (not used in this function).
    :return: A dictionary containing trending pools data.
    """
    url = "https://api.geckoterminal.com/api/v2/networks/trending_pools"
    params = {}
    if include:
        params['include'] = include
    params['page'] = page
    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
