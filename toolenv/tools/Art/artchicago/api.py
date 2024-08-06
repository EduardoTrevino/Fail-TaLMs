import requests
from typing import Optional, List


def artworks(limit: Optional[int] = 2, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A list of all artworks sorted by last updated date in descending order."
    """
    url = "https://api.artic.edu/api/v1/artworks"
    params = {
        'limit': limit,
        'page': page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def artworks_search(q: str, size: Optional[int] = 10, sort: Optional[str] = None, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search artworks data in the aggregator. Artworks in the groups of essentials are boosted so they'll show up higher in results."
    """
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {
        'q': q,
        'size': size
    }
    if sort:
        params['sort'] = sort

    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}


def agents(limit: Optional[int] = 2, page: Optional[int] = 1, toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A list of all agents sorted by last updated date in descending order."
    """
    url = "https://api.artic.edu/api/v1/agents"
    params = {
        'limit': limit,
        'page': page
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}
