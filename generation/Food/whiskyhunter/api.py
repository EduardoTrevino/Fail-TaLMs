import requests
from typing import Optional

def auction_data(slug: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: List only aggregated data for online auction {slug}.
    Parameters:
     slug [Required]: string [Path parameter. Example: 'catawiki']
    """
    url = f"https://api.whiskyhunter.net/api/auction_data/{slug}/"
    headers = {
        'X-RapidAPI-Key': toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def auctions_data(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: List all online auctions aggregated data.
    """
    url = "https://api.whiskyhunter.net/api/auctions_data/"
    headers = {
        'X-RapidAPI-Key': toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def auctions_info(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: List all online auctions main information.
    """
    url = "https://api.whiskyhunter.net/api/auctions_info/"
    headers = {
        'X-RapidAPI-Key': toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def distilleries_info(toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: List all distilleries main information.
    """
    url = "https://api.whiskyhunter.net/api/distilleries_info/"
    headers = {
        'X-RapidAPI-Key': toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def distillery_data(slug: str, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    Endpoint description: List data for distillery {slug}.
    Parameters:
     slug [Required]: string [Path parameter. Example: 'ardbeg']
    """
    url = f"https://api.whiskyhunter.net/api/distillery_data/{slug}/"
    headers = {
        'X-RapidAPI-Key': toolbench_rapidapi_key
    }

    response = requests.get(url, headers=headers)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}