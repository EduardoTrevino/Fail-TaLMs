import requests
import json
from typing import Optional

BASE_URL = "https://api.artic.edu/api/v1"

def artworks(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff', limit: int = 2, page: int = 1, fields: Optional[str] = None) -> dict:
    """
    Fetch latest artworks from the Art Institute of Chicago
    """
    url = f"{BASE_URL}/artworks"
    params = {
        "limit": limit,
        "page": page
    }
    if fields:
        params["fields"] = fields

    response = requests.get(url, params=params)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation
