import requests
from typing import Optional, Dict, List


def get_venues(lat1: Optional[float] = None, lat2: Optional[float] = None, lon1: Optional[float] = None, lon2: Optional[float] = None,
               category: Optional[str] = None, owner: Optional[str] = None, limit: Optional[int] = 50, offset: Optional[int] = 0,
               toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve a list of crypto ATMs based on location parameters and filter by provider.
    """
    url = "https://coinmap.org/api/v1/venues/"
    params = {
        "lat1": lat1,
        "lat2": lat2,
        "lon1": lon1,
        "lon2": lon2,
        "category": category,
        "owner": owner,
        "limit": limit,
        "offset": offset
    }
    response = requests.get(url, params={k: v for k, v in params.items() if v is not None})
    try:
        data = response.json()
    except ValueError:
        data = response.text
    return data


def get_ratings(venue_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff') -> Dict:
    """
    Retrieve ratings of a specific venue.
    """
    url = f"https://coinmap.org/api/v1/venues/{venue_id}/ratings/"
    response = requests.get(url)
    try:
        data = response.json()
    except ValueError:
        data = response.text
    return data
