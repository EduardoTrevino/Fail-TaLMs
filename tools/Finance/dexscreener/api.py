import requests
from typing import Optional, List, Dict

def get_pairs_by_chain_and_address(chain_id: str, pair_addresses: List[str], 
                                   toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get one or multiple pairs by chain and pair addresses.
    
    Parameters:
    chain_id (str): The blockchain chain id such as ethereum, bsc, polygon, etc.
    pair_addresses (List[str]): One or multiple, comma-separated pair addresses (up to 30 addresses).
    
    Returns:
    Dict: JSON response containing pairs information.
    """
    url = f"https://api.dexscreener.com/latest/dex/pairs/{chain_id}/" + ','.join(pair_addresses)
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_pairs_by_token_address(token_addresses: List[str],
                               toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Get one or multiple pairs by token addresses.
    
    Parameters:
    token_addresses (List[str]): One or multiple, comma-separated token addresses (up to 30 addresses).
    
    Returns:
    Dict: JSON response containing pairs information.
    """
    url = "https://api.dexscreener.com/latest/dex/tokens/" + ','.join(token_addresses)
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def search_pairs(query: str, 
                 toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Search for pairs matching the query.
    
    Parameters:
    query (str): Query that includes pair address, token address, token name, or token symbol.
    
    Returns:
    Dict: JSON response containing matching pairs information.
    """
    url = f"https://api.dexscreener.com/latest/dex/search/?q={query}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}