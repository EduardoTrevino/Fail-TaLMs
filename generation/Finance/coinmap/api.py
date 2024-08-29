import requests
from typing import Optional, Dict, Any

def get_venues(
    lat1: Optional[float] = None,
    lat2: Optional[float] = None,
    lon1: Optional[float] = None,
    lon2: Optional[float] = None,
    query: Optional[str] = None,
    category: Optional[str] = None,
    owner: Optional[str] = None,
    upvoter: Optional[str] = None,
    before: Optional[str] = None,
    after: Optional[str] = None,
    promoted: Optional[bool] = None,
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
    mode: Optional[str] = "list",
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve a list of venues with optional filtering parameters.
    """
    url = "https://coinmap.org/api/v1/venues/"
    params = {
        "lat1": lat1,
        "lat2": lat2,
        "lon1": lon1,
        "lon2": lon2,
        "query": query,
        "category": category,
        "owner": owner,
        "upvoter": upvoter,
        "before": before,
        "after": after,
        "promoted": promoted,
        "limit": limit,
        "offset": offset,
        "mode": mode
    }
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_venue(
    venue_id: int,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve information on a specific venue by ID.
    """
    url = f"https://coinmap.org/api/v1/venues/{venue_id}"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_comments(
    venue_id: int,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Retrieve comments for a specific venue by venue_id.
    """
    url = f"https://coinmap.org/api/v1/venues/{venue_id}/comments/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_rating(
    venue_id: int,
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Get ratings for a specific venue.
    """
    url = f"https://coinmap.org/api/v1/venues/{venue_id}/ratings/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_atm_operators(
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Get a list of ATM operators.
    """
    url = "https://coinmap.org/api/v1/atm-operators/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}

def get_coins(
    toolbench_rapidapi_key: str = '088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'
) -> Dict[str, Any]:
    """
    Get a list of coins.
    """
    url = "https://coinmap.org/api/v1/coins/"
    response = requests.get(url)
    try:
        return response.json()
    except Exception as e:
        return {"error": str(e), "response": response.text}