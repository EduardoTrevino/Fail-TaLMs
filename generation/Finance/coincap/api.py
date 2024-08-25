import requests
from typing import Optional

def get_assets(limit: Optional[int] = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint to get a list of all assets.
    Parameters:
    limit [Optional]: integer [Description: The number of assets to retrieve, default is 100]
    """
    url = "https://api.coincap.io/v2/assets"
    params = {
        'limit': limit
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_asset_by_id(asset_id: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint to get detailed information for a specific asset by ID.
    Parameters:
    asset_id [Required]: string [Description: Asset ID to retrieve details for]
    """
    url = f"https://api.coincap.io/v2/assets/{asset_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_markets(limit: Optional[int] = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint to get a list of all markets.
    Parameters:
    limit [Optional]: integer [Description: The number of markets to retrieve, default is 100]
    """
    url = "https://api.coincap.io/v2/markets"
    params = {
        'limit': limit
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_exchange_data(limit: Optional[int] = 100, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint to get a list of all exchanges.
    Parameters:
    limit [Optional]: integer [Description: The number of exchanges to retrieve, default is 100]
    """
    url = "https://api.coincap.io/v2/exchanges"
    params = {
        'limit': limit
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}